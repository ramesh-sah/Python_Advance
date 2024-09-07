print(""" 
       Welcome to Python Programming World!
       This is a simple text-based game. You will be presented with a series of choices. Choose wisely and make the right decisions to progress. Good luck!
       
       
    + --> ADD
    - --> SUBTRACT
    * --> MULTIPLY
    / --> DIVIDE   
       """ )

no1 = int(input("Enter the first Number:-" ))
no2= int (input ("Enter the second Number:-" ))
opr = input("Enter the Operator:- ")

if opr == '+':
    print(no1 + no2)
if opr == '-':
    print(no1 - no2)
    
if opr == '*':
    print(no1 * no2)
if opr == '/':
    print( no1 / no2 )
else:
    print("Invalid Operator")