from book import Book
from user import User
from cart import ShoppingCart

# Code to integrate and utilize the modules
# Create instances of Book
book1 = Book("Python Programming", "John Smith", 29.99, 29)
book2 = Book("Data Science for Beginners", "Jane Doe", 39.99, 15)

# Create instances of User
user1 = User("Alice", "password123", "alice@email.com", {})
user2 = User("Bob", "password456", "bob@email.com", {})

# Create instances of ShoppingCart
cart1 = ShoppingCart(user1)
cart2 = ShoppingCart(user2)

cart1.total_price = 100  # Set the total price of the cart
# print(cart1.total_price)  # Access the total price of the cart

# Add books to the carts
cart1.add_book(book1)
cart1.add_book(book2)
cart2.add_book(book2)

# View the contents of the carts
cart1.view_cart()
cart2.view_cart()
