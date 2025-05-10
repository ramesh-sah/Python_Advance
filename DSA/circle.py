""" Define a class circle with instance object variable radius . Provide setter and getter methods for radius. Also define getArea() and getCircumference() methods."""

class Circle:
    def __init__(self,radius=None):
        self.__radius = radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius

    def getArea(self):
        return (3.14*self.__radius*self.__radius)
    
    def getCircumference(self):
        return (2*3.14*self.__radius)


# create an instance of the Circle class
c1=Circle(5)
print(c1.getRadius())
print(c1.getArea())
print(c1.getCircumference())
print("  ")
c2=Circle()
c2.setRadius(6)
print(c2.getRadius())
print(c2.getCircumference())
print(c2.getArea())
        