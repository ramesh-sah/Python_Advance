class Test:
    x=5
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def show(self):
        print(self.a,self.b)
    
    #static method
    @staticmethod
    def f2():
        print("hello")
    
    
    @classmethod
    def f1(cls):
        print(cls.x)
    
t1=Test(3,4)
t1.show()
Test.f2()
Test.f1()
t1.f1()
t1.f2()