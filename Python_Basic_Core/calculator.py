print(""" 
      + --> ADD
      - --> SUBTRACT
      * --> MULTIPLY
      / --> DIVIDE
      """)
num1 = int(input("Enter the first Number:-"))
num2 = int(input("Enter the second Number:-"))
opr = input("Enter the Opr :- ")
if opr == "+":
    print(num1+num2)
elif opr == "-":
    if num1 > num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif opr == "*":
    print(num1*num2)
elif opr =="/":
    print(num1 / num2)
else:
    print("invalid operator %r" % opr)