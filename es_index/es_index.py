# -*-coding:utf-8-*-
import os

from elasticsearch import Elasticsearch, helpers
import time
import logging
from datetime import datetime
import sys
import pprint
import requests

pp = pprint.PrettyPrinter(indent=2)

MAX_SEQ_LENGTH = 510

# ELASTIC_PASSWORD = os.environ["ELASTIC_PASSWORD"]
# ELASTIC_CA_CERTS = os.environ["ELASTIC_CA_CERTS"]
# ELASTIC_CA_CERTS = os.environ["ELASTIC_CA_CERTS"]

EMB_API_URL = os.getenv("EMB_API_URL", "http://localhost:8888/encode")
ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")


log = logging.getLogger(__name__)

#es = Elasticsearch(
#    "https://localhost:9200",
#    ca_certs=ELASTIC_CA_CERTS,
#    basic_auth=("elastic", ELASTIC_PASSWORD),
#)

# https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Public/9.SentenceDetectorDL.ipynb#scrollTo=euCxCFU-Erpv
import spacy
spacy_nlp = spacy.load("en_core_web_sm")

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

    

def create_index(index_name):
    # create index, if the index does not exists
    if es.indices.exists(index=index_name):
        return False

    log.info("{} No index. Let's create one".format(index_name))

    # Create index for KNN search
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/dense-vector.html
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search-api.html
    mappings = {
        "properties": {
            "flattened_data": {"type": "flattened"},
            "url": {"type": "keyword"},
            "snippet_text": {"type": "text"},
            "title": {"type": "text"},
            "text": {"type": "text"},
            "text_embedding": {
                "type": "dense_vector",
                "dims": 768,
                "index": True,
                "similarity": "cosine",
            },
            "ts": {
                "type": "date",
                "format": "strict_date_optional_time||epoch_second",
            },
        }
    }

    res = es.indices.create(index=index_name, mappings=mappings)
    log.info("{} Index created".format(index_name))
    return res


def index_doc(title, snippet_text, flattened_data, url, index_name):
    try:
        log.info("Deleting document with URL {}".format(url))
        res = es.delete_by_query(index=index_name, query={"match": {"url": url}})
        log.info("Deleted {} documents".format(res["deleted"]))
    except Exception as e:
        log.info("Could not delete document with URL {}".format(url))

    log.info(f"Indexing {url}")

    text_list = []
    # text_list.append(snippet_text[:MAX_SEQ_LENGTH])

    sentences = spacy_nlp(snippet_text).sents
    for sentence in sentences:
        text_list.append(sentence.text[:MAX_SEQ_LENGTH])

    emb_list = _encode(text_list)

    bulk_data = []
    for text, emb in zip(text_list, emb_list):
        data = {
            "_index": index_name,
            "_source": {
               "flattened_data": flattened_data,
                "title": title,
                "url": url,
                "snippet_text": snippet_text,
                "text": text,
                "text_embedding": emb,
                "ts": time.time(),
            },
        }
        bulk_data.append(data)

    
    helpers.bulk(es, bulk_data)
    return len(bulk_data)
   


def delete_index(index_name):
    if es.indices.exists(index=index_name):
        res = es.indices.delete(index=index_name)
        log.info("{} Index deleted".format(index_name))
        return res
    else:
        log.info("{} Index does not exist".format(index_name))
        return False


def search_by_url(url, index_name):
      # refresh index
    es.indices.refresh(index=index_name)

    res = es.search(index=index_name, query={"match": {"url": url}})
    return res
