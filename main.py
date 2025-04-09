import cohere
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001", "https://sentiment-analysis-react-pbnzv62iv-bhaskars-projects-cbd2bc62.vercel.app", "http://35.224.157.50:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.post("/analyze")
def read_root(payload:dict):
    print("payload", payload)
    text = payload.get("text", "")
    print("text", text)
    co = cohere.Client("1tQuJVluwbSQMMAmCSaClts44fOQfoiuyYhbThA6")
    response = co.chat(
        model="command-r-plus-08-2024",
        message=f"What is the sentiment of this text: '{text}'? Respond with only one word: Positive, Negative, or Neutral.",
    )
    print(response.text)
    return {"sentiment": response.text.strip()}