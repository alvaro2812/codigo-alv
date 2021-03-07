
##audio

from pytube import YouTube
from tkinter import *
def gui():
	menu_l=Tk()

	menu_l.title('YouTube a mp3.py')

	menu_l.geometry('700x200')

	menu_l.configure(background='red')
	def interior():


		############################marco###########################
		marco=Frame(menu_l, width=650, height=500)
		marco.configure(background='black')
		marco.pack()

		#########################entrada texto######################

		usucua=Entry(marco,width=50)

		usucua.grid(row=0, column=1)

		usucua.place(x=94, y=90)

		#########################salida texto######################

		usut=Label(marco, text="link a descargar:")

		usut.place(x=80, y=50, )

		

		#########################boton#############################

		def link_t():
			link=usucua.get()
			yt=YouTube(link)
			t=yt.streams.filter(only_audio=True).all()
			t[0].download()

		botlog=Button(menu_l, text="descargar", command=link_t)

		botlog.place(x=458, y=90)

	interior()

	

	menu_l.mainloop()
gui()