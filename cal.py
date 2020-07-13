#_______________________________________________________________MyPythonCalculator_______________________________________________________________




#_______________________________Downloading Modules_______________________________


import os
os.system('pip install -r req.txt')


#_______________________________Importing Modules_________________________________

import tkinter.messagebox as msg
from ttkthemes import ThemedStyle
import tkinter as tk
import  tkinter.ttk as ttk
import simpleaudio as s
from math import *
import webbrowser

#____________________________________Sounds_______________________________________


welcome = s.WaveObject.from_wave_file("medias\\welcome.wav")
button_sound = s.WaveObject.from_wave_file("medias\\buttons.wav")
math_error = s.WaveObject.from_wave_file("medias\\matherror.wav")
syn_error = s.WaveObject.from_wave_file("medias\\syntax_error.wav")
delete_sound = s.WaveObject.from_wave_file("medias\\delete.wav")
thanks = s.WaveObject.from_wave_file("medias\\thanks.wav")
result = s.WaveObject.from_wave_file("medias\\result.wav")
great = s.WaveObject.from_wave_file("medias\\great.wav")


#____________________________________Profiles_____________________________________

url = "https://im-your-hari.github.io/profile/"


#_____________________________________Help________________________________________


error_statement='''[Syntax error] : It is one of several types of errors on calculators representing that the equation that has been input has incorrect syntax of numbers,operations and so on.

[Math error] : The calculation result is outside of the allowable calculation range or you are trying to perform an illegal mathematical operation (such as division by zero)

[Instructions] : Use braces for each scientific calculations.You can't perform the oprations like '10sin(60)' use '10*sin(60)'.

Thanks :
                Avishith & Harikrishnan
'''


#_____________________________________Theme________________________________________


def theme():
	global a
	global cal
	if a==0:
		style = ThemedStyle(cal)
		style.set_theme('black')
		a=1
		cal.config(bg='#ff0066')
	
	elif a==1:	
		style = ThemedStyle(cal)
		style.set_theme("plastik")
		a=2
		cal.config(bg='#ffb366')
		
	elif a==2:	
		style = ThemedStyle(cal)
		style.set_theme("alt")
		a=0
		cal.config(bg='#1affa3')

	
#_____________________________________Help________________________________________

def help():
	msg.showinfo( 'Help',error_statement)
	
	
#_____________________________________Exit________________________________________

def exit():
        MsgBox = msg.askquestion ('Exit Application','Are you sure you want to exit the application')
        if MsgBox == 'yes':
               #} thanks.play()
                cal.destroy()
                print('Thanks For Using Our Calculator...!')
        elif MsgBox == 'no':
                #great.play()
                print('Great Choice...!')

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
	global exp
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
		exp=''
		text.set(exp)
		s=0
	elif s==0:
		button_sin.grid_forget()
		button_cos.grid_forget()
		button_tan.grid_forget()
		button_log.grid_forget()
		button_open.grid_forget()
		button_close.grid_forget()
		button_equ=ttk.Button(cal,text="=",command=eql)
		button_equ.grid(row=7,columnspan=4,pady=20,padx=30,sticky=('nswe'))
		cal.bind("<Return>",eql)
		exp=''
		text.set(exp)
		s=1

#_____________________________________Clear________________________________________

def clear():
	global exp
	exp=entry.get()
	#delete_sound.play()
	exp=""
	text.set(exp)
	
#_____________________________________About________________________________________
def aboutus():
        webbrowser.open(url)
        
	


#______________________________________Press________________________________________
	
def press(num):
	global exp
	exp=entry.get()
	#button_sound.play()
	exp += str(num)
	text.set(exp)
	#entry.focus()
	
#-------------------


'''def one(event):
        global exp
        button_sound.play()
        exp += str(event.char)
        entry.focus()'''
        

        
	
#_____________________________________Answer________________________________________
def eql(*args):
        global exp
        exp=entry.get()
        try:
            exp=str(eval(exp))
            text.set(exp)
           # result.play()
        except ZeroDivisionError:
                math_error.play()
                text.set("Math Error occured...!")
        except SyntaxError:
                syn_error.play()
                text.set("Syntax Error occured...!")
        except NameError:
                math_error.play()
                text.set('Math Error occured....!')
        except TypeError:
                syn_error.play()
                text.set("Syntax Error occured...!")
                

#___________________________________Backspace_______________________________________

def delet():
	global exp
	exp=entry.get()
#	delete_sound.play()
	le=len(exp)
	exp=exp[0:(le-1)]
	text.set(exp)

#_____________________________________Main_______________________________________

#welcome.play()
cal=tk.Tk()
cal.title("My Python Calculator")
cal.config(bg='#1affa3')
cal.geometry('400x630')
#cal.iconbitmap(r'medias\\calc_icon.ico')
cal.resizable(0,0)

style = ThemedStyle(cal)
style.set_theme("alt")
a=0#variable for theme
s=1#variable for scientific_mode
exp=""
text=tk.StringVar()

#_____________________________________Nav-Bar________________________________________

mb=ttk.Menubutton(cal,text="MENU",width=5)
mb.grid(row=0,column=0)
mb.menu = tk.Menu(mb,tearoff=0)

help=ttk.Button(cal,text="HELP",command=help)
help.grid(row=0,column=1)

about=ttk.Button(cal,text="ABOUT",command=aboutus)
about.grid(row=0,column=2)

mb["menu"] =  mb.menu 
mb.menu.add_command ( label="THEME",command=theme) 
mb.menu.add_checkbutton ( label="SCIENTIFIC",command=sci)

#_____________________________________Entry________________________________________

entry=tk.Entry(cal,justify="right",font=("aril",20,'bold'),textvariable=text,bd=30,insertwidth=4,bg='gray')
entry.grid(row=1,columnspan=4,padx=20,pady=20,sticky=('nsew'))
entry.focus()

#_____________________________________Keypad________________________________________


button_1=ttk.Button(cal,text="1",command=lambda:press('1'))
button_1.grid(row=3,column=0,pady=20)
#entry.bind("<Key>",one)

button_2=ttk.Button(cal,text="2",command=lambda:press(2))
button_2.grid(row=3,column=1,pady=20)
#entry.bind("<Key>",one)

button_3=ttk.Button(cal,text="3",command=lambda:press(3))
button_3.grid(row=3,column=2,pady=20)

button_4=ttk.Button(cal,text="4",command=lambda:press('4'))
button_4.grid(row=4,column=0,pady=20)

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
button_equ.grid(row=7,columnspan=4,pady=20,padx=30,sticky=('nswe'))
cal.bind("<Return>",eql)


button_c=ttk.Button(cal,text="CLEAR",command=clear)
button_c.grid(row=8,columnspan=2,sticky=('nswe'),padx=20,pady=20)

button_exit=ttk.Button(cal,text="EXIT",command=exit)
button_exit.grid(row=8,column=2,columnspan=2,sticky=('nswe'),pady=20,padx=20)



button_clr=ttk.Button(cal,text="⌫",command=delet)
button_clr.grid(row=6,column=2,pady=20)
entry.bind('<BackSpace>')

cal.mainloop()

#_____________________________________DEAD-END________________________________________
