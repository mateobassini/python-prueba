#Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se encuentran en dicha frase.
frase = input("ingresa una frase: ")

contador_vocales = 0

vocales=['a', 'e', 'i', 'o', 'u']

for caracter in frase:
	caracter=caracter.lower()

	if caracter in vocales:
		contador_vocales += 1

print ("las cantidad de vocales son: ", contador_vocales)