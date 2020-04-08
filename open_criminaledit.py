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


def test1(p,j, j1, j2, j3,photoPath):
    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    t = tk.Tk()
    t.title('CRIMINAL')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    born1 = j[0][4]
    sss = born1.split('-')
    mmm = datetime.datetime.today()

    b = mmm.year - int(sss[0])
    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    def image_update():
        t.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("jpeg files", ".jpg"), ("all files", ".*")), master=t)
        t.load = Image.open(t.filename)
        t.load = t.load.resize((230, 200), Image.ANTIALIAS)
        t.photo1 = ImageTk.PhotoImage(t.load, master=t)
        t.img1 = Button(t, image=t.photo1, command=image_update)
        t.img1.image = t.photo1
        t.img1.place(x=1000, y=100,  width=200, height=200)
        empPhoto = convertToBinaryData(t.filename)
        cursor.execute("Update CRIMINAL set PHOTO=? where CRIMINALID=?", (empPhoto, j[0][0],))

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def updated_user():
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
        cursor.execute("UPDATE CRIMINAL1 set IDENTIFICATIONMARKS=? where CRIMINALID=?", (im1.get(), j1[0][0],))
        cursor.execute("UPDATE CRIMINAL2 set ADDRESS=? where CRIMINALID=?", (ad1.get(), j2[0][0],))
        cursor.execute("UPDATE CRIMINAL3 set CONTACT=? where CRIMINALID=?", (hd1.get(), j3[0][0],))

        connection.commit()
        tkinter.messagebox.showinfo('TITLE','CRIMINAL RECORD UPDATED')




    def delete():
        cursor.execute('DELETE from CRIMINAL where CRIMINALID=?', (j[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIMINAL1 where CRIMINALID=?', (j[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIMINAL2 where CRIMINALID=?', (j[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIMINAL3 where CRIMINALID=?', (j[0][0],))
        connection.commit()
        tkinter.messagebox.showinfo('TITLE','CRIMINAL RECORD DELETED')

    fn = StringVar(t)
    mn = StringVar(t)
    ln = StringVar(t)
    pid = StringVar(t)
    eid = StringVar(t)
    jur = StringVar(t)
    ms = StringVar(t)
    c1 = StringVar(t)
    c2 = StringVar(t)
    #bch = StringVar(t)
    ima = StringVar(t)
    add = StringVar(t)
    hdd=  StringVar(t)
    fih = tkFont.Font(family="Times New Roman", size=20)

    fname = Label(t, text='Full Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18, height=2)
    fname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=fn, borderwidth=2,
                   relief="solid")
    mname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=mn, borderwidth=2,
                   relief="solid")
    lname1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=ln, borderwidth=2,
                   relief="solid")
    priority = Label(t, text='Priority',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18, height=2)
    c_id = Label(t, text='Criminal ID',font=tkFont.Font(family="Times New Roman", size=16),borderwidth=2, relief="solid", width=18, height=2)
    status = Label(t, text='status',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,  relief="solid", width=18, height=2)
    c_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=pid, borderwidth=2,
                  relief="solid")
    status1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=eid, borderwidth=2,
                    relief="solid")
    priority1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=jur, borderwidth=2,
                      relief="solid")
    gender = Label(t, text='Gender',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18, height=2)
    gender1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=ms, borderwidth=2,
                    relief="solid")
    bloodgrp = Label(t, text='BLDGRP',font=tkFont.Font(family="Times New Roman", size=16),  borderwidth=2, relief="solid", width=18, height=2)
    bloodgrp1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=c1, borderwidth=2,
                      relief="solid")
    im = Label(t, text='INDENTIFICATION MARKS',font=tkFont.Font(family="Times New Roman", size=16),  borderwidth=2, relief="solid", width=18, height=2)
    im1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=ima, borderwidth=2,
                      relief="solid")
    ad = Label(t, text='ADDRESS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,  relief="solid", width=18, height=2)
    ad1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=add, borderwidth=2,
                relief="solid")
    hd = Label(t, text='CONTACT',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18, height=2)
    hd1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=hdd, borderwidth=2,
                relief="solid")
    back_button = Button(t, text='Go Back',font=fih, command=back, borderwidth=2, relief="solid", width=26, height=2).place(
        x=950, y=700)
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31]  # check for february and invalid details
    d = IntVar(t)
    d.set('Day')
    day = OptionMenu(t, d, *dayOptionList)
    monthOptionList = ['01','02','03','04','05','06','07','08','09','10','11','12']  # check for february and invalid details
    mth = StringVar(t)
    mth.set('Month')
    month = OptionMenu(t, mth, *monthOptionList)
    yearOptionList = []
    for i in range(1900, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    y.set('Year')
    u = str(y) + '-' + str(mth) + '-' + str(d)
    year = OptionMenu(t, y, *yearOptionList)
    day.place(x=300, y=140)
    month.place(x=380, y=140)
    year.place(x=480, y=140)


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
    dob = Label(t, text='DATE OF BIRTH',font=tkFont.Font(family="Times New Roman", size=16),  borderwidth=2, relief="solid", width=18, height=2)
    #dob1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=c2, borderwidth=2, relief="solid")
    #age = Label(t, text='AGE', borderwidth=2, relief="solid")
    #age1 = Entry(t, text=b ,font=tkFont.Font(family="Times New Roman", size=30), textvariable=bch, borderwidth=2,relief="solid")
    delete = Button(t, text='delete', command=delete,font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,  relief="solid", width=20, height=2)
    submitt = Button(t, text='submit', command=updated_user,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,  relief="solid", width=20, height=2)

    d_o_b = j[0][4]
    s = d_o_b.split('-')
    d.set(int(s[2]))
    mth.set(int(s[1]))
    y.set(int(s[0]))



    c_id.place(x=50, y=75)
    priority.place(x=50, y=560)
    c_id1.place(x=300, y=75)
    priority1.place(x=300, y=560)
    status.place(x=50, y=625)
    status1.place(x=300, y=625)
    fname.place(x=50, y=10)
    fname1.place(x=300, y=10)
    mname1.place(x=700, y=10)
    lname1.place(x=1100, y=10)

    hd.place(x=50, y=465)
    hd1.place(x=300, y=465)
    ad.place(x=50, y=335)
    ad1.place(x=300, y=335)
    im.place(x=50, y=400)
    im1.place(x=300, y=400)
    gender.place(x=50, y=270)
    gender1.place(x=300, y=270)
    dob.place(x=50, y=140)


    bloodgrp.place(x=50, y=205)
    bloodgrp1.place(x=300, y=205)
    delete.place(x=950, y=600)
    submitt.place(x=1250, y=600)

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

    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 350), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Button(t, image=t.photo1, command=image_update)
    t.img1.image = t.photo1
    t.img1.place(x=1000, y=100, width=200, height=200)



    mainloop()