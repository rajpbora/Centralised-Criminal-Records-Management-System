from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image,ImageTk
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
from tkinter import filedialog
import re
import os
def test(j,k):
    global im_var_2
    im_var_2=0

    def back():
        try:
            os.remove("pol" + j + ".jpg")
            print(j)
        except:
            print('Not Found')
            pass
        t.destroy()
        from sys_home import system_home
        system_home(k)

    def image_update():
        try:
            t.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(("jpeg files", ".jpg"), ("all files", ".*")), master=t)
            t.load = Image.open(t.filename)
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "No New Image selected.")
        else:
            global im_var_2
            im_var_2 = 1
            t.load = t.load.resize((250, 250), Image.ANTIALIAS)
            t.photo1 = ImageTk.PhotoImage(t.load, master=t)
            t.img1 = Button(t, image=t.photo1, command=image_update, borderwidth=2, relief="solid")
            t.img1.image = t.photo1
            t.img1.place(x=1025, y=50, width=250, height=250)

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def updated_user():
        try:
            d_o_b =str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
            cursor.execute("Update POLICE set PASSWORD=? where POLICEID=?",(password.get(),j,))
            cursor.execute("UPDATE POLICE set FNAME=?  where POLICEID=?",(first_name.get(),j,))
            cursor.execute("UPDATE POLICE set MNAME=?  where POLICEID=?",(middle_name.get(),j,))
            cursor.execute("UPDATE POLICE set LNAME=?  where POLICEID=?",(last_name.get(),j,))
            cursor.execute("UPDATE POLICE set EMAILID=?  where POLICEID=?",(email_id.get(),j,))
            cursor.execute("UPDATE POLICE set JURISDICTION=?  where POLICEID=?",(jurisdiction.get(),j,))
            cursor.execute("UPDATE POLICE set ADDRESS=?  where POLICEID=?", (address.get(), j,))
            cursor.execute("UPDATE POLICE set DOB=?  where POLICEID=?",(d_o_b,j,))
            cursor.execute("UPDATE POLICE set BATCH=? where POLICEID=?",(batch.get(),j,))
            cursor.execute("UPDATE POLICE set GENDER=? where POLICEID=?", (v.get(), j,))
            cursor.execute("UPDATE POLICE set RANK=? where POLICEID=?",(v2.get(),j,))
            cursor.execute("UPDATE POLICE set MARITALSTATUS=? where POLICEID=?",(ms.get(),j,))
            cursor.execute("UPDATE POLICE1 set CONTACT=(?) where POLICEID=(?) and CONTACT=(?)",(contact_number_1.get(),j,l[0],))
            mcq=cursor.execute("SELECT CONTACT from POLICE1 where POLICEID=(?)",(j,))
            global im_var_2
            if im_var_2 == 1:
                empPhoto = convertToBinaryData(t.filename)
                cursor.execute("Update POLICE set photo=? where POLICEID=?", (empPhoto, j,))
            tempor=mcq.fetchall()
            print(tempor)
            if len(tempor)==1 and contact_number_2.get()!='':
                cursor.execute("INSERT INTO POLICE1 VALUES(?,?)",(j,contact_number_2.get()))
            else:
                if contact_number_2.get()!='':
                    cursor.execute("UPDATE POLICE1 set CONTACT=(?) where POLICEID=(?) and CONTACT=(?)",(contact_number_2.get(),j,l[1]))
        except Exception as e:
            tkinter.messagebox.showinfo('Alert',"Couldn't connect to Database\nError Description : "+str(e))
        else:
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation', 'User Updated')

        try:
            os.remove("pol" + j+ ".jpg")
            print(j)
        except:
            print('Not Found')
            pass

        t.destroy()
        from sys_home import system_home
        system_home(k)

    #-------------------------------------

    t=Tk()
    t.title('Update Police User Details Form')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    fi = tkFont.Font(family="Times New Roman", size=25)
    fih = tkFont.Font(family="Times New Roman", size=16)
    l_first_name = Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                         relief="solid")
    l_first_name.place(x=50, y=50, width=200, height=50)
    l_middle_name = Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                          relief="solid")
    l_middle_name.place(x=50, y=120, width=200, height=50)
    l_last_name = Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                        relief="solid")
    l_last_name.place(x=50, y=190, width=200, height=50)
    OptionList11 = ['Male', 'Female', 'Others']
    v = StringVar(t)
    gender = OptionMenu(t, v, *OptionList11)
    menu = t.nametowidget(gender.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    gender.config(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    gender.place(x=50, y=260, width=200, height=50)

    l_date_of_birth = Label(t, text='Date of Birth', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                            relief="solid")
    l_date_of_birth.place(x=50, y=330, width=200, height=50)
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29, 30, 31]
    d = IntVar(t)
    day = OptionMenu(t, d, *dayOptionList)
    menu = t.nametowidget(day.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    monthOptionList = [1,2,3,4,5,6,7,8,9,10,11,12]
    mth = IntVar(t)
    month = OptionMenu(t, mth, *monthOptionList)
    menu = t.nametowidget(month.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    msOptionList = ['Married', 'Unmarried', 'Rather Not Say']
    ms = StringVar(t)
    ms1 = OptionMenu(t, ms, *msOptionList)
    menu = t.nametowidget(ms1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    yearOptionList = []
    for i in range(1950, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    year = OptionMenu(t, y, *yearOptionList)
    menu = t.nametowidget(year.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    day.place(x=275, y=330,width=130, height=50)
    month.place(x=405, y=330,width=130, height=50)
    year.place(x=535, y=330,width=140, height=50)
    day.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    month.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    year.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    ms1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    ms1.place(x=275, y=260, width=400, height=50)
    l_police_id = Label(t, text='Police ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_police_id.place(x=825, y=330, width=200, height=50)
    l_email_id = Label(t, text='Email ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_email_id.place(x=50, y=540, width=200, height=50)
    l_jurisdiction = Label(t, text='Jurisdiction',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_jurisdiction.place(x=825, y=540, width=200, height=50)
    l_address = Label(t, text='Address',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_address.place(x=50, y=610, width=200, height=50)
    v2 = StringVar(t)
    rank_options = ['ACP', 'CONSTABLE', 'SYSTEM ADMINISTRATOR']
    l_rank = Label(t, text='Rank',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_rank.place(x=825, y=400, width=200, height=50)
    rank_menu = OptionMenu(t, v2, *rank_options)
    rank_menu.place(x=1050, y=400, width=400, height=50)
    menu = t.nametowidget(rank_menu.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    rank_menu.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    l_contact_number_1 = Label(t, text='Contact Number 1',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_contact_number_1.place(x=50, y=400, width=200, height=50)
    l_contact_number_2 = Label(t, text='Contact Number 2',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_contact_number_2.place(x=50, y=470, width=200, height=50)
    l_batch = Label(t, text='Batch',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_batch.place(x=825, y=610, width=200, height=50)
    l_password = Label(t, text='Password',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_password.place(x=825, y=470, width=200, height=50)

    fn=StringVar(t)
    mn=StringVar(t)
    ln=StringVar(t)
    pid=StringVar(t)
    eid=StringVar(t)
    jur=StringVar(t)
    addr = StringVar(t)
    c1=StringVar(t)
    c2=StringVar(t)
    bch=StringVar(t)
    pas=StringVar(t)

    first_name=Entry(t,font=tkFont.Font(family="Times New Roman", size=20),textvariable=fn, borderwidth=2, relief="solid")
    middle_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=mn, borderwidth=2, relief="solid")
    last_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=ln, borderwidth=2, relief="solid")
    police_id = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=pid, borderwidth=2, relief="solid")
    email_id = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=eid, borderwidth=2, relief="solid")
    jurisdiction = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=jur, borderwidth=2, relief="solid")
    address = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=addr, borderwidth=2, relief="solid")
    contact_number_1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=c1, borderwidth=2, relief="solid")
    contact_number_2 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=c2, borderwidth=2, relief="solid")
    batch = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=bch, borderwidth=2, relief="solid")
    password = Entry(t, font=tkFont.Font(family="Times New Roman", size=20),textvariable=pas, borderwidth=2, relief="solid")
    update_user_2_button=Button(t, text='UPDATE USER',font=tkFont.Font(family="Times New Roman", size=16), command=updated_user, borderwidth=4, relief="solid")
    back_button = Button(t, text='GO BACK',font=tkFont.Font(family="Times New Roman", size=16), command=back,borderwidth=4, relief="solid")

    cursor.execute("SELECT * FROM POLICE where POLICEID=?",(j,))
    for row in cursor.fetchall():
        #print('Success1')
        pass
    cursor.execute("SELECT * FROM POLICE1 where POLICEID=?",(j,))
    l=[]
    for row1 in cursor.fetchall():
        l.append(row1[1])
        #print('Success2')

    fn.set(row[2])
    mn.set(row[3])
    ln.set(row[4])
    v.set(row[10])
    addr.set(row[9])
    pid.set(row[0])
    eid.set(row[7])
    jur.set(row[8])
    v2.set(row[13])
    ms.set(row[14])
    c1.set(l[0])
    if len(l)>1:
        c2.set(l[1])
    bch.set(row[12])
    pas.set(row[1])

    d_o_b = row[11]
    s = d_o_b.split('-')
    d.set(int(s[2]))
    mth.set(int(s[1]))
    y.set(int(s[0]))

    police_id.place(x=1050, y=330, width=400, height=50)
    password.place(x=1050, y=470, width=400, height=50)
    first_name.place(x=275, y=50, width=400, height=50)
    middle_name.place(x=275, y=120, width=400, height=50)
    last_name.place(x=275, y=190, width=400, height=50)
    email_id.place(x=275, y=540, width=400, height=50)
    jurisdiction.place(x=1050, y=540, width=400, height=50)
    address.place(x=275, y=610, width=400, height=50)
    contact_number_1.place(x=275, y=400, width=400, height=50)
    contact_number_2.place(x=275, y=470, width=400, height=50)
    batch.place(x=1050, y=610, width=400, height=50)
    update_user_2_button.place(x=650, y=690, width=250, height=50)
    back_button.place(x=250, y=690, width=250, height=50)

    cursor.execute("SELECT * FROM POLICE where POLICEID=?", (j,))
    for row in cursor.fetchall():
        #print("Id = ", row[0])
        pol_id = row[0]
        photo = row[5]
        photoPath = "pol" + pol_id + ".jpg"
    with open(photoPath, 'wb') as file:
        file.write(photo)

    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 250), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load,master=t)
    t.img1 = Button(t, image=t.photo1,command=image_update,borderwidth=2, relief="solid")
    t.img1.image = t.photo1
    t.img1.place(x=1025, y=50, width=250, height=250)
    mainloop()

#test('110','101')