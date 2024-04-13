"""
Task 3: Implementing the Shopping Cart Module
    - Create a module for the shopping cart, handling adding books to the cart, viewing the cart, and checkout processes.

Problem Statement:
    - The bookstore system needs a functional and efficient shopping cart system, managed through a separate module.
Expected Outcome:
    - A cart.py module with a ShoppingCart class and supplementary functions, demonstrating the use of modularity for efficient shopping cart management.
"""


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.books = {}  # Dictionary to store books in the cart

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title]['quantity'] += 1
        else:
            self.books[book.title] = {
                'author': book.author,
                'price': book.price,
                'quantity': 1
            }

    def remove_book(self, book):
        if book.title in self.books:
            if self.books[book.title]['quantity'] > 1:
                self.books[book.title]['quantity'] -= 1
            else:
                del self.books[book.title]
        else:
            print("Book not found in the cart.")

    def checkout(self):
        total_price = 0
        for book in self.books:
            total_price += self.books[book]['price'] * self.books[book]['quantity']
        return total_price

    def view_cart(self):
        for book in self.books:
            print(
                f"Title: {book}, Author: {self.books[book]['author']}, Quantity: {self.books[book]['quantity']}, Price: ${self.books[book]['price']}")
        print(f"Total Price: ${self.checkout()}")