from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
from tkinter import filedialog
import os
import sqlite3
import datetime
import uuid

def comp(uid):
	connection = sqlite3.connect('NCD.db')
	cursor = connection.cursor()

	cursor.execute('CREATE TABLE IF NOT EXISTS COMPLAINT (COMPLAINT_NO text PRIMARY KEY, PLACEOFCRIME text, TIMEOFCRIME date, CRIMEDESCRIPTION text, CITY text, POLICESTATION text, STATUS text, VFNAME text, VMNAME text, VLNAME text, AFNAME text, AMNAME text, ALNAME text, USERID text)')

	t=tk.Tk()
	t.title('Complaint Form')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("%dx%d+0+0" % (w, h))

	def goback():
		connection.close()
		t.destroy()
		import civilian_home as tty
		tty.civ_home(uid)


	def submit_details():

		try:			
			x=str(uuid.uuid4().fields[-1])[:5]
			data_tuple = (x,place1.get(),str(y.get())+'-'+str(mth.get())+'-'+str(d.get()),description.get().upper(),city1.get(),ps1.get(),'Complaint Filed', vfname1.get(),vmname1.get(),vlname1.get(), afname1.get(),amname1.get(),alname1.get(),uid)
			cursor.execute('INSERT INTO COMPLAINT VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',data_tuple)
		except Exception as e:
			tkinter.messagebox.showinfo('Alert', "Couldn't connect to Database\nError Description : "+str(e))
		else:
			connection.commit()
			tkinter.messagebox.showinfo('Title',"Complaint Number : "+x+"\nComplaint Registered.\nA corresponding officer will contact you within 48 hours")
			t.destroy()
			import civilian_home as tty
			tty.civ_home(uid)
			return
	def clear_details():
		city1.delete(0, 'end')
		ps1.delete(0, 'end')
		place1.delete(0, 'end')
		afname1.delete(0, 'end')
		amname1.delete(0, 'end')
		alname1.delete(0, 'end')
		vfname1.delete(0, 'end')
		vmname1.delete(0, 'end')
		vlname1.delete(0, 'end')
		description.delete(0, 'end')
		d.set('dd')
		mth.set('mm')
		y.set('yyyy')
		return

	head=Label(t, text='R E G I S T E R   C O M P L A I N T',font=tkFont.Font(family="Times New Roman", size=50), borderwidth=2, relief="solid")
	head.place(x=0, y=0, width=w, height=70)

	userid=Label(t, text='User ID : '+uid, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	userid.place(x=50, y=120, width=200, height=50)

	dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
	d = tk.IntVar(t)
	d.set('dd')
	day = tk.OptionMenu(t, d, *dayOptionList)
	menu = t.nametowidget(day.menuname)
	menu.config(font=tkFont.Font(family="Times New Roman", size=14))
	monthOptionList=[1,2,3,4,5,6,7,8,9,10,11,12]
	mth = tk.IntVar(t)
	mth.set('mm')
	month = tk.OptionMenu(t, mth, *monthOptionList)
	menu = t.nametowidget(month.menuname)
	menu.config(font=tkFont.Font(family="Times New Roman", size=14))
	yearOptionList=[]
	for i in range(1990,2020):
		yearOptionList.append(i)
	y = tk.IntVar(t)
	y.set('yyyy')
	year = tk.OptionMenu(t, y, *yearOptionList)
	menu = t.nametowidget(year.menuname)
	menu.config(font=tkFont.Font(family="Times New Roman", size=14))

	day.place(x=275, y=190, width=130, height=50)
	month.place(x=405, y=190, width=130, height=50)
	year.place(x=535, y=190, width=140, height=50)
	day.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
	month.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
	year.configure(font=tkFont.Font(family="Times New Roman", size=20), relief="solid")
	time=Label(t, text='Date of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	time.place(x=50, y=190, width=200, height=50)

	city=Label(t, text='City', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	city1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	city.place(x=825, y=190, width=200, height=50)
	city1.place(x=1050, y=190, width=400, height=50)

	ps=Label(t, text='Police Station', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	ps1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	ps.place(x=50, y=260, width=200, height=50)
	ps1.place(x=275, y=260, width=400, height=50)

	place=Label(t, text='Place of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	place1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

	acc = Label(t, text='ACCUSED', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
			   relief="solid")
	vic = Label(t, text='VICTIM', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
			   relief="solid")
	acc.place(x=270, y=400, width=200, height=50)
	vic.place(x=1045, y=400, width=200, height=50)

	afname=Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	amname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	alname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	afname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	amname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	alname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

	afname.place(x=50, y=470, width=200, height=50)
	amname.place(x=50, y=540, width=200, height=50)
	alname.place(x=50, y=610, width=200, height=50)
	afname1.place(x=275, y=470, width=400, height=50)
	amname1.place(x=275, y=540, width=400, height=50)
	alname1.place(x=275, y=610, width=400, height=50)

	vfname=Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vmname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vlname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vfname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	vmname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	vlname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")


	desc=Label(t, text='Crime Description', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	description=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	desc.place(x=50, y=330, width=200, height=50)
	description.place(x=275, y=330, width=400, height=50)	

	submit=Button(t, text='SUBMIT', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=4, relief="solid")
	reset=Button(t, text='RESET', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=4, relief="solid")

	place.place(x=825, y=260, width=200, height=50)
	place1.place(x=1050, y=260, width=400, height=50)

	vfname.place(x=825, y=470, width=200, height=50)
	vmname.place(x=825, y=540, width=200, height=50)
	vlname.place(x=825, y=610, width=200, height=50)
	vfname1.place(x=1050, y=470, width=400, height=50)
	vmname1.place(x=1050, y=540, width=400, height=50)
	vlname1.place(x=1050, y=610, width=400, height=50)

	submit.place(x=650, y=690, width=250, height=50)
	reset.place(x=1050, y=690, width=250, height=50)
	back=Button(t, text='GO BACK',command=goback, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=4, relief="solid").place(x=250, y=690, width=250, height=50)

	mainloop()
#comp('raj')