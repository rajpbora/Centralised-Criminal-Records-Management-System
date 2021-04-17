from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from PIL import Image,ImageTk
from tkinter import filedialog
import datetime
import os
import sqlite3


def test1(p, j, j1, j2, j3, photoPath):
    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    t = tk.Tk()
    t.title('CRIMINAL EDIT')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    global im_var_1
    im_var_1=0

    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    def image_update():
        try:
            t.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(("jpeg files", ".jpg"), ("all files", ".*")), master=t)
            t.load = Image.open(t.filename)
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "No New Image selected.")
        else:
            global im_var_1
            im_var_1 = 1
            t.load = t.load.resize((250, 250), Image.ANTIALIAS)
            t.photo1 = ImageTk.PhotoImage(t.load, master=t)
            t.img1 = Button(t, image=t.photo1, command=image_update, borderwidth=2, relief="solid")
            t.img1.image = t.photo1
            t.img1.place(x=1025, y=50, width=250, height=250)

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def updated_user():
        global im_var_1
        if im_var_1==1:
            empPhoto = convertToBinaryData(t.filename)
            cursor.execute("Update CRIMINAL set PHOTO=? where CRIMINALID=?", (empPhoto, j[0][0],))
        d_o_b = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
        cursor.execute("Update CRIMINAL set CRIMINALID=? where CRIMINALID=?", (c_id1.get(), j[0][0],))
        cursor.execute("Update CRIMINAL set FNAME=? where CRIMINALID=?", (fname1.get(), j[0][0],))
        cursor.execute("UPDATE CRIMINAL set MNAME=?  where CRIMINALID=?", (mname1.get(), j[0][0],))
        cursor.execute("UPDATE CRIMINAL set LNAME=?  where CRIMINALID=?", (lname1.get(), j[0][0],))
        cursor.execute("UPDATE CRIMINAL set DOB=?  where CRIMINALID=?", (d_o_b, j[0][0],))
        #cursor.execute("UPDATE CRIMINAL set Monthh=?  where CRIMINALID=?", (dob1.get(), j,))
        #cursor.execute("UPDATE CRIMINAL set Year=?  where CRIMINALID=?", (dob1.get(), j,))
        cursor.execute("UPDATE CRIMINAL set BLOODGROUP=?  where CRIMINALID=?", (bloodgrp1.get(), j[0][0],))
        cursor.execute("UPDATE CRIMINAL set STATUS=? where CRIMINALID=?", (status1.get(), j[0][0],))
        cursor.execute("UPDATE CRIMINAL set PRIORITY=? where CRIMINALID=?", (priority1.get(), j[0][0],))
        cursor.execute("UPDATE CRIMINAL set GENDER =? where CRIMINALID=?", (gender1.get(), j[0][0],))
        connection.commit()
        tkinter.messagebox.showinfo('TITLE','CRIMINAL RECORD UPDATED')

    def delete():
        try:
            cursor.execute('DELETE from CRIMINAL where CRIMINALID=?', (j[0][0],))
            cursor.execute('DELETE from CRIMINAL1 where CRIMINALID=?', (j[0][0],))
            cursor.execute('DELETE from CRIMINAL2 where CRIMINALID=?', (j[0][0],))
            cursor.execute('DELETE from CRIMINAL3 where CRIMINALID=?', (j[0][0],))
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
        else:
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Deletion Successfull')
            t.destroy()
            from acp_home import acp_home
            acp_home(p)

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

### Defining the text variables
    fn = StringVar(t)
    mn = StringVar(t)
    ln = StringVar(t)
    pid = StringVar(t)
    eid = StringVar(t)
    jur = StringVar(t)
    ms = StringVar(t)
    c1 = StringVar(t)
    #bch = StringVar(t)
    ima = StringVar(t)
    add = StringVar(t)
    hdd=  StringVar(t)

### Defining the Labels
    l_first_name = Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                         relief="solid")
    l_middle_name = Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                          relief="solid")
    l_last_name = Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                        relief="solid")
    gender = Label(t, text='Gender', font=fi, borderwidth=2, relief="solid")

    l_date_of_birth = Label(t, text='Date of Birth', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                            relief="solid")
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31]
    d = IntVar(t)
    day = OptionMenu(t, d, *dayOptionList)
    menu = t.nametowidget(day.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    monthOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
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

    bloodgrp = Label(t, text='Blood Group', font=fi, borderwidth=2, relief="solid")
    im = Label(t, text='Identification marks', font=fi, borderwidth=2, relief="solid")
    ad = Label(t, text='Address', font=fi, borderwidth=2, relief="solid")
    hd = Label(t, text='Contact number', font=fi, borderwidth=2, relief="solid")

    c_id = Label(t, text='Criminal ID', font=fi, borderwidth=2, relief="solid")
    status = Label(t, text='Status', font=fi, borderwidth=2, relief="solid")
    priority = Label(t, text='Priority', font=fi, borderwidth=2, relief="solid")

### Defining the Entry boxes
    fname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=fn, borderwidth=2,
                   relief="solid")
    mname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=mn, borderwidth=2,
                   relief="solid")
    lname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=ln, borderwidth=2,
                   relief="solid")
    gender1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=ms, borderwidth=2,
                    relief="solid")
    bloodgrp1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=c1, borderwidth=2,
                      relief="solid")
    im1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=ima, borderwidth=2,
                      relief="solid")
    ad1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=add, borderwidth=2,
                relief="solid")
    hd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=hdd, borderwidth=2,
                relief="solid")

    c_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=pid, borderwidth=2,
                  relief="solid")
    status1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=eid, borderwidth=2,
                    relief="solid")
    priority1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=jur, borderwidth=2,
                      relief="solid")

    #OptionList = [j1[0][1]]
    #v = tk.StringVar(t)
    #v.set('INDENTIFICATION MARKS ')
    #marks = tk.OptionMenu(t, v, *OptionList)
    #OptionList2 = [j2[0][1]]
    #OptionList3 = [j3[0][1]]
    #v2 = tk.StringVar(t)
    #v2.set('ADDRESS')
    #address = tk.OptionMenu(t, v2, *OptionList2)
    #v3 = tk.StringVar(t)
    #v3.set('HIDEOUTS')
    #hideout = tk.OptionMenu(t, v3, *OptionList3)
    #dob1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=c2, borderwidth=2, relief="solid")
    #age = Label(t, text='AGE', borderwidth=2, relief="solid")
    #age1 = Entry(t, text=b ,font=tkFont.Font(family="Times New Roman", size=30), textvariable=bch, borderwidth=2,relief="solid")


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
    day.place(x=275, y=330, width=130, height=50)
    month.place(x=405, y=330, width=130, height=50)
    year.place(x=535, y=330, width=140, height=50)
    bloodgrp1.place(x=275, y=400, width=400, height=50)
    im1.place(x=275, y=470, width=400, height=50)
    ad1.place(x=275, y=540, width=400, height=50)
    hd1.place(x=275, y=610, width=400, height=50)

    c_id1.place(x=1050, y=400, width=400, height=50)
    status1.place(x=1050, y=470, width=400, height=50)
    priority1.place(x=1050, y=540, width=400, height=50)

    '''cursor.execute("SELECT * FROM CRIMINAL where CRIMINALID=?", (j,))
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM CRIMINAL1 where CRIMINALID=?", (j,))
    l = []
    for row1 in cursor.fetchall():
        l.append(row1[1])
        print(row1)
    cursor.execute("SELECT * FROM CRIMINAL2 where CRIMINALID=?", (j,))
    l = []
    for row1 in cursor.fetchall():
        l.append(row1[1])
        print(row1)
    cursor.execute("SELECT * FROM CRIMINAL3 where CRIMINALID=?", (j,))
    l = []
    for row1 in cursor.fetchall():
        l.append(row1[1])
        print(row1)'''

### Defining the buttons
    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")
    delete = Button(t, text='DELETE', command=delete,font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=4,  relief="solid")
    submitt = Button(t, text='UPDATE RECORD', command=updated_user,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=4,  relief="solid")

    plus1 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_id_mark, borderwidth=4,
                   relief="solid")
    plus2 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_address, borderwidth=4,
                   relief="solid")
    plus3 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_contact, borderwidth=4,
                   relief="solid")

### Placing the buttons
    back_button.place(x=250, y=690, width=250, height=50)
    submitt.place(x=650, y=690, width=250, height=50)
    delete.place(x=1050, y=690, width=250, height=50)
    plus1.place(x=685, y=470, width=50, height=50)
    plus2.place(x=685, y=540, width=50, height=50)
    plus3.place(x=685, y=610, width=50, height=50)

### Setting the text variables
    fn.set(j[0][1])
    mn.set(j[0][2])
    ln.set(j[0][3])
    pid.set(j[0][0])
    eid.set(j[0][6])
    jur.set(j[0][7])
    ms.set(j[0][8])
    c1.set(j[0][5])
    #v.set(j1[0][1])
    #v2.set(j2[0][1])
    #v3.set(j3[0][1])
    ima.set(j1[0][1])
    add.set(j2[0][1])
    hdd.set(j3[0][1])

    d_o_b = j[0][4]
    s = d_o_b.split('-')
    d.set(int(s[2]))
    mth.set(int(s[1]))
    y.set(int(s[0]))

### Putting the image Button
    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 250), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Button(t, image=t.photo1, command=image_update,borderwidth=2, relief="solid")
    t.img1.image = t.photo1

### Placing the image Button
    t.img1.place(x=1025, y=50, width=250, height=250)

    mainloop()