class Book:
    def __init__(self, name):
        self.name = name
        self.borrows = 0

    def borrow(self):
        self.borrows += 1

    def total_borrows(self):
        return self.borrows


class Person:
    def __init__(self, name):
        self.name = name
        self.borrows = 0
        self.borrow_history = []

    def borrow_book(self, Book):
        Book.borrow()
        self.borrow_history.append(Book.name)
        self.borrows += 1

    def total_borrows(self):
        return self.borrows

    def history(self):
        return ', '.join(self.borrow_history)



b1 = Book("Harry Potter 1")
b2 = Book("Harry Potter 2")
p1 = Person("syswraith")
p1.borrow_book(b1)
p1.borrow_book(b2)
print(f'{p1.name} has borrowed {p1.history()}')
print(f'{p1.name} has borrowed total of {p1.total_borrows()} books')
print(f'{b1.name} has been borrowed {b1.total_borrows()} time(s)')
