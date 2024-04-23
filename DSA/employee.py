class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
    
e1=Employee()
e1.setEmpid(1)
e1.setName("ramesh")
e1.setSalary(50000)
print(e1.getEmpid())
print(e1.getName())
print(e1.getSalary())
#creating object of the class using factory
e2=Employee(2,'suresh',60000)
print(e2.getEmpid())
print(e2.getName())
print(e2.getSalary())