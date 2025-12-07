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
        # Call base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def details(self):
        # Return string for EBook
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def details(self):
        # Return string for PrintBook
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        # Initialize an empty list of books
        self.books = []

    def add_book(self, book):
        # Add a Book, EBook, or PrintBook to the library
        self.books.append(book)

    def list_books(self):
        # Print details of all books
        for book in self.books:
            print(book.details())
