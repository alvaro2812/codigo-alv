from tkinter import *

def login():
	marco=Frame(menu_l, width=500, height=200)
	marco.configure(background='green')
	marco.pack()

	usucua=Entry(marco)


	usut=Label(marco, text="usuario:")

	usut.place(x=80, y=50)

	usucua.grid(row=0, column=1)

	usucua.place(x=94, y=90)


	pascua=Entry(marco)


	past=Label(marco, text="contraseña:")

	past.place(x=80, y=120)

	pascua.grid(row=0, column=1)

	pascua.place(x=94, y=150)

	def sacar():
		print(str(usucua.get()))
		print(str(pascua.get()))
		compusu=usucua.get()
		comppas=pascua.get()

		if compusu=="SMR":
			print('usuario correcto')
			if comppas=="PRACTICA":
				print('contraseña correcta')
				menu()
			else:
				print('contraseña incorrecta')
		else:
			print('usuario o contraseña incorrecta')

	botlog=Button(menu_l, text="inicar sesion", command=sacar)

	botlog.place(x=118, y=200)

menu_l=Tk()

menu_l.title('alv.py')

menu_l.geometry('300x300')

menu_l.configure(background='green')

def salir():
	menu_l.destroy()


login()

def menu():

	
	salir()

	menu=Tk()

	menu.title('alv.py')

	menu.geometry('300x300')

	menu.configure(background='blue')

	menu_marc=Frame(menu, width=500, height=300)

	menu_marc.configure(background='blue')

	menu_marc.pack()
	
	texm=Label(menu_marc,text='selecciona una opcion')

	texm.place(x=92, y=5)

	crear=Button(menu_marc, text="crear usuario")


	crear.place(x=115, y=60)

	guar=Button(menu_marc, text="Guardar fecha")


	guar.place(x=114, y=100)


	lis=Button(menu_marc, text="hacer cat fichero")


	lis.place(x=108, y=140)

	cerrar=Button(menu_marc, text="cerrar sesion")


	cerrar.place(x=120, y=260)


	guar.mainloop()

menu_l.mainloop()