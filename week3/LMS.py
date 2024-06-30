#Tasks 1:
#   1. Define a class `Book` with attributes `title`, `author`, and `pages`. 
#           Include methods to get and set these attributes.
#   2. Create an instance of `Book` and demonstrate the use of getter and setter methods.
#   3. Implement a class method in the Book that calculates the reading time based 
#           on an assumed reading speed (e.g., 250 words per minute).
#   4. Implement inheritance by creating a subclass `Ebook` that 
#           inherits from `Book` and adds an attribute `format`. Override the `__str__()` 
#           method to display all attributes.

#Submission Requirements:
#    - Python code file (`LMS.py`) containing the implementation of the `Book` and `Ebook` classes.
#    - The code must be well commented and placed inside a directory/folder named Library Management System.
#    - The code must be error-free with the implementation of exceptional handling.

class Book:
    """
    A class representing a book with title, author, and pages.
    """
    WORDS_PER_MINUTE = 250  # Assumed reading speed

    def __init__(self, title, author, pages):
        """
        Initializes a Book object with title, author, and pages.
        Raises ValueError if pages is not a positive integer.
        """
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Number of pages must be a positive integer")
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        """
        Returns the title of the book.
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of the book.
        """
        self._title = title

    @property
    def author(self):
        """
        Returns the author of the book.
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of the book.
        """
        self._author = author

    @property
    def pages(self):
        """
        Returns the number of pages in the book.
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the number of pages in the book.
        Raises ValueError if pages is not a positive integer.
        """
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Number of pages must be a positive integer")
        self._pages = pages

    @classmethod
    def calculate_reading_time(cls, pages):
        """
        Calculates the estimated reading time in minutes based on assumed reading speed.
        """
        return pages / cls.WORDS_PER_MINUTE

    def __str__(self):
        """
        Returns a string representation of the book object.
        """
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"


class Ebook(Book):
    """
    Ebook subclass inheriting from Book, adding format attribute and overriding __str__ method.
    """

    def __init__(self, title, author, pages, format):
        """
        Initializes an Ebook object with title, author, pages, and format.
        Raises ValueError if pages is not a positive integer.
        """
        super().__init__(title, author, pages)  # Call parent constructor
        self._format = format

    @property
    def format(self):
        """
        Returns the format of the ebook.
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of the ebook.
        """
        self._format = format

    def __str__(self):
        """
        Returns a string representation of the Ebook object with all attributes.
        """
        return super().__str__() + f"\nFormat: {self.format}"  # Call parent __str__ and add format


# Demonstration
if __name__ == "__main__":
    try:
        book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 195)
        print(f"Book title: {book1.title}")

        # Try setting invalid pages (non-positive integer or string)
        book1.pages = "invalid"
    except ValueError as e:
        print(f"Error: {e}")

    print(f"\nEstimated reading time for {book1.title}: {Book.calculate_reading_time(book1.pages)} minutes")

    ebook1 = Ebook("A Fire Upon the Deep", "Vernor Vinge", 624, "epub")
    print(f"\nEbook details:\n{ebook1}")
