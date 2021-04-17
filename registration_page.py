from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import datetime
import sqlite3
import re

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS CIVILIAN1 (USERID text PRIMARY KEY CHECK(USERID <> ''), PASSWORD text NOT NULL CHECK(PASSWORD <> ''), FNAME text, MNAME text, LNAME text, DOB text, GENDER text, MARITALSTATUS text, EMAILID TEXT NOT NULL CHECK(EMAILID <> ""), OCCUPATION text, ADDRESS text, LASTLOGIN text, PHOTO blob)""")

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
        #print(len(uid.get()))
        u = uid.get()
        if len(u)<=3:
            tkinter.messagebox.showinfo('Alert','User ID must be atleast 4 characters long')
            return
        pword = pswd.get()
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, pword)
        if not mat:
            tkinter.messagebox.showinfo('Alert','Insecure Password.')
            return

        num = contact1.get()
        if type(num) != int and len(str(num)) != 10:
            tkinter.messagebox.showinfo('Alert','Enter correct Mobile Number')
            return

        e = email1.get()
        rege = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not (re.search(rege, e)):
            tkinter.messagebox.showinfo('Alert','Enter correct Email Address')
            return

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
            import subprocess
            subprocess.call('python login_page_first.py')
    else:
        tkinter.messagebox.showinfo('Alert','USER ID Already taken.')

def clear_details():
    fname1.delete(0, 'end')
    mname1.delete(0, 'end')
    lname1.delete(0, 'end')
    email1.delete(0, 'end')
    contact1.delete(0, 'end')
    d.set('dd')
    mth.set('mm')
    y.set('yyyy')
    v.set('Select Gender')
    v2.set('Marital Status')
    occupation1.delete(0, 'end')
    address1.delete(0, 'end')
    uid.delete(0, 'end')
    pswd.delete(0, 'end')
    image=Button(t, text='Choose Photo', font=tkFont.Font(family="Times New Roman", size=16), command=selectimg, borderwidth=2, relief="solid")
    image.place(x=1025, y=50, width=250, height=250)
    return

def goback():
    t.destroy()
    import subprocess
    subprocess.call('python login_page_first.py')

def convertToBinaryData():
    global temp
    with open(temp, 'rb') as file:
        blobData = file.read()
    return blobData


def selectimg():
    t.filename = filedialog.askopenfilename(initialdir="/", title="Select Profile Picture", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    load = Image.open(t.filename)
    load = load.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(load)
    img1 = Button(t, image=photo, command=selectimg,borderwidth=2, relief="solid")
    img1.image = photo
    img1.place(x=1025, y=50, width=250, height=250)
    global temp
    temp=t.filename
    return
    
fname=Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
mname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
lname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
fname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
mname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
lname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
email=Label(t, text='Email ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
contact=Label(t, text='Mobile Number', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
email1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
contact1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")



dob=Label(t, text='Date of Birth', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
d = tk.IntVar(t)
d.set('dd')
day = tk.OptionMenu(t, d, *dayOptionList)
menu = t.nametowidget(day.menuname)
menu.config(font=tkFont.Font(family="Times New Roman", size=14))


monthOptionList=[1,2,3,4,5,6,7,8,9,10,11,12]
mth = tk.IntVar(t)
mth.set('mm')
month = tk.OptionMenu(t, mth, *monthOptionList)
menu = t.nametowidget(month.menuname)
menu.config(font=tkFont.Font(family="Times New Roman", size=14))


yearOptionList=[]
for i in range(1970,2004):
    yearOptionList.append(i)
y = tk.IntVar(t)
y.set('yyyy')
year = tk.OptionMenu(t, y, *yearOptionList)
menu = t.nametowidget(year.menuname)
menu.config(font=tkFont.Font(family="Times New Roman", size=14))

day.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
month.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
year.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

OptionList=['Male','Female','Others']
v = tk.StringVar(t)
v.set('Select Gender')
gender = tk.OptionMenu(t, v, *OptionList)
menu = t.nametowidget(gender.menuname)
menu.config(font=tkFont.Font(family="Times New Roman", size=14))
gender.config(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")


OptionList2=['Married','Unmarried','Rather Not Say']
v2 = tk.StringVar(t)
v2.set('Marital Status')
marital = tk.OptionMenu(t, v2, *OptionList2)
menu = t.nametowidget(marital.menuname)
menu.config(font=tkFont.Font(family="Times New Roman", size=14))
marital.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

address=Label(t, text='Address', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
address1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

occupation=Label(t, text='Occupation', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
occupation1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

image=Button(t, text='Choose Photo', font=tkFont.Font(family="Times New Roman", size=16), command=selectimg, borderwidth=2, relief="solid")

user=Label(t, text='USER ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
password=Label(t, text='Password', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
uid=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd=Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")


cond = "For Security reasons, your password:\n\n> Should have at least one number.\n> Should have at least one uppercase and one lowercase character.\n> Should have at least one special symbol.\n> Should be between 6 to 20 characters long."
condi=Label(t, text=cond, font=tkFont.Font(family="Times New Roman", size=10), anchor = "w", foreground="red", borderwidth=0, relief="solid")


submit=Button(t, text='REGISTER', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=4, relief="solid")
reset=Button(t, text='CLEAR', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=4, relief="solid")
goback=Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=goback, borderwidth=4, relief="solid")


image.place(x=1025, y=50, width=250, height=250)

fname.place(x=50, y=50, width=200, height=50)
mname.place(x=50, y=120, width=200, height=50)
lname.place(x=50, y=190, width=200, height=50)

fname1.place(x=275, y=50, width=400, height=50)
mname1.place(x=275, y=120, width=400, height=50)
lname1.place(x=275, y=190, width=400, height=50)

dob.place(x=50, y=260, width=200, height=50)
day.place(x=275, y=260, width=130, height=50)
month.place(x=405, y=260, width=130, height=50)
year.place(x=535, y=260, width=140, height=50)

gender.place(x=50, y=330, width=200, height=50)
marital.place(x=275, y=330, width=400, height=50)

contact.place(x=50, y=400, width=200, height=50)
contact1.place(x=275, y=400, width=400, height=50)

user.place(x=825, y=400, width=200, height=50)
uid.place(x=1050, y=400, width=400, height=50)

email.place(x=50, y=470, width=200, height=50)
email1.place(x=275, y=470, width=400, height=50)

password.place(x=825, y=470, width=200, height=50)
pswd.place(x=1050, y=470, width=400, height=50)

condi.place(x=1050, y=525, width=400, height=100)

address.place(x=50, y=540, width=200, height=50)
address1.place(x=275, y=540, width=400, height=50)
occupation.place(x=50, y=610, width=200, height=50)
occupation1.place(x=275, y=610, width=400, height=50)

goback.place(x=250, y=690, width=250, height=50)
submit.place(x=650, y=690, width=250, height=50)
reset.place(x=1050, y=690, width=250, height=50)


req=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req1=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req2=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req3=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req4=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req5=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req6=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req7=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req8=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req9=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)
req10=Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor = "nw", foreground="red", borderwidth=0)

req.place(x=675, y=50, width=10, height=50)
req1.place(x=675, y=120, width=10, height=50)
req2.place(x=675, y=190, width=10, height=50)
req3.place(x=675, y=260, width=10, height=50)
req4.place(x=675, y=330, width=10, height=50)
req5.place(x=675, y=400, width=10, height=50)
req6.place(x=675, y=470, width=10, height=50)
req7.place(x=675, y=540, width=10, height=50)
req8.place(x=675, y=610, width=10, height=50)
req9.place(x=1450, y=400, width=10, height=50)
req10.place(x=1450, y=470, width=10, height=50)

day.config(font=tkFont.Font(family="Times New Roman", size=16))
month.config(font=tkFont.Font(family="Times New Roman", size=16))
year.config(font=tkFont.Font(family="Times New Roman", size=16))
gender.config(font=tkFont.Font(family="Times New Roman", size=18))
marital.config(font=tkFont.Font(family="Times New Roman", size=18))

mainloop()