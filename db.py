from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db")

def init_db():
    with engine.begin() as conn:   # better than connect()

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            department TEXT,
            salary INTEGER
        )
        """))

        # check if data already exists
        result = conn.execute(text("SELECT COUNT(*) FROM employees"))
        count = result.scalar()

        if count == 0:
            conn.execute(text("""
            INSERT INTO employees (name, department, salary)
            VALUES
            ('Alice', 'IT', 60000),
            ('Bob', 'HR', 45000),
            ('Charlie', 'IT', 80000)
            """))