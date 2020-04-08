from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3

def best1(p,k,k1,k2,):
    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    t=tk.Tk()
    t.title('CRIME')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    fih = tkFont.Font(family="Times New Roman", size=20)


    def update_crime():
        cursor.execute("Update CRIME set FIRNO=? where FIRNO=?", (fir_no1.get(), k[0][0],))
        cursor.execute("Update CRIME set DAMAGEAMOUNT=? where FIRNO=?", (da1.get(), k[0][0],))
        cursor.execute("UPDATE CRIME set INJURED=?  where FIRNO=?", (noi1.get(), k[0][0],))
        cursor.execute("UPDATE CRIME set DEATHS=?  where FIRNO=?", (nod1.get(), k[0][0],))
        # cursor.execute("UPDATE CRIMINAL set Datee=?  where CRIMINALID=?", (dob1.get(), j,))
        # cursor.execute("UPDATE CRIMINAL set Monthh=?  where CRIMINALID=?", (dob1.get(), j,))
        # cursor.execute("UPDATE CRIMINAL set Year=?  where CRIMINALID=?", (dob1.get(), j,))
        cursor.execute("UPDATE CRIME set DATEOFCRIME=?  where FIRNO=?", (doc1.get(), k[0][0],))
        cursor.execute("UPDATE CRIME2 set CRIMINALID=? where FIRNO=?", (ci1.get(), k1[0][0],))
        cursor.execute("UPDATE CRIME3 set SECTIONNUMBER=? where FIRNO=?", (sn1.get(), k2[0][0],))
        cursor.execute("UPDATE CRIME3 set PENALCODETYPE =? where FIRNO=?", (pc1.get(), k2[0][0],))
        cursor.execute("UPDATE CRIME set PLACEOFCRIME =? where FIRNO=?", (poc1.get(), k[0][0],))
        #cursor.execute("UPDATE CRIME set IDENTIFICATIONMARKS=? where CRIMINALID=?", (v.get(), j1[0][0],))
        #cursor.execute("UPDATE CRIMINAL2 set ADDRESS=? where CRIMINALID=?", (v2.get(), j2[0][0],))
        #cursor.execute("UPDATE CRIMINAL3 set CONTACT=? where CRIMINALID=?", (v3.get(), j3[0][0],))
        connection.commit()
        tkinter.messagebox.showinfo('TITLE','FIR UPDATED')
    def delete():
        cursor.execute('DELETE from CRIME where FIRNO=?', (k[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIME2 where FIRNO=?', (k1[0][0],))
        connection.commit()
        cursor.execute('DELETE from CRIME3 where FIRNO=?', (k2[0][0],))
        connection.commit()
        tkinter.messagebox.showinfo('TITLE','FIR DELETED')




    fir = StringVar(t)
    daa = StringVar(t)
    ing = StringVar(t)
    de = StringVar(t)
    dc = StringVar(t)
    pcr = StringVar(t)
    cii = StringVar(t)
    snn = StringVar(t)
    pcc = StringVar(t)
    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)



    #name=Label(t, text='Victim name', borderwidth=2, relief="solid")
    noi=Label(t, text='NUMBER OF INJURIES',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    nod=Label(t, text='NUMBER OF DEATHS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    #name1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    noi1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), textvariable=ing, borderwidth=2, relief="solid")
    nod1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),  textvariable=de, borderwidth=2, relief="solid")

    fir_no=Label(t, text='FIR',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    poc=Label(t, text='PLACE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    fir_no1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16),  textvariable=fir, borderwidth=2, relief="solid")
    poc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30),textvariable=pcr, borderwidth=2, relief="solid")
    ci = Label(t, text='CRIMINAL ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    ci1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), textvariable=cii, borderwidth=2,
                 relief="solid")
    # OptionList=[k1[0][1]]
    #v = tk.StringVar(t)
    #v.set('CRIMINAL')
    #c_id= tk.OptionMenu(t, v, *OptionList)
    doc=Label(t, text='DATE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    doc1=Entry(t,font=tkFont.Font(family="Times New Roman", size=16), textvariable=dc, borderwidth=2, relief="solid")
    sn = Label(t, text='SECTION NO',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    sn1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=16), textvariable=snn, borderwidth=2, relief="solid")
    pc = Label(t, text='PENAL CODE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    pc1 = Entry(t, font=tkFont.Font(family="PENAL CODE", size=30), textvariable=pcc, borderwidth=2, relief="solid")
    #OptionList2=[k2[0][1]]
    #OptionList3=[k2[0][2]]
    #v2 = tk.StringVar(t)
    #v2.set('SECTION NO')
    #sn= tk.OptionMenu(t, v2, *OptionList2)
    #v3 = tk.StringVar(t)
    #v3.set('PENAL CODE')
    #pc=tk.OptionMenu(t, v3, *OptionList3)

    da=Label(t, text='DAMAGE AMOUNT',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    da1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), textvariable=daa,  borderwidth=2, relief="solid")
    delete=Button(t, text='delete',command=delete,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid", width=20,height=2)
    submit=Button(t,text='submit',command=update_crime,font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid", width=20,height=2)
    back_button = Button(t, text='Go Back',font=fih,command=back, borderwidth=2, relief="solid", width=20, height=2).place(
        x=950, y=700)

    fir.set(k[0][0])
    daa.set(k[0][1])
    ing.set(k[0][2])
    de.set(k[0][3])
    dc.set(k[0][4])
    # v.set(k1[0][1])
    #v2.set(k2[0][1])
    #v3.set(k2[0][1])
    pcr.set(k[0][5])
    cii.set(k1[0][1])
    pcc.set(k2[0][1])
    snn.set(k2[0][2])

    noi.place(x=50, y=490)
    nod.place(x=50, y=430)
    # name1.place(x=225, y=150, width=150, height=70)
    noi1.place(x=300, y=490)
    nod1.place(x=300, y=430)
    fir_no.place(x=50, y=10)

    fir_no1.place(x=300, y=10)

    poc.place(x=50, y=205)
    poc1.place(x=300, y=205)

    pc.place(x=50, y=270)
    pc1.place(x=300, y=270)
    sn.place(x=50, y=335)
    sn1.place(x=300, y=335)
    ci.place(x=50, y=75)
    ci1.place(x=300, y=75)

    da.place(x=50, y=555)
    da1.place(x=300, y=555)
    doc.place(x=50, y=140)
    doc1.place(x=300, y=140)
    delete.place(x=750, y=600)
    submit.place(x=950, y=600)
    mainloop()