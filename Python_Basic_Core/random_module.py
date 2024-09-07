import random 
# n = random.randint(0,9)
# print(n)

# n=random.randrange(0,4)
# print(n)

def random_func(a,b):
    return random.randint(a,b)

def random_choice():
    l=['apple', 'orange','mango','orange','papaya']
    random_value=random.choices(l)
    return random_value

if __name__ == "__main__":
    n = random_func(0,9)
    print(n)
    print(random_choice())


