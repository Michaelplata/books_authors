from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select(id):
    # To return task object:
    #create an empty variable
    book = None
    # create sql string
    sql = "SELECT * FROM books WHERE id = %s"
    # create our values list
    values = [id]
    # run the sql and capture the result
    result = run_sql(sql, values)[0]
    # create a new task object 
    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['id'])
    # finally return the task object
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

