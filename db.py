import sqlite3

"""
Initialize the database and create a table in the database
"""

conn = sqlite3.connect("dante.db")

cursor = conn.cursor()
sql_query = """CREATE TABLE book (
    id INT PRIMARY KEY AUTOINCREMENT,
    author TEXT NOT NULL,
    title TEXT NOT NULL
)
"""

cursor.execute(sql_query)