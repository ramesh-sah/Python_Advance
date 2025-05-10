class Person:
    def __init__(self,name=None,age=None,address=None,city=None,state=None):
        self.name=name
        self.age=age
        self.address=address
        self.city=city
        self.state=state
        
    def setName(self,name):
        self.name=name
    def setAge(self,age):
        self.age=age
    def setAddress(self,address):
        self.address=address
    def setCity(self,city):
        self.city=city
    def setState(self,state):
        self.state=state
    
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def getState(self):
        return self.state
    
    def displayDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
        print("City:",self.city)
        print("State:",self.state)
        
        
p1=Person("Ramesh",20,"123 Main St","New York","NY")

p1.displayDetails()
    