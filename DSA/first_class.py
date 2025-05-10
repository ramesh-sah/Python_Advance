class Test:
    x=5
    def f1(self,x=None):
        print("Hello",self.x)
        
t1=Test()
print(t1.f1(5))
t2=Test()
print(t2.x)
