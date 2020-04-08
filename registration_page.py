from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import datetime
import sqlite3

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY, PASSWORD text NOT NULL, FNAME text, MNAME text, LNAME text, DOB date, GENDER text, MARITALSTATUS text, EMAILID text NOT NULL, OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)')
cursor.execute('CREATE TABLE IF NOT EXISTS CIVILIAN2 (USERID text , CONTACT number,FOREIGN KEY (USERID) REFERENCES CIVILIAN1(USERID))')

t=tk.Tk()
t.title('NCDS - Register ')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("%dx%d+0+0" % (w, h))
temp=''


def submit_details():

    u=cursor.execute('SELECT USERID from CIVILIAN1 where USERID =?',(uid.get(),))
    temp=u.fetchall()
    if len(temp)==0:
        try:
            prof = convertToBinaryData()
            data_tuple = (uid.get(), pswd.get(), fname1.get(), mname1.get(), lname1.get(), str(y.get())+'-'+str(mth.get())+'-'+str(d.get()),v.get(), v2.get(), email1.get(), occupation1.get(), address1.get(), datetime.datetime.now(), prof)
            cursor.execute('INSERT INTO CIVILIAN1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',data_tuple)
            cursor.execute('INSERT INTO CIVILIAN2 VALUES (?,?)',(uid.get(), contact1.get()))
            connection.commit()
            tkinter.messagebox.showinfo('Title', 'User Created')
            t.destroy()
        except Exception as e:
            tkinter.messagebox.showinfo('Alert','Connection to Database Failed due to :\n'+str(e))
        else:
            os.system('python login_page_first.py')
    else:
        tkinter.messagebox.showinfo('Alert','USERID Already taken')

def clear_details():
    t.destroy()
    os.system('python registration_page.py')
    return

def goback():
    t.destroy()
    os.system('python login_page_first.py')

def convertToBinaryData():
    global temp
    with open(temp, 'rb') as file:
        blobData = file.read()
    return blobData


def selectimg():
    t.filename = filedialog.askopenfilename(initialdir="/", title="Select Profile Picture", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    load = Image.open(t.filename)
    load = load.resize((250, 275), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    img1 = Button(t, image=photo, command=selectimg)
    img1.image = photo
    img1.place(x=800, y=450, width=250, height=275)
    global temp
    temp=t.filename
    return
    
fname=Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
mname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
lname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
fname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
mname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
lname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
email=Label(t, text='Email_ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
contact=Label(t, text='Mobile_Number', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
email1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
contact1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
d = tk.IntVar(t)
d.set('Day')
day = tk.OptionMenu(t, d, *dayOptionList)
monthOptionList=[1,2,3,4,5,6,7,8,9,10,11,12]
mth = tk.IntVar(t)
mth.set('Month')
month = tk.OptionMenu(t, mth, *monthOptionList)
yearOptionList=[]
for i in range(1950,2002):
    yearOptionList.append(i)
y = tk.IntVar(t)
y.set('Year')
year = tk.OptionMenu(t, y, *yearOptionList)

OptionList=['Male','Female','Others']
v = tk.StringVar(t)
v.set('Select Gender')
gender = tk.OptionMenu(t, v, *OptionList)

OptionList2=['Married','Unmarried','Rather Not Say']
v2 = tk.StringVar(t)
v2.set('Marital Status')
marital = tk.OptionMenu(t, v2, *OptionList2)

address=Label(t, text='Address', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
address1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

occupation=Label(t, text='Occupation', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
occupation1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

image=Button(t, text='Choose Photo', font=tkFont.Font(family="Times New Roman", size=16), command=selectimg, borderwidth=2, relief="solid")

user=Label(t, text='USER_ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
password=Label(t, text='Password', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
uid=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")



submit=Button(t, text='REGISTER', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=4, relief="solid")
reset=Button(t, text='RESET', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=4, relief="solid")
goback=Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=goback, borderwidth=4, relief="solid")


fname.place(x=50, y=50, width=200, height=70)
mname.place(x=500, y=50, width=200, height=70)
lname.place(x=950, y=50, width=200, height=70)
fname1.place(x=275, y=50, width=200, height=70)
mname1.place(x=725, y=50, width=200, height=70)
lname1.place(x=1175, y=50, width=225, height=70)
email.place(x=50, y=150, width=175, height=70)
contact.place(x=950, y=150, width=190, height=70)
email1.place(x=250, y=150, width=675, height=70)
contact1.place(x=1150, y=150, width=250, height=70)
day.place(x=50, y=250, width=250, height=70)
month.place(x=300, y=250, width=250, height=70)
year.place(x=550, y=250, width=250, height=70)
gender.place(x=900, y=250, width=200, height=70)
marital.place(x=1200, y=250, width=200, height=70)
address.place(x=50, y=350, width=200, height=70)
address1.place(x=300, y=350, width=1100, height=70)
occupation.place(x=50, y=450, width=200, height=70)
occupation1.place(x=300, y=450, width=400, height=70)
image.place(x=800, y=450, width=250, height=275)

user.place(x=50, y=550, width=200, height=70)
password.place(x=50, y=650, width=200, height=70)
uid.place(x=300, y=550, width=400, height=70)
pswd.place(x=300, y=650, width=400, height=70)

submit.place(x=1125, y=490, width=225, height=50)
reset.place(x=1125, y=570, width=225, height=50)
goback.place(x=1125, y=650, width=225, height=50)


day.config(font=tkFont.Font(family="Times New Roman", size=16))
month.config(font=tkFont.Font(family="Times New Roman", size=16))
year.config(font=tkFont.Font(family="Times New Roman", size=16))
gender.config(font=tkFont.Font(family="Times New Roman", size=16))
marital.config(font=tkFont.Font(family="Times New Roman", size=16))

mainloop()