l = [10,20,30,40,50,60,70]
print(len(l))
s="welcome"
print(len(s))

class WS:
    def displayInfo(self,name=''):
        print("WElcome to wscubete tech")

if __name__ == '__main__':
    obj=WS()
    obj.displayInfo()
    obj.displayInfo("Python")