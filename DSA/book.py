class Book:
    def __init__(self,bookid,title,price):
        self.bookid=bookid
        self.title=title
        self.price=price
        
    def show(self):
        print(self.bookid,self.title,self.price)

b1=Book(101,"Python",500)
b1.show()