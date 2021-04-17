from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import datetime


def test(k,j,j1,j2,j3,photoPath):
    t = tk.Tk()
    t.title('CRIMINAL')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    born1 = j[0][4]
    sss = born1.split('-')
    mmm = datetime.datetime.today()

    b = mmm.year - int(sss[0])

    def back():
        t.destroy()
        from constable_home import const_home
        const_home(k)

    fi = tkFont.Font(family="Times New Roman", size=16)

### Defining the Labels
    fname = Label(t, text='Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    gender = Label(t, text='Gender', font=fi, borderwidth=2, relief="solid")
    l_date_of_birth = Label(t, text='Date of Birth', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                            relief="solid")
    age = Label(t, text='AGE', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",
                width=18, height=2)

    bloodgrp = Label(t, text='Blood Group', font=fi, borderwidth=2, relief="solid")

    c_id = Label(t, text='Criminal ID', font=fi, borderwidth=2, relief="solid")
    status = Label(t, text='Status', font=fi, borderwidth=2, relief="solid")
    priority = Label(t, text='Priority', font=fi, borderwidth=2, relief="solid")

    im = Label(t, text='Identification marks', font=fi, borderwidth=2, relief="solid")
    ad = Label(t, text='Address', font=fi, borderwidth=2, relief="solid")
    hd = Label(t, text='Contact number', font=fi, borderwidth=2, relief="solid")

### Defining the Entry boxes
    fname1 = Label(t, text=j[0][1] + " " + j[0][2] + " " + j[0][3], font=tkFont.Font(family="Times New Roman", size=18),
                   borderwidth=2, relief="solid", width=15, height=2)
    gender1 = Label(t, text=j[0][8], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,
                    relief="solid")
    dob1 = Label(t, text=j[0][4], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid",
                 width=15, height=2)
    age1 = Label(t, text=b, font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,
                 relief="solid", width=15, height=2)
    bloodgrp1 = Label(t, text=j[0][5], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,
                      relief="solid")

    c_id1 = Label(t, text=j[0][0], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    status1 = Label(t, text=j[0][6], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    priority1 = Label(t, text=j[0][7], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2,
                      relief="solid")

    OptionList = []
    c = 0
    for i00 in j1:
        OptionList.append(j1[c][1])
        c = c + 1
    v = tk.StringVar(t)
    v.set('INDENTIFICATION MARKS ')
    marks = tk.OptionMenu(t, v, *OptionList)

    OptionList2 = []
    c = 0
    for i11 in j2:
        OptionList2.append(j2[c][1])
        c = c + 1

    v2 = tk.StringVar(t)
    v2.set('ADDRESS')
    address = tk.OptionMenu(t, v2, *OptionList2)

    OptionList3 = []
    c = 0
    for i22 in j3:
        OptionList3.append(j3[c][1])
        c = c + 1
    v3 = tk.StringVar(t)
    v3.set('CONTACT')
    hideout = tk.OptionMenu(t, v3, *OptionList3)

    menu = t.nametowidget(marks.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    menu = t.nametowidget(address.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    menu = t.nametowidget(hideout.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    marks.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    address.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    hideout.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

### Placing the Labels
    fname.place(x=50, y=50, width=200, height=50)
    gender.place(x=50, y=120, width=200, height=50)
    l_date_of_birth.place(x=50, y=190, width=200, height=50)
    age.place(x=50, y=260, width=200, height=50)
    bloodgrp.place(x=50, y=330, width=200, height=50)
    im.place(x=50, y=400, width=200, height=50)
    ad.place(x=50, y=470, width=200, height=50)
    hd.place(x=50, y=540, width=200, height=50)

    c_id.place(x=825, y=400, width=200, height=50)
    status.place(x=825, y=470, width=200, height=50)
    priority.place(x=825, y=540, width=200, height=50)

### Placing the Entry Boxes
    fname1.place(x=275, y=50, width=400, height=50)
    gender1.place(x=275, y=120, width=400, height=50)
    dob1.place(x=275, y=190, width=400, height=50)
    age1.place(x=275, y=260, width=400, height=50)
    bloodgrp1.place(x=275, y=330, width=400, height=50)

    marks.place(x=275, y=400, width=400, height=50)
    address.place(x=275, y=470, width=400, height=50)
    hideout.place(x=275, y=540, width=400, height=50)

    c_id1.place(x=1050, y=400, width=400, height=50)
    status1.place(x=1050, y=470, width=400, height=50)
    priority1.place(x=1050, y=540, width=400, height=50)

### Defining the buttons
    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")

### Placing the buttons
    back_button.place(x=250, y=690, width=250, height=50)

### Putting the image Button
    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 350), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load, master=t)
    t.img1 = Label(t, image=t.photo1, borderwidth=2, relief="solid")
    t.img1.image = t.photo1

### Placing the image Button
    t.img1.place(x=1025, y=50, width=250, height=250)

    mainloop()