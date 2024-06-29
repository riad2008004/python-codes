file=open("Name.txt","w")
file.write("Hi It is Riad\n")
file.write("Do you know me?")
file.close()

file=open("Name.txt","r")
data=file.read()
file.close()
print(data)

