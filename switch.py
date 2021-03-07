
def  menutexto():
    print("******************************************************************")
    print("MENU")
    print("******************************************************************")
    print("1.- Crear un usuario")
    print("2.- Guardar la fecha y hora tontamente")
    print("3.- Mostrar fichero")
    print("4.- Salir")
    print("******************************************************************")

def sist():
	 import os
	 import time
	 sist=os.name
	 if sist=="nt":
	 	os.system('cls')
	 	
	 	time.sleep(1)

	 else:
	 	os.system('clear')
	 	time.sleep(1)



def part1():
	 import os
	 import time
	 sist=os.name
	

	 if sist=="ntr":

	 	

	 	time.sleep(1)

	 	os.system('echo',(usunun))

	 	os.system('cls')
	 	menutexto()

	 else:
	 	
	 	print("vete a linux!!!!!")
	 



usu=str(input("hola cual es tu usuario: "))
usupas="SMR"
while True:
    
   
    if usu==usupas:
        pas=str(input("pon tu contraseña: "))
        paspas="PRACTICA"
        if pas==paspas:

        	
            

            while True:

                opciones=["1", "2", "3", "4"]

                sist()

                menutexto()

                while True:
                	


                    opcion = input("seleciona una opcion: ")

                    var= opcion in opciones

                    if opcion == "1":
                        print("hola")
                        part1()
                        sist()
                        menutexto()

                    if opcion == "2":
                        print("hola 2")
                        sist()
                        menutexto()

                    if opcion == "3":
                        print("miau")
                        sist()
                        menutexto()

                    if opcion == "4":
                        exit()

                    if var==False:

                        print("opcinon incorrecta prueba de nuevo")

                        menutexto()
            menutexto()
        else:
        	print("contraseña incorecta")

    else:
    	print("no esta wien escrito")
    	usu=str(input("hola cual es tu usuario: "))
    	usupas="SMR"
       
        

