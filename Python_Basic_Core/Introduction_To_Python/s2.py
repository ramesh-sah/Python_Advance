class S2:
    def SS2(self):
        w = "welcome to wscube"
        print(w[0:7]) # gives data upto 6
        print(w[0::2]) # increment by value 2
        print(w[2])
        print(2[0:5:2])
        print(w[-1:-10:-2]) #reverse decreasement
        print(w[-1:: -1]) # reverse decrement
if __name__=="__main__":
    obj = S2()
    obj.SS2()