#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

def Pop_up(text):
    win = Tk()
    win.geometry("200x200")
    win.title('ToDO')
    Label(win, text=text, font=('Helvetica 14 bold')).pack(pady=20)
    win.mainloop()
    Pop_up('test')