import cohere
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.post("/analyze")
def read_root(payload: dict):
    text = payload.get("text", "")
    co = cohere.Client("1tQuJVluwbSQMMAmCSaClts44fOQfoiuyYhbThA6")
    response = co.chat(
        model="command-r-plus-08-2024",
        message=f"What is the sentiment of this text: '{text}'? Respond with only one word: Positive, Negative, or Neutral.",
    )
    print(response.text)
    return {"sentiment": response.text.strip()}