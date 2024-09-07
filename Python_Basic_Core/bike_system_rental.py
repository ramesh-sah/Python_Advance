class bikeShop:
    def __init__(self,stock):
        self.stock = stock
    
    def displayBike(self):
        print("Total: " , self.stock)
    
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value less than the stock ",self.stock)
        else:
            self.stock =self.stock -q
            print("Total Price ", q*100)
            print("Total bikes",self.stock)
            
while True:
    obj = bikeShop(100)
    uc=int(input(""" 
                 1. Display Stock
                 2. Rent Bike
                 3. Exit
                 
                 """))
    
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n = int(input("Enter the Qty:- "))
        obj.rentForBike(n)
    elif uc==3:
        break;
    else:
        print("Invalid Choice")