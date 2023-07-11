from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("300x300")
root.title("Login Page")

def submitact():

    user = username.get()
    passw = password.get()

    if user == "admin" and passw == "admin":
        messagebox.showinfo("Login Success !")
    elif user == '' and passw == '':
        messagebox.showinfo('Fill empty fields')
    else:
        messagebox.showinfo("Wrong Username/Password")
    print(user, passw)


lblfirstrow = Label(root, text="Username *")
lblfirstrow.place(x=50, y=20)
lblsecondrow = Label(root, text="Password *")
lblsecondrow.place(x=50, y=50)

username = Entry(root, width=35)
username.place(x=150, y=20, width=100)
password = Entry(root, width=35)
password.place(x=150, y=50, width=100)

btnsubmit = Button(root, text="Login", command=submitact).place(x=150, y=135, width=55)


root.mainloop()
