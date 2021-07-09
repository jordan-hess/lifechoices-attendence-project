
from tkinter import *

root = Tk()
root.title("Admin Login")
from tkinter import messagebox
root.geometry("500x400")

# usernames and passwords
userList = "admin"
passwList = "adim123"


def login():
        if loginUser == userList and passwList == passwList:
            root.grid_forget()
            root.grid_forget()
            messagebox.showinfo(message="welcome")
        else:
         messagebox.showerror(message="password or username is invalid, try again")


loginLabelUser = Label(root, text="Log in:").place(x=50, y=100)

loginUser = StringVar()
loginUsername = Entry(root, textvariable=loginUser, width=40)
loginUsername.place(x=150, y=100)

loginLabelPassw = Label(root, text="Password:")
loginLabelPassw.place(x=50, y=150)

loginPassw = StringVar()
loginPassword = Entry(root, textvariable=loginPassw, width=40)
loginPassword.place(x=150, y=150)

# button to login, this will start the function login()
button = Button(root, text="Continue...", command=login).place(x=150, y=200)

root = mainloop()