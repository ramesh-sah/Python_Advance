## Write a python script to create a list of the first N terms of a Fabonacci series??
N=10
fibonacci_series=[0,1]
while len(fibonacci_series)<N:
    next_number =fibonacci_series[-1]+fibonacci_series[-2]
    fibonacci_series.append(next_number)
print(fibonacci_series)
    