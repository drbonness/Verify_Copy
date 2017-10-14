#!python3

#import Tkinter
#import tkFileDialog
import tkinter
from tkinter import filedialog 

root = tkinter.Tk()

root.geometry('{}x{}'.format(400,400))

def callback():
	path = filedialog.askdirectory() 

b = tkinter.Button(root, text="TEST", command=callback)
b.pack()

# Code to add widgets will go here...
root.mainloop()