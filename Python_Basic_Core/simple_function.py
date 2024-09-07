def simple_function():
    print("Welcome to wscubetech")

def sum(a,b):
    print(a+b)

def multiply(a,b):
    print(a*b)

def add(a,b=None):
    if b is None:
        b = 0
    print(a+b)
    
def minus(a,b=1):
    print(a-b)

def square(a):
    return a*a
    

if __name__ == '__main__':
    simple_function()
    sum(10,20)
    multiply(10,20)
    add(10)
    minus(10)
    d=square(10)
    print(d)
    