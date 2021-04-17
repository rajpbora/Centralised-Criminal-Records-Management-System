from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import tkinter as tk
from PIL import Image,ImageTk
import os
import re
from tkinter import filedialog
from edit_user import *
import sqlite3
connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
def test4(k):

    def back():
        t1.destroy()
        from sys_home import system_home
        system_home(k)

    def getting_user_details():
        j = user_id.get()
        c=0
        cursor.execute("SELECT * FROM POLICE")
        for row in cursor.fetchall():
            if (j==row[0]):
                c=1
            else:
                pass
        if(c==1):
            t1.destroy()
            test(j,k)
            print('SuccessF1')
        else:
            tkinter.messagebox.showinfo('Failure', 'No  such user')

    t1 = tk.Tk()
    t1.geometry('600x400')
    t1.title("Choose User for Update")
    anr=StringVar(t1)
    l_user_id=Label(t1, text='User ID',font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid", width=10, height=2)
    user_id=Entry(t1,font=tkFont.Font(family="Times New Roman", size=30),textvariable=anr, borderwidth=2, relief="solid")
    next_1_button=Button(t1, text='NEXT',font=tkFont.Font(family="Times New Roman", size=16),command=getting_user_details,borderwidth=4, relief="solid", width=12,height=2)
    l_user_id.place(x=200, y=100, width=200, height=50)
    user_id.place(x=200, y=175,width=200, height=50)
    back = Button(t1, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)
    next_1_button.place(x=225, y=275, width=150, height=50)
    mainloop()