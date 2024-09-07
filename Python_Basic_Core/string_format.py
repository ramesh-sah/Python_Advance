fname="wscube"
lname="Tech"


txt1 = "Welcome to {fname} {lname}".format(fname=fname, lname=lname)
print(txt1)
txt3 = f"Welcome to {fname} {lname}".format(fname=fname, lname=lname)
print(txt3)

txt2 = "Welcome {} to {} Wscubetech".format("Hello",20)
print(txt2)

txt4 = "Welcome {0} to {1} Wscubetech".format("Hello",10)
print(txt4)
txt5 = "Welcome {a} to {b} Wscubetech".format(a=10, b=20)

print(txt5)

w="Welcome {b:11} to {a:5} wscubetech".format(a=20,b=11);
print(w) 