from scholarly import scholarly

import requests
import os
import sys


INDEX_API_URL = os.getenv("INDEX_API_URL", "http://localhost:8889")

def _create_index(index_name="scholarly"):
    payload = {'index_name': index_name}
    response = requests.post(INDEX_API_URL + "/create_index", json=payload)

    if response.status_code != 200:
        print("Error code: {} {} {}".format(response.status_code, response.text, payload))
        raise Exception("Error: {}".format(response.text))
    
    return response.json()

def _index(title, abs, url, flattened_data, index_name="scholarly"):
    payload = {'title': title, 'snippet_text': abs, 'url': url, 'flattened_data': {}, 'index_name': index_name}

    response = requests.post(INDEX_API_URL + "/index", json=payload)
    if response.status_code != 200:
        print("Error code: {} {} {}".format(response.status_code, response.text, payload))
        raise Exception("Error: {}".format(response.text))
 
    json_out = response.json()
    return json_out

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
def index_author(author_id):
    author = scholarly.search_author_id(author_id)
    scholarly.pprint(author)

    if author is None:
        print(f"Author {author_id} not found")
        return

    publications = scholarly.fill(author, sections=['publications'])

    for publication in publications['publications']:
        publication = scholarly.fill(publication, sections=[])
        print(publication['bib']['title'], publication['bib']['abstract'], publication['pub_url'])
        _index(publication['bib']['title'], publication['bib']['abstract'], publication['pub_url'], publication)

    # scholarly.pprint(publications)

if __name__ == "__main__":

    res = _create_index()
    print(res)

    print(f"Arguments count: {len(sys.argv)}")
    for arg in sys.argv[1:]:
        print(f"Indexing Auther ID: {arg}")
        index_author(arg)

    index_author("JE_m2UgAAAAJ")