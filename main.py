from tkinter import *
from tkinter import messagebox
import pymysql

root = Tk()


class Main_Window:
    def __init__(self):
        self.root = root
        self.root.title("HOME PAGE")
        self.root.geometry("1000x700+250+50")
        self.root.config(bg='#ccccff')
        self.root.resizable(FALSE, FALSE)


    def Signup_Frame(self):
        signup = Toplevel()
        self.signup = signup
        self.signup.title("Registration Form")
        self.signup.geometry('1000x700+250+50')
        self.signup.config(bg='light gray')

        # all Labels

        self.head = Label(self.signup, text="Create Your Account").place(x=300, y=100)


        self.lbl_Name = Label(self.signup, text='Name :', bg="light gray").place(x=240, y=190)

        self.id_lbl = Label(self.signup, text='ID Number  :', bg="light gray").place(x=240, y=310)

        self.srname_lbl = Label(self.signup, text='Surname:', bg="light gray").place(x=240, y=250)


        self.num_lbl = Label(self.signup, text='Phone :', bg="light gray").place(x=240, y=370)

        self.nxtk_label = Label(self.signup, text='Next of Kin name :', bg="light gray").place(x=240, y=430)

        self.nxtk_num_label = Label(self.signup, text='Next of Kin number :', bg="light gray").place(x=240, y=490)

        # All Entry Boxes
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

        # Button
        self.create_Account = Button(self.signup, text='Create Account', font=('sans-serif'), command=lambda: self.Registration())
        self.create_Account.place(x=580, y=540)


    def Exit_Signup(self):
        self.signup.destroy()

    # Database

    def Registration(self):
            con = pymysql.connect(user="lifechoices", password="@Lifechoices1234", database="Logins")
            cur = con.cursor()
            cur.execute("Insert into Logins(Names, Surnames, Id_Number, Phone_Num, relative_nm, relative_num) values ('%s', '%s', '%s', '%s' ,'%s', '%s')" % (
            self.nm_entry.get(), self.surnm_entry.get(), self.num_entry.get(), self.id_entry.get(), self.rel_entry.get(), self.rel_num_entry))
            con.commit()
            con.close()
            messagebox.showinfo("Success", 'Account Created Succesfully')
            self.Exit_Signup()

m = Main_Window()
root.mainloop()