###Define a class Book with insance object variable bookid, title, price . Initialise then via __init__() method. also define mthod to show book variables

class book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def showVariable(self):
        print(f"Bookid::{self.bookid}, \nTitle:: {self.title}, \nPrice:: {self.price}")
    



c = book("boom", "1234zz", 450)

c.showVariable()


