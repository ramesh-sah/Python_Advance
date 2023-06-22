#using for loop
for i in range(10):
    print(i,end="")
    #break the loop as soon it sees 6
    if i==6:
        break
print()

#loop from 1 to 10
i=0
while i<10:
    #if i is equal to 6
    #continue to next iteration without printing
    if i==6:
        i+=1
        continue
    else:
        #otherwise print the value of i
        print(i,end="")
    i+=1



