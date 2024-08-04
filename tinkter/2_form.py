import tkinter as tk

window=tk.Tk()
window.title("Form")
window.geometry("450x650")

def exit_00():
    exit()

label1=tk.Label(window,text="Registration Form",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=70,y=30)
label2=tk.Label(window,text="First Name : ",width=20,font=("arial",12))
label2.place(x=14,y=100)
label3=tk.Label(window,text="Last Name : ",width=20,font=("arial",12))
label3.place(x=13,y=140)
label4=tk.Label(window,text="Date of Birth : ",width=20,font=("arial",12))
label4.place(x=18,y=180)
label5=tk.Label(window,text="Country : ",width=20,font=("arial",12))
label5.place(x=2,y=220)

button_1=tk.Button(window,text="Log In",width=10,bg='brown',fg='white',relief='ridge',font=("arial",12,'bold'))
button_1.place(x=110,y=600)
button_2=tk.Button(window,text="Exit",width=10,bg='brown',fg='white',relief='ridge',font=("arial",12,'bold'),command=exit_00)
button_2.place(x=230,y=600)


window.mainloop()