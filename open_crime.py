from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk

def best(p,k,k1,k2):
    t=tk.Tk()
    t.title('CRIME')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" %(w,h))
    def back():
        t.destroy()
        from constable_home import const_home
        const_home(p)

    fir_no = Label(t, text='FIR Number', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                   relief="solid")
    ci = Label(t, text='Criminal ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
               relief="solid")
    doc = Label(t, text='Date of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    poc = Label(t, text='Place of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    ch = Label(t, text='Charges', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
    nod = Label(t, text='No. of Deaths', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    noi = Label(t, text='No. of Injured', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    da = Label(t, text='Cost of Damages', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
               relief="solid")

    fir_no1 = Label(t, text=k[0][0], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    doc1 = Label(t, text=k[0][4], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    poc1 = Label(t, text=k[0][5], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    nod1 = Label(t, text=k[0][3], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    noi1 = Label(t, text=k[0][2], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")
    da1 = Label(t, text=k[0][1], font=tkFont.Font(family="Times New Roman", size=18), borderwidth=2, relief="solid")

    OptionList = []
    c = 0
    for i00 in k1:
        OptionList.append(k1[c][1])
        c = c + 1
    v = tk.StringVar(t)
    v.set('IDs')
    ci1 = tk.OptionMenu(t, v, *OptionList)

    menu = t.nametowidget(ci1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    ci1.configure(font=tkFont.Font(family="Times New Roman", size=18), relief="solid")

    OptionList2 = []
    c = 0
    for i11 in k2:
        OptionList2.append(str(k2[c][1]) + " " + str(k2[c][2]))
        c = c + 1
    v2 = tk.StringVar(t)
    v2.set('Charges')
    ch1 = tk.OptionMenu(t, v2, *OptionList2)

    menu = t.nametowidget(ch1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    ch1.configure(font=tkFont.Font(family="Times New Roman", size=18), relief="solid")

    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")
    back_button.place(x=250, y=690, width=250, height=50)

    fir_no.place(x=50, y=50, width=200, height=50)
    ci.place(x=50, y=120, width=200, height=50)
    doc.place(x=50, y=190, width=200, height=50)
    poc.place(x=50, y=260, width=200, height=50)
    ch.place(x=50, y=330, width=200, height=50)
    nod.place(x=50, y=400, width=200, height=50)
    noi.place(x=50, y=470, width=200, height=50)
    da.place(x=50, y=540, width=200, height=50)
    fir_no1.place(x=275, y=50, width=400, height=50)
    ci1.place(x=275, y=120, width=400, height=50)
    doc1.place(x=275, y=190, width=400, height=50)
    poc1.place(x=275, y=260, width=400, height=50)
    ch1.place(x=275, y=330, width=400, height=50)
    nod1.place(x=275, y=400, width=400, height=50)
    noi1.place(x=275, y=470, width=400, height=50)
    da1.place(x=275, y=540, width=400, height=50)





    mainloop()