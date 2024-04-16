def main():
	# Solicitar al usuario que ingrese el primer número
	num1 = float(input("Ingresa el primer número: "))

	# Solicitar al usuario que ingrese el segundo número
	num2 = float(input("Ingresa el segundo número: "))

	# Solicitar al usuario que ingrese el tercer número
	num3 = float(input("Ingresa el tercer número: "))

	# Sumar los dos primeros números ingresados por el usuario
	suma = num1 + num2

	#multiplicar la suma por el tercer número ingresado por el usuario
	mult = suma*num3

	# Mostrar el resultado de la suma
	print("La respuesta es", mult)

if __name__ == "__main__":
	main()