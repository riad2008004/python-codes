import tkinter as tk
from tkinter import StringVar
from PIL import Image,ImageTk

window=tk.Tk()
window.title("Form")
window.geometry("450x650")

image_src="D:/Codes/python_codes/images/registration-icon-png-9.jpg"
image=Image.open(image_src)
image = image.resize((150, 110))
photo=ImageTk.PhotoImage(image)
lab_p=tk.Label(image=photo)
lab_p.place(x=155,y=6)

# fn=tk.StringVar() # a way of express string var at that case not need to import string var
# ln=tk.StringVar()
# dob=tk.StringVar()

fn=StringVar()
ln=StringVar()
dob=StringVar()
cntry=StringVar()

radio_var=StringVar()
ban=StringVar()
en=StringVar()
hin=StringVar()

def print_info():
    f_name=fn.get()
    print(f_name)
    # exit_00()
    
def exit_00():
    exit()

label1=tk.Label(window,text="Registration Form",relief="solid",width=20,font=("arial",17,"bold"))
label1.place(x=81,y=154)
label2=tk.Label(window,text="First Name : ",width=20,font=("arial",12))
label2.place(x=14,y=240)
label3=tk.Label(window,text="Last Name : ",width=20,font=("arial",12))
label3.place(x=13,y=280)
label4=tk.Label(window,text="Date of Birth : ",width=20,font=("arial",12))
label4.place(x=18,y=320)
label5=tk.Label(window,text="Country : ",width=20,font=("arial",12))
label5.place(x=0,y=360)
label6=tk.Label(window,text="Gender : ",width=20,font=("arial",12))
label6.place(x=0,y=400)
label7=tk.Label(window,text="Languages : ",width=20,font=("arial",12))
label7.place(x=12,y=440)

entry1=tk.Entry(window,textvar=fn)
entry1.place(x=200,y=245)
entry2=tk.Entry(window,textvar=ln)
entry2.place(x=200,y=285)
entry3=tk.Entry(window,textvar=dob)
entry3.place(x=200,y=325)

list=["Bangladesh","Nepal","Bhutan","India","Pakistan","Arabia","UAE","Srilanka"]
drop_optn=tk.OptionMenu(window,cntry,*list)
cntry.set("Select Country")
drop_optn.config(width=14)
drop_optn.place(x=198,y=355)

r1=tk.Radiobutton(window,text="Male",variable=radio_var,value="Male")
r1.place(x=194,y=403)
r2=tk.Radiobutton(window,text="Female",variable=radio_var,value="Female")
r2.place(x=265,y=403)

c1=tk.Checkbutton(window,variable=ban,text="Bangla")
c1.place(x=194,y=450)
c2=tk.Checkbutton(window,variable=en,text="English")
c2.place(x=266,y=450)
c3=tk.Checkbutton(window,variable=hin,text="Hindi")
c3.place(x=194,y=475)

button_1=tk.Button(window,text="Submit",width=10,bg='brown',fg='white',relief='ridge',font=("arial",12,'bold'),command=print_info)
button_1.place(x=110,y=580)
button_2=tk.Button(window,text="Exit",width=10,bg='brown',fg='white',relief='ridge',font=("arial",12,'bold'),command=exit_00)
button_2.place(x=230,y=580)

window.mainloop()