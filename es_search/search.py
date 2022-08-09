# -*-coding:utf-8-*-
import os
import requests

from elasticsearch import Elasticsearch, helpers
import time
import logging

import pprint
pp = pprint.PrettyPrinter(indent=2)

MAX_SEQ_LENGTH = 510


EMB_API_URL = os.getenv("EMB_API_URL", "http://localhost:8888/encode")
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")

log = logging.getLogger(__name__)

es = Elasticsearch(
    ELASTIC_URL,
)

def _encode(strList):
    sentences = {"sentences": strList}

    response = requests.post(EMB_API_URL, json=sentences)
    if response.status_code != 200:
        print("Error code: {} {} {} {}".format(EMB_API_URL, response.status_code, response.text, sentences))
        raise Exception("Error: {}".format(response.text))
 
    json_out = response.json()
    if 'embeddings' not in json_out:
        print("Error: No embeddings in response {} {}".format(json_out, sentences))
        raise Exception("Error: No embeddings in response {}".format(response))

    return json_out['embeddings']

def _search_bm25(inp_query, filter, source, index_name, max_results=10):
    log.info("Input question: {}".format(inp_query))

    # Lexical search
    esResult = es.search(
        index=index_name,
        query={"bool": {"must": [{"match": {"text": inp_query}}], "filter": filter}},
        source=source,
        size=max_results,
    )

    return esResult


def _search_knn_api(inp_query, filter, source, index_name, max_results=10):
    log.info("Input question: {}".format(inp_query))

    encode_start_time = time.time()
    query_embedding = _encode([inp_query])[0]
    encode_end_time = time.time()

    # Sematic search
    # https://www.elastic.co/guide/en/elasticsearch/reference/8.2/knn-search-api.html

  
    sem_results = es.knn_search(
        index=index_name,
        knn={
            "field": "text_embedding",
            "query_vector": query_embedding,
            "k": max_results,
            # must be less than 10000
            "num_candidates": min(max_results * 50, 10000),
        },
        filter=filter,
        source=source,
    )

    log.info(
        "Computing the embedding took {:.3f} seconds, KNN API with ES took {:.3f} seconds".format(
            encode_end_time - encode_start_time, sem_results["took"] / 1000
        )
    )

    return sem_results

def _search(search_func, inp_query, index_name, max_results=10, author_name=None, date_range_str=None):
    log.info("Input question: {}".format(inp_query))

    # Filter list
    filter = []

    # Add user filter
    if author_name:
        filter.append({"term": {"user_name": author_name}})

    # Add date range
    if date_range_str:
        filter.append({"range": {"ts": {"gte": date_range_str}}})

    source = ["title", "text", "url", "snipper_text"]

    # Lexical search
    esResult = search_func(inp_query, filter, source, index_name, max_results)
    pp.pprint(esResult)

    resultList = []
    for hit in esResult["hits"]["hits"][0:max_results]:
        hit["_source"]["score"] = hit["_score"]
        resultList.append(hit["_source"])
        log.debug("\t{}".format(hit["_source"]["text"][:80]))

    return resultList

def search(inp_query):
    bm_results = _search(_search_bm25, inp_query, "scholarly", 10)
    knn_results = _search(_search_knn_api, inp_query, "scholarly", 10)

    # Merge two results
    results = bm_results + knn_results
    return results

if __name__ == "__main__":
    results = search("machine learning")
    pp.pprint(results)