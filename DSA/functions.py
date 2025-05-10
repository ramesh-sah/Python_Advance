class Test:
    x=5 #class object variable 
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def show(self):
        print(self.a,self.b)
    
    @staticmethod
    def f2():
        print("Hello")
    
    @classmethod
    def f1(cls):
        print(cls.x)
        
t1=Test(3,5)
t1.show()
Test.f1()
Test.f2()