# Que muestre todoslos números primos entre 0 y 100 e imprima cuántos números primos hay.
def es_primo(numero):
	if numero <= 1:
		return False
	for i in range(2, int(numero**0.5) + 1):
		if numero % i == 0:
			return False
	return True

numeros_primos = []

for num in range(101):
	if es_primo(num):
		numeros_primos.append(num)

print("Los números primos entre 0 y 100 son:")
for primo in numeros_primos:
	print(primo, end=" ")

print("\nHay", len(numeros_primos), "números primos en total.")