class Student:
    def __init__(self):
        self.__name=""
    
    def setName(self,Name):
        self.__name=Name
    
    def getName(self,name=None):
        self.__name=name
        

obj = Student()
obj.setName("Testing")
name = obj.getName()
print(name)