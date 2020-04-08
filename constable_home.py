from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os
import sqlite3
import datetime
from police_search1 import worst
from police_profile import police



def const_home(j):

    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    q = cursor.execute('SELECT * FROM POLICE where POLICEID=?', (j,))
    u = q.fetchall()

    t = tk.Tk()
    t.title('NCDS - Constable ')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    fing = tkFont.Font(family="Times New Roman", size=20)

    def dashboard():
        t.destroy()
        from visual1 import worst
        worst(j)
        return


    def search():
        t.destroy()
        worst(j)
        return

    def last():

        tkinter.messagebox.showinfo('Last Login', u[0][6])
        return

    def logout():
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE POLICE set LASTLOGIN=? where POLICEID=?", (b, j))
        connection.commit()
        t.destroy()
        os.system('python login_page_first.py')

    def enter_profile():

        photo = u[0][5]

        photoPath = "const" + j+ ".jpg"
        with open(photoPath, 'wb') as file:
            file.write(photo)

        t.destroy()
        police(j,photoPath)





    name = Label(t, text=str(u[0][2]).upper()+' '+str(u[0][4]).upper(), bg='white',fg='grey', borderwidth=2, relief="solid")

    profile = Button(t, text='YOUR PROFILE',font=fing, command=enter_profile, borderwidth=2, relief="solid")
    dash = Button(t, text='DASHBOARD',font=fing, command=dashboard, borderwidth=2, relief="solid")
    access = Button(t, text='ACCESS RECORDS',font=fing, command=search, borderwidth=2, relief="solid")
    last = Button(t, text='LAST LOGIN DETAILS',font=fing, command=last, borderwidth=2, relief="solid")
    logout = Button(t, text='LOGOUT',font=fing, command=logout, borderwidth=2, relief="solid")
    name.configure(font=("Times New Roman", 50, 'bold'))


    name.place(x=0, y=50, width=w, height=100)

    access.place(x=200, y=225, width=400, height=100)
    dash.place(x=200, y=375, width=400, height=100)
    last.place(x=200, y=525, width=400, height=100)

    profile.place(x=950, y=225, width=400, height=100)
    logout.place(x=950, y=525, width=400, height=100)

    mainloop()
