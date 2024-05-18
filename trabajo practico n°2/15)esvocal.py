# Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
letra = input("ingresa una letra.")

if len(letra) == 1:
	letra=letra.lower()

	if letra in ['a', 'e', 'i', 'o', 'u']:
		print("es vocal")
	else:
		print("no es vocal")

else:
	print("inrese un solo caracter")