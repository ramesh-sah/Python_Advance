class Book:
    
    def __init__(self, name, price,description):
        self.name = name
        self.price = price
        self.description = description
    
    def get_book_info(self):
        dic = {'name':self.name,'price':self.price,'description':self.description}
        return dic
    def set_book_info(self, name, price,description):
        self.name = name
        self.price = price
        self.description = description
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_description(self):
        return self.description
    def set_name(self,name):
        self.name = name
    def set_price(self,price):
        self.price = price
    def set_description(self,description):
        self.description = description
    def print_info(self):
        print("Name of Book:",self.name)
        print("Price of Book:",self.price)
        print("Description of Book:",self.description)

if __name__ == "__main__":
    b1 = Book("DSA",123,"This is a DSA book.")
    b1.set_name("CS")
    b1.set_description("This is a CS book")
    b1.print_info()