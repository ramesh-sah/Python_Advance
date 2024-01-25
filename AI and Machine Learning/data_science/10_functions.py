def greet_user():
    print("Hello, user!")
    
greet_user()

def add(x,y):
    return x+y

result = add(30,50)
print(result)

def aoa(name):
    print(f"hello this is {name}")

aoa("Ramesh")

def square(number):
    return number*number

result = square(5)
print(result)


def fact(n):
    if (n==1):
        return 1
    else:
        return n*fact(n-1)

a = fact(4)
print(a)