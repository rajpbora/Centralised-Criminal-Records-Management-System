from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
import sqlite3
from matplotlib import pyplot as plt


connection = sqlite3.connect('NCD.db')
cursor = connection.cursor()

def bargraph():
    k = cursor.execute("SELECT COUNT(CLOSEDATE) FROM CASE1")
    p = k.fetchall()
    kkk = cursor.execute("SELECT COUNT(CASENO) FROM CASE1 ")
    ppp = kkk.fetchall()
    kkkk=ppp[0][0]-p[0][0]
    fig = plt.figure()
    ax = fig.add_axes([0.2, 0.2, 0.5, 0.8])
    langs = ['CLOSED', 'OPEN']
    cases = [p[0][0],kkkk]
    ax.bar(langs, cases)
    plt.show()

def bargraph2(j):
    k = cursor.execute("SELECT COUNT(CLOSEDATE) FROM CASE1 NATURAL JOIN CASE2 WHERE CASE1.CASENO=CASE2.CASENO AND POLICEID=?",(j,))
    p = k.fetchall()
    kkk = cursor.execute("SELECT COUNT(CASENO) FROM CASE1 NATURAL JOIN CASE2 WHERE CASE1.CASENO=CASE2.CASENO AND POLICEID=?",(j,))
    ppp=kkk.fetchall()
    kkkk=ppp[0][0]-p[0][0]
    fig = plt.figure()
    print(p)
    ax = fig.add_axes([0.2, 0.2, 0.5, 0.8])
    langs = ['CLOSED', 'OPEN']
    cases = [p[0][0],kkkk]
    ax.bar(langs, cases)
    plt.show()

def linegraph(b,c):
    from datetime import datetime as dt
    p = dt.strptime(b, "%Y-%m-%d")
    q = dt.strptime(c, "%Y-%m-%d")
    cursor.execute("SELECT OPENDATE FROM CASE1")
    l=[]
    for rows in cursor.fetchall():
        a = dt.strptime(rows[0], "%Y-%m-%d")
        print(a)
        if a<p and a>q:
            l.append(rows[0])
            print('success')

    l = list(dict.fromkeys(l))
    l.sort(key=lambda date: dt.strptime(date, '%Y-%m-%d'))
    hii=[]
    for i in l:
        h = cursor.execute("SELECT COUNT(CASENO) FROM CASE1 WHERE OPENDATE=? ", (i,))
        x = h.fetchall()
        print(x)
        hii.append(x[0][0])
    plt.plot(l,hii)
    plt.show()

def piechart():
    h = cursor.execute("SELECT COUNT(DESCRIPTION),DESCRIPTION FROM CASE1 GROUP BY DESCRIPTION")
    x = h.fetchall()
    pieLabels=[]
    casesvalue=[]
    for i in range(len(x)):
        pieLabels.append(x[i][1])
        casesvalue.append(x[i][0])
    figureObject, axesObject = plt.subplots()
    axesObject.pie(casesvalue, labels=pieLabels,autopct='%1.2f',startangle=90)
    axesObject.axis('equal')
    plt.show()


