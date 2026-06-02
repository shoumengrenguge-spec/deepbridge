from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(
            "https://api.deepseek.com/chat/completions",
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            },
            json=body,
        )
    return JSONResponse(resp.json())
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

print("KEY=", DEEPSEEK_API_KEY)