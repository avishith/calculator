#idea_spot 

#1) Dark and white UI
#2) Sound O/P if possiable
#3)find alternate for winsound

#======importing  the frame works====
 
from ttkthemes import ThemedStyle
import os
import tkinter as tk
import  tkinter.ttk as ttk
import tkinter.messagebox as msg

#from ttkthemes import themed_tk as th


#ivade modules set cheyyam
'''try:
        from ttkthemes import themed_tk as th
except ModuleNotFoundError:
        os.system('pip install ttkthemes')
'''


#======function for theme======='''

def theme():
	global a
	if a==0:
		style = ThemedStyle(cal)
		style.set_theme('plastik')
		a=1
	
	elif a==1:	
		style = ThemedStyle(cal)
		style.set_theme("black")
		a=2
	elif a==2:
		style = ThemedStyle(cal)
		style.set_theme('breeze')
		a=3
	
	elif a==3:	
		style = ThemedStyle(cal)
		style.set_theme("yaru")
		a=4
		
	elif a==4:	
		style = ThemedStyle(cal)
		style.set_theme("alt")
		a=0
		
	'''m=["classic","black","alt","winxpblue",'plastik',"breeze"]
	m= m[random.randint(0,5)]'''
	

#cal=th.ThemedTk()
#cal.set_theme('black')
#cal.iconbitmap(r'calc_icon.ico')

#=========help====+====

def help():
	msg.showinfo( 'Help','MATH ERROR :               Syntax Eroor :')
#============exit===========

def exit():
	msg.showwarning("Calculator", "DO YOU REALLY WANTS TO EXIT..?")
	button_exit.command=cal.destroy

#=====Function for clear button======

def clear():
	global exp
	exp=""
	text.set(exp)
	
#======Function for number press=====
	
def press(num):
	global exp
	exp += str(num)
	text.set(exp)
	
#========Functoion for equl to=======

def eql():
        try:
            global exp
            exp=str(eval(exp))
            text.set(exp)
        except ZeroDivisionError:
                text.set("Math Error occured...!")
        except SyntaxError:
                text.set("Syntax Error occured...!")
	
#========Delet the last degit=========

def delet():
	global exp
	le=len(exp)
	exp=exp[0:(le-1)]
	text.set(exp)
'''
def exi():
        exit()
        print("Thanks for using my calculator")
	
'''	


cal=tk.Tk()
cal.title("My Python Calculator")
cal.geometry('400x150')
style = ThemedStyle(cal)
style.set_theme("alt")
a=0#variable for theme
exp=""
text=tk.StringVar()

#menu setting for calculotor

mb=ttk.Menubutton(cal,text="options",width=5)
mb.grid(row=0,column=0)
mb.menu = tk.Menu(mb)

help=ttk.Button(cal,text="Help",command=help)
help.grid(row=0,column=1)

mb["menu"] =  mb.menu
mb.menu.add_checkbutton ( label="Sound") 
mb.menu.add_checkbutton ( label="THEME",command=theme) 


#( label="Change Theme",command=theme)

entry=tk.Entry(cal,justify="right",font=("aril",20,'bold'),textvariable=text,bd=30,insertwidth=4,bg='gray')
entry.grid(row=1,columnspan=4,sticky=('nsew'))
entry.focus()


#===========BUttons===============


button_1=ttk.Button(cal,text="1",width=5,command=lambda:press('1'))
button_1.grid(row=2,column=0,pady=20)#padx=16,pady=16)

button_2=ttk.Button(cal,text="2",command=lambda:press(2))
button_2.grid(row=2,column=1,pady=20)

button_3=ttk.Button(cal,text="3",command=lambda:press(3))
button_3.grid(row=2,column=2,pady=20)#,padx=16)

button_4=ttk.Button(cal,text="4",command=lambda:press('4'))
button_4.grid(row=3,column=0,pady=20)#,padx=10,pady=10)

button_5=ttk.Button(cal,text="5",command=lambda:press('5'))
button_5.grid(row=3,column=1,pady=20)

button_6=ttk.Button(cal,text="6",command=lambda:press('6'))
button_6.grid(row=3,column=2,pady=20)

button_7=ttk.Button(cal,text="7",command=lambda:press('7'))
button_7.grid(row=4,column=0,pady=20)

button_8=ttk.Button(cal,text="8",command=lambda:press('8'))
button_8.grid(row=4,column=1,pady=20)


button_9=ttk.Button(cal,text="9",command=lambda:press('9'))
button_9.grid(row=4,column=2,pady=20)

button_0=ttk.Button(cal,text="0",command=lambda:press('0'))
button_0.grid(row=5,column=1,pady=20)

button_dec=ttk.Button(cal,text=".",command=lambda:press("."))
button_dec.grid(row=5,column=0,pady=20)

button_plus=ttk.Button(cal,text="+",command=lambda:press('+'))
button_plus.grid(row=2,column=3,pady=20)

button_sub=ttk.Button(cal,text="-",command=lambda:press('-'))
button_sub.grid(row=3,column=3,pady=20)

button_mul=ttk.Button(cal,text="*",command=lambda:press('*'))
button_mul.grid(row=4,column=3,pady=20)

button_div=ttk.Button(cal,text="/",command=lambda:press('/'))
button_div.grid(row=5,column=3,pady=20)

button_equ=ttk.Button(cal,text="=",command=eql)
button_equ.grid(row=6,columnspan=4,pady=20,sticky=('nswe'))


button_c=ttk.Button(cal,text="del",command=delet)
button_c.grid(row=7,columnspan=2,sticky=('nswe'),pady=20,padx=20)

button_exit=ttk.Button(cal,text="exit",command=exit)
button_exit.grid(row=7,column=2,columnspan=2,sticky=('nswe'),pady=20)

button_clr=ttk.Button(cal,text="C",command=clear)
button_clr.grid(row=5,column=2,pady=20)
cal.mainloop()

#============END=============