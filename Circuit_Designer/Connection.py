
import Prueba2
from tkinter import *
from tkinter import ttk

from tkinter import messagebox


But1 = None
Pos = None
Grafo = {}

def Connection1(button,pos,window):

	global But1
	global Pos
	if (But1 == None):
		But1 = button
		Pos = pos 

	else: 

		temp = But1
		But1 = None
		temp2 = Pos
		Pos = None
		return Connection(temp, button,temp2,pos,window)

def Connection(buttonA, buttonB , pos1,pos2,window):
	if (pos1>pos2):
		Ver = buttonA
		Hor = buttonB
	elif (pos1<pos2):
		Ver = buttonB
		Hor = buttonA
	else:
		if(buttonA.winfo_rooty()<buttonB.winfo_rooty):
			Ver = buttonA
			Hor = buttonB
		else:
			Ver = buttonB
			Hor = buttonA


	Diference = 0
	Width = Hor.winfo_rootx()-Ver.winfo_rootx()		
	if (Width<0):
		Diference = abs(Width)
	But1 = Button(window,bg="blue",fg="black", relief = "flat")
	But1.place(x=Ver.winfo_rootx()-62-Diference,y=Hor.winfo_rooty()-23,width = abs(Width), heigh = 5)

	Diference = 0
	Heigh = Ver.winfo_rooty()-Hor.winfo_rooty()
	if (Heigh<0):
		Diference = abs(Heigh)
	But2 = Button(window,bg="blue",fg="black", relief = "flat")
	But2.place(x=Ver.winfo_rootx()-62,y=Hor.winfo_rooty()-23-Diference,width = 5, heigh = abs(Heigh))


class NodoButton:  
	def __init__(self):
		self.Nodo = {}
		self.Botones = []


	def getNodoList(self):
		return self.NodeList

	def getNodo(self,nombre):
		for nodo in self.NodeList:
			if (nodo.Name == nombre):
				return nodo.getDic

	def getGeneralDic(self):
		newDic = {}

def interfaz_prueba():
	window=Tk()
	window.state("zoomed")

	




	A1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	A1.place(x=100,y=200)
	A1.config(command=lambda B = A1 , a = 1 , W = window: Connection1(B,a,W))



	A2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	A2.place(x=100,y=225)
	A2.config(command=lambda B = A2 , a = 1 , W = window: Connection1(B,a,W))


	B1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	B1.place(x=400,y=100)
	B1.config(command=lambda B = B1 , a = 0 , W = window: Connection1(B,a,W))

	B2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	B2.place(x=425,y=100)
	B2.config(command=lambda B = B2 , a = 0 , W = window: Connection1(B,a,W))


	C1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	C1.place(x=700,y=200)
	C1.config(command=lambda B = C1 , a = 1 , W = window: Connection1(B,a,W))

	C2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	C2.place(x=700,y=225)
	C2.config(command=lambda B = C2 , a = 1 , W = window: Connection1(B,a,W))


	D1=Button(window,text="a",bg="red",fg="black",font=("Bodoni MT Black","10"))
	D1.place(x=400,y=400)
	D1.config(command=lambda B = D1 , a = 0 , W = window: Connection1(B,a,W))

	D2=Button(window,text="b",bg="red",fg="black",font=("Bodoni MT Black","10"))
	D2.place(x=425,y=400)
	D2.config(command=lambda B = D2 , a = 0 , W = window: Connection1(B,a,W))











	window.mainloop()

def Pelear1(event,a):
	print(a)

def second_win():
	root = Tk()
	root.state("zoomed")


	D2=Button(root,bg="blue",fg="black", relief = "flat")
	D2.place(x=100,y=110,width = 10, heigh = -10)

	D1=Button(root,bg="red",fg="black", relief = "flat")
	D1.place(x=500,y=100,width = 200, heigh = -300)



#	calibCanvas = Canvas(root,bg="white")  
##	calibCanvas.pack()   
##	canvasRect = calibCanvas.create_rectangle(50, 0, 100, 50, fill='red') 
##	canvasRect.bind("<ButtonPress-1>", lambda event=0 , A = "a": Pelear1(event,a))
##	print (calibCanvas.coords(canvasRect))
	root.update()
	print(D2.winfo_rootx(),D2.winfo_rooty())
	root.mainloop()



#second_win()

interfaz_prueba()