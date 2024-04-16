def main():
	#solicitar al usuario la base
	base = float(input("ingresa la base:"))

	#solicitar al usuario la altura
	altura = float(input("ingresa la altura:"))

	#base por altura dividido 2 para hallar la superficie del triangulo
	mult = base * altura
	sup = mult / 2

	#mostrar el resultado
	print("la superficie del triangulo es: ", sup)

if __name__ == "__main__":
	main()