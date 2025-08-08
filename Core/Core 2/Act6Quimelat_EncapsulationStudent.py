class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, new_title):
        self.__title = new_title
        return self.__title

    def set_author(self, new_author):
        self.__author = new_author
        return self.__author


# Add an object book
b = Book("Python Basics", "John Smith")
print("Title:", b.get_title())
print("Author:", b.get_author())

# Update the book
print("Title:", b.set_title("Python for Beginner"))
print("Author:", b.set_author("Maria Santos"))