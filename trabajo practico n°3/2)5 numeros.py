print("Ingrese 5 números:")
numeros = []
for i in range(5):
	numero = float(input("Número {}: ".format(i+1)))
	numeros.append(numero)

numeros.sort()

print("Números ordenados:")
for numero in numeros:
	print(numero)
