class dtlist:
    def Dtlist(self):
        a = 5
        print (a)
        print(a, type(a)) #<class 'int'>
        a = 5.5
        print(a, type(a)) # <class 'float'>
        a = 2 +5j
        print (a, type(a)) #<class 'Complex'>
if __name__=="__main__":
    obj = dtlist()
    obj.Dtlist()