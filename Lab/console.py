import pdb 
from models.book import Book
from models.authors import Authors

import repositories.book_repo as book_repo
import repositories.authors_repo as authors_repo


book_repo.delete_all()
authors_repo.delete_all()


book1 = Book ('IT', 'Horror', 'English', 'Stephen King', 1989)
book_repo.save(book1)
# add new book here to build up the repo

book2 = Book ('Shining', 'Horror', 'English', 'Stephen King', 1977)
book_repo.save(book2)

book_repo.select_all()

authors1 = Authors('Stephen King', 74, "USA")
authors_repo.save(authors1)

authors2 = Authors('Douglas Adams', 53, "United Kingdom")
authors_repo.save(authors2)