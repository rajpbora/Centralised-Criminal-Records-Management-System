from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import datetime
from PIL import Image,ImageTk
from your_profile import police
import sqlite3
import os


def acp_home(j):
    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()

    q = cursor.execute('SELECT * FROM POLICE where POLICEID=?', (j,))
    u = q.fetchall()
    t = tk.Tk()
    t.title('ACP HOME')
    t.configure(background='white')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    fing = tkFont.Font(family="Times New Roman", size=20)
    def enter_profile():
        photo = u[0][5]
        photoPath = "acp" + j + ".jpg"
        with open(photoPath, 'wb') as file:
            file.write(photo)
        t.destroy()
        police(j, photoPath)
        return

    def dashboard():
        t.destroy()
        import visual2 as tty
        tty.worst(j)
        return

    def search():
        t.destroy()
        from police_search import worst
        worst(j)

    def add():
        t.destroy()
        from add_acp import wii
        wii(j)

    def last():
        s = u[0][6].split()
        tkinter.messagebox.showinfo('Last Login Details','Welcome ' + u[0][2] + '\nLast Login Date: ' + s[0] + '\nLast Login Time: ' + s[1])
        return

    def logout():
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE POLICE set LASTLOGIN=? where POLICEID=?", (b, j))
        connection.commit()
        t.destroy()
        os.system('python login_page_first.py')

    name=Label(t, text=str(u[0][2]).upper()+' '+str(u[0][4]).upper(),bg='white', fg='grey', borderwidth=2, relief="solid")

    profile=Button(t, text='MY PROFILE',font=fing, command=enter_profile, borderwidth=2, relief="solid")
    dash=Button(t, text='DASHBOARD',font=fing, command=dashboard, borderwidth=2, relief="solid")
    access=Button(t, text='ACCESS RECORDS',font=fing, command=search, borderwidth=2, relief="solid")
    last=Button(t, text='LAST LOGIN DETAILS',font=fing, command=last, borderwidth=2, relief="solid")
    logout=Button(t, text='LOGOUT', command=logout,font=fing, borderwidth=2, relief="solid")
    add=Button(t, text='ADD DATA',command=add,font=fing, borderwidth=2, relief="solid")
    name.configure(font=("Times New Roman",50 , 'bold'))
    name.place(x=0, y=50, width=w, height=100)
    dash.place(x=200, y=450, width=400, height=100)
    access.place(x=200, y=300, width=400, height=100)
    add.place(x=200, y=600, width=400, height=100)
    profile.place(x=950, y=300, width=400, height=100)
    logout.place(x=950, y=600, width=400, height=100)
    last.place(x=950, y=450, width=400, height=100)
    mainloop()