from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from PIL import Image,ImageTk
import sqlite3

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
            tkinter.messagebox.showinfo('Deletion Messege', 'I.D. Deleted')
        else:
            tkinter.messagebox.showinfo('No Deletion Messege', 'No such I.D. found.')
        t1.destroy()
        from sys_home import system_home
        system_home(k)

    t1 = Tk()
    t1.title('Enter User Page')
    w, h = t1.winfo_screenwidth(), t1.winfo_screenheight()
    t1.geometry("%dx%d+0+0" % (w, h))
    anr = StringVar(t1)
    l_user_id = Label(t1, text='User I.D. :', font=tkFont.Font(family="Times New Roman", size=16), anchor='w',
                      borderwidth=2, relief="solid", width=10, height=2)
    user_id = Entry(t1, font=tkFont.Font(family="Times New Roman", size=30), textvariable=anr, borderwidth=2,
                    relief="solid")
    next_1_button = Button(t1, text='Next', font=tkFont.Font(family="Times New Roman", size=16),
                           command=deletion_message, borderwidth=2, relief="solid", width=12, height=2)
    l_user_id.place(x=615, y=300)
    user_id.place(x=720, y=300)
    back_button = Button(t1, text='Go Back', font=tkFont.Font(family="Times New Roman", size=16), command=back,
                         borderwidth=2, relief="solid", width=10, height=2)
    back_button.place(x=50, y=50)
    next_1_button.place(x=750, y=450)
    mainloop()