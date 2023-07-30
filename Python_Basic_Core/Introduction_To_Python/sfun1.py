class SFUN1:
    def SFun(self):
        w = "Welcome"
        print(w.find('e'))
        print(w.find('e',2)) #staring from 2
        print(w.find('s'))

        w = "Welcome"
        print(w.index('e'))
        print(w.index('e',2))
        print(w.index('s',2)) # error output not found index

if __name__== "__main__":
    obj = SFUN1()
    obj.SFun()