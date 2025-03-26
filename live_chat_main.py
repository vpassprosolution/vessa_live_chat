from fastapi import FastAPI, Request
from faq_model import get_best_answer

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "VESSA LIVE CHAT is running ✅"}

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question")

    if not question:
        return {"answer": "❌ No question received."}

    answer = await get_best_answer(question)
    return {"answer": answer}
