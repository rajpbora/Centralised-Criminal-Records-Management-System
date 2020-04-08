from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import os
import sqlite3

def compdisplay(pid,cid):
	connection = sqlite3.connect('NCD.db')
	cursor = connection.cursor()

	t=tk.Tk()
	t.title('NCDS - Complaint ')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("%dx%d+0+0" % (w, h))

	u=cursor.execute('SELECT * FROM COMPLAINT where COMPLAINT_NO =?',(cid,))
	q=u.fetchall()[0]

	def submit_details():
		t.destroy()
		import add_case as tty
		tty.add4(pid,cid)


	def clear_details():
		t.destroy()
		import acp_home as tty
		tty.acp_home(pid)
		return

	head=Label(t, text='  C O M P L A I N T  D E T A I L S',font=tkFont.Font(family="Times New Roman", size=50), borderwidth=2, relief="solid")
	head.place(x=0, y=0, width=w, height=70)

	userid=Label(t, text='User ID : '+q[13], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	userid.place(x=50, y=100, width=400, height=70)

	day=Label(t, text='Date', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	month=Label(t, text=q[2], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	day.place(x=500, y=100, width=100, height=70)
	month.place(x=650, y=100, width=100, height=70)

	time=Label(t, text='Your Police ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	time1=Label(t,text=pid, font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	time.place(x=950, y=100, width=200, height=70)
	time1.place(x=1200, y=100, width=200, height=70)

	city=Label(t, text='City', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	city1=Label(t,text=q[4], font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	city.place(x=50, y=200, width=200, height=70)
	city1.place(x=300, y=200, width=400, height=70)

	ps=Label(t, text='Police Station', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	ps1=Label(t, text=q[5],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	ps.place(x=750, y=200, width=200, height=70)
	ps1.place(x=1000, y=200, width=400, height=70)

	place=Label(t, text='Place of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	place1=Label(t,text=q[1],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	place.place(x=50, y=300, width=200, height=70)
	place1.place(x=300, y=300, width=1100, height=70)

	afname=Label(t, text='ACCUSED First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	amname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	alname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	afname1=Label(t, text=q[10],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	amname1=Label(t, text=q[11],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	alname1=Label(t, text=q[12],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

	afname.place(x=50, y=400, width=200, height=70)
	amname.place(x=500, y=400, width=200, height=70)
	alname.place(x=950, y=400, width=200, height=70)
	afname1.place(x=275, y=400, width=200, height=70)
	amname1.place(x=725, y=400, width=200, height=70)
	alname1.place(x=1175, y=400, width=200, height=70)


	vfname=Label(t, text='VICTIM First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vmname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vlname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vfname1=Label(t, text=q[7],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	vmname1=Label(t, text=q[8],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	vlname1=Label(t, text=q[9],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")

	vfname.place(x=50, y=500, width=200, height=70)
	vmname.place(x=500, y=500, width=200, height=70)
	vlname.place(x=950, y=500, width=200, height=70)
	vfname1.place(x=275, y=500, width=200, height=70)
	vmname1.place(x=725, y=500, width=200, height=70)
	vlname1.place(x=1175, y=500, width=200, height=70)

	desc=Label(t, text='Crime Description', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	description=Label(t,text=q[3],font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
	desc.place(x=50, y=600, width=200, height=70)
	description.place(x=275, y=600, width=1100, height=70)

	submit=Button(t, text='ADD CASE', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=2, relief="solid")
	goback=Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=2, relief="solid")

	submit.place(x=50, y=700, width=300, height=70)
	goback.place(x=500, y=700, width=125, height=70)

	mainloop()
#		cursor.execute('UPADTE COMPLAINT set status="Case Accepted" where COMLAINT_NO=?',(cid,))
#		connection.commit()