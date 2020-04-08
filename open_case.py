from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
def fest(p,i,i1,i2,i3):
    t=tk.Tk()
    t.title('CASE')
    w, h = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry("%dx%d+0+0" % (w,h))
    def back():
        t.destroy()
        from constable_home import const_home
        const_home(p)


    fih = tkFont.Font(family="Times New Roman", size=20)

    victim=Label(t, text='NAME OF VICTIM',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=17,height=2)
    od=Label(t, text='OPENING DATE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    address=Label(t, text='VICTIM ADDRESS',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    victim1=Label(t,text=i2[0][1]+' '+ i2[0][2] +' '+ i2[0][3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=27,height=2)
    od1=Label(t,text=i[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    address1=Label(t,text=i2[0][5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=27,height=2)

    case_id=Label(t, text='CASE ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    status=Label(t, text='COMPLAINT ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    case_id1=Label(t,text=i2[0][0],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    status1=Label(t,text=i[0][7],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)

    desc=Label(t, text='DESCRIPTION',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    desc1=Label(t,text=i[0][4],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    cd=Label(t, text='CLOSING DATE',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    cd1=Label(t,text=i[0][6],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    OptionList=[i3[0][1]]
    v = tk.StringVar(t)
    v.set('FIR NUMBER ')
    fir= tk.OptionMenu(t, v, *OptionList)
    OptionList2=[i1[0][1]]
    OptionList3=[str(i[0][1])+' '+str(i[0][2])]
    v2 = tk.StringVar(t)
    v2.set('POLICE ID')
    police_id= tk.OptionMenu(t, v2, *OptionList2)
    v3 = tk.StringVar(t)
    v3.set('PENAL NUMBER')
    penal_no=tk.OptionMenu(t, v3, *OptionList3)
    ps=Label(t, text='POLICE STATION',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid",width=15,height=2)
    ps1=Label(t,text=i[0][3],font=tkFont.Font(family="Times New Roman", size=15), borderwidth=2, relief="solid",width=15,height=2)
    age=Label(t, text='AGE', font=tkFont.Font(family="Times New Roman", size=16),borderwidth=2, relief="solid",width=15,height=2)
    age1=Label(t,text=i2[0][4] ,font=tkFont.Font(family="Times New Roman", size=15), borderwidth=2, relief="solid",width=15,height=2)
    back_button = Button(t, text='GO BACK',font=fih, command=back, borderwidth=2, relief="solid", width=26, height=2).place(
        x=950, y=700)


    victim.place(x=50, y=400)
    victim1.place(x=300, y=400)
    age.place(x=50, y=75)
    age1.place(x=300, y=75)
    address.place(x=50, y=140)


    address1.place(x=300, y=140)
    case_id.place(x=50, y=10)
    case_id1.place(x=300, y=10)
    status.place(x=50, y=530)
    status1.place(x=300, y=530)


    penal_no.place(x=850, y=245, width=300, height=70)
    police_id.place(x=850, y=60, width=300, height=70)
    fir.place(x=850, y=140, width=300, height=70)
    desc.place(x=50,y=465)
    desc1.place(x=300, y=465)
    ps.place(x=50, y=330)
    ps1.place(x=300,y=330)
    od.place(x=50, y=205)
    od1.place(x=300, y=205)
    cd.place(x=50,y=270)
    cd1.place(x=300,y=270)
    mainloop()