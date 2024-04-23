class Rectangle:
  def __init__(self):
    self.length = 0
    self.breadth = 0

  def setDimensions(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def showDimensions(self):
    print(f"Length: {self.length} Breadth: {self.breadth}")

  def getArea(self):
    return self.length * self.breadth

rect = Rectangle()
rect.setDimensions(5, 4)
rect.showDimensions()
print(rect.getArea())