from flask import Flask, render_template, redirect, request

from flask import Blueprint
from repositories import authors_repo
from repositories import book_repo
from models.book import Book

book_blueprint = Blueprint("book", __name__)

@book_blueprint.route("/book")
def book():
    book = book_repo.select_all()
    return render_template("book/index.html", all_book = book)

@book_blueprint.route("/book/new", methods= ['GET'])
def new_book():
    book = book_repo.select_all()
    return render_template("book/new.html", all_book = book)

@book_blueprint.route("/book", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.genre['genre']
    language = request.language['language']
    author = request.author['author']
    release = request.release['release']
    book = book_repo.select(id)
    book = Book(title, genre, language, author, release)
    book_repo.save(book)
