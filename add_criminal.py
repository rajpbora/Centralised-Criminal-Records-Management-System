from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def add2(p):
    t = tk.Tk()
    t.title('ADD CRIMINAL RECORD')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def image_choos():
        t.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
        print(t.filename)
        t.load = Image.open(t.filename)
        t.load = t.load.resize((230, 200), Image.ANTIALIAS)
        t.photo = ImageTk.PhotoImage(t.load,master=t)
        t.img1 = Button(t, image=t.photo, command=image_choos)
        t.img1.image = t.photo
        t.img1.place(x = 1000, y = 140, width=250, height=350)

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData
    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    def add3():
        empPhoto = convertToBinaryData(t.filename)
        u = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
        cursor.execute("INSERT INTO CRIMINAL VALUES(?,?,?,?,?,?,?,?,?,?)", (c_id1.get(), fname1.get(), mname1.get(), lname1.get(), u,bloodgrp1.get(), status1.get(),priority1.get(),gender1.get(),empPhoto))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
        cursor.execute("INSERT INTO CRIMINAL1 VALUES(?,?)", (c_id1.get(), im1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
        cursor.execute("INSERT INTO CRIMINAL2 VALUES(?,?)", (c_id1.get(), ad1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
        cursor.execute("INSERT INTO CRIMINAL3 VALUES(?,?)",(c_id1.get(), hd1.get()))
        connection.commit()
        connection.commit()
        tkinter.messagebox.showinfo('Confirmation', 'created')
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    fi = tkFont.Font(family="Times New Roman", size=16)
    fih = tkFont.Font(family="Times New Roman", size=20)
    fname = Label(t, text='Full Name',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    fname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,
                   relief="solid")
    mname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                   relief="solid")
    lname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                   relief="solid")
    priority = Label(t, text='Priority',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    c_id = Label(t, text='Criminal ID',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    status = Label(t, text='status',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    c_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                  relief="solid")
    status1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    priority1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                      relief="solid")
    gender = Label(t, text='Gender',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    gender1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                    relief="solid")
    bloodgrp = Label(t, text='BLDGRP',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    bloodgrp1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                      relief="solid")
    im = Label(t, text='INDENTIFICATION MARKS',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    im1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                relief="solid")
    ad = Label(t, text='ADDRESS',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    ad1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                relief="solid")
    hd = Label(t, text='CONTACT',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    hd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,
                relief="solid")
    back_button = Button(t, text='Go Back', command=back, borderwidth=2, relief="solid", width=20, height=2).place(x=950, y=700)


    dob = Label(t, text='DATE OF BIRTH',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28,29, 30, 31]  # check for february and invalid details
    d = IntVar(t)
    d.set('Day')
    day = OptionMenu(t, d, *dayOptionList)
    day.configure(font=fi, relief="solid")
    monthOptionList = [1,2,3,4,5,6,7,8,9,10,11,12]  # check for february and invalid details
    mth = IntVar(t)
    mth.set('Month')
    month = OptionMenu(t, mth, *monthOptionList)
    month.configure(font=fi, relief="solid")
    yearOptionList = []
    for i in range(1955, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    y.set('Year')



    year = OptionMenu(t, y, *yearOptionList)
    year.configure(font=fi, relief="solid")
    day.place(x=300, y=140)
    month.place(x=380, y=140)
    year.place(x=480, y=140)

    age = Label(t, text='AGE',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    age1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2,
                 relief="solid")

    submitt = Button(t, text='SUBMIT', command=add3, borderwidth=2, relief="solid", width=20,height=2)
    image_button = Button(t, text='CHOOSE IMAGE FILE', command=image_choos, borderwidth=2, relief="solid", width=20,height=2)

    fname.place(x=50, y=10)
    fname1.place(x=300,y=10)
    mname1.place(x=700,y=10)
    lname1.place(x=1100,y=10)
    c_id.place(x=50,y=75)
    priority.place(x=50, y=530)
    c_id1.place(x=300, y=75)
    priority1.place(x=300, y=530)
    status.place(x=50, y=595)
    status1.place(x=300, y=595)


    hd.place(x=50, y=465)
    hd1.place(x=300,y=465)
    ad.place(x=50, y=335)
    ad1.place(x=300,y=335)
    im.place(x=50,y=400)
    im1.place(x=300,y=400)

    gender.place(x=50, y=270)
    gender1.place(x=300,y=270)
    dob.place(x=50,y=140)

    bloodgrp.place(x=50, y=205)
    bloodgrp1.place(x=300,y=205)
    submitt.place(x=950, y=600)
    image_button.place(x = 1000, y = 140, width=250, height=350)



    mainloop()