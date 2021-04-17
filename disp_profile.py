from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import sqlite3
import re

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()


def display_details(user, user2):

    oldpswd = user[1]   
    u = user[0]

    t = tk.Tk()
    
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def goback():
        import os
        os.remove('c'+u+'.jpg')
        t.destroy()
        import civilian_home as tty
        tty.civ_home(u)


    def submit_details():
        #print(user[1])
        #print(oldpswd)
        if oldpswd==pswd1.get():
            pword = pswd2.get()
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)
            mat = re.search(pat, pword)
            if not mat:
                tkinter.messagebox.showinfo('Alert','Insecure Password.\nFor Security reasons, your password:\n\n> Should have at least one number.\n> Should have at least one uppercase and one lowercase character.\n> Should have at least one special symbol.\n> Should be between 6 to 20 characters long.')
                return
            else:
                cursor.execute("UPDATE CIVILIAN1 set PASSWORD =? where USERID=?", (pswd2.get(), u,))
                connection.commit()
                tkinter.messagebox.showinfo('TITLE','PASSWORD UPDATED')
        else:
            tkinter.messagebox.showinfo('Alert','Incorrect Password')
            return
            

    def clear_details():
        pswd1.delete(0, 'end')
        pswd2.delete(0, 'end')
        return



    path = "c" + user[0] + '.jpg'

    with open(path, 'wb') as file:
        file.write(user[12])

    t.load2 = Image.open(path)
    t.load2 = t.load2.resize((300, 300), Image.ANTIALIAS)
    t.photo2 = ImageTk.PhotoImage(t.load2, master=t)
    t.img2 = Button(t, image=t.photo2, borderwidth=2, relief="solid")
    t.img2.image = t.photo2

    tnm=user[2].upper()+' '+user[3].upper()+' '+user[4].upper()
    t.title('Profile - '+tnm)

    fname1 = Label(t, text=tnm, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    email1 = Label(t, text=user[8], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    contact1 = Label(t, text=user2[1], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    day = Label(t, text='Date Of Birth', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    mth = Label(t, text=user[5], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    lgender = Label(t, text='Gender', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    gender = Label(t, text=user[6], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    address1 = Label(t, text=user[10], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    occupation1 = Label(t, text=user[9], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    
    fname = Label(t, text='Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    #mname = Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    #lname = Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    email = Label(t, text='Email_ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    contact = Label(t, text='Mobile_Number', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid")
    address = Label(t, text='Address', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    occupation = Label(t, text='Occupation', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid")
    lmarital = Label(t, text=user[7], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    marital = Label(t, text='Marital Status', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    
    user=Label(t, text='USER ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    userid = Label(t, text=u, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")

    #uid = Label(t, text=user[0], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    password1=Label(t, text='Current Password', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    pswd1=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    password2=Label(t, text='New Password', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    pswd2=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

    submit=Button(t, text='CHANGE PASSWORD', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=4, relief="solid")
    reset=Button(t, text='CLEAR', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=4, relief="solid")
    goback=Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=goback, borderwidth=4, relief="solid")

    t.img2.place(x=1000, y=50, width=250, height=250)
    fname.place(x=90, y=50, width=200, height=50)
    fname1.place(x=315, y=50, width=400, height=50)

    lgender.place(x=90, y=120, width=200, height=50)
    gender.place(x=315, y=120, width=400, height=50)

    day.place(x=90, y=190, width=200, height=50)
    mth.place(x=315, y=190, width=400, height=50)

    marital.place(x=90, y=260, width=200, height=50)
    lmarital.place(x=315, y=260, width=400, height=50)

    contact.place(x=90, y=330, width=200, height=50)
    contact1.place(x=315, y=330, width=400, height=50)

    user.place(x=825, y=400, width=200, height=50)
    userid.place(x=1050, y=400, width=400, height=50)
    password1.place(x=825, y=470, width=200, height=50)
    pswd1.place(x=1050, y=470, width=400, height=50)
    password2.place(x=825, y=540, width=200, height=50)
    pswd2.place(x=1050, y=540, width=400, height=50)

    email.place(x=90, y=400, width=200, height=50)
    email1.place(x=315, y=400, width=400, height=50)

    address.place(x=90, y=470, width=200, height=50)
    address1.place(x=315, y=470, width=400, height=50)
    occupation.place(x=90, y=540, width=200, height=50)
    occupation1.place(x=315, y=540, width=400, height=50)


    goback.place(x=250, y=690, width=250, height=50)
    submit.place(x=650, y=690, width=250, height=50)
    reset.place(x=1050, y=690, width=250, height=50)


    mainloop()


