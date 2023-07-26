class String:
    def string(self):
        s = "Hello@123"
        print(type(s))
        s = '''
        hello
        welcome to wscubetech'''
        print(s)
        print(type(s))
        s = '10'
        print(type(s))

if __name__=="__main__":
    obj = String()
    obj.string()