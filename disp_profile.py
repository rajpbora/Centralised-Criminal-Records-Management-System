from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk

def display_details(user, user2):

    t = tk.Tk()
    
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))

    def edit():
        editdata(user, user2)
        return

    def goback():
        import os
        os.remove('c'+user[0]+'.jpg')
        t.destroy()
        import civilian_home as tty
        tty.civ_home(user[0])


    path = "c" + user[0] + '.jpg'

    with open(path, 'wb') as file:
        file.write(user[12])

    t.load2 = Image.open(path)
    t.load2 = t.load2.resize((300, 300), Image.ANTIALIAS)
    t.photo2 = ImageTk.PhotoImage(t.load2, master=t)
    t.img2 = Button(t, image=t.photo2, borderwidth=2, relief="solid")
    t.img2.image = t.photo2

    tnm=user[2].upper()+' '+user[3].upper()+' '+user[4].upper()
    t.title('Profile - '+tnm)

    fname1 = Label(t, text=tnm, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    email1 = Label(t, text=user[8], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    contact1 = Label(t, text=user2[1], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    day = Label(t, text='Date Of Birth', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    mth = Label(t, text=user[5], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    lgender = Label(t, text='Gender', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    gender = Label(t, text=user[6], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    address1 = Label(t, text=user[10], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    occupation1 = Label(t, text=user[9], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    uid = Label(t, text='USER_ID : '+user[0], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    fname = Label(t, text='Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    #mname = Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    #lname = Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    email = Label(t, text='Email_ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    contact = Label(t, text='Mobile_Number', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid")
    address = Label(t, text='Address', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    occupation = Label(t, text='Occupation', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,relief="solid")
    lmarital = Label(t, text=user[7], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    marital = Label(t, text='Marital Status', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")    

    fname.place(x=50, y=50, width=200, height=70)
    fname1.place(x=275, y=50, width=750, height=70)

    lgender.place(x=50, y=150, width=200, height=70)
    gender.place(x=275, y=150, width=250, height=70)

    day.place(x=550, y=150, width=200, height=70)
    mth.place(x=775, y=150, width=250, height=70)

    marital.place(x=50, y=250, width=200, height=70)
    lmarital.place(x=275, y=250, width=250, height=70)

    email.place(x=50, y=350, width=200, height=70)
    contact.place(x=550, y=250, width=200, height=70)
    email1.place(x=275, y=350, width=475, height=70)
    contact1.place(x=775, y=250, width=250, height=70)

    occupation.place(x=50, y=450, width=200, height=70)
    occupation1.place(x=275, y=450, width=475, height=70)

    address.place(x=50, y=550, width=200, height=70)
    address1.place(x=275, y=550, width=1100, height=70)

    back=Button(t, text='GO BACK', command=goback, borderwidth=4, relief="solid").place(x=50,y=675, width=200, height=70)

    uid.place(x=1070, y=375, width=300, height=70)

    t.img2.place(x=1070, y=50, width=300, height=300)

    edit = Button(t, text='EDIT', command=edit, borderwidth=4, relief="solid")

    mainloop()
    