class Identity:
    def identity(self):
        x = 10
        y = 10
        print(x is y, x ==y)
        print(x !=y, x is not y)

if __name__=="__main__":
    obj = Identity()
    obj.identity()