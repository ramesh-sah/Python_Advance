class Logical:
    def Logical(self):
        x = 10
        y =20
        print(x ==10 and x<y)
        print(x ==10 and x<y and x ==y)
        print( x !=10 or x>y or x ==y)
        print(not x !=10)
        print(not(x!=10 and x>y and x==y))

if __name__ =="__main__":
    obj = Logical()
    obj.Logical()