class IFstatement:
    def iFstatement(self):
        a = int(input("Enter the value:-"))
        if (a%2) ==0:
            print(f"{a} is even number")

        b = int(input("Enter yout age"))
        if b>18:
            print(f"your age is {b}, you are teenager, thank you ")
if __name__=="__main__":
    obj = IFstatement()
    obj.iFstatement()