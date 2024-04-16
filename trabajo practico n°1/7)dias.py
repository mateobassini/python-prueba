def main():
	# Solicitar al usuario que ingrese el número de días
	dias = int(input("Ingresa el número de días: "))

	# Calcular el número de horas, minutos y segundos
	horas = dias * 24
	minutos = horas * 60
	segundos = minutos * 60

	# Mostrar el resultado
	print(f"{dias} días equivalen a:")
	print("Horas:", horas)
	print("Minutos:", minutos)
	print("Segundos:", segundos)

if __name__ == "__main__":
	main()
