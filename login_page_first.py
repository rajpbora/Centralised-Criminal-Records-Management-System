from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3
import datetime
from civilian_home import civ_home
from acp_home import acp_home
from constable_home import const_home
from sys_home import system_home

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
xtr=str(datetime.datetime.now())

cursor.execute('CREATE TABLE IF NOT EXISTS POLICE(POLICEID TEXT PRIMARY KEY CHECK(POLICEID <> ""), PASSWORD TEXT NOT NULL CHECK(PASSWORD <> ""),FNAME TEXT NOT NULL CHECK(FNAME <> ""), MNAME TEXT, LNAME TEXT NOT NULL CHECK(LNAME <> ""), PHOTO BLOB NOT NULL, LASTLOGIN TEXT, EMAILID TEXT NOT NULL CHECK(EMAILID <> ""), JURISDICTION TEXT NOT NULL CHECK(JURISDICTION <> ""), ADDRESS TEXT NOT NULL CHECK(ADDRESS <> ""), GENDER TEXT NOT NULL CHECK(GENDER <> ""), DOB TEXT NOT NULL CHECK(DOB <> ""), BATCH TEXT NOT NULL CHECK(BATCH <> ""), RANK TEXT NOT NULL CHECK(RANK <> ""), MARITALSTATUS TEXT NOT NULL)')

cursor.execute("""CREATE TABLE IF NOT EXISTS POLICE1(POLICEID TEXT, CONTACT TEXT NOT NULL, FOREIGN KEY (POLICEID) REFERENCES POLICE(POLICEID))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS COMPLAINT (COMPLAINT_NO text PRIMARY KEY, PLACEOFCRIME text NOT NULL CHECK(PLACEOFCRIME <> ''), TIMEOFCRIME text, CRIMEDESCRIPTION text, CITY text, POLICESTATION text, STATUS text, VFNAME text, VMNAME text, VLNAME text, AFNAME text, AMNAME text, ALNAME text, USERID text, FOREIGN KEY(USERID) REFERENCES CIVILIAN1(USERID))""")

cursor.execute("""CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY CHECK(USERID <> ''), PASSWORD text NOT NULL CHECK(PASSWORD <> ''), FNAME text, MNAME text, LNAME text, DOB text, GENDER text, MARITALSTATUS text, EMAILID text NOT NULL, OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)""")

cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN2 (USERID text , CONTACT number,FOREIGN KEY (USERID) REFERENCES CIVILIAN1(USERID))')

cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL(CRIMINALID number PRIMARY KEY, FNAME text, MNAME text, LNAME text, DOB text, BLOODGROUP text, STATUS text, PRIORITY number, GENDER text, PHOTO BLOB NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS CASE1 (CASENO number PRIMARY KEY, PENALCODETYPE text, SECTIONNUMBER number, POLICESTATION text, DESCRIPTION text NOT NULL, OPENDATE text NOT NULL, CLOSEDATE text, COMPLAINT_NO TEXT, FOREIGN KEY (COMPLAINT_NO) REFERENCES COMPLAINT(COMPLAINT_NO))')

cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL3 (CRIMINALID text, CONTACT text, FOREIGN KEY (CRIMINALID) REFERENCES CRIMINAL(CRIMINALID))')

cursor.execute('CREATE TABLE IF NOT EXISTS CASE2(CASENO number, POLICEID text, FOREIGN KEY (POLICEID) REFERENCES POLICE(POLICEID), FOREIGN KEY(CASENO) REFERENCES CASE1(CASENO))')

cursor.execute('CREATE TABLE IF NOT EXISTS CASE3(CASENO number , VFNAME text, VMNAME text, VLNAME text, VAGE number, VADDRESS text, FOREIGN KEY (CASENO) REFERENCES CASE1(CASENO))')

cursor.execute('CREATE TABLE IF NOT EXISTS CASE4(CASENO number, FIRNO number, FOREIGN KEY(CASENO) REFERENCES CASE1(CASENO), FOREIGN KEY(FIRNO) REFERENCES CRIME(FIRNO))')

cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL2(CRIMINALID text, ADDRESS text, FOREIGN KEY (CRIMINALID) REFERENCES CRIMINAL(CRIMINALID))')

cursor.execute('CREATE TABLE IF NOT EXISTS CRIMINAL1 (CRIMINALID text, IDENTIFICATIONMARKS text,FOREIGN KEY (CRIMINALID) REFERENCES CRIMINAL(CRIMINALID))')

cursor.execute('CREATE TABLE IF NOT EXISTS CRIME2 (FIRNO number, CRIMINALID number, FOREIGN KEY(FIRNO) REFERENCES CRIME(FIRNO), FOREIGN KEY(CRIMINALID) REFERENCES CRIMINAL(CRIMINALID))')

cursor.execute('CREATE TABLE IF NOT EXISTS CRIME3 (FIRNO number, PENALCODETYPE text, SECTIONNUMBER number, FOREIGN KEY (FIRNO) REFERENCES CRIME(FIRNO))')

cursor.execute( 'CREATE TABLE IF NOT EXISTS CRIME(FIRNO number PRIMARY KEY, DAMAGEAMOUNT number, INJURED number, DEATHS number, DATEOFCRIME text NOT NULL, PLACEOFCRIME text)')

connection.commit()

t=tk.Tk()
t.title('NCDS')
t.configure(background = 'white')
#t.geometry("1500x800+30+30")
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))
#fontStyle = tkFont.Font(family="Times New Roman", size=60)

def enter():
    getuid = uid.get()
    getpswd = pswd.get()
    if v.get()=='Civilian':
        u = cursor.execute('SELECT USERID FROM CIVILIAN1 where USERID=(?) and PASSWORD=(?)', (getuid,getpswd))
        temp=u.fetchall()
        if getuid == temp[0][0] and len(temp)>0:
            tkinter.messagebox.showinfo('Title','Logged_In')
            clear()
            t.destroy()
            civ_home(getuid)
        else:
            tkinter.messagebox.showinfo('Alert','Incorrect Username or Password')
    elif v.get()=='Police':
        u = cursor.execute('SELECT POLICEID,RANK FROM POLICE where POLICEID=(?) and PASSWORD=(?)', (getuid,getpswd))
        temp=u.fetchall()
        if len(temp)>0:
            if getuid == temp[0][0]:
                if temp[0][1] == 'ACP':
                    tkinter.messagebox.showinfo('Title','Logged_In')
                    clear()
                    t.destroy()
                    acp_home(getuid)
                elif temp[0][1] == 'CONSTABLE':
                    tkinter.messagebox.showinfo('Title','Logged_In')
                    clear()
                    t.destroy()
                    const_home(getuid)
                elif temp[0][1] == 'SYSTEM ADMINISTRATOR':
                    tkinter.messagebox.showinfo('Title','Logged_In')
                    clear()
                    t.destroy()
                    system_home(getuid)
                else:
                    tkinter.messagebox.showinfo('Alert','Incorrect Username or Password')
        else:
            tkinter.messagebox.showinfo('Alert','Incorrect Username or Password')
    else:
        tkinter.messagebox.showinfo('Title','Choose User Type')


def clear():
    uid.delete(0, 'end')
    pswd.delete(0, 'end')
    v.set('User Type')
    return

def register():
    t.destroy()
    os.system('python registration_page.py')
    return

def close():
    try:
        for i in range(6):
            os.remove('z'+str(i)+'.jpg')
    except:
        pass
    t.destroy()
    import sys
    sys.exit()
    return

OptionList=['Police','Civilian']
v = tk.StringVar(t)
v.set('Select User Type'.upper())
opt = tk.OptionMenu(t, v, *OptionList)

fing=tkFont.Font(family="Times New Roman", size=16)
opt.configure(relief="solid",font=tkFont.Font(family="Times New Roman", size=20))
impmsg=Label(t, text='WELCOME TO POLICE PORTAL',bg='black', fg='white',font=tkFont.Font(family="Times New Roman", size=60), borderwidth=2, relief="solid")
wanted=Label(t, text='T   O   P      W   A   N   T   E   D', fg='red',font=tkFont.Font(family="Times New Roman", size=40), borderwidth=2, relief="solid")
detail=Label(t, text='Enter Below details to Login',bg='white',fg='black',font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")

user=Label(t, text='USER ID ',font=fing,borderwidth=2, relief="solid")
password=Label(t, text='PASSWORD',font=fing, borderwidth=2,relief="solid")
uid=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
submit=Button(t, text='SUBMIT', command=enter,font=fing, borderwidth=2, relief="solid")
reset=Button(t, text='CLEAR', command=clear,font=fing, borderwidth=2, relief="solid")
signup=Button(t, text='REGISTER', command=register, borderwidth=2, relief="solid")
close=Button(t, text='EXIT', command=close, font=fing,borderwidth=2, relief="solid")
signup.configure(font=("Times New Roman",25,'bold'))


f=cursor.execute('SELECT PHOTO from CRIMINAL order by priority')
temp=f.fetchall()
plist=[]
if len(temp)>=6:
    for i in range(6):
        path = "z" + str(i) + '.jpg'
        with open(path, 'wb') as file:
            file.write(temp[i][0])
        plist.append(path)
else:
    for i in range(len(temp)):
        path = "z" + str(i) + '.jpg'
        with open(path, 'wb') as file:
            file.write(temp[i][0])
        plist.append(path)
    for i in range (len(temp)-1,6):
        plist.append('demo.jpg')


t.load1 = Image.open(plist[0])
t.load1 = t.load1.resize((200, 200), Image.ANTIALIAS)
t.photo1 = ImageTk.PhotoImage(t.load1, master=t)
t.img1 = Label(t, image=t.photo1, borderwidth=2, relief="solid")
t.img1.image = t.photo1

t.load2 = Image.open(plist[1])
t.load2 = t.load2.resize((200, 200), Image.ANTIALIAS)
t.photo2 = ImageTk.PhotoImage(t.load2, master=t)
t.img2 = Label(t, image=t.photo2, borderwidth=2, relief="solid")
t.img2.image = t.photo2

t.load3 = Image.open(plist[2])
t.load3 = t.load3.resize((200, 200), Image.ANTIALIAS)
t.photo3 = ImageTk.PhotoImage(t.load3, master=t)
t.img3 = Label(t, image=t.photo3, borderwidth=2, relief="solid")
t.img3.image = t.photo3

t.load4 = Image.open(plist[3])
t.load4 = t.load4.resize((200, 200), Image.ANTIALIAS)
t.photo4 = ImageTk.PhotoImage(t.load4, master=t)
t.img4 = Label(t, image=t.photo4, borderwidth=2, relief="solid")
t.img4.image = t.photo4

t.load5 = Image.open(plist[4])
t.load5 = t.load5.resize((200, 200), Image.ANTIALIAS)
t.photo5 = ImageTk.PhotoImage(t.load5, master=t)
t.img5 = Label(t, image=t.photo5, borderwidth=2, relief="solid")
t.img5.image = t.photo5

t.load6 = Image.open(plist[5])
t.load6 = t.load6.resize((200, 200), Image.ANTIALIAS)
t.photo6 = ImageTk.PhotoImage(t.load6, master=t)
t.img6 = Label(t, image=t.photo6, borderwidth=2, relief="solid")
t.img6.image = t.photo6


impmsg.place(x=0, y=5, width=w, height=100)

wanted.place(x=600, y=160, width=800, height=70)

detail.place(x=90 , y=200, width=410, height=75)

opt.place(x = 90, y = 300 , width=410, height=70)
user.place(x = 90, y = 380 , width=200, height=70)
uid.place(x = 300, y = 380 , width=200, height=70)
password.place(x = 90, y = 460 , width=200, height=70)
pswd.place(x = 300, y = 460 , width=200, height=70)

submit.place(x = 90, y = 540, width=200, height=70)
reset.place(x = 300, y = 540 , width=200, height=70)

signup.place(x= 90, y = 630, width = 200, height = 70)
close.place(x= 300, y = 630, width = 200, height = 70)

t.img1.place(x = 600, y = 250 , width=200, height=200)
t.img2.place(x = 900, y = 250 , width=200, height=200)
t.img3.place(x = 1200, y = 250 , width=200, height=200)
t.img4.place(x = 600, y = 500 , width=200, height=200)
t.img5.place(x = 900, y = 500 , width=200, height=200)
t.img6.place(x = 1200, y = 500 , width=200, height=200)
mainloop()
