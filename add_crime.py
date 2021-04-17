from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def add1(p):
    t = tk.Tk()
    t.title('CRIMEADD')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def add():
        try:
            d_o_c = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY,DAMAGEAMOUNT number,INJURED number,DEATHS number,DATEOFCRIME text,PLACEOFCRIME text)')
            cursor.execute("INSERT INTO CRIME VALUES(?,?,?,?,?,?)",
                           (fir_no1.get(), da1.get(), noi1.get(), nod1.get(), d_o_c, poc1.get()))
            cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2(FIRNO number PRIMARY KEY,CRIMINALID number)')
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS CRIME3(FIRNO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number)')
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
        else:
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation', 'Crime record created')
            t.destroy()
            from acp_home import acp_home
            acp_home(p)

    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    def add_cid():
        try:
            if fir_no1.get()!='' and ci1.get()!='':
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY,DAMAGEAMOUNT number,INJURED number,DEATHS number,DATEOFCRIME text,PLACEOFCRIME text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2(FIRNO number PRIMARY KEY,CRIMINALID number)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIME3(FIRNO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number)')
                cursor.execute("INSERT INTO CRIME2 VALUES(?,?)", (fir_no1.get(), ci1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "Put FIR No.")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
            ci1.delete(0, 'end')
        else:
            if fir_no1.get() != '' and ci1.get()!='':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            ci1.delete(0, 'end')
            return

    def add_con():
        try:
            if fir_no1.get()!='' and sn1.get()!='' and pc1.get()!='':
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY,DAMAGEAMOUNT number,INJURED number,DEATHS number,DATEOFCRIME text,PLACEOFCRIME text)')
                cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2(FIRNO number PRIMARY KEY,CRIMINALID number)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS CRIME3(FIRNO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number)')
                cursor.execute("INSERT INTO CRIME3 VALUES(?,?,?)", (fir_no1.get(), pc1.get(), sn1.get()))
            else:
                tkinter.messagebox.showinfo('Alert', "FIR No./ Penal Code/ Section Number Missing")
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
            pc1.delete(0, 'end')
            sn1.delete(0, 'end')
        else:
            if fir_no1.get() != '' and sn1.get()!='' and pc1.get()!='':
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'Added')
            pc1.delete(0, 'end')
            sn1.delete(0, 'end')
            return

    def clear_details():
        fir_no1.delete(0, 'end')
        ci1.delete(0, 'end')
        poc1.delete(0, 'end')
        pc1.delete(0, 'end')
        sn1.delete(0, 'end')
        nod1.delete(0, 'end')
        noi1.delete(0, 'end')
        da1.delete(0, 'end')

        d.set('dd')
        mth.set('mm')
        y.set('yyyy')
        return

### Defining the Labels
    fir_no = Label(t, text='FIR Number', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                         relief="solid")
    ci = Label(t, text='Criminal ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                          relief="solid")
    doc = Label(t, text='Date of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                        relief="solid")
    poc = Label(t, text='Place of Crime',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    pc = Label(t, text='Penal Code',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    sn = Label(t, text='Section No.',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    nod = Label(t, text='No. of Deaths',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    noi = Label(t, text='No. of Injured',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    da = Label(t, text='Cost of Damages',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

### Defining the Entry boxes
    fir_no1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,
                   relief="solid")
    ci1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")

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

    poc1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,
                   relief="solid")
    pc1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")
    nod1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2,
                   relief="solid")
    noi1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")
    da1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),  borderwidth=2,
                   relief="solid")

    #name1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    #OptionList2=[k2[0][1]]
    #OptionList3=[k2[0][2]]
    #v2 = tk.StringVar(t)
    #v2.set('SECTION NO')
    #sn= tk.OptionMenu(t, v2, *OptionList2)
    #v3 = tk.StringVar(t)
    #v3.set('PENAL CODE')
    #pc=tk.OptionMenu(t, v3, *OptionList3)

### Placing the Labels
    fir_no.place(x=50, y=50, width=200, height=50)
    ci.place(x=50, y=120, width=200, height=50)
    doc.place(x=50, y=190, width=200, height=50)
    poc.place(x=50, y=260, width=200, height=50)
    pc.place(x=50, y=330, width=200, height=50)
    sn.place(x=50, y=400, width=200, height=50)
    nod.place(x=50, y=470, width=200, height=50)
    noi.place(x=50, y=540, width=200, height=50)
    da.place(x=50, y=610, width=200, height=50)

### Placing the Entry Boxes
    fir_no1.place(x=275, y=50, width=400, height=50)
    ci1.place(x=275, y=120, width=400, height=50)
    day.place(x=275, y=190,width=130, height=50)
    month.place(x=405, y=190,width=130, height=50)
    year.place(x=535, y=190,width=140, height=50)
    poc1.place(x=275, y=260, width=400, height=50)
    pc1.place(x=275, y=330, width=400, height=50)
    sn1.place(x=275, y=400, width=400, height=50)
    nod1.place(x=275, y=470, width=400, height=50)
    noi1.place(x=275, y=540, width=400, height=50)
    da1.place(x=275, y=610, width=400, height=50)

    # name.place(x=50, y=150, width=150, height=70)
    # name1.place(x=225, y=150, width=150, height=70)

### Defining the buttons
    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")
    submitt = Button(t, text='ADD RECORD', font=tkFont.Font(family="Times New Roman", size=16), command=add,
                     borderwidth=4, relief="solid")
    reset = Button(t, text='RESET', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details,
                   borderwidth=4, relief="solid")

    plus11 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_cid, borderwidth=4,
                   relief="solid")
    plus22 = Button(t, text='+', font=tkFont.Font(family="Times New Roman", size=24), command=add_con, borderwidth=4,
                   relief="solid")

### Placing the buttons
    back_button.place(x=250, y=690, width=250, height=50)
    submitt.place(x=650, y=690, width=250, height=50)
    reset.place(x=1050, y=690, width=250, height=50)
    plus11.place(x=685, y=120, width=50, height=50)
    plus22.place(x=685, y=330, width=50, height=120)

### Setting the initial variables
    d.set('dd')
    mth.set('mm')
    y.set('yyyy')

    req = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                borderwidth=0)
    req1 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req2 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req3 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req4 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req5 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req6 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req7 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req8 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)

    req.place(x=675, y=50, width=10, height=50)
    req1.place(x=675, y=120, width=10, height=50)
    req2.place(x=675, y=190, width=10, height=50)
    req3.place(x=675, y=260, width=10, height=50)
    req4.place(x=675, y=330, width=10, height=50)
    req5.place(x=675, y=400, width=10, height=50)
    req6.place(x=675, y=470, width=10, height=50)
    req7.place(x=675, y=540, width=10, height=50)
    req8.place(x=675, y=610, width=10, height=50)

    mainloop()