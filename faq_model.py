from db import connect_db
from rapidfuzz import fuzz

# Get best matching FAQ answer from DB
async def get_best_answer(user_question: str) -> str:
    conn = await connect_db()
    if not conn:
        return "❌ Failed to connect to the database."

    try:
        rows = await conn.fetch("SELECT question, answer FROM faq")
        best_score = 0
        best_answer = "🤖 Sorry, I don't understand that question yet."

        for row in rows:
            score = fuzz.partial_ratio(user_question.lower(), row["question"].lower())
            if score > best_score:
                best_score = score
                best_answer = row["answer"]

        return best_answer
    except Exception as e:
        print(f"❌ Error fetching FAQ: {e}")
        return "❌ An error occurred while searching for an answer."
    finally:
        await conn.close()
