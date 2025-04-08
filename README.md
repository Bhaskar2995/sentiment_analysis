**Sentiment Analysis API (FastAPI + Cohere)**

This project is a sentiment analysis API built with **FastAPI** and powered by **Cohere's large language model (LLM)**. 
It receives a text string, analyzes the sentiment using the Cohere API, and returns the result: **Positive**, **Negative**, or **Neutral**.

Open the project here: https://sentiment-analysis-react-pbnzv62iv-bhaskars-projects-cbd2bc62.vercel.app/

**Prerequisites:**
1) python 3.6+
2) A Cohere API key (for the sentiment analysis)

**Required Libraries**
1) cohere -  For accessing Cohere's LLM API
2) fastapi - For creating the backend API

Start the server using: uvicorn main:app --host 0.0.0.0 --port 8000
