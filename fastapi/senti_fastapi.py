from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the input schema
class InputText(BaseModel):
    text: str

# Define the endpoint
@app.post("/sentiment")
async def get_sentiment(input_text: InputText):
    predicted_class = len(input_text.text)%2

    # Return the sentiment result
    if predicted_class == 1:
        return {"sentiment": "positive"}
    else:
        return {"sentiment": "negative"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6001)
