from typing import List
from classes.Employee import Employee
from classes.Book import Book

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"{book.author_name} {book.author_surname}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student}\nOrder Date:{self.order_date}\nBooks:\n{book_list}"