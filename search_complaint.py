from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import os
import sqlite3

def selcomp(p):

    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()

    t=tk.Tk()
    t.title('NCDS - Select Complaint ')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    u=cursor.execute('SELECT COMPLAINT_NO from COMPLAINT where STATUS = "Complaint Filed"')
    mcq=u.fetchall()
    complist=[]
    try:
        for i in range(len(mcq)):
            complist.append(mcq[i][0])
    except:
        complist=['NO COMPLAINTS']   
    v = tk.StringVar(t)
    v.set('ADD FOR')
    opti = tk.OptionMenu(t, v, *complist)
    opti.place(x=615, y=300, width=350, height=80)
    opti.configure( relief="solid")

    def nex():
        xyz=v.get()
        if xyz=='ADD FOR':
            tkinter.messagebox.showinfo('Alert','Select Complaint Number')
        else:
            t.destroy()
            import compdisp as tty
            tty.compdisplay(p,xyz)

    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(p)

    submit = Button(t, text='Submit', command=nex, borderwidth=2, relief="solid")
    submit.place(x=680, y=450, width=200, height=70)
    back_button = Button(t, text='BACK', command=back, borderwidth=2, relief="solid", width=10, height=2).place(x=50, y=50)
    mainloop()