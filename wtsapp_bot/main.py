import pyautogui as pyo
import time

i=0
limit =int(input("Enter text limit number: "))
message=input("Enter The Message: ")
lim=limit+1

time.sleep(10)

while i<lim:
    pyo.typewrite(str(i)+". "+message)
    pyo.press("enter")
    i+=1








