class C2:
    def c2(self):
        percentage = int(input("enter the value"))
        if percentage >=60:
            print(f"your percentage is {percentage} \n you score first division")
        elif percentage >=48:
            print(f"your percentage is {percentage} \n you score second division")
        elif percentage >= 35:
            print(f"your percentage is {percentage} \n you score third division")
        else:
            print(f"you r fail, sorry")


if __name__=="__main__":
    obj = C2()
    obj.c2()