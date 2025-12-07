# Base class
class Book:
    def __init__(self, title, author):
        # Initialize Book attributes
        self.title = title
        self.author = author

    def details(self):
        # Return string for Book
        return f"Book: {self.title} by {self.author}"


# Derived class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size       # Additional attribute in KB

    def details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count     # Additional attribute

    def details(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # Store Book, EBook, or PrintBook instances

    def add_book(self, book):
        self.books.append(book)  # Add book instance to library

    def list_books(self):
        for book in self.books:
            print(book.details())  # Print detail
