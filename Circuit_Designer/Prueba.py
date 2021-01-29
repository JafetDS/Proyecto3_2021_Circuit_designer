
import Prueba2
from tkinter import *
from tkinter import ttk

from tkinter import messagebox


But1 = None


def makeline2(button,a,window):
	print (window.coords(button))

	global But1
	if (But1 == None):
		But1 = button

	else: 
		temp = But1
		But1 = None
		return makeline2(But1, button)




def interfaz_prueba():
	win=Tk()
	win.state("zoomed")
	window = Canvas(win , width = 2000 , heigh = 2000 , background = "white")
	window.grid(row = 0, column = 0)




	A1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	A1.place(x=100,y=200)
	A1.config(command=lambda B = A1 , a = "2" , W = window: makeline2(B, a , W))




	A2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	A2.place(x=100,y=225)


	B1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	B1.place(x=400,y=100)

	B2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	B2.place(x=425,y=100)


	C1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	C1.place(x=700,y=200)

	C2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	C2.place(x=700,y=225)


	D1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	D1.place(x=400,y=400)

	D2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	D2.place(x=425,y=400)











	win.mainloop()

def Pelear1(event,a):
	print(a)

def second_win():
	root = Tk()
	root.state("zoomed")


	D2=Button(root,bg="blue",fg="black", relief = "flat")
	D2.place(x=100,y=110,width = 10, heigh = 10)

	D1=Button(root,bg="red",fg="black", relief = "flat")
	D1.place(x=0,y=100,width = 100, heigh = 10)



#	calibCanvas = Canvas(root,bg="white")  
##	calibCanvas.pack()   
##	canvasRect = calibCanvas.create_rectangle(50, 0, 100, 50, fill='red') 
##	canvasRect.bind("<ButtonPress-1>", lambda event=0 , A = "a": Pelear1(event,a))
##	print (calibCanvas.coords(canvasRect))
	root.update()
	print(D2.winfo_rootx(),D2.winfo_rooty())
	root.mainloop()



second_win()