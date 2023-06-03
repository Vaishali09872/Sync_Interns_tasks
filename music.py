import os
from tkinter import *
import pygame
pygame.init()

def play():
    l = Label(trackframe, text='', font=("times new roman", 12, "bold"), bg='orange')
    l.grid(row=0)
    s=playlist.get(ACTIVE)
    pygame.mixer.music.load(playlist.get(ACTIVE))
    pygame.mixer.music.play()
    l=Label(trackframe,text=s,font=("times new roman",12,"bold"),bg='orange')
    l.grid(row=0)

def pause():
    pygame.mixer.music.pause()
def stop():
    pygame.mixer.music.stop()
def unpause():
    pygame.mixer.music.unpause()
root=Tk()
root.geometry('900x200')

track=StringVar()
trackframe = LabelFrame(root,text="Song Track",font=("times new roman",15,"bold"),bg="Navyblue",fg="white",bd=5,relief=GROOVE)
trackframe.place(x=0,y=0,width=600,height=100)

songtrack = Label(trackframe, textvariable=track, width=20, font=("times new roman", 24, "bold"), bg="Orange",fg="gold").grid(row=0, column=0, padx=10, pady=5)




frame=LabelFrame(root,text='control panel')
frame.place(x=0, y=100, width=600, height=100)
Button(frame,text="play",command=play).grid(row=0,column=0,padx=10,pady=5)
Button(frame,text="pause",command=pause).grid(row=0,column=1,padx=10,pady=5)
Button(frame,text="stop",command=stop).grid(row=0,column=2,padx=10,pady=5)
Button(frame,text="unpause",command=unpause).grid(row=0,column=3,padx=10,pady=5)

song_frame=LabelFrame(root,text='Song Playlist')
song_frame.place(x=600,y=0,width=400,height=200)
scrol_y=Scrollbar(song_frame,orient=VERTICAL)


playlist = Listbox(song_frame,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)

songlist=os.listdir("C:\\Users\\HP\\Desktop\\vsc")
for track in songlist:
    playlist.insert(END,track)
root.mainloop()