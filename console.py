import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Jk Rowling")
author_repository.save(author1)

author2 = Author("Louis")
author_repository.save(author2)

author3 = Author("Michael")
author_repository.save(author3)


book1 = Book("Harry potter", author1)
book_repository.save(book1)

book2 = Book("2", author2)
book_repository.save(book2)

book3 = Book("Harry potter 2", author1)
book_repository.save(book3)

book_repository.delete(2)




pdb.set_trace()