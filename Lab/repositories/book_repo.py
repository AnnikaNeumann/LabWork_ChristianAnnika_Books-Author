
from db.run_sql import run_sql

from models.authors import Authors
from models.book import Book

import repositories.authors_repo as authors_repo

def save(book):
    sql = "INSERT INTO books (title, genre, language, author, release) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.language, book.author, book.release]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book 


def select_all():
    book = []
    sql = "SELECT * FROM book"
    results = run_sql(sql) 
    for row in results:
        book = Book(row['title'], row ['genre'], row ['language'], row ['author'], row ['release'])
    return book




