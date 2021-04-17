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
    t.geometry('600x400')

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

    u=cursor.execute('SELECT COMPLAINT_NO from COMPLAINT where STATUS = "Complaint Filed"')
    mcq=u.fetchall()

    if len(mcq)!=0:
        complist = []
        for i in range(len(mcq)):
            complist.append(mcq[i][0])

        v = tk.StringVar(t)
        v.set('ADD FOR')
        opti = tk.OptionMenu(t, v, *complist)
        opti.place(x=200, y=100, width=225, height=70)
        opti.configure(relief="solid")
        menu = t.nametowidget(opti.menuname)
        menu.config(font=tkFont.Font(family="Times New Roman", size=16))
        opti.configure(relief="solid", font=tkFont.Font(family="Times New Roman", size=16))

        submit = Button(t, text='SUBMIT', command=nex, borderwidth=4, relief="solid",
                        font=tkFont.Font(family="Times New Roman", size=16))
        submit.place(x=225, y=200, width=175, height=50)

    else:
        fi = tkFont.Font(family="Times New Roman", size=16)
        fm = Label(t, text='NO COMPLAINTS', font=fi, borderwidth=2, relief="solid")
        fm.place(x=200, y=100, width=225, height=70)

    back = Button(t, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)

    mainloop()