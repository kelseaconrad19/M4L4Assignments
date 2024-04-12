""""""
"""
Task 1: Designing the Book Module
    - Create a module for managing book-related functionalities. This includes classes and functions for book attributes, book availability, and any other book-specific operations.

Problem Statement:
    - The bookstore system requires a dedicated module for handling various aspects related to books, such as title, author, price, and stock status.
    
Expected Outcome:
    - A well-structured book.py module with a Book class and other necessary functions, focusing on clear, concise, and modular code.
"""


class Book:
    def __init__(self, title: str, author: str, price: float, quantity: int):
        self.title = title
        self.author = author
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):  # returns integer
        return self.__quantity

    @quantity.setter
    def set_quantity(self, new_quantity):  # returns none
        if new_quantity >= 0:
            self.__quantity = new_quantity
        else:
            raise ValueError("Quantity cannot be less than 0.")

    def check_availability(self):  # returns boolean
        return self.quantity > 0

    def get_book_info(self):  # returns dictionary
        return {
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'quantity': self.quantity
        }



