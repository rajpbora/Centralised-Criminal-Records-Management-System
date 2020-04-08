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
        os.system('python login_page_first.py')
        
    def last():
        q = cursor.execute("SELECT * FROM POLICE where POLICEID=?", (k,))
        u = q.fetchall()
        s = u[0][6].split()
        tkinter.messagebox.showinfo('Last Login Details','Welcome ' + u[0][2] + '\nLast Login Date: ' + s[0] + '\nLast Login Time: ' + s[1])

    fil = tkFont.Font(family="Times New Roman", size=22)
    v = StringVar(t2)

    empty_box_1 = Label(t2, font=tkFont.Font(family="Times New Roman", size=150), borderwidth=2,relief="solid").place(x=50, y=138,width=472,height=360)
    finishing_1 = Label(t2, text='DATABASE CONTROLS', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid").place(x=136, y=80, width=300, height=50)
    user_detail_1 = Label(t2, text='Name : ', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid", width=13, height=2).place(x=790, y=425)
    user_detail_2 = Label(t2, text='ID : ', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid", width=13, height=2).place(x=790, y=485)
    user_detail_3 = Label(t2, text='Date of Birth : ', font=tkFont.Font(family="Times New Roman", size=18),borderwidth=2, relief="solid", width=13, height=2).place(x=790, y=545)
    user_detail_4 = Label(t2, text='Rank : ', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid", width=13, height=2).place(x=790, y=605)
    user_detail_5 = Label(t2, text='Email ID : ', font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,relief="solid", width=13, height=2).place(x=790, y=665)
    v = StringVar(t2)
    add_user = Button(t2, text='ADD NEW USER',font=fil, command=add_user, borderwidth=2, relief="solid", width=26, height=2)
    update_user = Button(t2, text='UPDATE USER INFORMATION',font=fil, command=update_user, borderwidth=2, relief="solid",width=26, height=2)
    delete_user = Button(t2, text='DELETE A USER',font=fil, command=delete_user, borderwidth=2, relief="solid", width=26, height=2)
    logout_user = Button(t2, text='LOGOUT',font=fil, command=logout, borderwidth=2, relief="solid", width=25, height=2)
    last_button = Button(t2, text='LAST LOGIN',font=fil, command=last, borderwidth=2, relief="solid", width=25,height=2)
    
    x=cursor.execute("SELECT * FROM POLICE where POLICEID=?", (k,))
    y=cursor.fetchall()

    for row in y:
        pol_id = row[0]
        photo = row[5]
        photoPath = "sys" + pol_id + ".jpg"
    with open(photoPath, 'wb') as file:
        file.write(photo)

    t2.load11 = Image.open(photoPath)
    t2.load11 = t2.load11.resize((250, 350), Image.ANTIALIAS)
    t2.photo11 = ImageTk.PhotoImage(t2.load11, master=t2)
    t2.img11 = Label(t2, image=t2.photo11)
    t2.img11.image = t2.photo11

    add_user.place(x=70, y=180)
    delete_user.place(x=70, y=280)
    update_user.place(x=70, y=380)
    t2.img11.place(x=1000, y=60)
    logout_user.place(x=80, y=650)
    last_button.place(x=80, y=550)

    cursor.execute("SELECT * FROM POLICE where POLICEID=?", (k,))
    for row in cursor.fetchall():
        l_name = Label(t2, text=row[2].upper() + ' ' + row[3].upper() + ' ' + row[4].upper(), anchor='w', font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid", width=30,height=2).place(x=1000, y=425)
        l_police_id = Label(t2, text=row[0], font=tkFont.Font(family="Times New Roman", size=20), anchor='w', borderwidth=2,relief="solid", width=30, height=2).place(x=1000, y=485)
        l_dob = Label(t2, text=row[11], font=tkFont.Font(family="Times New Roman", size=20), anchor='w', borderwidth=2,relief="solid", width=30, height=2).place(x=1000, y=545)
        l_rank = Label(t2, text=row[13], font=tkFont.Font(family="Times New Roman", size=20), anchor='w', borderwidth=2,relief="solid", width=30, height=2).place(x=1000, y=605)
        l_email_id = Label(t2, text=row[7].upper(), font=tkFont.Font(family="Times New Roman", size=20), anchor='w', borderwidth=2,relief="solid", width=30, height=2).place(x=1000, y=665)
    
    t2.title('System Administrator - '+row[2] + ' ' + row[3]+ ' ' + row[4])

    mainloop()