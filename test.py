import sqlite3
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("dante.db")
    except sqlite3.error as e:
        print(e)
    return conn        

@app.route("/online/request", methods=["GET", "POST"])
def index():
    api_key = ""
    base_url = "https://newsapi.org/v2/everything?q=tesla&from=2022-04-17&sortBy=publishedAt&apiKey={}"

    api_url = base_url.format(api_key)
    response = requests.get(api_url)
    result = response.json()

    return result

@app.route("/books", methods=["GET", "POST"])    
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM book")
        books=[
            dict(id=row[0],author=row[1],title=row[2])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        request_data = request.get_json()
        new_author = request_data["author"]
        new_title = request_data["title"]
        sql = """INSERT INTO book (author, title) VALUES (?,?)"""
        cursor = cursor.execute(sql, (new_author, new_title))
        conn.commit()

        return f"Book with id: {cursor.lastrowid} created successfully"


 