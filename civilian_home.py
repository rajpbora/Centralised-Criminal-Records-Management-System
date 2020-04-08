from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3
import datetime
from disp_profile import display_details

def civ_home(id):
    t=tk.Tk()
    t.title('NCDS - Civilian ')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    connection = sqlite3.connect('NCD.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY, PASSWORD text NOT NULL, FNAME text, MNAME text, LNAME text, DOB date, GENDER text, MARITALSTATUS text, EMAILID text NOT NULL, OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)')
    cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN2 (USERID text PRIMARY KEY, CONTACT number)')

    retrieve=cursor.execute('SELECT * FROM CIVILIAN1 WHERE USERID = (?) ',(id,))
    temp=retrieve.fetchall()

    retrieve2=cursor.execute('SELECT * FROM CIVILIAN2 WHERE USERID = (?) ',(id,))
    temp2=retrieve2.fetchall()


    def enter_profile():
        t.destroy()
        display_details(temp[0],temp2[0])
        #os.system('python disp_profile.py')
        return
    def complaint():
        t.destroy()
        import complaintform as tty
        tty.comp(id)
        return
    def status():
        t.destroy()
        import complaint_status as tty
        tty.stat(id)
        #os.system('python complaint_status.py')
        return
    def data_analysis():
        t.destroy()
        import visual as tty
        tty.worst(id)
        return
    def logout():
        import datetime
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE CIVILIAN1 set LASTLOGIN=? where USERID=?", (b,id))
        connection.commit()
        t.destroy()
        os.system('python login_page_first.py')

    def lastlogin():
        q = cursor.execute("SELECT LASTLOGIN, FNAME FROM CIVILIAN1 where USERID=?", (id,))
        u = q.fetchall()
        s = u[0][0].split()
        tkinter.messagebox.showinfo('Last Login Details','Welcome ' + u[0][1] + '\nLast Login Date: ' + s[0] + '\nLast Login Time: ' + s[1])

    t.configure(background = 'white')


    name=Label(t, text=temp[0][2].upper()+' '+temp[0][3].upper()+' '+temp[0][4].upper(), fg='grey',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
    profile=Button(t, text='YOUR PROFILE'.upper(), font=tkFont.Font(family="Times New Roman", size=16),command=enter_profile, borderwidth=2, relief="solid")
    complain=Button(t, text='REGISTER COMPLAINT'.upper(), command=complaint, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    track=Button(t, text='TRACK COMPLAINT STATUS'.upper(), command=status, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    view=Button(t, text='VIEW DATA'.upper(), command=data_analysis, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    logout=Button(t, text='LOGOUT '.upper(), command=logout, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))
    lastlog=Button(t, text='LASTLOGIN ', command=lastlogin, borderwidth=2, relief="solid", font=tkFont.Font(family="Times New Roman", size=16))

    name.place(x=0, y=90, width=w, height=100)
    profile.place(x=950, y=300, width=400, height=100)
    logout.place(x=950, y=600, width=400, height=100)
    complain.place(x=200, y=300, width=400, height=100)
    track.place(x=200, y=450, width=400, height=100)
    lastlog.place(x=950, y=450, width=400, height=100)
    view.place(x=200, y=600, width=400, height=100)
    
    mainloop()