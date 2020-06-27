from tkinter import *
from tkinter import ttk
cal=Tk()

button_1=ttk.Button(cal,text="1")
button_1.grid(row=2,column=0)

button_2=ttk.Button(cal,text="2")
button_2.grid(row=2,column=1)

button_3=ttk.Button(cal,text="3")
button_3.grid(row=2,column=2)

button_4=ttk.Button(cal,text="4")
button_4.grid(row=3,column=0)

button_5=ttk.Button(cal,text="5")
button_5.grid(row=3,column=1)

button_6=ttk.Button(cal,text="6")
button_6.grid(row=3,column=2)

button_7=ttk.Button(cal,text="7")
button_7.grid(row=4,column=0)

button_8=ttk.Button(cal,text="8")
button_8.grid(row=4,column=1)


button_9=ttk.Button(cal,text="9")
button_9.grid(row=4,column=2)

button_0=ttk.Button(cal,text="0")
button_0.grid(row=5,column=1)

button_dec=ttk.Button(cal,text=".")
button_dec.grid(row=5,column=0)

button_clr=ttk.Button(cal,text="clear")
button_clr.grid(row=5,column=2)

button_plus=ttk.Button(cal,text="+")
button_plus.grid(row=2,column=3)

button_sub=ttk.Button(cal,text="-")
button_sub.grid(row=3,column=3)

button_mul=ttk.Button(cal,text="*")
button_mul.grid(row=4,column=3)

button_div=ttk.Button(cal,text="/")
button_div.grid(row=5,column=3)

button_equ=ttk.Button(cal,text="=")
button_equ.grid(rowspan=4,column=3)



#button_0=ttk.Button(cal,text="0'')
#button_0.grid(row=5,column=0)





cal.mainloop()