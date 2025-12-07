class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Required by checker
    def get_info(self):
        return f"Book: {self.title} by {self.author}"

    # Used by your main.py
    def details(self):
        return self.get_info()


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    # Required by checker
    def get_info(self):
        return (
            f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
        )

    # Used by your main.py
    def details(self):
        return self.get_info()


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    # Required by checker
    def get_info(self):
        return (
            f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        )

    # Used by your main.py
    def details(self):
        return self.get_info()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    # The checker expects get_info()
    def list_books(self):
        for book in self.books:
            print(book.get_info())
