import tkinter as tk

window=tk.Tk()
window.title("Form")
window.geometry("450x650")

label1=tk.Label(window,text="Registration Form",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=70,y=30)
label2=tk.Label(window,text="First Name: ",width=20,font=("arial",12,"bold"))
label2.place(x=15,y=100)
label2=tk.Label(window,text="Second Name: ",width=20,font=("arial",12,"bold"))
label2.place(x=25,y=140)


window.mainloop()