class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print(f"area of the reactangle is :", a * b)
        elif a!=None and b==None:
            print(f"area of square is :",a*a)
        else:
            print("you need to provide both length and breadth")

if __name__=="__main__":
    obj = Area()
    obj.find_area(5, 6)
    obj.find_area(7)
    obj.find_area()