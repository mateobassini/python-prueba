año = int(input("Por favor, ingresa un año: "))

# Verificar si es bisiesto o no
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
	print(año, "es bisiesto")
else:
	print(año, "no es bisiesto")