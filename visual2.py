from tkinter import *
import tkinter as tk
import sqlite3
import tkinter.font as tkFont
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
def worst(wi):
    root = tk.Tk()
    root.geometry('600x400')
    root.title("VISUALS")

    OptionList = ['OPEN & CLOSED CASES', 'CRIME DISTRIBUTION', 'CRIME RATE','MY OPEN & CLOSED CASES']
    v = tk.StringVar(root)
    v.set('SEARCH FOR')
    opt = tk.OptionMenu(root, v, *OptionList)
    opt.place(x=200, y=100, width=225, height=70)
    menu = root.nametowidget(opt.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=10))
    opt.configure(relief="solid", font=tkFont.Font(family="Times New Roman",size=10))

    def next():
        if v.get() == 'OPEN & CLOSED CASES':
            from dashboard import bargraph
            bargraph()
        elif v.get() == 'CRIME DISTRIBUTION':
            from dashboard import piechart
            piechart()
        elif v.get() == 'MY OPEN & CLOSED CASES':
            from dashboard import bargraph2
            bargraph2(wi)
        elif v.get() == 'CRIME RATE':
            root.destroy()
            import chosedate2 as tty
            tty.chdate2(wi)


    def back():
        root.destroy()
        from acp_home import acp_home
        acp_home(wi)


    submit = Button(root, text='SUBMIT', command=next, borderwidth=4, relief="solid",font=tkFont.Font(family="Times New Roman", size=16))
    submit.place(x=225, y=200, width=175, height=50)
    back = Button(root, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)


    root.mainloop()