a= int(input("Enter the number :-"))
try:
    x =a/5
    print(x)
except Exception:
    print("Invalid number input type:")
else:
    print(x)
    
finally:
    print("Thank You ")