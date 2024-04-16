def main():
	#solicitar al usuario que ingrese el total de la cuenta
	cuenta = float(input("ingresa el valor de la cuenta:$"))

	#solicitar al usuario el numero de comensales
	comensales = int(input("ingresa el numero de comensales:"))

	#divide la cuenta por el numero de comensales 
	div = cuenta / comensales

	#mostrar el resultado de la division
	print("cada persona debe pagar:$", div)

if __name__ == "__main__":
	main()