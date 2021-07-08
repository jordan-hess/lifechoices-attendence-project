from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

root = Tk()

class Main_Window:
    def __init__(self):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x400")
        self.root.config(bg='white')

        self.img = ImageTk.PhotoImage(file="Logo-Life-Choices.jpg")
        Label(self.root, image=self.img, height=130, width=400).place(x=50, y=20)

        # Labels And Entry Boxes Login

        self.entry = Entry(self.root)
        self.entry.place(x=250, y=200)
        self.label = Label(self.root, text="Username", bg="white").place(x=100, y=200)

        self.entry2 = Entry(self.root)
        self.entry2.place(x=250, y=250)
        self.entry2.config(show='*')
        self.label2 = Label(self.root, text="Password", bg="white").place(x=100, y=250)

        self.login_button = Button(self.root, text='LOGIN',command=lambda: self.login_database())
        self.login_button.place(x=300, y=300)

        self.label = Label(self.root, text="Dont Have an Account?", bg="white").place(x=100, y=360)

        self.sign = Button(self.root, text='SignUp', command=lambda: self.Signup_Frame())
        self.sign.place(x=295, y=350)

    def Signup_Frame(self):
        signup = Toplevel()
        self.signup = signup
        self.signup.title("Registration Form")
        self.signup.geometry('800x800')
        self.signup.config(bg='light gray')

        # all Labels for registration

        self.head = Label(self.signup, text="Create Your Account", bg="light gray").place(x=420, y=130)

        self.lbl_Name = Label(self.signup, text='Name :', bg="light gray").place(x=240, y=190)

        self.id_lbl = Label(self.signup, text='ID Number  :', bg="light gray").place(x=240, y=310)

        self.srname_lbl = Label(self.signup, text='Surname:', bg="light gray").place(x=240, y=250)


        self.num_lbl = Label(self.signup, text='Phone :', bg="light gray").place(x=240, y=370)

        self.nxtk_label = Label(self.signup, text='Next of Kin name :', bg="light gray").place(x=240, y=430)

        self.nxtk_num_label = Label(self.signup, text='Next of Kin number :', bg="light gray").place(x=240, y=490)

        self.user_lbl = Label(self.signup, text='Username :', bg="light gray").place(x=240, y=540)

        self.passw_lbl = Label(self.signup, text='Password:', bg="light gray").place(x=240, y=590)

        # All Entry Boxes for registration
        self.nm_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=190)
        self.nm_entry = StringVar()

        self.surnm_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=250)
        self.surnm_entry = StringVar()

        self.id_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=310)
        self.id_entry =StringVar()

        self.num_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=370)
        self.num_entry = StringVar()

        self.rel_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=430)
        self.rel_entry = StringVar()

        self.rel_num_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=490)
        self.rel_num_entry = StringVar()

        self.user_nm_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=540)
        self.user_nm_entry = StringVar()

        self.passw_entry = Entry(self.signup, font=('sans-serif')).place(x=380, y=590)
        self.passw_entry = StringVar()

        # create acc Button
        self.create_Account = Button(self.signup, text='Create Account', font=('sans-serif'), command=lambda: self.Registration())
        self.create_Account.place(x=400, y=630)


    def Exit_Signup(self):
        self.signup.destroy()

    # Database

    def Registration(self):
            con = pymysql.connect(user="lifechoices", password="@Lifechoices1234", database="register")
            cur = con.cursor()
            cur.execute("insert into register values (%s, %s, %s, %s ,%s, %s,%s, %s)", (self.nm_entry.get(), self.surnm_entry.get(), self.num_entry.get(), self.id_entry.get(), self.rel_entry.get(), self.rel_num_entry, self.user_nm_entry.get(),self.passw_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", 'Account Created Succesfully')
            self.Exit_Signup()

    # login
    def login_database(self):
        if self.entry.get() == "Username":
            messagebox.showerror("Error", 'Please Enter User Name To Login')
        elif self.entry2.get() == 'Password':
            messagebox.showerror("Error", 'Please Enter Password To Login')
        else:
            con = pymysql.connect(user="lifechoices", password="@Lifechoices1234", database="register")
            cur = con.cursor()
            cur.execute("Select * from register where Username=%s and Password=%s",(self.entry.get(), self.entry2.get()))
            self.data = cur.fetchone()
            if (self.data == None):
                messagebox.showerror("Error", 'Please Enter a valid username and password')

            else:
                con.close()
                messagebox.showinfo("Successfully", 'Login Successfully')
                self.inbuild_values()

    def inbuild_values(self):
        self.entry.delete(0, END)
        self.entry2.delete(0, END)
        self.entry.insert(0, '  username')
        self.entry2.insert(0, '  *****')


m = Main_Window()
root.mainloop()