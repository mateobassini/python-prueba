# Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla el grupo que le corresponde.
nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (H para hombre, M para mujer): ")

nombre = nombre.lower()

if (sexo.lower() == "m" and nombre < 'm') or (sexo.lower() == "h" and nombre >= 'n'):
	grupo = "A"
else:
	grupo = "B"

print("Tu grupo es:", grupo)
