#Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.
def calc_potencia(base, exponente):
	if exponente < 0:
		return "el exponente debe ser positivo"
	else:
	   return base ** exponente

numero= int(input("ingresa un numero positivo: "))
potencia= int(input("ingrese la potencia: "))

resultado = calc_potencia(numero, potencia)
print("el resultado de {} elevado a {} es: {}".format(numero,potencia,resultado))


