import os
import re
import streamlit as st
from sqlalchemy import text
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from db import engine

load_dotenv()

# -----------------------
# Load Groq LLM
# -----------------------
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

# -----------------------
# Generate SQL
# -----------------------
def generate_sql(question: str) -> str:
    prompt = f"""
You are a SQL expert.

Convert the request into SQLite SQL.

IMPORTANT RULES:
- All string comparisons must be case-insensitive
- Use LOWER(column) for comparisons
- Example:
  WHERE LOWER(name) = LOWER('alice')

Return ONLY SQL.
No explanations.
No markdown.

Request: {question}
"""
    response = llm.invoke(prompt)
    return response.content

# -----------------------
# CLEAN SQL OUTPUT (FIX ERROR)
# -----------------------
def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()

# -----------------------
# Safety check
# -----------------------
def is_safe(sql: str) -> bool:
    banned = ["DROP", "ALTER", "TRUNCATE"]
    return not any(word in sql.upper() for word in banned)

# -----------------------
# Execute SQL
# -----------------------
def run_sql(sql: str):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))

            if sql.strip().lower().startswith("select"):
                return {
                    "success": True,
                    "data": result.fetchall()
                }

            conn.commit()

            return {
                "success": True,
                "data": "Query executed successfully"
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }