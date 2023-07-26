class C1:
    def c1(self):
        a = int(input("enter the value:"))
        if (a %2 ==0):
            print(f"{a} is even number")
        else:
            print(f"{a} is odd number")
        age = int(input("Enter your age:"))
        if (age>=18):
            print(f"Your age is {age} , your  are eligible for voting \n welcome to new journey")
        else:
            print("YOu are not eligible for votiing")
if __name__=="__main__":
    obj= C1()
    obj.c1()
