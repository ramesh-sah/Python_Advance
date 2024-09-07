from array import * 
a1 = array('i',[5, 1,3,5,6,7,7])
print(type(a1))
for i in range(len(a1)):
    print(a1[i],end=' ')
for i in a1:
    print(i)
    
    
i =0
while i < len(a1):
    print(a1[i],end=' ')
    i += 1