#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk, Image

# Need to do:
# Function to stop the interaction
# Function to start the interaction

# Main window
root = Tk()
root.title("Tuffy Aide")
root.geometry("1200x700")
#Keeps the window from resizing
root.resizable(0,0)
icon = Image.open("icon.png")
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)
root.configure(background="#FF7900")

# Title text
Label(root, text="Tuffy Aide", bg="#FF7900", font=("Times 40 bold")).pack()


# Tuffy character photo
tuffy = Image.open("tuffy.png").resize((200,250))
tuffy = ImageTk.PhotoImage(tuffy)
Label(root, image=tuffy).pack()

# Profile button
prof = Image.open("prof.png").resize((50,50))
prof = ImageTk.PhotoImage(prof)
prof_button = Menubutton(root, image=prof, activebackground="black")
prof_button.menu = Menu(prof_button, tearoff=0)
prof_button["menu"] = prof_button.menu

# Figure out how to implement a button to open a window and then create a profile through that window
var1 = IntVar()

  
prof_button.menu.add_checkbutton(label = "Add profile", variable = var1)  
prof_button.place(x=1020, y=5)

# Microphone button
mic = Image.open("mic.png").resize((50, 50))
mic = ImageTk.PhotoImage(mic)
Button(root, image=mic).place(x=1080, y=5)

# Exit interaction buttom
ext = Image.open("x.png").resize((50,50))
ext = ImageTk.PhotoImage(ext)
Button(root, image=ext).place(x=1140, y=5)


root.mainloop()
