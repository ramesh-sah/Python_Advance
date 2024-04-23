class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        return self.name,self.age
    
p1=Person("Ramesh",20)
print(p1.show())
