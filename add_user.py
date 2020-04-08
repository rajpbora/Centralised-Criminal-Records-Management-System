import sqlite3
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def test5(k):
    def back():
        t.destroy()
        from sys_home import system_home
        system_home(k)

    def image_choose():
        t.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
        load55 = Image.open(t.filename)
        load55 = load55.resize((250, 350), Image.ANTIALIAS)
        photo6 = ImageTk.PhotoImage(load55)
        img15 = Button(t, image=photo6, command=image_choose)
        img15.image = photo6
        img15.place(x = 1050, y = 10, width=250, height=350)

    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def save_user():
        try:
            empPhoto = convertToBinaryData(t.filename)
            d_o_b = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
            cursor.execute("CREATE TABLE IF NOT EXISTS POLICE(POLICEID TEXT PRIMARY KEY NOT NULL CHECK(POLICEID <> ''),"
                           "PASSWORD TEXT NOT NULL CHECK(PASSWORD <> ''),FNAME TEXT NOT NULL CHECK(FNAME <> ''),"
                           "MNAME TEXT,LNAME TEXT NOT NULL CHECK(LNAME <> ''),PHOTO BLOB NOT NULL CHECK(PHOTO <> ''),"
                           "LASTLOGIN TEXT, EMAILID TEXT CHECK(EMAILID <> ''),JURISDICTION TEXT CHECK(JURISDICTION  <> ''),ADDRESS TEXT CHECK("
                           "ADDRESS <> ''),GENDER TEXT NOT NULL CHECK(GENDER <> ''),DOB TEXT NOT NULL CHECK(DOB <> "
                           "''),BATCH TEXT NOT NULL CHECK(BATCH <> ''),RANK TEXT NOT NULL CHECK(RANK <> ''),MARITALSTATUS "
                           "TEXT NOT NULL CHECK(MARITALSTATUS <> ''))")

            cursor.execute("INSERT INTO POLICE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (police_id.get(), password.get(), first_name.get(), middle_name.get(), last_name.get(),empPhoto,last_login,email_id.get(),jurisdiction.get(),address.get(), v.get(),d_o_b, batch.get(), v2.get(), ms.get()))
            cursor.execute("CREATE TABLE IF NOT EXISTS POLICE1(POLICEID TEXT, CONTACT TEXT,FOREIGN KEY (POLICEID) REFERENCES POLICE0(POLICEID))")
            cursor.execute("INSERT INTO POLICE1 VALUES(?,?)", (police_id.get(), contact_number_1.get()))
            if contact_number_2.get()!='':
                cursor.execute("INSERT INTO POLICE1 VALUES(?,?)", (police_id.get(), contact_number_2.get()))
        except Exception as e:
            tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
        else:
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation', 'User created')
            t.destroy()
            from sys_home import system_home
            system_home(k)

    #------------------------------------
    t = Tk()
    t.title('Add Police User Form')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    fi = tkFont.Font(family="Times New Roman", size=25)
    l_first_name = Label(t, text='First Name :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    l_first_name.place(x=50,y=10)
    l_middle_name = Label(t, text='Middle Name :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    l_middle_name.place(x=50,y=75)
    l_last_name = Label(t, text='Last Name :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    l_last_name.place(x=50,y=140)
    gender = Label(t, text='Gender :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    gender .place(x=50, y=205)
    v = StringVar()
    r1=Radiobutton(t, text='Male',font=tkFont.Font(family="Times New Roman", size=20), variable=v, value='Male')
    r1.place(x=230, y=205)
    r2=Radiobutton(t, text='Female',font=tkFont.Font(family="Times New Roman", size=20), variable=v, value='Female')
    r2.place(x=350, y=205)
    r3=Radiobutton(t, text='Other',font=tkFont.Font(family="Times New Roman", size=20), variable=v, value='Other')
    r3.place(x=500, y=205)
    l_date_of_birth = Label(t, text='Date of Birth :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    l_date_of_birth.place(x=50, y=270)
    dayOptionList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29, 30, 31]
    d = IntVar(t)
    day = OptionMenu(t, d, *dayOptionList)
    monthOptionList = [1,2,3,4,5,6,7,8,9,10,11,12]
    mth = IntVar(t)
    month = OptionMenu(t, mth, *monthOptionList)
    msOptionList = ['Married', 'Unmarried', 'Rather Not Say']
    ms = StringVar(t)
    ms1 = OptionMenu(t, ms, *msOptionList)
    yearOptionList = []
    for i in range(1950, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    year = OptionMenu(t, y, *yearOptionList)
    day.place(x=230, y=270)
    month.place(x=350, y=270)
    year.place(x=500, y=270)
    day.configure(font=fi, relief="solid")
    month.configure(font=fi, relief="solid")
    year.configure(font=fi, relief="solid")
    ms1.place(x=230, y=595)
    ms1.configure(font=fi, relief="solid")
    l_police_id = Label(t, text='Police ID :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12, height=2)
    l_police_id.place(x=50, y=335)
    l_email_id = Label(t, text='Email I.D. :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12, height=2)
    l_email_id .place(x=50,y=400)
    l_jurisdiction = Label(t, text='Jurisdiction :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12, height=2)
    l_jurisdiction .place(x=50, y=465)
    l_address = Label(t, text='Address :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12, height=2)
    l_address.place(x=850,y=660)
    v2 = StringVar(t)
    rank_options = ['ACP', 'CONSTABLE', 'SYSTEM ADMINISTRATOR']
    l_rank = Label(t, text='Rank :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12, height=2)
    l_rank.place(x=50, y=530)
    rank_menu = OptionMenu(t, v2, *rank_options)
    rank_menu.place(x=230, y=530)
    rank_menu.configure(font=fi, relief="solid")
    l_marital_status = Label(t, text='Marital\n Status :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12,height=2)
    l_marital_status .place(x=50, y=595)
    l_contact_number_1 = Label(t, text='Contact \nNumber 1 :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12,height=2)
    l_contact_number_1.place(x=850,y=400)
    l_contact_number_2 = Label(t, text='Contact \nNumber 2 :',font=tkFont.Font(family="Times New Roman", size=16), anchor='w', borderwidth=2, relief="solid", width=12,height=2)
    l_contact_number_2.place(x=850,y=465)
    l_batch = Label(t, text='Batch :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    l_batch.place(x=850,y=595)
    l_password = Label(t, text='PASSWORD :', anchor='w',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=12, height=2)
    l_password.place(x=850,y=530)


    first_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    middle_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    last_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    police_id = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    email_id = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    jurisdiction = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    address= Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    contact_number_1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    contact_number_2 = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    batch = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
    password = Entry(t, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

    add_user_button = Button(t, text='SAVE USER',font=tkFont.Font(family="Times New Roman", size=16), command=save_user, borderwidth=4, relief="solid", width=26,height=2)
    image_button=Button(t, text='Choose image file', command=image_choose, borderwidth=2, relief="solid")
    back_button=Button(t, text='RETURN',font=tkFont.Font(family="Times New Roman", size=16), command=back,borderwidth=4, relief="solid", width=26,height=2)
    back_button.place(x=50, y=700)
    police_id.place(x=230,y=335)
    password.place(x=1050,y=530)
    first_name.place(x=230, y=10)
    middle_name.place(x=230, y=75)
    last_name.place(x=230, y=140)
    email_id.place(x=230,y=400)
    jurisdiction.place(x=230,y=465)
    address.place(x=1050,y=660)
    contact_number_1.place(x=1050,y=400)
    contact_number_2.place(x=1050,y=465)
    batch.place(x=1050,y=595)
    add_user_button.place(x=416, y=700)
    #x=516, y=640 
    image_button.place(x = 1050, y = 10, width=250, height=350)

    v.set('Female')
    d.set('Day')
    mth.set('Month')
    y.set('Year')
    ms.set('Marital Status')
    v2.set(rank_options[2])
    last_login = '0 0'

    mainloop()

#test5('101')