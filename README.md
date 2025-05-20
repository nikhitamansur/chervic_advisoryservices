# NL2SQL Conversion Demo

## Objective
Convert natural language queries to SQL using pre-trained models from Hugging Face. Evaluate conversion quality based on exact match and execution accuracy.

## Tools Used
- Python 3.8+
- Hugging Face Transformers (`tscholak/optimum-nl2sql`)
- SQLite (for execution testing)
- Google Colab 

## Sample Query & Output
**Natural Language:**
> List all employee names in the Sales department

**Generated SQL:**
```sql
SELECT name FROM employees WHERE department = 'Sales';
```

## Evaluation Metrics
- **Exact Match Accuracy**: done
- **Execution Accuracy**: matches expected rows from test DB

## Known Limitations
- May fail on complex joins or nested queries.
- Performance may vary by model and input phrasing.

## How to Run
1. Open the Colab Notebook or run the Python script locally.
2. Ensure internet access to load the Hugging Face model.
3. Modify/add test cases as needed.

---
