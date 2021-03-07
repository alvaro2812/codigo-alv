#son funciones con varios datos

lista1=["gato","perro","loro"]


#añadir elementos a la lista
lista1.append("michi")
#añadir elementos a la lista y darle orden
lista1.insert(2,"perla")
#añadir varios elementos a la lista
lista1.extend(["cat","dog","bird","kitty"])

#imprimir toda la lista
print(lista1[:])
#saber el numero de un elemeto
print("esta en el", lista1.index("cat"))

#imprimir una parte (recuerda que el primero es 0)
print(lista1[2])
#funcion hacia atras
print(lista1[-2])
#acceder a multiples elementos si se  omite el primer 0 piensa que el por defecto es 0
print(lista1[0:2])
#ordenar al reves
print(lista1[1:])

#comprobar si existe
print("mici" in lista1)

#eliminar elementos

lista1.remove("cat")
print(lista1[:])

#eliminar ultimo elemento

lista1.pop()
print(lista1[:])

#sumar listas diferentes

lista2=["algo","algo2"]

lista3=lista1+lista2
print(lista3[:])

#repetir listas

lista4=["lag","miau"] * 3

print(lista4[:])