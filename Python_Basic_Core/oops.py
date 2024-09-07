class DemoClass:

  def __init__(self):
    pass

  def sum(self,a,b):
    return a+b

  def diff(self,a,b):
    return a-b

  def multiply(self,a,b):
    return a*b

class Main:

  def __init__(self):
    pass

  def main(self):

    if __name__ == '__main__':

      obj = DemoClass()

      print('Sum:', obj.sum(5, 10))
      print('Difference:', obj.diff(15, 10))  
      print('Multiplication:', obj.multiply(3, 5))

if __name__ == '__main__':
  main = Main()
  main.main()