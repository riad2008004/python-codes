import tkinter as tk

window = tk.Tk()
window.title("Welcome")
window.geometry("450x650")

level_1=tk.Label(window,text="Welcome to my CONSOLE",bg='yellow',fg='black',relief='solid',font=("arial",16,'bold'))
level_1.pack()
# level_1.place(x=100,y=100)
button_1=tk.Button(window,text="Submit",bg='white',fg='green',relief='ridge',font=("arial",16,'bold'))
button_1.place(x=330,y=600)

window.mainloop()

