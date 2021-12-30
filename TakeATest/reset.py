import pickle

filename = "D:\Aryan\Coding\Python\projects\Test\TestNames.txt"

reset = []

file = open(filename,"wb")
pickle.dump(reset, file)
file.close()