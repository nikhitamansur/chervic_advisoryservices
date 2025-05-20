from transformers import pipeline
import sqlite3
import pandas as pd

nl2sql = pipeline("text2text-generation", model="b-mc2/sqlcoder", device=0)

query = "List all employee names in the Sales department"
sql_output = nl2sql(query, max_length=256, do_sample=False)[0]['generated_text']

print("Generated SQL:", sql_output)

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (1, 'Alice', 'Sales', 50000),
    (2, 'Bob', 'IT', 60000),
    (3, 'Charlie', 'Sales', 55000)
])
conn.commit()

try:
    result = pd.read_sql_query(sql_output, conn)
    print("\nExecution Result:")
    print(result)
except Exception as e:
    print("\nError executing SQL:", e)

expected_sql = "SELECT name FROM employees WHERE department = 'Sales';"
def exact_match(pred, target):
    return pred.strip().lower() == target.strip().lower()

print("\nExact Match:", exact_match(sql_output, expected_sql))