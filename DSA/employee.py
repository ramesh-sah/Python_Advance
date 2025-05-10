""" Create a class Employee with attributes empId , name , salary and also define methods to access properties of employee"""

class Employee:
    def __init__(self,empId=None,name=None,salary=None):
        self.empId=empId
        self.name=name
        self.salary=salary
    
    def setEmpId(self,empId):
        self.empId=empId
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
        
    def getEmpId(self):
        return self.empId
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
    
# create an instance of Employee class
e1=Employee()
e1.setName("John")
e1.setEmpId(1)
e1.setSalary(4000)
print(e1.getEmpId(),e1.getName(),e1.getSalary())

e2=Employee(2, 'ramesh',40000)
print(e2.getEmpId(),e2.getName(),e2.getSalary())
