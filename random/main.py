import random
import csv

filename=input("Enter File_name: ")
input_value=input("Enter The Lower number and Higher number: ")
max_data=int(input("Enter The data limit: "))

filename=filename+".csv"
print("")
print("The file will be saved as: " + filename)
print("....................................")

value=input_value.split()
low=int(value[0])
high=int(value[1])

with open(filename, mode='w', newline= '') as csvfile:
    writer=csv.writer(csvfile)  
    
    for i in range(max_data):
        rand= random.randint(low,high)
        writer.writerow([rand])
        # print("Random: ", rand)

print("Data Written Successfully.")   