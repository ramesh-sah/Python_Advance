import json 
file = open("posts.json","r")
x=file.read()
finaldata=json.loads(x)
print(finaldata)

