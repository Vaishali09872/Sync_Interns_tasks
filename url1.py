import pyshorteners
from tkinter import *
import pyperclip
def clipboard():
    import pyperclip
    pyperclip.copy(short_url)
    label4=Label(text='URL copied')
    label4.pack()
def myfunc():
    s = pyshorteners.Shortener()
    url = box_value.get()
    global  short_url
    short_url = s.tinyurl.short(url)
    label2=Label(text=short_url)
    label2.pack()
    Button(text='copy URL', command=clipboard).pack()

root=Tk()
root.title('URL shortner')
root.geometry('300x300')
title=Label(root,text='URL shortener Program',bg='black',fg='white')
title.pack()
title.config(font=('Helvetica bold', 16))
label=Label(text='Enter URL ')
label.pack()
box_value=StringVar()
box_entry=Entry(root,textvariable=box_value)
box_entry.pack()
Button(text='submit',command=myfunc).pack()
root.mainloop()