from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import os
import sqlite3
from PIL import Image,ImageTk
from open_criminal import test
from open_crime import best
from open_case import fest
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()


def worst(wi):
    root = tk.Tk()
    root.geometry('600x400')
    root.title("SEARCH")

    finm = tkFont.Font(family="Times New Roman", size=16)

    OptionList = ['CRIMINAL ID', 'CASE ID', 'FIR NUMBER']
    v = tk.StringVar(root)
    v.set('SEARCH BY')
    opt = tk.OptionMenu(root, v, *OptionList)
    opt.place(x=200, y=100, width=200, height=50)
    opt.configure(font=finm, relief="solid")
    menu = root.nametowidget(opt.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    opt.configure(relief="solid", font=tkFont.Font(family="Times New Roman", size=14))
    e1 = Entry(root, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=20))
    e1.place(x=200, y=175, width=200, height=50)

    def back():
        root.destroy()
        from constable_home import const_home
        const_home(wi)

    def next():
        if v.get() == 'CRIMINAL ID':
            try:
                x = e1.get()
                u = cursor.execute('SELECT * FROM CRIMINAL where CRIMINALID=(?)', (x,))
                j = u.fetchall()

                r = cursor.execute('SELECT * FROM CRIMINAL1 where CRIMINALID=(?)', (x,))
                j1 = r.fetchall()

                q = cursor.execute('SELECT * FROM CRIMINAL2 where CRIMINALID=(?)', (x,))
                j2 = q.fetchall()

                p = cursor.execute('SELECT * FROM CRIMINAL3 where CRIMINALID=(?)', (x,))
                j3 = p.fetchall()
            except Exception as e:
                tkinter.messagebox.showinfo('Alert',
                                            "Wong Entry/Couldn't connect to Database\nError Description : " + str(
                                                e))
            else:
                if len(j) == 1:
                    photo = j[0][9]
                    photoPath = "D:\z" + str(20180829_004758) + ".jpg"
                    with open(photoPath, 'wb') as file:
                        file.write(photo)
                    print("Stored blob data into: ", photoPath, "\n")

                    root.destroy()
                    test(wi, j, j1, j2, j3, photoPath)
                else:
                    tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')

        elif v.get() == 'FIR NUMBER':
            try:
                x = e1.get()
                z = cursor.execute('SELECT * FROM CRIME where FIRNO=(?)', (x,))
                k = z.fetchall()
                z1 = cursor.execute('SELECT * FROM CRIME2 where FIRNO=(?)', (x,))
                k1 = z1.fetchall()
                z2 = cursor.execute('SELECT * FROM CRIME3 where FIRNO=(?)', (x,))
                k2 = z2.fetchall()

            except Exception as e:
                tkinter.messagebox.showinfo('Alert',
                                            "Wong Entry/Couldn't connect to Database\nError Description : " + str(
                                                e))
            else:
                if len(k) == 1:
                    root.destroy()
                    best(wi, k, k1, k2)
                else:
                    tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')

        elif v.get() == 'CASE ID':
            try:
                x = e1.get()
                w = cursor.execute('SELECT * FROM CASE1 where CASENO=(?)', (x,))
                i = w.fetchall()
                w1 = cursor.execute('SELECT * FROM CASE2 where CASENO=(?)', (x,))
                i1 = w1.fetchall()
                w2 = cursor.execute('SELECT * FROM CASE3 where CASENO=(?)', (x,))
                i2 = w2.fetchall()
                w3 = cursor.execute('SELECT * FROM CASE4 where CASENO=(?)', (x,))
                i3 = w3.fetchall()
            except Exception as e:
                tkinter.messagebox.showinfo('Alert',
                                            "Wong Entry/Couldn't connect to Database\nError Description : " + str(
                                                e))
            else:
                if len(i) == 1:
                    root.destroy()
                    fest(wi, i, i1, i2, i3)
                else:
                    tkinter.messagebox.showinfo('Title', 'DOES NOT EXIST')
        return

    submit = Button(root, text='SUBMIT', command=next, borderwidth=4, relief="solid",
                    font=tkFont.Font(family="Times New Roman", size=16))
    submit.place(x=225, y=275, width=150, height=50)

    back = Button(root, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)

    root.mainloop()