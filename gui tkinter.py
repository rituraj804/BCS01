from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")


def hellocallback():
    msg = messagebox.showinfo("Hello Python", "Hello World")


B1 = Button(top, text="Hello", command=hellocallback)
B1.place(x=50, y=50)
top.mainloop()
