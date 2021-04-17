from tkinter import *
import tkinter as tk
import tkinter.messagebox
import sqlite3
import tkinter.font as tkFont

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
def chdate2(wi):
    t = tk.Tk()
    t.geometry('850x600')
    t.title("CRIME RATE")
    t1 = Label(t, text='From Date', borderwidth=2, relief="solid",font=tkFont.Font(family="Times New Roman", size=16))
    t1.place(x=50, y=180, width=150, height=70)
    t2 = Label(t, text='To Date', borderwidth=2, relief="solid",font=tkFont.Font(family="Times New Roman", size=16))
    t2.place(x=50, y=280, width=150, height=70)
    dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    d = tk.IntVar(t)
    d.set('dd')
    day = tk.OptionMenu(t, d, *dayOptionList)
    monthOptionList=[1,2,3,4,5,6,7,8,9,10,11,12]
    mth = tk.IntVar(t)
    mth.set('mm')
    month = tk.OptionMenu(t, mth, *monthOptionList)
    yearOptionList=[]
    for i in range(2000,2020):
        yearOptionList.append(i)
    y = tk.IntVar(t)
    y.set('yyyy')
    year = tk.OptionMenu(t, y, *yearOptionList)

    day.place(x=250, y=180, width=150, height=70)
    month.place(x=450, y=180, width=150, height=70)
    year.place(x=650, y=180, width=150, height=70)

    d2 = tk.IntVar(t)
    d2.set('dd')
    day2 = tk.OptionMenu(t, d2, *dayOptionList)
    mth2 = tk.IntVar(t)
    mth2.set('mm')
    month2 = tk.OptionMenu(t, mth2, *monthOptionList)
    y2 = tk.IntVar(t)
    y2.set('yyyy')
    year2 = tk.OptionMenu(t, y2, *yearOptionList)


    day.config(font=tkFont.Font(family="Times New Roman", size=20))
    month.config(font=tkFont.Font(family="Times New Roman", size=20))
    year.config(font=tkFont.Font(family="Times New Roman", size=20))

    day2.config(font=tkFont.Font(family="Times New Roman", size=20))
    month2.config(font=tkFont.Font(family="Times New Roman", size=20))
    year2.config(font=tkFont.Font(family="Times New Roman", size=20))


    day2.place(x=250, y=280, width=150, height=70)
    month2.place(x=450, y=280, width=150, height=70)
    year2.place(x=650, y=280, width=150, height=70)

    def next():
        a,b='',''
        try:

            sd,sm,sy = d.get(),mth.get(),y.get()
            ed,em,ey = d2.get(),mth2.get(),y2.get()

            if(ey>sy):
                pass
            elif (ey==sy):
                if(em>sm):
                    pass
                elif (em==sm):
                    if(ed>sd):
                        pass
                    else:
                        tkinter.messagebox.showinfo('Alert','From Date must be less than To Date')
                        return
                else:
                    tkinter.messagebox.showinfo('Alert','From Date must be less than To Date')
                    return
            else:
                tkinter.messagebox.showinfo('Alert','From Date must be less than To Date')
                return

            a = str(y.get())+'-'+str(mth.get())+'-'+str(d.get())
            b = str(y2.get())+'-'+str(mth2.get())+'-'+str(d2.get())
            #if mth.get()==2 and d.get()>29:
                #raise Exception
        except Exception as e:
            tkinter.messagebox.showinfo('Alert','Date Chosen is Not Correct\n'+str(e))
        else:
            from dashboard import linegraph
            linegraph(b,a)
            

    submit = Button(t, text='SUBMIT', command=next, borderwidth=4, relief="solid",font=tkFont.Font(family="Times New Roman", size=16))
    submit.place(x=350, y=400, width=150, height=50)

    def back():
        t.destroy()
        from acp_home import acp_home
        acp_home(wi)

    back = Button(t, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)
    d.set('dd')
    mth.set('mm')
    y.set('yyyy')

    t.mainloop()

