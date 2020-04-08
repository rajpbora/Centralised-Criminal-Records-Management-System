from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import os
import sqlite3
from add_crime import*
from add_criminal import*
from add_case import*

def wii(p):
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("ADD DATA")

    fing = tkFont.Font(family="Times New Roman", size=20)
    fins = tkFont.Font(family="Times New Roman", size=10)
    finm = tkFont.Font(family="Times New Roman", size=16)

    OptionList = ['CRIMINAL', 'CASE', 'FIR']
    v = tk.StringVar(root)
    v.set('ADD BY')
    opti = tk.OptionMenu(root, v, *OptionList)
    opti.place(x=615, y=300, width=350, height=80)
    opti.configure(font=finm, relief="solid")

    def nex():
        if v.get() == 'FIR':
            root.destroy()
            add1(p)
        elif v.get() == 'CRIMINAL':
            root.destroy()
            add2(p)
        elif v.get() == 'CASE':
            root.destroy()
            import search_complaint as tty
            tty.selcomp(p)
        else:
            tkinter.messagebox.showinfo('Title', 'CHOOSE RECORD TYPE')
    def back():
        root.destroy()
        from acp_home import acp_home
        acp_home(p)

    submit = Button(root, text='Submit',font=fing, command=nex, borderwidth=2, relief="solid")
    submit.place(x=680, y=450, width=200, height=70)
    back_button = Button(root, text='BACK', command=back,font=fins, borderwidth=2, relief="solid", width=10, height=2).place(x=50, y=50)
    mainloop()