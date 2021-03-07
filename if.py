#pasar datos

print("programa de notas")

notas=input("introduce una nota: ")

#if basico de comparar


def clas(aprov):
	val="aprobado"
	if aprov<5:
		val="suspenso"
		print("estas suspenso")
	return val
print(clas(int(notas)))


