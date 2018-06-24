from tkinter import*
import sqlite3
import os
with sqlite3.connect('r2.db') as db:
    a = db.cursor()

a.execute('CREATE TABLE IF NOT EXISTS python (username TEXT NOT NULL,'
          'password TEXT NOT NULL,email TEXT NOT NULL,'
           'phoneno TEXT NOT NULL)')
db.commit()
db.close()

class main:

    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.phoneno = IntVar()
        self.widgets()

    def new_user(self):
        with sqlite3.connect('r2.db') as db:
            a = db.cursor()

        find_user = ('SELECT * FROM python WHERE username = ? '
                     'and password = ? and email = ? and phoneno = ?')
        a.execute(find_user,[(self.username.get()),(self.password.get()),(self.email.get()),(self.phoneno.get())])
        result=a.fetchall()

        if result:
            os.system("python lion1.py")
            self.username.set('')
            self.password.set('')
            self.email.set('')
            self.phoneno.set('')


        insert = 'INSERT INTO python(username,password,email,phoneno) VALUES(?,?,?,?)'
        a.execute(insert,[(self.username.get()),(self.password.get()),(self.email.get()),(self.phoneno.get())])
        db.commit()

    def widgets(self):
        self.frame = Frame(self.master,bg="dark slate blue")
        Label(self.frame, text="          REGISTRATION FORM          ", font=("Trebuchet MS", 35, "bold"), bg="dark slate blue", fg="goldenrod",
              padx=170,pady=20).grid(columnspan=3)
        Label(self.frame,text="CUSTOMER ID:",bg="dark slate blue", fg="spring green", font=("Trebuchet MS", 15,"bold"), padx=-20, pady=15).grid(row=2,column=0,sticky=E)
        Label(self.frame,text="PASSWORD:",bg="dark slate blue", fg="spring green", font=("Trebuchet MS", 15,"bold"), padx=-20, pady=15).grid(row=3,column=0,sticky=E)
        Label(self.frame, text="EMAIL:",bg="dark slate blue" ,fg="spring green", font=("Trebuchet MS", 15, "bold"), padx=-20, pady=15).grid(row=4, column=0, sticky=E)
        Label(self.frame, text="PHONE NO:",bg="dark slate blue", fg="spring green", font=("Trebuchet MS", 15, "bold"), padx=-20, pady=15).grid(row=5, column=0, sticky=E)
        Entry(self.frame, textvariable=self.username, bd=5).grid(row=2, column=1, sticky=E)
        Entry(self.frame, textvariable=self.password, bd=5,show='*').grid(row=3, column=1, sticky=E)
        Entry(self.frame, textvariable=self.email, bd=5).grid(row=4, column=1, sticky=E)
        Entry(self.frame, textvariable=self.phoneno, bd=5).grid(row=5, column=1, sticky=E)
        Button(self.frame, text="SUBMIT", font=("Trebuchet MS", 12), relief=RAISED, bg="dark slate blue", fg="goldenrod",padx=30,
               pady=5, activebackground="springgreen", command=self.new_user,activeforeground="goldenrod").grid( columnspan=3)
        Label(self.frame, text="", bg="dark slate blue").grid(columnspan=3)
        self.frame.grid()

if __name__ == '__main__':
    root=Tk()
    root.title('Bank Managment System')
    main(root)
    root.mainloop()


