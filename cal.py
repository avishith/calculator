import tkinter as tk
import  tkinter.ttk as ttk

cal=tk.Tk()
cal.title("My Python Calculator")
cal.iconbitmap(r'Calc.ico')
exp=""
text=tk.StringVar()

def clear():
	global exp
	exp=""
	text.set(exp)
	
def press(num):
	global exp
	exp += str(num)
	text.set(exp)

def eql():
	global exp
	ttl=str(eval(exp))
	text.set(ttl)
#delet the last degit
def delet():
	global exp
	le=len(exp)
	exp=exp[0:(le-1)]
	text.set(exp)



entry=ttk.Entry(cal,justify="right",textvariable=text)
entry.grid(row=0,columnspan=5,sticky=('nsew'))
#


button_1=ttk.Button(cal,text="1",command=lambda:press('1'))
button_1.grid(row=2,column=0)

button_1.bind('<1>',button_1)

button_2=ttk.Button(cal,text="2",command=lambda:press(2))
button_2.grid(row=2,column=1)

button_3=ttk.Button(cal,text="3",command=lambda:press(3))
button_3.grid(row=2,column=2)

button_4=ttk.Button(cal,text="4",command=lambda:press('4'))
button_4.grid(row=3,column=0)

button_5=ttk.Button(cal,text="5",command=lambda:press('5'))
button_5.grid(row=3,column=1)

button_6=ttk.Button(cal,text="6",command=lambda:press('6'))
button_6.grid(row=3,column=2)

button_7=ttk.Button(cal,text="7",command=lambda:press('7'))
button_7.grid(row=4,column=0)

button_8=ttk.Button(cal,text="8",command=lambda:press('8'))
button_8.grid(row=4,column=1)


button_9=ttk.Button(cal,text="9",command=lambda:press('9'))
button_9.grid(row=4,column=2)

button_0=ttk.Button(cal,text="0",command=lambda:press('0'))
button_0.grid(row=5,column=1)

button_c=ttk.Button(cal,text="c",command=delet)
button_c.grid(row=7,column=0)

button_dec=ttk.Button(cal,text=".",command=lambda:press("."))
button_dec.grid(row=5,column=0)

button_clr=ttk.Button(cal,text="clear",command=clear)
button_clr.grid(row=5,column=2)

button_plus=ttk.Button(cal,text="+",command=lambda:press('+'))
button_plus.grid(row=2,column=3)

button_sub=ttk.Button(cal,text="-",command=lambda:press('-'))
button_sub.grid(row=3,column=3)

button_mul=ttk.Button(cal,text="*",command=lambda:press('*'))
button_mul.grid(row=4,column=3)

button_div=ttk.Button(cal,text="/",command=lambda:press('/'))
button_div.grid(row=5,column=3)

button_equ=ttk.Button(cal,text="=",command=eql)
button_equ.grid(row=6,columnspan=4,sticky=('nswe'))

#button_equ=ttk.Button(cal,text="=")
#button_equ.grid(column=4,rowspan=2,sticky=('nswe'))



#button_0=ttk.Button(cal,text="0'')
#button_0.grid(row=5,column=0)
#error in pulling




cal.mainloop()
