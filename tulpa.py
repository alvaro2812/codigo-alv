# tupla es una lista de solo lectura , estas son mas comodas y rapidas en ciertos casos

tulpa1=("miau", "tac", 3, "gato")

#imprimir
print("esto es una tupla", tulpa1)

#crear varias variables y desempaquetal tuplas

A1, A2, A3, A4=(tulpa1)
print(A1)
print(A2)

#convertir a lista
listacon=list(tulpa1)
print("esto es un a lista", listacon)

# convertir listas a tuplas
tuplacon=tuple(listacon)
print("esto es una tupla convertida", tuplacon)

#comprobar si existe

print("tac" in tulpa1)

# saber cuantos elementos hay repetidos

print("se repite ", tulpa1.count(3))

#saber lo larga que es
print("es de larga", len(tulpa1))

#tupla unitaria 
tupla2=("jua",)
print(len(tupla2))

