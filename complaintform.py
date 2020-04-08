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
		t.destroy()
		os.system('python complaintform.py')
		return

	head=Label(t, text='R E G I S T E R   C O M P L A I N T',font=tkFont.Font(family="Times New Roman", size=50), borderwidth=2, relief="solid")
	head.place(x=0, y=0, width=w, height=70)

	userid=Label(t, text='User ID : '+uid, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	userid.place(x=50, y=100, width=400, height=70)

	dayOptionList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
	d = tk.IntVar(t)
	d.set('Day')
	day = tk.OptionMenu(t, d, *dayOptionList)
	monthOptionList=[1,2,3,4,5,6,7,8,9,10,11,12]
	mth = tk.IntVar(t)
	mth.set('Month')
	month = tk.OptionMenu(t, mth, *monthOptionList)
	yearOptionList=[]
	for i in range(1990,2020):
		yearOptionList.append(i)
	y = tk.IntVar(t)
	y.set('Year')
	year = tk.OptionMenu(t, y, *yearOptionList)

	day.place(x=750, y=100, width=150, height=70)
	month.place(x=950, y=100, width=150, height=70)
	year.place(x=1150, y=100, width=150, height=70)

	time=Label(t, text='Date of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	time.place(x=500, y=100, width=200, height=70)

	city=Label(t, text='City', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	city1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	city.place(x=50, y=200, width=200, height=70)
	city1.place(x=275, y=200, width=425, height=70)

	ps=Label(t, text='Police Station', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	ps1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	ps.place(x=725, y=200, width=200, height=70)
	ps1.place(x=950, y=200, width=425, height=70)

	place=Label(t, text='Place of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	place1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")



	afname=Label(t, text='ACCUSED First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	amname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	alname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	afname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	amname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	alname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

	afname.place(x=50, y=400, width=200, height=70)
	amname.place(x=500, y=400, width=200, height=70)
	alname.place(x=950, y=400, width=200, height=70)
	afname1.place(x=275, y=400, width=200, height=70)
	amname1.place(x=725, y=400, width=200, height=70)
	alname1.place(x=1175, y=400, width=200, height=70)

	vfname=Label(t, text='VICTIM First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vmname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vlname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vfname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	vmname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	vlname1=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

	

	desc=Label(t, text='Crime Description', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	description=Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	desc.place(x=50, y=600, width=200, height=70)
	description.place(x=275, y=600, width=1100, height=70)

	submit=Button(t, text='Submit', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=4, relief="solid")
	reset=Button(t, text='Clear', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=4, relief="solid")

	submit.place(x=50, y=700, width=300, height=70)
	reset.place(x=500, y=700, width=125, height=70)

	place.place(x=50, y=500, width=200, height=70)
	place1.place(x=275, y=500, width=1100, height=70)

	vlname1.place(x=1175, y=300, width=200, height=70)
	vfname.place(x=50, y=300, width=200, height=70)
	vmname.place(x=500, y=300, width=200, height=70)
	vlname.place(x=950, y=300, width=200, height=70)
	vfname1.place(x=275, y=300, width=200, height=70)
	vmname1.place(x=725, y=300, width=200, height=70)



	back=Button(t, text='Cancel',command=goback, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=4, relief="solid").place(x=775, y=700, width=125, height=70)

	mainloop()
#comp('raj')