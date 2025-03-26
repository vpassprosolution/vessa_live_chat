from db import connect_db
from rapidfuzz import fuzz

# Get best matching FAQ answer from DB using fuzzy logic
async def get_best_answer(user_question: str) -> str:
    user_question = user_question.strip().lower()
    if not user_question:
        return ""

    conn = await connect_db()
    if not conn:
        return ""

    try:
        rows = await conn.fetch("SELECT question, answer FROM faq")
        best_score = 0
        best_answer = ""

        for row in rows:
            score = fuzz.partial_ratio(user_question, row["question"].lower())
            if score > best_score:
                best_score = score
                best_answer = row["answer"]

        # ✅ Only return if confidence is 70 or above
        return best_answer if best_score >= 70 else ""
        
    except Exception as e:
        print(f"❌ Error fetching FAQ: {e}")
        return ""

    finally:
        await conn.close()
