import pytest

import es_index as ei
index_name = "test"

def test_create_index():
    res = ei.create_index(index_name)
    assert res["acknowledged"] == True
    assert res["index"] == index_name

    # Second create should fail
    res = ei.create_index(index_name)
    assert res == False

def test_index():
    res = ei.index_doc(title="title", snippet_text="Hello", url="url", flattened_data={'ok':'ok'}, index_name=index_name)
    # Should be one
    assert res == 1

    long_text = """
    Hello, world!
    This is a long text.
    Let's see if it works.
    """
    res = ei.index_doc(title="title", snippet_text=long_text, url="url2", flattened_data={'ok':'ok'}, index_name=index_name)
    assert res > 2

def test_search_by_url():
    res = ei.search_by_url(url="url", index_name=index_name)
    assert res["hits"]["hits"][0]["_source"]["url"] == "url"

    res = ei.search_by_url(url="url2", index_name=index_name)
    assert res["hits"]["hits"][0]["_source"]["url"] == "url2"

def test_delete_index():
    res = ei.delete_index(index_name)
    assert res["acknowledged"] == True

    # Second delete should fail
    res = ei.delete_index(index_name)
    assert res == False

