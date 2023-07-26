class Comparison:
    def comparison(self):
        x = 10
        y =20
        print(x ==y) # false
        print(x !=y) #True
        print(x>y) #false
        print(x<y) #true
        print(x>=y) #false
        print(x<=y) #true

if __name__ =="__main__":
    #calling the class
    obj = Comparison()
    obj.comparison()