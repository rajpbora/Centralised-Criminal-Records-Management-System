from tkinter import *
import tkinter as tk
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
def worst(wi):
    root = tk.Tk()
    root.geometry('600x400')
    root.title("VISUALS")

    OptionList = ['OPEN AND CLOSED CASES', 'CRIME DISTRIBUTION CHART', 'CRIME RATE']
    v = tk.StringVar(root)
    v.set('SEARCH FOR')
    opt = tk.OptionMenu(root, v, *OptionList)
    opt.place(x=100, y=100, width=200, height=70)

    def next():
        if v.get() == 'OPEN AND CLOSED CASES':
            from dashboard import bargraph
            bargraph()
        elif v.get() == 'CRIME DISTRIBUTION CHART':
            from dashboard import piechart
            piechart()
        elif v.get() == 'CRIME RATE':
            root.destroy()
            import chosedate as tty
            tty.chdate(wi)

    def back():
        root.destroy()
        from civilian_home import civ_home
        civ_home(wi)

    submit = Button(root, text='Submit', command=next, borderwidth=4, relief="solid")
    submit.place(x=100, y=200, width=200, height=70)
    back = Button(root, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)


    root.mainloop()