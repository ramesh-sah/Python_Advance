import random 
import random

def project1():
    cnumber = random.randrange(1,101)
    user_input = int(input("Enter your Number:- "))
    
    if user_input>100:
        print("please enter a number less than 100")
    elif user_input<0: 
        print("please enter a number greater than 0")
    else:
        if user_input> cnumber:
            print("your number {user_input} is greater than the computer number {cnumber}".format(user_input=user_input, cnumber=cnumber))
            
        elif user_input<cnumber:
            print("your number {user_input} is less than the computer number {cnumber}".format(user_input=user_input, cnumber=cnumber))
             
        elif user_input==cnumber:
            print("Congratulations, you've guessed the correct number!")
if __name__ =="__main__":
    project1()