from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import json


app = FastAPI(title="EMB_MODEL_SERV_APP", version="0.1.0")

from sentence_transformers import SentenceTransformer

#model = SentenceTransformer("hunkim/sentence-transformer-klue", device='cpu')

# model = SentenceTransformer("upstage/simcse-nli-sbert-sts-klue-roberta-base", device='cpu', use_auth_token=True)
#model = SentenceTransformer("upstage/simcse-nli-sbert-sts-klue-roberta-base", use_auth_token=True)
model = SentenceTransformer("hunkim/sentence-transformer-klue")

@app.post("/encode")
async def encode(request: Request):
    body = await request.body()
    body_json = json.loads(body)
    embeddings = model.encode(body_json["sentences"])
    return JSONResponse(content={"embeddings": embeddings.tolist()})


if __name__ == "__main__":
    # uvicorn app:app --reload
    # python -m uvicorn app:app --reload --port 8082
    payload = ["Hello, world!", "I am a sentence"]
    print(model.encode(payload))
