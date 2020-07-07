#_______________________________________________________________MyPythonCalculator_______________________________________________________________


#_______________________________Downloading Modules_______________________________
import os
os.system('pip install -r req.txt')
#_______________________________Importing Modules_________________________________
import tkinter.messagebox as msg
#from ttkthemes import ThemedStyle
import tkinter as tk
import  tkinter.ttk as ttk
#import simpleaudio as s
from math import *

#____________________________________Sounds_______________________________________

'''welcome = s.WaveObject.from_wave_file("medias\\welcome.wav")
button_sound = s.WaveObject.from_wave_file("medias\\buttons.wav")
math_error = s.WaveObject.from_wave_file("medias\\matherror.wav")
syn_error = s.WaveObject.from_wave_file("medias\\syntax_error.wav")
delete_sound = s.WaveObject.from_wave_file("medias\\delete.wav")
thanks = s.WaveObject.from_wave_file("medias\\thanks.wav")
result = s.WaveObject.from_wave_file("medias\\result.wav")'''

#_____________________________________Help________________________________________

error_statement='''[Syntax error] : It is one of several types of errors on calculators
representing that the equation that has been input has incorrect syntax of numbers,operations and so on.

[Math error] : The calculation result is outside of the allowable calculation range or you are trying to perform an illegal mathematical operation (such as division by zero)'''

#_____________________________________Theme________________________________________
'''def theme():
	global a
	if a==0:
		style = ThemedStyle(cal)
		style.set_theme('black')
		a=1
	
	elif a==1:	
		style = ThemedStyle(cal)
		style.set_theme("plastik")
		a=2
		
	elif a==2:	
		style = ThemedStyle(cal)
		style.set_theme("blue")
		a=3
	elif a==3:	
		style = ThemedStyle(cal)
		style.set_theme("alt")
		a=0'''
		
'''These are themes m=["classic","black","alt","winxpblue",'plastik',"breeze"]
	m= m[random.randint(0,5)]'''
	
#_____________________________________Help________________________________________

def help():
	msg.showinfo( 'Help',error_statement)
	
#_____________________________________Exit________________________________________

def exit():
    #thanks.play()
    MsgBox = msg.askquestion ('Exit Application','Are you sure you want to exit the application')
    if MsgBox == 'yes':
       cal.destroy()
    print('Thanks For Using Our Calculator...!')
#__________________________________Scientific_____________________________________

def sci():
	global s
	global button_log
	global button_sin
	global button_cos
	global button_tan
	global button_open
	global button_close
	global button_equ
	if s==1:
		button_equ.grid_forget()
		button_sin=ttk.Button(cal,text="sin",command=lambda:press('sin('))
		button_sin.grid(row=2,column=0,pady=20)
		
		button_cos=ttk.Button(cal,text="cos",command=lambda:press("cos("))
		button_cos.grid(row=2,column=1,pady=20)
		
		button_tan=ttk.Button(cal,text="tan",command=lambda:press("tan("))
		button_tan.grid(row=2,column=2,pady=20)
		
		button_log=ttk.Button(cal,text="log",command=lambda:press("log("))
		button_log.grid(row=2,column=3,pady=20)

		button_open=ttk.Button(cal,text="(",command=lambda:press("("))
		button_open.grid(row=7,column=0,pady=20,padx=20,sticky=('nswe'))
		button_close=ttk.Button(cal,text=")",command=lambda:press(")"))
		button_close.grid(row=7,column=3,pady=20,padx=20,sticky=('nswe'))
		button_equ=ttk.Button(cal,text="=",command=eql)
		button_equ.grid(row=7,column=1,columnspan=2,pady=20,sticky=('nswe'))
		cal.bind("<Return>",eql)
		s=0
	elif s==0:
		button_sin.grid_forget()
		button_cos.grid_forget()
		button_tan.grid_forget()
		button_log.grid_forget()
		button_open.grid_forget()
		button_close.grid_forget()
		button_equ=ttk.Button(cal,text="=",command=eql)
		button_equ.grid(row=7,columnspan=4,pady=20,sticky=('nswe'))
		cal.bind("<Return>",eql)
		s=1

#_____________________________________Clear________________________________________

def clear():
	global exp
	#delete_sound.play()
	exp=""
	text.set(exp)

def aboutus():
	about=tk.Tk()
	about.title("ABOUT US")
	ttk.Button(about, text = "", image = "IMG.jpg").pack()
	about.geometry('200x200')
#cal.iconbitmap(r'medias\\calc_icon.ico')
	cal.resizable(0,0)
	about.mainloop()
	
#______________________________________Press________________________________________
	
def press(num):
	global exp
	#button_sound.play()
	exp += str(num)
	text.set(exp)
	
#_____________________________________Answer________________________________________

def eql():
        global exp
        #exp=exp[::-1]
        #if '(' in exp:
        #        exp=exp.replace('(','*')
        #if '*nis' not in exp:
        #        exp=exp.replace(')','')
        #if '*nis' in exp:
        #        exp=exp.replace('*nis','sin(')
        try:
            #result.play()
            exp=str(eval(exp))
            text.set(exp)
        except ZeroDivisionError:
                #math_error.play()
                text.set("Math Error occured...!")
        #except SyntaxError:
                #syn_error.play()
               # text.set("Syntax Error occured...!")
        except NameError:
         	#math_error.play()
         	text.set('Syntax Error occured....!')

#___________________________________Backspace_______________________________________

def delet():
	global exp
	#delete_sound.play()
	le=len(exp)
	exp=exp[0:(le-1)]
	text.set(exp)

#_____________________________________Main________________________________________

#welcome.play()
cal=tk.Tk()
cal.title("My Python Calculator")
cal.geometry('385x580')
#cal.iconbitmap(r'medias\\calc_icon.ico')
cal.resizable(0,0)

#style = ThemedStyle(cal)
#style.set_theme("alt")
a=0#variable for theme
s=1
exp=""
text=tk.StringVar()

#_____________________________________Nav-Bar________________________________________

mb=ttk.Menubutton(cal,text="MENU",width=5)
mb.grid(row=0,column=0)
mb.menu = tk.Menu(mb,tearoff=0)

help=ttk.Button(cal,text="HELP",command=help)
help.grid(row=0,column=1)

about=ttk.Button(cal,text="About Us",command=aboutus)
about.grid(row=0,column=2)

mb["menu"] =  mb.menu 
mb.menu.add_command ( label="THEME",)#command=theme) 
mb.menu.add_checkbutton ( label="SCIENTIFIC",command=sci)

#_____________________________________Entry________________________________________

entry=tk.Entry(cal,justify="right",font=("aril",20,'bold'),textvariable=text,bd=30,insertwidth=4,bg='gray')
entry.grid(row=1,columnspan=4,sticky=('nsew'))
entry.focus()

#_____________________________________Keypad________________________________________

button_1=ttk.Button(cal,text="1",command=lambda:press('1'))
button_1.grid(row=3,column=0,pady=20)#padx=16,pady=16)

button_2=ttk.Button(cal,text="2",command=lambda:press(2))
button_2.grid(row=3,column=1,pady=20)

button_3=ttk.Button(cal,text="3",command=lambda:press(3))
button_3.grid(row=3,column=2,pady=20)#,padx=16)

button_4=ttk.Button(cal,text="4",command=lambda:press('4'))
button_4.grid(row=4,column=0,pady=20)#,padx=10,pady=10)

button_5=ttk.Button(cal,text="5",command=lambda:press('5'))
button_5.grid(row=4,column=1,pady=20)

button_6=ttk.Button(cal,text="6",command=lambda:press('6'))
button_6.grid(row=4,column=2,pady=20)

button_7=ttk.Button(cal,text="7",command=lambda:press('7'))
button_7.grid(row=5,column=0,pady=20)

button_8=ttk.Button(cal,text="8",command=lambda:press('8'))
button_8.grid(row=5,column=1,pady=20)


button_9=ttk.Button(cal,text="9",command=lambda:press('9'))
button_9.grid(row=5,column=2,pady=20)

button_0=ttk.Button(cal,text="0",command=lambda:press('0'))
button_0.grid(row=6,column=1,pady=20)


button_dec=ttk.Button(cal,text=".",command=lambda:press("."))
button_dec.grid(row=6,column=0,pady=20)

button_plus=ttk.Button(cal,text="+",command=lambda:press('+'))
button_plus.grid(row=3,column=3,pady=20)

button_sub=ttk.Button(cal,text="-",command=lambda:press('-'))
button_sub.grid(row=4,column=3,pady=20)

button_mul=ttk.Button(cal,text="*",command=lambda:press('*'))
button_mul.grid(row=5,column=3,pady=20)

button_div=ttk.Button(cal,text="/",command=lambda:press('/'))
button_div.grid(row=6,column=3,pady=20)



button_equ=ttk.Button(cal,text="=",command=eql)
button_equ.grid(row=7,columnspan=4,pady=20,sticky=('nswe'))
cal.bind("<Return>",eql)

button_c=ttk.Button(cal,text="del",command=delet)
button_c.grid(row=8,columnspan=2,sticky=('nswe'),pady=20,padx=20)

button_exit=ttk.Button(cal,text="exit",command=exit)
button_exit.grid(row=8,column=2,columnspan=2,sticky=('nswe'),pady=20,padx=20)



button_clr=ttk.Button(cal,text="C",command=clear)
button_clr.grid(row=6,column=2,pady=20)

cal.mainloop()

#_____________________________________DEAD-END________________________________________

