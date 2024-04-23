class Circle:
    def __init__(self,radius):
        self.radius=radius
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius
        
circle1 = Circle(5)
circle1.getArea()
circle1.getCircumference()
print(circle1.getArea())
print("The circumference of the circle is",circle1.getCircumference())