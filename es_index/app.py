from numpy import tile
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import json

import es_index as ei


app = FastAPI(title="ES_INDEX", version="0.1.0")


@app.post("/index")
async def index(request: Request):
    body = await request.body()
    body_json = json.loads(body)
    res = ei.index_doc(title=body_json["title"], snippet_text=body_json["snippet_text"], 
    url=body_json["url"], flattened_data=body_json["flattened_data"], index_name=body_json["index_name"])
    return JSONResponse(content={"res":str(res)})

@app.post("/search_by_url")
async def search_by_url(request: Request):
    body = await request.body()
    body_json = json.loads(body)
    res = ei.search_by_url(url=body_json["url"], index_name=body_json["index_name"])
    return JSONResponse(content={"res":str(res)})


@app.post("/create_index")
async def create_index(request: Request):
    body = await request.body()
    body_json = json.loads(body)
    res = ei.create_index(index_name=body_json["index_name"])
    return JSONResponse(content={"res":str(res)})

@app.post("/delete_index")
async def delete_index(request: Request):
    body = await request.body()
    body_json = json.loads(body)
    res = ei.delete_index(index_name=body_json["index_name"])
    return JSONResponse(content={"res":str(res)})
