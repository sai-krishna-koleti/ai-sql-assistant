# 🧠 AI SQL Assistant (Groq + LangChain + Streamlit)

An AI-powered SQL assistant that converts natural language into SQL queries and executes them on a SQLite database using Groq LLM and LangChain.

---

## 🚀 Features

- 🧠 Natural language → SQL conversion
- ⚡ Powered by Groq LLM (Llama3)
- 🗄️ SQLite database integration
- ✍️ Full CRUD support (Create, Read, Update, Delete)
- 🔍 Case-insensitive search support
- 🖥️ Interactive Streamlit UI
- 📊 Real-time query results display

---

## 🏗️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- SQLAlchemy
- SQLite

---


---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/sai-krishna-koleti/ai-sql-assistant.git
cd sql-crud-ai

2. Create virtual environment
py -3.11 -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt


4. Add environment variables
GROQ_API_KEY=your_groq_api_key_here


▶️ Run the application
streamlit run app.py