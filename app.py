import streamlit as st
from db import init_db
from sql_engine import generate_sql, clean_sql, run_sql, is_safe

# Initialize DB
if "db_initialized" not in st.session_state:
    init_db()
    st.session_state["db_initialized"] = True

st.set_page_config(page_title="AI CRUD SQL Assistant", layout="wide")

st.title("🧠 AI CRUD SQL Assistant (Groq + SQLite)")

query = st.text_area("Enter your request (CRUD supported):")

if st.button("Execute Query"):
    if query:

        # Step 1: Generate SQL
        sql = generate_sql(query)

        # Step 2: Clean SQL (IMPORTANT FIX)
        sql = clean_sql(sql)

        st.subheader("Generated SQL")
        st.code(sql)

        # Step 3: Safety check
        if is_safe(sql):

            # Step 4: Execute SQL
            result = run_sql(sql)

            st.subheader("Result")

            if result["success"]:
                if isinstance(result["data"], list):
                    st.dataframe(result["data"])
                else:
                    st.success(result["data"])
            else:
                st.error("Unable to execute the generated SQL query,please give statement in a proper way.")
                st.code(sql)
                st.warning(result["error"])

        else:
            st.error("Unsafe SQL detected!")