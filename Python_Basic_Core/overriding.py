class A:
    def showData(self):
        print("I am in A class")
class B(A):
    def showData(self):
        print("I am in B class")
    
    
if __name__=="__main__":
    obj = B()
    obj.showData()
    