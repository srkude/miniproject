#/usr/bin/env python

from tkinter import*
from tkinter import messagebox as ms
import sqlite3
import os
with sqlite3.connect('r2.db') as db:
    a = db.cursor()

class main:

    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.widgets()

    def Login(self):

        with sqlite3.connect('r2.db') as db:
            a = db.cursor()

        user = ('SELECT * FROM python WHERE username = ? and password = ?')
        a.execute(user,[(self.username.get()),(self.password.get())])
        result = a.fetchall()

        if result:
            os.system("python lion3.py ")
            self.username.set('')
            self.password.set('')

        else:
            ms.showerror('Oops!','RE-Enter your password or username')
            self.username.set('')
            self.password.set('')

    def SignUp(self):
        os.system("python lion.py")



    def widgets(self):
        self.frame=Frame(self.master,bg="dark slate blue")
        Label(self.frame,text="WELCOME TO", font=("Trebuchet MS", 35,"bold"), bg="dark slate blue", fg="goldenrod", padx=170).grid(columnspan=3)
        Label(self.frame, text="RAIL-TICKET BOOKING SYSTEM", font=("Trebuchet MS", 55, "bold"), bg="dark slate blue", fg="goldenrod",padx=170).grid(columnspan=3)
        Label(self.frame, text="", font=("Trebuchet MS", 35, "bold"), bg="dark slate blue", fg="spring green",pady=10).grid(columnspan=3)
        Label(self.frame, text="Customer Login", font=("Trebuchet MS", 25, "bold"), bg="dark slate blue", fg="spring green",pady=25).grid(columnspan=3)
        Label(self.frame, text="Username:", font=("Trebuchet MS", 17, "bold"), bg="dark slate blue", fg="spring green",padx=-20,pady=10).grid(row=4,column=0,sticky=E)
        Label(self.frame, text="Password:", font=("Trebuchet MS", 17, "bold"), bg="dark slate blue", fg="spring green",padx=-20,pady=10).grid(row=5,column=0,sticky=E)
        Entry(self.frame,textvariable=self.username,bd= 5).grid(row=4, column=1, sticky=E)
        Entry(self.frame,textvariable=self.password, bd=5,show="*").grid(row=5, column=1, sticky=E)
        Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
        Button(self.frame,text="Login", font=("Century Gothic", 15, "bold"), relief=RAISED, bg="dark slate blue", fg="goldenrod",
               padx=30, pady=5, activebackground="white", activeforeground="black", command=self.Login).grid(row=7,column=0,sticky=E)
        Button(self.frame, text="SignUP", font=("Century Gothic", 15, "bold"), relief=RAISED, bg="dark slate blue", fg="goldenrod",
               padx=30, pady=5, activebackground="white", activeforeground="black", command=self.SignUp).grid( row=7,column=1,sticky=E)
        Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
        self.frame.grid()


if __name__ == '__main__':
    root=Tk()
    root.title('railway ticket booking System')
    main(root)
    root.mainloop()

