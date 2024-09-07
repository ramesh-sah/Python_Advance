import pickle
example = {1:'6', 2:'7', 3:'8', 4:'9'}

# Open the file in binary write mode
pickle_write = open("writedate.txt",'wb')
pickle.dump(example,pickle_write)
pickle_write.close()



# read the file in binary read mode

pickle_read = open("writedate.txt",'rb')
loaded_dict = pickle.load(pickle_read)
pickle_read.close()

print(loaded_dict)