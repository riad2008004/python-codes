class car:
    
    # name=""
    # reg_number=""
    
    def __init__(self,n,r):   #need to remove this function if mycar=car() Non parameterized object created
        self.name=n
        self.reg_number=r
    
    def start(self):
        print("The Car is starting")

# mycar=car()
# mycar.name="Premio"
# mycar.reg_number="10240520"

# print(mycar.name)
# print(mycar.reg_number)
# mycar.start()  

anothercar=car("Corolla","10541")
print(anothercar.name)
print(anothercar.reg_number)
      
    