#! python2

import Tkinter
import tkFileDialog
#import tkinter
#from tkinter import filedialog 

root = Tkinter.Tk()

root.geometry('{}x{}'.format(400,400))

def callback():
	path = tkFileDialog.askdirectory() 

b = Tkinter.Button(root, text="TEST", command=callback)
b.pack()

# Code to add widgets will go here...
root.mainloop()