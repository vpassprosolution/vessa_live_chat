import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")

async def connect_db():
    try:
        conn = await asyncpg.connect(DB_URL)
        return conn
    except Exception as e:
        print(f"❌ DB Connection Error: {e}")
        return None
