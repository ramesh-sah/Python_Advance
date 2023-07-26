class list1:
    def List1(self):
        l = [10,'ws', 5.5]
        print(l, type(l))
        l[2] = 10 #update value function
        print(l, type(l))
if __name__=="__main__":
    obj = list1()
    obj.List1()