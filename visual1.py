from tkinter import *
import tkinter as tk
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
def worst(wi):
    root = tk.Tk()
    root.geometry('600x400')
    root.title("VISUALS")

    OptionList = ['OPEN AND CLOSED CASES', 'CRIME DISTRIBUTION CHART', 'CRIME RATE','YOUR OPEN AND CLOSED CASES']
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
        elif v.get() == 'YOUR OPEN AND CLOSED CASES':
            from dashboard import bargraph2
            bargraph2(wi)
        elif v.get() == 'CRIME RATE':
            root.destroy()
            import chosedate1 as tty
            tty.chdate1(wi)




    def back():
        root.destroy()
        from constable_home import const_home
        const_home(wi)



    submit = Button(root, text='Submit', command=next, borderwidth=4, relief="solid")
    submit.place(x=100, y=200, width=200, height=70)
    back = Button(root, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)

    root.mainloop()