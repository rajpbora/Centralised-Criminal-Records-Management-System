from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3

def stat(id):

	def goback():
		t.destroy()
		import civilian_home as ty
		ty.civ_home(id)

	t=tk.Tk()
	t.title('NCDS - Complaint Status ')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("%dx%d+0+0" % (w, h))

	connection = sqlite3.connect('NCD.db')
	cursor = connection.cursor()

	cursor.execute('CREATE TABLE IF NOT EXISTS COMPLAINT (COMPLAINT_NO text PRIMARY KEY, PLACEOFCRIME text, TIMEOFCRIME date, CRIMEDESCRIPTION text, CITY text, POLICESTATION text, STATUS text, VFNAME text, VMNAME text, VLNAME text, AFNAME text, AMNAME text, ALNAME text)')

	def track_status():
		num = number.get()
		u = cursor.execute('SELECT STATUS FROM COMPLAINT WHERE COMPLAINT_NO = (?)',(num,))
		temp=u.fetchall()
		if len(temp)>0:
			tkinter.messagebox.showinfo('COMPLAINT STATUS',temp[0][0])
		else:
			tkinter.messagebox.showinfo('COMPLAINT STATUS','NO RECORD FOUND')


	compno=Label(t, text='Enter Complaint Number', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	number=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	track=Button(t, text='Track Status',font=tkFont.Font(family="Times New Roman", size=30), command=track_status, borderwidth=2, relief="solid")

	compno.place(x=450, y=50, width=600, height=70)
	number.place(x=550, y=200, width=400, height=70)
	track.place(x=625, y=350, width=250, height=70)



	goback=Button(t, text='GO BACK',command=goback, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=4, relief="solid").place(x=50,y=600,width=150,height=70)

	mainloop()