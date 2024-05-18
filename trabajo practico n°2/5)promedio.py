# Que dado tres números ingresados por el usuario nos devuelva el promedio.
def calcular_promedio(num1,num2,num3):
	promedio= (num1+num2+num3)/3
	return promedio

try:
	num1=float(input("ingrese el primer numero: "))
	num2=float(input("ingrese el segundo numero: "))
	num3=float(input("ingrese el tercer numero: "))
finally:
	promedio=calcular_promedio(num1,num2,num3)
	print("el promedio es: ", promedio)