import datetime
import sqlite3
from queries import *
from data_classes import *



class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):

        self.cursor.execute(books_check)
        if not self.cursor.fetchall():
            self.cursor.execute(create_books_table)


        self.cursor.execute(readers_check)
        if not self.cursor.fetchall():
            self.cursor.execute(create_readers_table)


        self.cursor.execute(borrowed_books_check)
        if not self.cursor.fetchall():
            self.cursor.execute(create_borrowed_books_table)

        return print("Done")

    def add_book(self, title, author, year):
        self.cursor.execute(repeat_check, (title,))
        if self.cursor.fetchone():
            return print("Book is already exist")
        self.cursor.execute(add_new_book,(title, author, year))
        self.conn.commit()
        return print("Done")

    def add_reader(self, name, age):
        self.cursor.execute(add_new_reader, (name, age))
        self.conn.commit()

        return print("Done")

    def borrow_book(self, reader_id, book_id):

        self.cursor.execute(borrow_check, (book_id,))

        if not self.cursor.fetchone():
            return print("Book is already borrowed or does not exist")
        now =  datetime.date.today()
        self.cursor.execute(add_data_to_borrowed_books, (reader_id, book_id, now))
        self.cursor.execute(change_status_to_borrowed, (book_id,))

        self.conn.commit()

        return print("Book borrowed successfully")

    def return_book(self, book_id, reader_id):
        self.cursor.execute(return_check, (reader_id, book_id))

        if not self.cursor.fetchone():
            return print("You didn't borrow this book")

        self.cursor.execute(del_book, (reader_id, book_id))
        self.cursor.execute(change_status_to_available, book_id)

        self.conn.commit()

        return print("Book returned successfully")

    def search_books(self, keyword):
        self.cursor.execute(search_book, (keyword, keyword))

        results = self.cursor.fetchall()  # Получаем все результаты

        if not results:
            return "No titles or authors with this name"


        books = [Book(*result) for result in results]
        return print(books)

    def get_borrowed_books(self):
        self.cursor.execute(borrowed_books_get)

        return print(self.cursor.fetchall())


    def get_statistics(self):
        self.cursor.execute(borrowed_books_get2)
        print("Занятые книги:")
        print(self.cursor.fetchall())

        self.cursor.execute(not_borrowed_books_get)
        print("Незанятые книги:")
        return print(self.cursor.fetchall())

