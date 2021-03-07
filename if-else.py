

usu= str(input("dime cual es tu usuario "))
usupas=["SMR","MF"]
var= usu in usupas



def sist():
	 import os
	 
	 sist=os.name
	 if sist=="nt":
	 	print("miau")

sist()

if var==True:
	print("hola bienvenido")
	
while var==False:
	print("tu usuario no existe")
	usu= str(input("dime cual es tu usuario "))
	usupas=["SMR","MF"]
	var= usu in usupas

	if var==True:
		print("hola bienvenido")
		break

	

