import tkinter as tk

window = tk.Tk()
window.title("Welcome")
window.geometry("450x650")

level_1=tk.Label(window,text="Welcome to my CONSOLE",bg='yellow',fg='green',font=("arial",16,'bold')).pack()

window.mainloop()

