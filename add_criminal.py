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
        t.load = t.load.resize((250, 250), Image.ANTIALIAS)
        t.photo = ImageTk.PhotoImage(t.load,master=t)
        t.img1 = Button(t, image=t.photo, command=image_choos,borderwidth=2, relief="solid")
        t.img1.image = t.photo
        t.img1.place(x=1025, y=50, width=250, height=250)

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    def add3():
        try:
            empPhoto = convertToBinaryData(t.filename)
            u = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
            cursor.execute("INSERT INTO CRIMINAL VALUES(?,?,?,?,?,?,?,?,?,?)", (
            c_id1.get(), fname1.get(), mname1.get(), lname1.get(), u, bloodgrp1.get(), status1.get(), priority1.get(),
            gender1.get(), empPhoto))
            cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
            cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
            cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
        else:
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Criminal record created')
            t.destroy()
            from acp_home import acp_home
            acp_home(p)

    def clear_details():
        fname1.delete(0, 'end')
        mname1.delete(0, 'end')
        lname1.delete(0, 'end')
        gender1.delete(0, 'end')
        bloodgrp1.delete(0, 'end')
        im1.delete(0, 'end')
        ad1.delete(0, 'end')
        hd1.delete(0, 'end')

        c_id1.delete(0, 'end')
        status1.delete(0, 'end')
        priority1.delete(0, 'end')

        d.set('dd')
        mth.set('mm')
        y.set('yyyy')

        image_button= Button(t, text='Choose Photo', font=tkFont.Font(family="Times New Roman", size=16), command=image_choos,
                       borderwidth=2, relief="solid")
        image_button.place(x=1025, y=50, width=250, height=250)

        return

    def add_id_mark():
        try:
            if c_id1.get()!='' and im1.get()!='':
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
                cursor.execute("INSERT INTO CRIMINAL1 VALUES(?,?)", (c_id1.get(), im1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "Criminal Id/ Identification Mark is missing.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
            im1.delete(0, 'end')
        else:
            if c_id1.get()!='' and im1.get()!='':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            im1.delete(0, 'end')
            return

    def add_address():
        try:
            if c_id1.get()!='' and ad1.get()!='':
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
                cursor.execute("INSERT INTO CRIMINAL2 VALUES(?,?)", (c_id1.get(), ad1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "Criminal Id/ Address is missing.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
            ad1.delete(0, 'end')
        else:
            if c_id1.get()!='' and ad1.get()!='':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            ad1.delete(0, 'end')
            return

    def add_contact():
        try:
            if c_id1.get()!='' and hd1.get()!='':
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY,FNAME text,MNAME text,LNAME text,DOB text,BLOODGROUP text,STATUS number,PRIORITY number,GENDER text,PHOTO BLOB)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIMINAL1(CRIMINALID number PRIMARY KEY,IDENTIFICATIONMARKS text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID number PRIMARY KEY,ADDRESS text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3(CRIMINALID number PRIMARY KEY,CONTACT text)')
                cursor.execute("INSERT INTO CRIMINAL3 VALUES(?,?)", (c_id1.get(), hd1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "Criminal Id/ Contact Number is missing.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
            hd1.delete(0, 'end')
        else:
            if c_id1.get()!='' and hd1.get()!='':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            hd1.delete(0, 'end')
            return

    fi = tkFont.Font(family="Times New Roman", size=16)

### Defining the Labels
    l_first_name = Label(t, text='First Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_middle_name = Label(t, text='Middle Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_last_name = Label(t, text='Last Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    gender = Label(t, text='Gender',font=fi, borderwidth=2, relief="solid")

    l_date_of_birth = Label(t, text='Date of Birth',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29, 30, 31]
    d = IntVar(t)
    day = OptionMenu(t, d, *dayOptionList)
    menu = t.nametowidget(day.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    monthOptionList = [1,2,3,4,5,6,7,8,9,10,11,12]
    mth = IntVar(t)
    month = OptionMenu(t, mth, *monthOptionList)
    menu = t.nametowidget(month.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    yearOptionList = []
    for i in range(1950, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    year = OptionMenu(t, y, *yearOptionList)
    menu = t.nametowidget(year.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    day.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    month.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    year.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    bloodgrp = Label(t, text='Blood Group',font=fi, borderwidth=2, relief="solid")
    im = Label(t, text='Identification marks',font=fi, borderwidth=2, relief="solid")
    ad = Label(t, text='Address',font=fi, borderwidth=2, relief="solid")
    hd = Label(t, text='Contact number',font=fi, borderwidth=2, relief="solid")

    c_id = Label(t, text='Criminal ID',font=fi, borderwidth=2, relief="solid")
    status = Label(t, text='Status',font=fi, borderwidth=2, relief="solid")
    priority = Label(t, text='Priority',font=fi, borderwidth=2, relief="solid")

### Defining the Entry boxes
    fname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,
                   relief="solid")
    mname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")
    lname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")
    gender1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                    relief="solid")
    bloodgrp1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                      relief="solid")
    im1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                relief="solid")
    ad1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                relief="solid")
    hd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,
                relief="solid")

    c_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                  relief="solid")
    status1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                    relief="solid")
    priority1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                      relief="solid")

### Placing the Labels
    l_first_name.place(x=50, y=50, width=200, height=50)
    l_middle_name.place(x=50, y=120, width=200, height=50)
    l_last_name.place(x=50, y=190, width=200, height=50)
    gender.place(x=50, y=260, width=200, height=50)
    l_date_of_birth.place(x=50, y=330, width=200, height=50)
    bloodgrp.place(x=50, y=400, width=200, height=50)
    im.place(x=50, y=470, width=200, height=50)
    ad.place(x=50, y=540, width=200, height=50)
    hd.place(x=50, y=610, width=200, height=50)

    c_id.place(x=825, y=400, width=200, height=50)
    status.place(x=825, y=470, width=200, height=50)
    priority.place(x=825, y=540, width=200, height=50)

### Placing the Entry Boxes
    fname1.place(x=275, y=50, width=400, height=50)
    mname1.place(x=275, y=120, width=400, height=50)
    lname1.place(x=275, y=190, width=400, height=50)
    gender1.place(x=275, y=260, width=400, height=50)
    day.place(x=275, y=330,width=130, height=50)
    month.place(x=405, y=330,width=130, height=50)
    year.place(x=535, y=330,width=140, height=50)
    bloodgrp1.place(x=275, y=400, width=400, height=50)
    im1.place(x=275, y=470, width=400, height=50)
    ad1.place(x=275, y=540, width=400, height=50)
    hd1.place(x=275, y=610, width=400, height=50)

    c_id1.place(x=1050, y=400, width=400, height=50)
    status1.place(x=1050, y=470, width=400, height=50)
    priority1.place(x=1050, y=540, width=400, height=50)

### Defining the buttons
    image_button = Button(t, text='Choose Photo', font=tkFont.Font(family="Times New Roman", size=16), command=image_choos, borderwidth=4, relief="solid")

    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back, borderwidth=4, relief="solid")
    submitt = Button(t, text='ADD RECORD', font=tkFont.Font(family="Times New Roman", size=16), command=add3, borderwidth=4, relief="solid")
    reset = Button(t, text='RESET', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details,
                   borderwidth=4, relief="solid")

    plus1=Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_id_mark, borderwidth=4, relief="solid")
    plus2 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_address, borderwidth=4,
                   relief="solid")
    plus3 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_contact, borderwidth=4,
                   relief="solid")

### Placing the buttons
    image_button.place(x=1025, y=50, width=250, height=250)

    back_button.place(x=250, y=690, width=250, height=50)
    submitt.place(x=650, y=690, width=250, height=50)
    reset.place(x=1050, y=690, width=250, height=50)
    plus1.place(x=685, y=470, width=50, height=50)
    plus2.place(x=685, y=540, width=50, height=50)
    plus3.place(x=685, y=610, width=50, height=50)

### Setting the initial variables
    d.set('dd')
    mth.set('mm')
    y.set('yyyy')

    req = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                borderwidth=0)

    req2 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req3 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req4 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)

    req9 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req10 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)
    req11 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)

    req.place(x=675, y=50, width=10, height=50)
    req2.place(x=675, y=190, width=10, height=50)
    req3.place(x=675, y=260, width=10, height=50)
    req4.place(x=675, y=330, width=10, height=50)

    req9.place(x=1450, y=400, width=10, height=50)
    req10.place(x=1450, y=470, width=10, height=50)
    req11.place(x=1450, y=540, width=10, height=50)
    reqp = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)
    reqp.place(x=1275, y=50, width=10, height=50)

    mainloop()