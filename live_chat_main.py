from fastapi import FastAPI, Request
from faq_model import get_best_answer

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "VESSA LIVE CHAT is running ✅"}

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "").strip()

    if not question:
        return {"answer": ""}  # Let Telegram handle fallback

    answer = await get_best_answer(question)

    if not answer or answer.strip() == "":
        return {"answer": ""}  # Let Telegram show "I don't have an answer"

    return {"answer": answer}
