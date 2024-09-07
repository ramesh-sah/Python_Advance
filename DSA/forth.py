##write a python script to create a list of the first N prime numbers .
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
N=10
prime_numbers=[]
num=2
while len(prime_numbers)<N:
    if is_prime(num):
        prime_numbers.append(num)
    num+=1
print(prime_numbers)