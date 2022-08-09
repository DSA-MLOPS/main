from fastapi.testclient import TestClient

from app import app

client = TestClient(app)



def test_create_index():
    response = client.post("/create_index", json={"index_name":"test"})
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}

def test_index():
    response = client.post("/index", json={"title":"title", "snippet_text":"Hello", "url":"url", "flattened_data":{'ok':'ok'}, "index_name":"test"})
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}

def test_search_by_url():
    response = client.post("/search_by_url", json={"url":"url", "index_name":"test"})
    assert response.status_code == 200
    print(type(response.json()["res"]))

    # assert response.json() == {"msg": "Hello World"}

def test_delete_index():
    response = client.post("/delete_index", json={"index_name":"test"})
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}