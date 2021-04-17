from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image,ImageTk
import sqlite3
import tkinter as tk

connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()
def test3(k):


    def back():
        t1.destroy()
        from sys_home import system_home
        system_home(k)

    def deletion_message():
        c = 0
        cursor.execute("SELECT * FROM POLICE")
        for row in cursor.fetchall():
            if (user_id.get() == row[0]):
                c = 1
            else:
                pass
        if (c==1):
            cursor.execute('DELETE from POLICE where POLICEID=?', (user_id.get(),))
            connection.commit()
            cursor.execute('DELETE from POLICE1 where POLICEID=?', (user_id.get(),))
            connection.commit()
            tkinter.messagebox.showinfo('Confirmation Message', 'I.D. Deleted')
        else:
            tkinter.messagebox.showinfo('Confirmation Message', 'No such I.D. found.')
        t1.destroy()
        from sys_home import system_home
        system_home(k)

    t1 = tk.Tk()
    t1.geometry('600x400')
    t1.title("Delete User")
    anr = StringVar(t1)
    l_user_id = Label(t1, text='User ID', font=tkFont.Font(family="Times New Roman", size=16),
                      borderwidth=2, relief="solid", width=10, height=2)
    user_id = Entry(t1, font=tkFont.Font(family="Times New Roman", size=30), textvariable=anr, borderwidth=2,
                    relief="solid")
    next_1_button = Button(t1, text='DELETE', font=tkFont.Font(family="Times New Roman", size=16),
                           command=deletion_message, borderwidth=4, relief="solid", width=12, height=2)
    l_user_id.place(x=200, y=100, width=200, height=50)
    user_id.place(x=200, y=175,width=200, height=50)
    back = Button(t1, text='<--', command=back, borderwidth=4, relief="solid")
    back.place(x=20, y=20, width=50, height=30)
    next_1_button.place(x=225, y=275, width=150, height=50)
    mainloop()