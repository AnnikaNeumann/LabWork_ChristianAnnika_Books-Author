from db.run_sql import run_sql

from models.authors import Authors
from models.book import Book

import repositories.book_repo as book_repo

def save(authors):
    sql = "INSERT INTO authors (name, age, country) VALUES (%s, %s, %s) RETURNING *"
    values = [authors.name, authors.age, authors.country]
    results = run_sql(sql, values)
    id = results[0]['id']
    authors.id = id
    return authors

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql) 
    for row in results:
        authors = Authors(row['name'], row ['age'], row ['country'])
    return authors


    