#Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
#a. Todos los números impares desde 1 hasta ese número separados por comas.
#b. La cuenta atrás desde ese número hasta cero separados por comas.
#c. Que indique si es primo o no.
#d. Por último, su factorial.
def es_primo(num):
	if num <= 1:
		return False
	for i in range(2, int(num**0.5)+1):
		if num % i == 0:
			return False
	return True

def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num - 1)
	
numero = int(input("ingrese un numero entero positivo: "))

impares = [str(i) for i in range(1, numero + 1, 2)]
print("Números impares desde 1 hasta", numero, ":", ", ".join(impares))


cuenta_atras = [str(i) for i in range(numero, -1, -1)]
print("Cuenta atrás desde", numero, "hasta 0:", ", ".join(cuenta_atras))


if es_primo(numero):
	print(numero, "es un número primo.")
else:
	print(numero, "no es un número primo.")


fact = factorial(numero)
print("Factorial de", numero, ":", fact)