from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/signals/{ticker}")
async def get_latest_signal(ticker: str):
    # Retrieve from cache/DB
    return {"ticker": ticker, "sentiment": 0.85, "confidence": 0.92}