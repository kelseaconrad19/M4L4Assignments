import re
""""""
"""
Task 2: Creating the User Management Module
    - Develop a module dedicated to user management, including user registration, login, and profile management.

Problem Statement:
    - The online bookstore needs to manage its users effectively, requiring a separate module for user-related functionalities.

Expected Outcome:
    - A user.py module with a User class and related functions, showcasing the application of modularity in handling user management.
"""


class User:
    # Define user attributes and methods for registration, login, etc.
    def __init__(self, name, password, email, purchase_history):
        self.name = name  # String - used for email greetings and displaying in their profile
        self.__password = password  # String - used to log in
        self.email = email  # String - used to log in and send emails to them
        self.__purchase_history = purchase_history  # Dictionary to store past purchases - used to personalize adds and recommendations

# Additional functions for user management
    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", new_password) and 8 <= len(new_password) <= 26:
            self.__password = new_password

    def get_purchase_history(self):
        return self.__purchase_history

    def add_to_purchase_history(self, title, author):
        """Adds a book to the purchase history dictionary."""
        self.get_purchase_history()[title] = [author]

    def login(self, input_password):
        if input_password == self.get_password():
            return "You are now logged in."
        else:
            return "Incorrect password."
