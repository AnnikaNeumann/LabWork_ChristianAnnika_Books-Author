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
    return redirect('/book')

@book_blueprint.route("/book/<id>/delete", methods=["POST"])
def delete_task(id):
    book_repo.delete(id)
    return redirect('/book')

@book_blueprint.route("/book/<id>", methods = ['GET'])
def show_book(id):
    task = book_repo.select(id)
    return render_template('book/show.html', book = book)

@book_blueprint.route("/book/<id>/edit", methods =['GET'])
def edit_book(id):
    book = book_repo.select(id)
    authors = authors_repo.select_all()
    return render_template("/book/edit.html", book = book, all_authors = authors)

@book_blueprint.route("/book/<id>", methods = ['POST'])
def update_book(id):
    title = request.form['title']
    user_id = request.form['user_id']
    language = request.form['language']
    authors = request.form['authors']
    release = request.form['release']
    genre = request.form['genre']
    completed = request.form['completed']
    authors = authors_repo.select(user_id)

    book = Book(title, genre, language, authors, release, id)
    book_repo.update(book)
    return redirect('/book')