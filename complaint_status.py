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
	track=Button(t, text='TRACK STATUS',font=tkFont.Font(family="Times New Roman", size=16), command=track_status, borderwidth=4, relief="solid")

	compno.place(x=450, y=70, width=600, height=70)
	number.place(x=550, y=250, width=400, height=70)
	track.place(x=625, y=400, width=250, height=70)



	goback=Button(t, text='<--',command=goback,  borderwidth=4, relief="solid").place(x=20, y=20, width=50, height=30)

	mainloop()