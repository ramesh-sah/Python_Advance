#python program to illustrate
#function with main
def getInteger():
    result= int(input("Enter your value"))
    return result
def Mian():
    print("Started")
    #calling the getInteger functions
    output = getInteger()
    print(output)
    #now we are required to tell python for main function exist
if __name__=="__main__":
    Mian()