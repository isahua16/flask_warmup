from dbhelpers import run_statement
from flask import Flask
import json

app = Flask(__name__)

@app.get("/books")
def get_books():
    results = run_statement("CALL get_books_authors()")
    if(type(results) == list):
        json_books = json.dumps(results, default=str)
        return json_books
    else:
        "Sorry, something went wrong. Try again"

@app.get("/author-sales")
def get_author_sales():
    results = run_statement("CALL get_book_count_per_author()")
    if(type(results) == list):
        json_author_sales = json.dumps(results, default=str)
        return json_author_sales
    else:
        "Sorry, something went wrong. Try again"

@app.get("/best-seller")
def get_best_seller():
    results = run_statement("CALL get_best_seller()")
    if(type(results) == list):
        json_best_seller = json.dumps(results, default=str)
        return json_best_seller
    else:
        "Sorry, something went wrong. Try again"

@app.get("/best-selling-authors")
def get_best_selling_authors():
    results = run_statement("CALL get_author_sales()")
    if(type(results) == list):
        json_best_selling_author = json.dumps(results, default=str)
        return json_best_selling_author
    else:
        "Sorry, something went wrong. Try again"

app.run(debug=True)