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

	acc = Label(t, text='ACCUSED', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
				relief="solid")
	vic = Label(t, text='VICTIM', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2,
				relief="solid")
	acc.place(x=270, y=400, width=200, height=50)
	vic.place(x=1045, y=400, width=200, height=50)
	userid=Label(t, text='User ID : '+q[13], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	userid.place(x=50, y=100, width=400, height=70)

	day=Label(t, text='Date', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	month=Label(t, text=q[2], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	day.place(x=50, y=190, width=200, height=50)
	month.place(x=275, y=190, width=400, height=50)

	policeid=Label(t, text='Your Police ID', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	policeid1=Label(t,text=pid, font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	policeid.place(x=825, y=330, width=200, height=50)
	policeid1.place(x=1050, y=330, width=400, height=50)

	city=Label(t, text='City', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	city1=Label(t,text=q[4], font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	city.place(x=825, y=190, width=200, height=50)
	city1.place(x=1050, y=190, width=400, height=50)

	ps=Label(t, text='Police Station', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	ps1=Label(t, text=q[5],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	ps.place(x=50, y=260, width=200, height=50)
	ps1.place(x=275, y=260, width=400, height=50)

	place=Label(t, text='Place of Crime', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	place1=Label(t,text=q[1],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	place.place(x=825, y=260, width=200, height=50)
	place1.place(x=1050, y=260, width=400, height=50)

	afname=Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	amname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	alname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	afname1=Label(t, text=q[10],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	amname1=Label(t, text=q[11],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	alname1=Label(t, text=q[12],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

	afname.place(x=50, y=470, width=200, height=50)
	amname.place(x=50, y=540, width=200, height=50)
	alname.place(x=50, y=610, width=200, height=50)
	afname1.place(x=275, y=470, width=400, height=50)
	amname1.place(x=275, y=540, width=400, height=50)
	alname1.place(x=275, y=610, width=400, height=50)


	vfname=Label(t, text='First Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vmname=Label(t, text='Middle Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vlname=Label(t, text='Last Name', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vfname1=Label(t, text=q[7],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vmname1=Label(t, text=q[8],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	vlname1=Label(t, text=q[9],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")

	vfname.place(x=825, y=470, width=200, height=50)
	vmname.place(x=825, y=540, width=200, height=50)
	vlname.place(x=825, y=610, width=200, height=50)
	vfname1.place(x=1050, y=470, width=400, height=50)
	vmname1.place(x=1050, y=540, width=400, height=50)
	vlname1.place(x=1050, y=610, width=400, height=50)

	desc=Label(t, text='Crime Description', font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	description=Label(t,text=q[3],font=tkFont.Font(family="Times New Roman", size=16), borderwidth=2, relief="solid")
	desc.place(x=50, y=330, width=200, height=50)
	description.place(x=275, y=330, width=400, height=50)

	submit=Button(t, text='ADD CASE', font=tkFont.Font(family="Times New Roman", size=16), command=submit_details, borderwidth=4, relief="solid")
	goback=Button(t, text='GO BACK', font=tkFont.Font(family="Times New Roman", size=16), command=clear_details, borderwidth=4, relief="solid")

	submit.place(x=650, y=690, width=250, height=50)
	goback.place(x=250, y=690, width=250, height=50)

	mainloop()
#		cursor.execute('UPADTE COMPLAINT set status="Case Accepted" where COMLAINT_NO=?',(cid,))
#		connection.commit()