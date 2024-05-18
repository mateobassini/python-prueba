# Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos ejemplos de posiblesrespuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto
año = int(input("Por favor, ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
	print(año, "es bisiesto")
else:
	print(año, "no es bisiesto")