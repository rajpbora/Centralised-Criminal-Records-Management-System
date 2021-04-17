import tkinter.font as tkFont
from tkinter import *
from PIL import Image, ImageTk
import os
import sqlite3
import datetime
from del_user import test3
from choose_user import *
from add_user import test5
import re
from time import sleep

import tkinter.messagebox
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()


def system_home(k):
    photoPath=''
    t2 = Tk()
    t2.configure(background='white')
    
    w, h = t2.winfo_screenwidth(), t2.winfo_screenheight()
    t2.geometry("%dx%d+0+0" % (w, h))

    def add_user():
        t2.destroy()
        test5(k)

    def update_user():
        t2.destroy()
        test4(k)

    def delete_user():
        t2.destroy()
        test3(k)

    def logout():
        os.remove('sys'+pol_id+'.jpg')
        t2.destroy()
        b = str(datetime.datetime.now())
        cursor.execute("UPDATE POLICE set LASTLOGIN=? where POLICEID=?", (b, k,))
        connection.commit()
        import subprocess
        subprocess.call("python login_page_first.py")
        
    def last():
        q = cursor.execute("SELECT * FROM POLICE where POLICEID=?", (k,))
        u = q.fetchall()
        s = u[0][6].split()
        tkinter.messagebox.showinfo('Last Login Details','Welcome ' + u[0][2] + '\nLast Login Date: ' + s[0] + '\nLast Login Time: ' + s[1])

    fil = tkFont.Font(family="Times New Roman", size=22)
    v = StringVar(t2)

    name=Label(t2, text="S Y S T E M    A D M I N I S T R A T O R", fg='grey',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
    name.place(x=0, y=30, width=w, height=100)

    user_detail_1 = Label(t2, text='Name', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid")
    user_detail_2 = Label(t2, text='Police ID', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid")
    user_detail_3 = Label(t2, text='Date of Birth', font=tkFont.Font(family="Times New Roman", size=18),borderwidth=2, relief="solid")
    user_detail_4 = Label(t2, text='Email ID', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid")
    user_detail_1.place(x=825, y=470, width=200, height=50)
    user_detail_2.place(x=825, y=540, width=200, height=50)
    user_detail_3.place(x=825, y=610, width=200, height=50)
    user_detail_4.place(x=825, y=680, width=200, height=50)

    v = StringVar(t2)
    add_user = Button(t2, text='ADD USER',font=fil, command=add_user, relief="raised")
    update_user = Button(t2, text='EDIT USER',font=fil, command=update_user, relief="raised")
    delete_user = Button(t2, text='DELETE USER',font=fil, command=delete_user, relief="raised")
    logout_user = Button(t2, text='LOGOUT',font=fil, command=logout, relief="raised")
    last_button = Button(t2, text='LAST LOGIN',font=fil, command=last, relief="raised")
    
    x=cursor.execute("SELECT * FROM POLICE where POLICEID=?", (k,))
    y=cursor.fetchall()

    for row in y:
        pol_id = row[0]
        photo = row[5]
        photoPath = "sys" + pol_id + ".jpg"
    with open(photoPath, 'wb') as file:
        file.write(photo)

    t2.load11 = Image.open(photoPath)
    t2.load11 = t2.load11.resize((250, 250), Image.ANTIALIAS)
    t2.photo11 = ImageTk.PhotoImage(t2.load11, master=t2)
    t2.img11 = Label(t2, image=t2.photo11,borderwidth=2, relief="solid")
    t2.img11.image = t2.photo11
    t2.img11.place(x=1025, y=190, width=250, height=250)

    add_user.place(x=170, y=200, width=400, height=80)
    delete_user.place(x=170, y=310, width=400, height=80)
    update_user.place(x=170, y=420, width=400, height=80)
    last_button.place(x=170, y=530, width=400, height=80)
    logout_user.place(x=170, y=640, width=400, height=80)

    cursor.execute("SELECT * FROM POLICE where POLICEID=?", (k,))
    for row in cursor.fetchall():
        l_name = Label(t2, text=row[2].upper() + ' ' + row[3].upper() + ' ' + row[4].upper(), anchor='w', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
        l_police_id = Label(t2, text=row[0], font=tkFont.Font(family="Times New Roman", size=18), anchor='w', borderwidth=2,relief="solid")
        l_dob = Label(t2, text=row[11], font=tkFont.Font(family="Times New Roman", size=18), anchor='w', borderwidth=2,relief="solid")
        l_email_id = Label(t2, text=row[7], font=tkFont.Font(family="Times New Roman", size=18), anchor='w', borderwidth=2,relief="solid")
    l_name.place(x=1050, y=470, width=400, height=50)
    l_police_id.place(x=1050, y=540, width=400, height=50)
    l_dob.place(x=1050, y=610, width=400, height=50)
    l_email_id.place(x=1050, y=680, width=400, height=50)
    t2.title('System Administrator - '+row[2] + ' ' + row[3]+ ' ' + row[4])

    mainloop()