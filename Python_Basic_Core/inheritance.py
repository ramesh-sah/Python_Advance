class A:
    def displayA(self):
        print("WElcome to class A")
    
class B(A):
    def displayB(self):
        print("WElcome to class B")
    
class C(A):
    def displayC(self):
        print("WElcome to class C")
class D(A,B):
    def displayD(self):
        print("WElcome to class D")
        
if __name__ == "__main__":
    objA = A()
    objB = B()
    objC = C()
    objD = D()
    
    objA.displayA()
    objB.displayB()
    objB.displayA()
    
    objC.displayC()
    objC.displayA()
    objD.displayA()
    objD.displayB()
   
    
