from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
def fest(p,iy,i1,i2,i3):
    t=tk.Tk()
    t.title('CASE')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w,h))

    def back():
        t.destroy()
        from constable_home import const_home
        const_home(p)

    fi = tkFont.Font(family="Times New Roman", size=16)

    ### Defining the Labels
    status = Label(t, text='Complaint No.', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                   relief="solid")
    case_id = Label(t, text='Case ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                    relief="solid")
    pi = Label(t, text='Police ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
               relief="solid")
    ps = Label(t, text='Police Station', font=fi, borderwidth=2, relief="solid")

    od = Label(t, text='Opening Date', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
               relief="solid")
    cd = Label(t, text='Closing Date', font=fi, borderwidth=2, relief="solid")

    OptionList = []
    c = 0
    for i00 in i2:
        OptionList.append(i2[c][1] + " " + i2[c][2] + " " + i2[c][3] + " " + str(i2[c][4]))
        c = c + 1
    v = tk.StringVar(t)
    v.set('Victim Name And Age ')
    vic_det11 = tk.OptionMenu(t, v, *OptionList)

    OptionList1 = []
    c = 0
    for i00 in i2:
        OptionList1.append(i2[c][1] + " " + i2[c][3] + " " + i2[c][5])
        c = c + 1
    v1 = tk.StringVar(t)
    v1.set('Victim Name And Address ')
    vic_det22 = tk.OptionMenu(t, v1, *OptionList1)

    OptionList2 = []
    c = 0
    for i11 in i1:
        OptionList2.append(i1[c][1])
        c = c + 1

    v2 = tk.StringVar(t)
    v2.set('Police Id')
    pi1 = tk.OptionMenu(t, v2, *OptionList2)

    OptionList3 = []
    c = 0
    for i22 in i3:
        OptionList3.append(i3[c][1])
        c = c + 1
    v3 = tk.StringVar(t)
    v3.set('FIR No.')
    fr1 = tk.OptionMenu(t, v3, *OptionList3)

    menu = t.nametowidget(vic_det11.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    menu = t.nametowidget(vic_det22.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    menu = t.nametowidget(pi1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))
    menu = t.nametowidget(fr1.menuname)
    menu.config(font=tkFont.Font(family="Times New Roman", size=14))

    vic_det11.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    vic_det22.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    pi1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
    fr1.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")

    pno = Label(t, text='Penal Code', font=fi, borderwidth=2, relief="solid")
    sn = Label(t, text='Section no.', font=fi, borderwidth=2, relief="solid")
    desc = Label(t, text='Description', font=fi, borderwidth=2, relief="solid")

    fr = Label(t, text='FIR No.', font=fi, borderwidth=2, relief="solid")
    vic_det1 = Label(t, text='Victim & Age', font=fi, borderwidth=2, relief="solid")
    vic_det2 = Label(t, text='Victim & Address', font=fi, borderwidth=2, relief="solid")

    ### Defining the Labels Entries
    status1 = Label(t, text=iy[0][7], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                    relief="solid")
    case_id1 = Label(t, text=i2[0][0], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                     relief="solid")
    ps1 = Label(t, text=iy[0][3], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    od1 = Label(t, text=iy[0][5], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    cd1 = Label(t, text=iy[0][6], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    pno1 = Label(t, text=iy[0][1], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                 relief="solid")
    sn1 = Label(t, text=iy[0][2], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                relief="solid")
    desc1 = Label(t, text=iy[0][4], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
                  relief="solid")

    ### Placing the Labels
    status.place(x=50, y=50, width=200, height=50)
    case_id.place(x=50, y=120, width=200, height=50)
    pi.place(x=50, y=190, width=200, height=50)
    ps.place(x=50, y=260, width=200, height=50)
    od.place(x=50, y=330, width=200, height=50)
    cd.place(x=50, y=400, width=200, height=50)
    pno.place(x=50, y=470, width=200, height=50)
    sn.place(x=50, y=540, width=200, height=50)
    desc.place(x=50, y=610, width=200, height=50)

    fr.place(x=825, y=190, width=200, height=50)
    vic_det1.place(x=825, y=260, width=200, height=50)
    vic_det2.place(x=825, y=330, width=200, height=50)

    ### Placing the Entry Boxes
    status1.place(x=275, y=50, width=400, height=50)
    case_id1.place(x=275, y=120, width=400, height=50)
    pi1.place(x=275, y=190, width=400, height=50)
    ps1.place(x=275, y=260, width=400, height=50)
    od1.place(x=275, y=330, width=400, height=50)
    cd1.place(x=275, y=400, width=400, height=50)

    pno1.place(x=275, y=470, width=400, height=50)
    sn1.place(x=275, y=540, width=400, height=50)
    desc1.place(x=275, y=610, width=400, height=50)

    fr1.place(x=1050, y=190, width=400, height=50)
    vic_det11.place(x=1050, y=260, width=400, height=50)
    vic_det22.place(x=1050, y=330, width=400, height=50)

    ### Defining the buttons
    back_button = Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=4, relief="solid")

    ### Placing the buttons
    back_button.place(x=250, y=690, width=250, height=50)

    mainloop()
