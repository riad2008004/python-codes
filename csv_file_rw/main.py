import csv

file=open("test.csv","w")

file.write("A,B,C\n")
file.write("2,5,12\n")
file.write("8,10,15\n")
file.write("14,24,66")

file.close()

file=open("test.csv","r")
data=csv.DictReader(file)

for x in data:
    print(x['A'])
file.close()
