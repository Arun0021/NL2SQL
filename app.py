import os
from dotenv import load_dotenv
import streamlit as st
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt template
PROMPT = """
You are an expert at translating English questions into SQL queries.
The database has a table named STUDENT with the following columns: NAME, CLASS, SECTION.

Return only the SQL query without explanations or formatting.

Examples:
Q: How many students are there?
A: SELECT COUNT(*) FROM STUDENT;

Q: Show all students in Data Science class.
A: SELECT * FROM STUDENT WHERE CLASS = "Data Science";

Question:
"""

# Gemini Query Function
def generate_sql(question: str) -> str:
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    try:
        response = model.generate_content(PROMPT + question)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

# Execute SQL function
def execute_sql(query: str, db_path: str = "student.db"):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return [("SQL Error", str(e))]

# Streamlit UI
st.title("NL ➡️ SQL Converter with Gemini")

user_input = st.text_input("Ask a question about the STUDENT table:")
if st.button("Convert"):
    sql_query = generate_sql(user_input)
    st.code(sql_query, language="sql")

    if sql_query.strip().upper().startswith("SELECT"):
        results = execute_sql(sql_query)
        st.subheader("Query Results:")
        st.write(results)
