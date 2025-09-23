print("Hello, World!")
print("Welcome to Python programming.")
print("This is a simple script.")
class MyClass:
    def __init__(self,value):
        self.value = value
    
    def display(self):
        print(f"the value is :{self.value}")


class AnotherClass(MyClass):
    def show(self):
        print("This is AnotherClass")


if __name__ == "__main__":
    obj = MyClass(10)
    obj.display()
    obj2 = AnotherClass(20)
    obj2.display()
    obj2.show()
    print("Script execution completed.")