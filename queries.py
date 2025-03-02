from re import search

books_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='books';"
readers_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='readers';"
borrowed_books_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='borrowed_books';"

create_books_table = """
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    status TEXT CHECK(status IN ('available', 'borrowed'))
);
"""
create_readers_table = """
CREATE TABLE readers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
"""

create_borrowed_books_table = """
CREATE TABLE borrowed_books (
    reader_id INTEGER,
    book_id INTEGER,
    borrow_date TEXT,
    FOREIGN KEY (reader_id) REFERENCES readers(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    PRIMARY KEY (reader_id, book_id)
);
"""

add_new_book = "INSERT INTO books(title, author, year, status) VALUES(?,?,?,'available')"

add_new_reader = "INSERT INTO readers(name, age) VALUES(?,?)"

borrow_check = """
SELECT 1
FROM books 
WHERE books.id = ? AND NOT EXISTS (
    SELECT 1 FROM borrowed_books  WHERE borrowed_books.book_id = books.id
);
"""


add_data_to_borrowed_books = "INSERT INTO borrowed_books(reader_id, book_id, borrow_date) VALUES(?, ?, ?)"

change_status_to_borrowed = """
UPDATE books 
SET status = 'borrowed' 
WHERE id = ?;"""

change_status_to_available = """
UPDATE books 
SET status = 'available' 
WHERE id = ?;"""

return_check = """
SELECT 1
FROM borrowed_books
WHERE borrowed_books.reader_id = ? and borrowed_books.book_id = ?
"""

del_book = """
DELETE FROM borrowed_books
WHERE borrowed_books.reader_id = ? and borrowed_books.book_id = ?
"""

search_book = """
SELECT * FROM books
WHERE ? = books.title or ? = books.author
"""

borrowed_books_get = """
SELECT books.title, books.author, borrowed_books.borrow_date
FROM borrowed_books
INNER JOIN books on books.id = borrowed_books.book_id
"""

not_borrowed_books_get = """
SELECT *
FROM books
WHERE status IS 'available';
"""

borrowed_books_get2 = """
SELECT *
FROM books
WHERE status IS 'borrowed';
"""

repeat_check = """
SELECT 1 FROM books
WHERE books.title = ?"""

