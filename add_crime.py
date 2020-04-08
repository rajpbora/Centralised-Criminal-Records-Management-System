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
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY,DAMAGEAMOUNT number,INJURED number,DEATHS number,DATEOFCRIME text,PLACEOFCRIME text)')
        cursor.execute("INSERT INTO CRIME VALUES(?,?,?,?,?,?)", (fir_no1.get(), da1.get(), noi1.get(), nod1.get(), doc1.get(), poc1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2(FIRNO number PRIMARY KEY,CRIMINALID number)')
        cursor.execute("INSERT INTO CRIME2 VALUES(?,?)", (fir_no1.get(),ci1.get()))
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS CRIME3(FIRNO number PRIMARY KEY,PENALCODETYPE text,SECTIONNUMBER number)')
        cursor.execute("INSERT INTO CRIME3 VALUES(?,?,?)", (fir_no1.get(), pc1.get(),sn1.get()))
        connection.commit()
        connection.close()
        tkinter.messagebox.showinfo('Confirmation', 'created')
        t.destroy()
        from acp_home import acp_home
        acp_home(p)
    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    fi = tkFont.Font(family="Times New Roman", size=16)
    fih = tkFont.Font(family="Times New Roman", size=20)
    noi=Label(t, text='NUMBER OF INJURIES',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    nod=Label(t, text='NUMBER OF DEATHS',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    #name1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    noi1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    nod1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")

    fir_no=Label(t, text='FIR',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    poc=Label(t, text='PLACE OF CRIME',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    fir_no1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),   borderwidth=2, relief="solid")
    poc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    ci = Label(t, text='CRIMINAL ID',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    ci1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2,
                 relief="solid")
    
    doc=Label(t, text='DATE OF CRIME',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    doc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    sn = Label(t, text='SECTION NO',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")
    pc = Label(t, text='PENAL CODE',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    pc1 = Entry(t, font=tkFont.Font(family="PENAL CODE", size=30),  borderwidth=2, relief="solid")
    back_button = Button(t, text='Go Back',font=fih, command=back, borderwidth=2, relief="solid", width=20, height=2).place(x=950, y=700)
    #OptionList2=[k2[0][1]]
    #OptionList3=[k2[0][2]]
    #v2 = tk.StringVar(t)
    #v2.set('SECTION NO')
    #sn= tk.OptionMenu(t, v2, *OptionList2)
    #v3 = tk.StringVar(t)
    #v3.set('PENAL CODE')
    #pc=tk.OptionMenu(t, v3, *OptionList3)

    da=Label(t, text='DAMAGE AMOUNT',font=fi, borderwidth=2, relief="solid", width=15,height=2)
    da1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  borderwidth=2, relief="solid")

    submit=Button(t,text='submit',font=fih,command=add, borderwidth=2, relief="solid", width=20,height=2)
    # name.place(x=50, y=150, width=150, height=70)
    noi.place(x=50, y=465)
    nod.place(x=50,y=400)
    # name1.place(x=225, y=150, width=150, height=70)
    noi1.place(x=300,y=465)
    nod1.place(x=300,y=400)
    fir_no.place(x=50, y=10)

    fir_no1.place(x=300, y=10)

    poc.place(x=50, y=205)
    poc1.place(x=300,y=205)

    pc.place(x=50, y=270)
    pc1.place(x=300,y=270)
    sn.place(x=50, y=335)
    sn1.place(x=300,y=335)
    ci.place(x=50,y=75)
    ci1.place(x=300, y=75)

    da.place(x=50, y=530)
    da1.place(x=300, y=530)
    doc.place(x=50,y=140)
    doc1.place(x=300, y=140)

    submit.place(x=950, y=600)
    mainloop()