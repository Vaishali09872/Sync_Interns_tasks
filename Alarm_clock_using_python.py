# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:17:44 2023

@author: Admin
"""

from tkinter import *
import winsound
import datetime
import time
root=Tk()
root.title("Alarm Clock")
root.geometry('350x250')
def alarm():
    while True:
        set=f'{h.get()}:{m.get()}'
        time.sleep(1)
        current=datetime.datetime.now().strftime('%H:%M')
        print(set,current)
        if set==current:
            print("Time to wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
Label(root,text='Alarm Clock',font='Helvetica 20 bold',fg='Blue').pack()
Label(root,text='set time',font='Helvetica 13 bold',fg='black').pack()
Label(root,text='set time in 24 hour format').pack()
f=Frame(root)
f.pack()
h=StringVar(root)
hour=('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
h.set([hour[0]])
h1=OptionMenu(f,h,*hour)
h1.grid(row=3,column=2)

m=StringVar()
min=('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
m.set(min[0])
m1=OptionMenu(f,m,*min)
m1.grid(row=3,column=3)
Button(root,text='Set alarm',command=alarm).pack()
root.mainloop()