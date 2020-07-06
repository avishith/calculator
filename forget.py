
from tkinter import *
from tkinter.ttk import *

root = Tk() 

def forget(widget): 

	
	widget.grid_forget() 


def retrieve(widget): 
	widget.grid(row = 0, column = 0, ipady = 10, pady = 10, padx = 5) 


b1 = Button(root, text = "Btn 1") 
b1.grid(row = 0, column = 0, ipady = 10, pady = 10, padx = 5) 


b2 = Button(root, text = "Btn 2", command = lambda : forget(b1)) 
b2.grid(row = 0, column = 1, ipady = 10, pady = 10, padx = 5) 


b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1)) 
b3.grid(row = 0, column = 2, ipady = 10, pady = 10, padx = 5) 


mainloop() 
