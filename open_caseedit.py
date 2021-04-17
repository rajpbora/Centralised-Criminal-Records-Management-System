from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3

def fest1(p,iy,i1,i2,i3):
    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    t=tk.Tk()
    t.title('CASE')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    print(iy)

    def update_case():
        od1 = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
        if s1[0] != 'yyyy' and s1[1] != 'mm' and s1[2] != 'dd':
            cd1 = str(y1.get()) + '-' + str(mth1.get()) + '-' + str(d1.get())
        else:
            cd1 = y1.get() + '-' + mth1.get() + '-' + d1.get()

        

        cursor.execute("Update CASE1 set CASENO=? where CASENO=?", (case_id1.get(), iy[0][0],))
        cursor.execute("Update CASE1 set PENALCODETYPE=? where CASENO=?", (pno1.get(), iy[0][0],))
        cursor.execute("Update CASE1 set SECTIONNUMBER =? where CASENO=?", (sn1.get(), iy[0][0],))
        cursor.execute("Update CASE1 set POLICESTATION=? where CASENO=?", (ps1.get(), iy[0][0],))
        cursor.execute("Update CASE1 set DESCRIPTION=? where CASENO=?", (desc1.get(), iy[0][0],))
        cursor.execute("Update CASE1 set OPENDATE=? where CASENO=?", (od1, iy[0][0],))
        cursor.execute("Update CASE1 set CLOSEDATE=? where CASENO=?", (cd1, iy[0][0],))
        connection.commit()
        tkinter.messagebox.showinfo('TITLE','CASE UPDATED')

    def delete():
        try:
            cursor.execute('DELETE from CASE1 where CASENO=?', (iy[0][0],))
            cursor.execute('DELETE from CASE2 where CASENO=?', (i1[0][0],))
            cursor.execute('DELETE from CASE2 where CASENO=?', (i2[0][0],))
            cursor.execute('DELETE from CASE4 where CASENO=?', (i3[0][0],))
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
        else:
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Deletion Successfull')
            t.destroy()
            from acp_home import acp_home
            acp_home(p)

    def add_vic():
        try:
            if case_id1.get() != '' and victim11.get() != '' and victim31.get() != '' and age1.get() != '':
                cursor.execute("INSERT INTO CASE3 VALUES(?,?,?,?,?,?)",
                               (case_id1.get(), victim11.get(), victim21.get(), victim31.get(), age1.get(),
                                address1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "Victim Details/ Case Id is missing.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : " + str(e))
            victim11.delete(0, 'end')
            victim21.delete(0, 'end')
            victim31.delete(0, 'end')
            age1.delete(0, 'end')
            address1.delete(0, 'end')
        else:
            if case_id1.get() != '' and victim11.get() != '' and victim31.get() != '' and age1.get() != '':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            victim11.delete(0, 'end')
            victim21.delete(0, 'end')
            victim31.delete(0, 'end')
            age1.delete(0, 'end')
            address1.delete(0, 'end')
            return

    def add_fir():
        try:
            if case_id1.get() != '' and fr1.get() != '':
                cursor.execute("INSERT INTO CASE4 VALUES(?,?)", (case_id1.get(), fr1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "FIR No./ Case Id.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : " + str(e))
            fr1.delete(0, 'end')
        else:
            if case_id1.get() != '' and fr1.get() != '':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            fr1.delete(0, 'end')
            return

    def add_pid():
        try:
            if case_id1.get() != '' and pi1.get() != '':
                cursor.execute("INSERT INTO CASE2 VALUES(?,?)", (case_id1.get(), pi1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "Police Id/ Case Id is missing.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : " + str(e))
            pi1.delete(0, 'end')
        else:
            if case_id1.get() != '' and pi1.get() != '':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            pi1.delete(0, 'end')
            return

    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    fi = tkFont.Font(family="Times New Roman", size=16)

### Defining Text Variables
    ci = StringVar(t)
    pii = StringVar(t)
    pss = StringVar(t)
    pnoo = StringVar(t)
    snn = StringVar(t)
    des = StringVar(t)

    frn = StringVar(t)
    vn = StringVar(t)
    vn1 = StringVar(t)
    vn2 = StringVar(t)
    ag = StringVar(t)
    addre= StringVar(t)

### Defining the Labels
    status = Label(t, text='Complaint No.', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                   relief="solid")
    case_id = Label(t, text='Case ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                    relief="solid")
    pi = Label(t, text='Police ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
               relief="solid")
    ps = Label(t, text='Police Station', font=fi, borderwidth=2, relief="solid")

    od = Label(t, text='Opening Date', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                            relief="solid")
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31]
    monthOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    yearOptionList = []
    for i in range(2000, 2020):
        yearOptionList.append(i)

    d = IntVar(t)
    day = OptionMenu(t, d, *dayOptionList)
    menu = t.nametowidget(day.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    mth = IntVar(t)
    month = OptionMenu(t, mth, *monthOptionList)
    menu = t.nametowidget(month.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    y = IntVar(t)
    year = OptionMenu(t, y, *yearOptionList)
    menu = t.nametowidget(year.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    day.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    month.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    year.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    cd = Label(t, text='Closing Date', font=fi, borderwidth=2, relief="solid")

    dayOptionList1 = []
    for i in range(1, 32):
        dayOptionList1.append(str(i))
    monthOptionList1 = []
    for i in range(1, 13):
        monthOptionList1.append(str(i))
    yearOptionList1 = []
    for i in range(2000, 2020):
        yearOptionList1.append(str(i))
    print(monthOptionList1)

    d1 = StringVar(t)
    day1 = OptionMenu(t, d1, *dayOptionList1)
    menu = t.nametowidget(day1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    mth1 = StringVar(t)
    month1= OptionMenu(t, mth1, *monthOptionList1)
    menu = t.nametowidget(month1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    y1 = StringVar(t)
    year1 = OptionMenu(t, y1, *yearOptionList1)
    menu = t.nametowidget(year1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    day1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    month1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    year1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    pno = Label(t, text='Penal Code', font=fi, borderwidth=2, relief="solid")
    sn = Label(t, text='Section no.', font=fi, borderwidth=2, relief="solid")
    desc = Label(t, text='Description', font=fi, borderwidth=2, relief="solid")

    fr = Label(t, text='FIR No.', font=fi, borderwidth=2, relief="solid")
    victim1 = Label(t, text='Victim First Name', font=fi, borderwidth=2, relief="solid")
    victim2 = Label(t, text='Victim Middle Name', font=fi, borderwidth=2, relief="solid")
    victim3 = Label(t, text='Victim Last Name', font=fi, borderwidth=2, relief="solid")
    age = Label(t, text='Victim Age', font=fi, borderwidth=2, relief="solid")
    address = Label(t, text='Victim Address', font=fi, borderwidth=2, relief="solid")

### Defining the Entry boxes
    status1 = Label(t, text=iy[0][7], font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,relief="solid")
    case_id1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=ci, borderwidth=2,
                     relief="solid")
    pi1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=pii, borderwidth=2,
                relief="solid")
    ps1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=pss, borderwidth=2,
                relief="solid")
    pno1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=pnoo, borderwidth=2,
                 relief="solid")
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=snn, borderwidth=2,
                relief="solid")
    desc1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=des, borderwidth=2,
                  relief="solid")

    fr1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=frn, borderwidth=2, relief="solid")
    victim11 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=vn, borderwidth=2, relief="solid")
    victim21 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=vn1, borderwidth=2, relief="solid")
    victim31 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=vn2, borderwidth=2,
                     relief="solid")
    age1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=ag, borderwidth=2,
                 relief="solid")
    address1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), textvariable=addre, borderwidth=2,
                     relief="solid")

### Placing the Labels
    status.place(x=50, y=50, width=200, height=50)
    case_id.place(x=50, y=120, width=200, height=50)
    pi.place(x=50, y=190, width=200, height=50)
    ps.place(x=50, y=260, width=200, height=50)
    od.place(x=50, y=330, width=200, height=50)
    cd.place(x=50, y=400, width=200, height=50)
    pno.place(x=50, y=470, width=200, height=50)
    sn.place(x=50, y=540, width=200, height=50)
    desc.place(x=50, y=610, width=200, height=50)

    fr.place(x=825, y=190, width=200, height=50)
    victim1.place(x=825, y=260, width=200, height=50)
    victim2.place(x=825, y=330, width=200, height=50)
    victim3.place(x=825, y=400, width=200, height=50)
    age.place(x=825, y=470, width=200, height=50)
    address.place(x=825, y=540, width=200, height=50)

### Placing the Entry Boxes
    status1.place(x=275, y=50, width=400, height=50)
    case_id1.place(x=275, y=120, width=400, height=50)
    pi1.place(x=275, y=190, width=400, height=50)
    ps1.place(x=275, y=260, width=400, height=50)

    day.place(x=275, y=330, width=130, height=50)
    month.place(x=405, y=330, width=130, height=50)
    year.place(x=535, y=330, width=140, height=50)

    day1.place(x=275, y=400, width=130, height=50)
    month1.place(x=405, y=400, width=130, height=50)
    year1.place(x=535, y=400, width=140, height=50)

    pno1.place(x=275, y=470, width=400, height=50)
    sn1.place(x=275, y=540, width=400, height=50)
    desc1.place(x=275, y=610, width=400, height=50)

    fr1.place(x=1050, y=190, width=400, height=50)
    victim11.place(x=1050, y=260, width=400, height=50)
    victim21.place(x=1050, y=330, width=400, height=50)
    victim31.place(x=1050, y=400, width=400, height=50)
    age1.place(x=1050, y=470, width=400, height=50)
    address1.place(x=1050, y=540, width=400, height=50)

### Defining the buttons
    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")
    submitt = Button(t, text='UPDATE RECORD', font=tkFont.Font(family="Times New Roman", size=16), command=update_case,
                     borderwidth=4, relief="solid")
    delete = Button(t, text='DELETE', font=tkFont.Font(family="Times New Roman", size=16), command=delete,
                   borderwidth=4, relief="solid")

    plus1 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_vic, borderwidth=4,
                   relief="solid")
    plus2 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_fir, borderwidth=4,
                   relief="solid")
    plus3 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_pid, borderwidth=4,
                   relief="solid")

### Placing the buttons
    back_button.place(x=250, y=690, width=250, height=50)
    submitt.place(x=650, y=690, width=250, height=50)
    delete.place(x=1050, y=690, width=250, height=50)
    plus1.place(x=1460, y=260, width=50, height=330)
    plus2.place(x=1460, y=190, width=50, height=50)
    plus3.place(x=685, y=190, width=50, height=50)

### Setting the initial variables
    ci.set(iy[0][0])
    #v3.set(i3[0][1])
    pss.set(iy[0][3])
    des.set(iy[0][4])

    vn.set(i2[0][1])
    vn1.set(i2[0][2])
    vn2.set(i2[0][3])
    ag.set(i2[0][4])
    #v.set(i[0][1])
    #v2.set(i[0][1])
    frn.set(i3[0][1])
    pnoo.set(iy[0][1])
    pii.set(i1[0][1])
    addre.set(i2[0][5])
    snn.set(iy[0][2])

    o = iy[0][5]
    s = o.split('-')
    d.set(int(s[2]))
    mth.set(int(s[1]))
    y.set(int(s[0]))


    c = iy[0][6]
    s1 = c.split('-')
    if s1[0]!='yyyy' and s1[1]!='mm' and s1[2]!='dd':
        d1.set(int(s1[2]))
        mth1.set(int(s1[1]))
        y1.set(int(s1[0]))
    else:
        d1.set('dd')
        mth1.set('mm')
        y1.set('yyyy')

    mainloop()
