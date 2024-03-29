from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import sqlite3
from datetime import datetime
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()


def police(j,photoPath):
    t = tk.Tk()
    t.title('POLICE PROFILE ')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    t.load = Image.open(photoPath)
    t.load = t.load.resize((300,300), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Label(t, image=t.photo1)
    t.img1.image = t.photo1

    def back():
        import os
        os.remove('const'+j+'.jpg')
        t.destroy()
        from constable_home import const_home
        const_home(j)

    p = cursor.execute('SELECT * FROM POLICE where POLICEID=?', (j,))
    u = p.fetchall()
    p1 = cursor.execute('SELECT * FROM POLICE1 where POLICEID=?', (j,))
    u1 = p1.fetchall()

    email1 = Label(t, text=u[0][7], borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    fname1 = Label(t, text=u[0][2].upper()+' '+u[0][3].upper()+' '+u[0][4].upper(), borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    contact1 = Label(t, text=u1[0][1], borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    juris1 = Label(t, text=u[0][8], borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    dob1 = Label(t, text=u[0][11], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    lgender = Label(t, text='Gender', font=tkFont.Font(family="Times New Roman", size=14), borderwidth=2, relief="solid")
    gender = Label(t, text=u[0][10], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid")
    lmarital = Label(t, text='Marital Status', font=tkFont.Font(family="Times New Roman", size=14), borderwidth=2, relief="solid")
    marital = Label(t, text=u[0][14], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    batch1 = Label(t, text=u[0][12], borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    rank1 = Label(t, text=u[0][13], borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    pid = Label(t, text='POLICE_ID', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    pid1 = Label(t, text=u[0][0], borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    email = Label(t, text='Email_ID', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    fname = Label(t, text='Name', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    contact = Label(t, text='Mobile_Number', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    juris = Label(t, text='Jurisdiction', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    batch = Label(t, text='Batch', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    rank = Label(t, text='Rank', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    address = Label(t, text='Address', borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    address1 = Label(t, text=u[0][9], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    dob = Label(t, text='Date of Birth', font=tkFont.Font(family="Times New Roman", size=14), borderwidth=2, relief="solid")

    fname.place(x=50, y=120, width=200, height=50)
    fname1.place(x=275, y=120, width=400, height=50)

    lgender.place(x=50, y=260, width=200, height=50)
    gender.place(x=275, y=260, width=400, height=50)

    dob.place(x=50, y=190, width=200, height=50)
    dob1.place(x=275, y=190, width=400, height=50)

    marital.place(x=275, y=330, width=400, height=50)
    lmarital.place(x=50, y=330, width=200, height=50)

    contact.place(x=50, y=400, width=200, height=50)
    contact1.place(x=275, y=400, width=400, height=50)

    email.place(x=50, y=470, width=200, height=50)
    email1.place(x=275, y=470, width=400, height=50)

    address.place(x=50, y=540, width=200, height=50)
    address1.place(x=275, y=540, width=400, height=50)

    juris.place(x=825, y=540, width=200, height=50)
    juris1.place(x=1050, y=540, width=400, height=50)

    batch.place(x=825, y=610, width=200, height=50)
    batch1.place(x=1050, y=610, width=400, height=50)
    rank.place(x=825, y=470, width=200, height=50)
    rank1.place(x=1050, y=470, width=400, height=50)

    pid.place(x=825, y=400, width=200, height=50)
    pid1.place(x=1050, y=400, width=400, height=50)
    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")
    back_button.place(x=250, y=690, width=250, height=50)

    t.img1.place(x=1025, y=50, width=250, height=250)


    mainloop()