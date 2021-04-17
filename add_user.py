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
        load55 = load55.resize((250, 250), Image.ANTIALIAS)
        photo6 = ImageTk.PhotoImage(load55)
        img15 = Button(t, image=photo6, command=image_choose,borderwidth=2, relief="solid")
        img15.image = photo6
        img15.place(x=1025, y=50, width=250, height=250)


    def convertToBinaryData(filena):
        with open(filena, 'rb') as file:
            blobData = file.read()
        return blobData

    def save_user():
        
        cursor.execute('CREATE TABLE IF NOT EXISTS POLICE(POLICEID TEXT PRIMARY KEY CHECK(POLICEID <> ""), PASSWORD TEXT NOT NULL CHECK(PASSWORD <> ""),FNAME TEXT NOT NULL CHECK(FNAME <> ""), MNAME TEXT, LNAME TEXT NOT NULL CHECK(LNAME <> ""), PHOTO BLOB NOT NULL, LASTLOGIN TEXT, EMAILID TEXT NOT NULL CHECK(EMAILID <> ""), JURISDICTION TEXT NOT NULL CHECK(JURISDICTION <> ""), ADDRESS TEXT NOT NULL CHECK(ADDRESS <> ""), GENDER TEXT NOT NULL CHECK(GENDER <> ""), DOB TEXT NOT NULL CHECK(DOB <> ""), BATCH TEXT NOT NULL CHECK(BATCH <> ""), RANK TEXT NOT NULL CHECK(RANK <> ""), MARITALSTATUS TEXT NOT NULL)')
        cursor.execute("""CREATE TABLE IF NOT EXISTS POLICE1(POLICEID TEXT, CONTACT TEXT NOT NULL, FOREIGN KEY (POLICEID) REFERENCES POLICE(POLICEID))""")


        u1=cursor.execute('SELECT POLICEID from POLICE where POLICEID =?',(police_id.get(),))
        temp=u1.fetchall()
        if len(temp)==0:
            #print(len(uid.get()))
            u2 = police_id.get()
            if len(u2)<=3:
                tkinter.messagebox.showinfo('Alert','Police ID must be atleast 4 characters long')
                return
            pword = password.get()
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)
            mat = re.search(pat, pword)
            if not mat:
                tkinter.messagebox.showinfo('Alert','Insecure Password.')
                return

            num = contact_number_1.get()
            if type(num) != int and len(str(num)) != 10:
                tkinter.messagebox.showinfo('Alert','Enter correct Mobile Number 1')
                return

            if contact_number_2.get()!='':
                num2 = contact_number_2.get()
                if type(num2) != int and len(str(num2)) != 10:
                    tkinter.messagebox.showinfo('Alert','Enter correct Mobile Number 2')
                    return

            e = email_id.get()
            rege = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            if not (re.search(rege, e)):
                tkinter.messagebox.showinfo('Alert','Enter correct Email Address')
                return

            try:
                empPhoto = convertToBinaryData(t.filename)
                d_o_b = str(y.get()) + '-' + str(mth.get()) + '-' + str(d.get())
                cursor.execute('CREATE TABLE IF NOT EXISTS POLICE(POLICEID TEXT PRIMARY KEY CHECK(POLICEID <> ""), PASSWORD TEXT NOT NULL CHECK(PASSWORD <> ""),FNAME TEXT NOT NULL CHECK(FNAME <> ""), MNAME TEXT, LNAME TEXT NOT NULL CHECK(LNAME <> ""), PHOTO BLOB NOT NULL, LASTLOGIN TEXT, EMAILID TEXT NOT NULL CHECK(EMAILID <> ""), JURISDICTION TEXT NOT NULL CHECK(JURISDICTION <> ""), ADDRESS TEXT NOT NULL CHECK(ADDRESS <> ""), GENDER TEXT NOT NULL CHECK(GENDER <> ""), DOB TEXT NOT NULL CHECK(DOB <> ""), BATCH TEXT NOT NULL CHECK(BATCH <> ""), RANK TEXT NOT NULL CHECK(RANK <> ""), MARITALSTATUS TEXT NOT NULL)')
                cursor.execute("""CREATE TABLE IF NOT EXISTS POLICE1(POLICEID TEXT, CONTACT TEXT NOT NULL, FOREIGN KEY (POLICEID) REFERENCES POLICE(POLICEID))""")

                cursor.execute("INSERT INTO POLICE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (police_id.get(), password.get(), first_name.get(), middle_name.get(), last_name.get(),empPhoto,last_login,email_id.get(),jurisdiction.get(),address.get(), v.get(),d_o_b, batch.get(), v2.get(), ms.get()))
                cursor.execute("INSERT INTO POLICE1 VALUES(?,?)", (police_id.get(), contact_number_1.get()))
                if contact_number_2.get()!='':
                    cursor.execute("INSERT INTO POLICE1 VALUES(?,?)", (police_id.get(), contact_number_2.get()))

            except Exception as e:
                tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e)+"\n\nPlease Check all Details and Retry.")
            
            else:
                connection.commit()
                tkinter.messagebox.showinfo('Confirmation', 'User created')
                t.destroy()
                from sys_home import system_home
                system_home(k)
        else:
            tkinter.messagebox.showinfo('Alert','Police ID Already Exists.')

        

    def clear_details():
        first_name.delete(0, 'end')
        middle_name.delete(0, 'end')
        last_name.delete(0, 'end')
        email_id.delete(0, 'end')
        batch.delete(0, 'end')
        jurisdiction.delete(0, 'end')
        address.delete(0, 'end')
        contact_number_1.delete(0, 'end')
        contact_number_2.delete(0, 'end')
        password.delete(0, 'end')
        police_id.delete(0, 'end')

        d.set('dd')
        mth.set('mm')
        y.set('yyyy')
        ms.set('Marital Status')
        v2.set('Select')
        v.set('Select Gender')

        image_button= Button(t, text='Choose Photo', font=tkFont.Font(family="Times New Roman", size=16), command=image_choose,
                       borderwidth=2, relief="solid")
        image_button.place(x=1025, y=50, width=250, height=250)

        return

    #------------------------------------
    t = Tk()
    t.title('Add Police User Form')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

### Defining the Labels
    l_first_name = Label(t, text='First Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_middle_name = Label(t, text='Middle Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_last_name = Label(t, text='Last Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    OptionList11 = ['Male', 'Female', 'Others']
    v = StringVar(t)
    gender = OptionMenu(t, v, *OptionList11)
    menu = t.nametowidget(gender.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    gender.config(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    msOptionList = ['Married', 'Unmarried', 'Rather Not Say']
    ms = StringVar(t)
    ms1 = OptionMenu(t, ms, *msOptionList)
    menu = t.nametowidget(ms1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    ms1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    l_date_of_birth = Label(t, text='Date of Birth',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
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
    yearOptionList = []
    for i in range(1950, 2002):
        yearOptionList.append(i)
    y = IntVar(t)
    year = OptionMenu(t, y, *yearOptionList)
    menu = t.nametowidget(year.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    day.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    month.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    year.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    l_contact_number_1 = Label(t, text='Contact Number 1',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_contact_number_2 = Label(t, text='Contact Number 2',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_email_id = Label(t, text='Email ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_address = Label(t, text='Address',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")


    l_police_id = Label(t, text='Police ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

    rank_options = ['ACP', 'CONSTABLE', 'SYSTEM ADMINISTRATOR']
    v2 = StringVar(t)
    l_rank = Label(t, text='Rank',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    rank_menu = OptionMenu(t, v2, *rank_options)
    menu = t.nametowidget(rank_menu.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    rank_menu.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    l_password = Label(t, text='Password',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_jurisdiction = Label(t, text='Jurisdiction',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    l_batch = Label(t, text='Batch',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

### Placing the Labels
    l_first_name.place(x=50, y=50, width=200, height=50)
    l_middle_name.place(x=50, y=120, width=200, height=50)
    l_last_name.place(x=50, y=190, width=200, height=50)
    gender.place(x=50, y=260, width=200, height=50)
    l_date_of_birth.place(x=50, y=330, width=200, height=50)
    l_contact_number_1.place(x=50, y=400, width=200, height=50)
    l_contact_number_2.place(x=50, y=470, width=200, height=50)
    l_email_id.place(x=50, y=540, width=200, height=50)
    l_address.place(x=50, y=610, width=200, height=50)

    l_police_id.place(x=825, y=330, width=200, height=50)
    l_rank.place(x=825, y=400, width=200, height=50)
    l_password.place(x=825, y=470, width=200, height=50)
    l_jurisdiction.place(x=825, y=540, width=200, height=50)
    l_batch.place(x=825, y=610, width=200, height=50)

### Defining the Entry boxes
    first_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    middle_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    last_name = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    contact_number_1 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    contact_number_2 = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    email_id = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    address= Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")

    police_id = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    password = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    jurisdiction = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")
    batch = Entry(t, font=tkFont.Font(family="Times New Roman", size=20), borderwidth=2, relief="solid")


### Placing the Entry Boxes
    police_id.place(x=1050, y=330, width=400, height=50)
    rank_menu.place(x=1050, y=400, width=400, height=50)
    password.place(x=1050, y=470, width=400, height=50)
    jurisdiction.place(x=1050, y=540, width=400, height=50)
    batch.place(x=1050, y=610, width=400, height=50)

    first_name.place(x=275, y=50, width=400, height=50)
    middle_name.place(x=275, y=120, width=400, height=50)
    last_name.place(x=275, y=190, width=400, height=50)
    ms1.place(x=275, y=260, width=400, height=50)
    day.place(x=275, y=330,width=130, height=50)
    month.place(x=405, y=330,width=130, height=50)
    year.place(x=535, y=330,width=140, height=50)
    contact_number_1.place(x=275, y=400, width=400, height=50)
    contact_number_2.place(x=275, y=470, width=400, height=50)
    email_id.place(x=275, y=540, width=400, height=50)
    address.place(x=275, y=610, width=400, height=50)

### Defining the Buttons
    image_button = Button(t, text='Choose photo', font=tkFont.Font(family="Times New Roman", size=16),
                          command=image_choose, borderwidth=2, relief="solid")

    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")
    add_user_button = Button(t, text='SAVE USER', font=tkFont.Font(family="Times New Roman", size=16),
                             command=save_user, borderwidth=4, relief="solid")
    reset = Button(t, text='RESET', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details,
                   borderwidth=4, relief="solid")
### Placing the Buttons
    image_button.place(x=1025, y=50, width=250, height=250)

    back_button.place(x=250, y=690, width=250, height=50)
    add_user_button.place(x=650, y=690, width=250, height=50)
    reset.place(x=1050, y=690, width=250, height=50)

### Setting the initial variables
    d.set('dd')
    mth.set('mm')
    y.set('yyyy')
    ms.set('Marital Status')
    v.set('Select Gender')
    v2.set('Select')
    last_login = '0 0'

    req = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                borderwidth=0)
    req1 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req2 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req3 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req4 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req5 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req7 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req8 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req9 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                 borderwidth=0)
    req10 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)
    req11 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)
    req12 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)
    req13 = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)

    req1.place(x=250, y=260, width=10, height=50)
    req.place(x=675, y=50, width=10, height=50)
    req2.place(x=675, y=190, width=10, height=50)
    req3.place(x=675, y=260, width=10, height=50)
    req4.place(x=675, y=330, width=10, height=50)
    req5.place(x=675, y=400, width=10, height=50)
    req7.place(x=675, y=540, width=10, height=50)
    req8.place(x=675, y=610, width=10, height=50)

    req9.place(x=1450, y=330, width=10, height=50)
    req10.place(x=1450, y=400, width=10, height=50)
    req11.place(x=1450, y=470, width=10, height=50)
    req12.place(x=1450, y=540, width=10, height=50)
    req13.place(x=1450, y=610, width=10, height=50)

    reqp = Label(t, text='*', font=tkFont.Font(family="Times New Roman", size=12), anchor="nw", foreground="red",
                  borderwidth=0)
    reqp.place(x=1275, y=50, width=10, height=50)

    mainloop()
