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
    root.geometry('600x400')
    root.title("ADD DATA")

    # fing = tkFont.Font(family="Times New Roman", size=20)
    # fins = tkFont.Font(family="Times New Roman", size=10)

    OptionList = ['CRIMINAL', 'CASE', 'FIR']
    v = tk.StringVar(root)
    v.set('ADD BY')
    opti = tk.OptionMenu(root, v, *OptionList)
    opti.place(x=200, y=100, width=200, height=70)
    opti.configure(relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    menu = root.nametowidget(opti.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=10))

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

    submit = Button(root, text='SUBMIT',font=tkFont.Font(family="Times New Roman", size=16), command=nex, borderwidth=4, relief="solid")
    submit.place(x=200, y=200, width=200, height=50)
    back = Button(root, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)

    mainloop()