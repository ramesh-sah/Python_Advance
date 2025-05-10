class Rectangle:
  def __init__(self,length=None,width=None):
    self.__length = length
    self.__width = width
  
  def set_length(self, length):
    self.__length = length if length > 0 else 0
  def set_width(self, width):
    self.__width = width if width > 0 else 0
    
  def setDimensions(self, length,width):
    self.set_length(length)
    self.set_width(width)
    
  def get_length(self):
    return self.__length
  def get_width(self):
    return self.__width
  def getDimensions(self):
    return self.get_length(), self.get_width()
  
  def calculate_area(self):
    return self.__length * self.__width

r=Rectangle(10,14)
print(r.get_length())
print(r.get_width())
print(r.getDimensions())
print(r.calculate_area())

r1=Rectangle()

r1.setDimensions(3,5)
print(r1.getDimensions())
print(r1.calculate_area())