class Book:
    def __init__(self, title):
        self.title = title

    def book(self):
        print(f"The title of the book is", self.title)

    
b = Book('Math')
b.book()


class teacher:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print("Teachers name ", self.name)

T = teacher("Gouri")
T.getName()