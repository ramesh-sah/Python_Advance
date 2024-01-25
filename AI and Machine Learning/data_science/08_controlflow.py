#conditional statements 
x = 10
if x>0:
    print("x is positive ")
    
else:
    print("X is negative")

y = 110
if y==110:
    print("y is equal to ", y)
elif(y>0):
    print("y is  positive")
elif(y<0):
    print("y is negative ")
    
else:
    print("Nothing")

foods = ['dahi bhallay',"biryani","Daal","SAmosay", "Shami","plak Paneer"]
for food in foods:
    print(food)

i =1
while i<6:
    print(i)
    i +=1

for letters in "Python":
    if letters =="h":
        break
    print(letters)

for letters in "Python":
    if letters =="h":
        continue
    print(letters)