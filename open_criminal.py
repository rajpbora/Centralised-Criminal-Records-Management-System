from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import datetime


def test(k,j,j1,j2,j3,photoPath):

    t=tk.Tk()
    t.title('CRIMINAL')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w, h))
    def back():
        t.destroy()
        from constable_home import const_home
        const_home(k)

    fih = tkFont.Font(family="Times New Roman", size=20)

    fname=Label(t, text='Full Name',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    fname1=Label(t,text=j[0][1]+'   '+j[0][2]+'   '+j[0][3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)

    born1=j[0][4]
    sss= born1.split('-')
    mmm = datetime.datetime.today()

    b = mmm.year - int(sss[0])






    priority=Label(t, text='PRIORITY',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    c_id=Label(t, text='CRIMINAL ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    status=Label(t, text='STATUS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    c_id1=Label(t,text=j[0][0],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    status1=Label(t,text=j[0][6],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    priority1=Label(t,text=j[0][7],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    gender=Label(t, text='GENDER',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    gender1=Label(t,text=j[0][8],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    bloodgrp=Label(t, text='BLOOD GROUP',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    bloodgrp1=Label(t,text=j[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    OptionList=[j1[0][1]]
    v = tk.StringVar(t)
    v.set('INDENTIFICATION MARKS ')
    marks= tk.OptionMenu(t, v, *OptionList)
    OptionList2=[j2[0][1]]
    OptionList3=[j3[0][1]]
    v2 = tk.StringVar(t)
    v2.set('ADDRESS')
    address= tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('CONTACT')
    hideout=tk.OptionMenu(t, v3, *OptionList3)
    dob=Label(t, text='DATE OF BIRTH',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    dob1=Label(t,text=j[0][4],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    age=Label(t, text='AGE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=18,height=2)
    age1=Label(t,text=b,font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    back_button = Button(t, text='Go Back',font=fih, command=back, borderwidth=2, relief="solid", width=26, height=2).place(
        x=950, y=700)

    t.load = Image.open(photoPath)
    t.load = t.load.resize((250, 350), Image.ANTIALIAS)
    t.photo1 = ImageTk.PhotoImage(t.load,master=t)
    t.img1 = Label(t, image=t.photo1)
    t.img1.image = t.photo1
    t.img1.place(x = 1000, y = 100, width=200, height=200)




    fname.place(x=50, y=10)
    fname1.place(x=300, y=10)

    c_id.place(x=50, y=75)
    priority.place(x=50, y=560)
    c_id1.place(x=300, y=75)
    priority1.place(x=300, y=560)
    status.place(x=50, y=625)
    status1.place(x=300, y=625)

    marks.place(x=50, y=420, width=300, height=70)
    address.place(x=50, y=495, width=300, height=70)
    hideout.place(x=50, y=345, width=300, height=70)
    gender.place(x=50, y=270)
    gender1.place(x=300, y=270)
    dob.place(x=50, y=140)
    dob1.place(x=300, y=140)
    age.place(x=50, y=690)
    age1.place(x=300, y=690)
    bloodgrp.place(x=50, y=205)
    bloodgrp1.place(x=300, y=205)







    mainloop()