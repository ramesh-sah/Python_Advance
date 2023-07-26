class Calculator:
    def calculator(self):
        print(""" + for ADD
        - for Subtract
        * for multiply 
        / for divide """)
        num1 = eval(input("enter the first number:"))
        num2 = eval(input("enter the second number: "))
        opr = input("Enter the operator")
        if (opr =="+"):
            print(f"sum of numbers is {num1+num2}")
        elif(opr =="-"):
            if(num1>num2):
                print(f"the difference of number is {num1-num2}")
            else:
                print(f"the diffrence of number is {num2 - num1}")
        elif(opr =="*"):
            print(f"multiplication of numbers is {num1*num2}")
        elif(opr =="/"):
            print(f"division of the numbers is {num1/num2}")
        else:
            print("please enter the valid operator")
if __name__=="__main__":
    obj = Calculator()
    obj.calculator()