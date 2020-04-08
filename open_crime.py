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

    fih = tkFont.Font(family="Times New Roman", size=20)

    noi=Label(t, text='NUMBER OF INJURIES',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    nod=Label(t, text='NUMBER OF DEATHS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)

    noi1=Label(t,text=k[0][2],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    nod1=Label(t,text=k[0][3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)

    fir_no=Label(t, text='FIR NUMBER',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    poc=Label(t, text='PLACE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    fir_no1=Label(t,text=k[0][0],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    poc1=Label(t,text=k[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)

    OptionList=[k1[0][1]]
    v = tk.StringVar(t)
    v.set('CRIMINAL ID')
    c_id= tk.OptionMenu(t, v, *OptionList)
    doc=Label(t, text='DATE OF CRIME',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    doc1=Label(t,text=k[0][4],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)

    OptionList2=[k2[0][2]]
    OptionList3=[k2[0][1]]
    v2 = tk.StringVar(t)
    v2.set('SECTION NO')
    sn= tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('PENAL CODE')
    pc=tk.OptionMenu(t, v3, *OptionList3)

    da=Label(t, text='DAMAGE AMOUNT',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=18,height=2)
    da1=Label(t,text=k[0][1],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=15,height=2)
    back_button = Button(t, text='GO BACK',font=fih ,command=back, borderwidth=2, relief="solid", width=20, height=2).place(
        x=950, y=700)
    noi.place(x=50, y=490)
    nod.place(x=50, y=430)
    # name1.place(x=225, y=150, width=150, height=70)
    noi1.place(x=300, y=490)
    nod1.place(x=300, y=430)
    fir_no.place(x=50, y=10)

    fir_no1.place(x=300, y=10)

    poc.place(x=50, y=205)
    poc1.place(x=300, y=205)

    pc.place(x=50, y=270,width=300,height=70)

    sn.place(x=50, y=350,width=300,height=70)

    c_id.place(x=50, y=65,width=300,height=70)


    da.place(x=50, y=555)
    da1.place(x=300, y=555)
    doc.place(x=50, y=140)
    doc1.place(x=300, y=140)






    mainloop()