try: from tkinter import *
except: from Tkinter import *
import runpy
import sys, string, os

toe = Tk()

#Window Properties
toe.resizable(width=FALSE, height=FALSE)
toe.configure(background="#FF944D")
toe.geometry("300x350+450+100")
toe.title("Tic Tac Toe!")

def xfile(afile, globalz=None, localz=None):
    with open(afile, "r") as fh:
        exec(fh.read(), globalz, localz)

def oneplayer():
    toe.destroy()
    runpy.run_path("tictactoewithai.py")

def twoplayer():
    toe.destroy()
    runpy.run_path("tictactoefor2.py")

space = Label(text="", bg="#FF944D", font="Arial 30").pack(pady=1)
space = Label(text="Tic Taco Toe", bg="#FF944D", font="Arial 30").pack()
credit = Label(text="By Somil Govani", bg="#FF944D", font="Arial 15").pack(pady=20)
One = Button(text="One Player Game", width = 20, command=oneplayer)
One.pack(pady=20)
Two = Button(text="Two Player Game", width = 20, command=twoplayer)
Two.pack()




mainloop()
