#!/usr/bin/env python3

from tkinter import *
top = Tk()

def helloCallBack():
   label = Message( "Hello Python", "Hello World")
   return label

B = Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()