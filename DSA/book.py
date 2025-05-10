class Book:
    def __init__(self,bookid=None,title=None,price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
    def setBookid(self,bookid):
        self.bookid=bookid
    def setTitle(self,title):
        self.title=title
    def setPrice(self,price):
        self.price=price
    
    def getBookid(self):
        return self.bookid
    def getTitle(self):
        return self.title
    def getPrice(self):
        return self.price
        
    def show(self):
        # print(f"bookid:{self.bookid}\ntitle:{self.title} \nprice:{self.price}")
        print(f"Book ID: {self.bookid}\nTitle: {self.title}\nPrice: {self.price}")


b1=Book(101,"Python",500)
b1.show()