class Tuple:
    def tuple(self):
        t = (10, 20,"hello")
        print(t, type(t)) #tuple
        t = (10)
        print(t, type(t)) # integer

if __name__ =="__main__":
    obj =Tuple()
    obj.tuple()