class Demo:
    a = 10
    def __init__(self):
        print("Welcome to wscubetech")
    def showvalue(self):
        self.c = self.a*self.a
        print("Value of c is:", self.c)
    
    def showvalue1(self,a,b):
        print(a+b)

obj=Demo()
obj.showvalue()

obj.showvalue1(10,20)


        
    