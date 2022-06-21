import sqlite3

def create_employees(path):
    SQL = """CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        password TEXT,
        salt TEXT);
        """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(SQL)

if __name__ == "__main__":
    create_employees('test.db')