##given a list of hetrogeneous elements. Write a Python script to remove all the non-integer values from the list

my_list = [1,'Hello',2.4,3,'world',4.7]
integer_list =[x for x in my_list if isinstance(x,int)]
print(integer_list)
