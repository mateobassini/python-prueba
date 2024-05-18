# Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso en que ambos números son iguales.
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

if num1 > num2:
	print("el numero mayor es: ",num1)
elif num1 < num2:
	print("el numero mayor es: ",num2)
else:
	print("los numeros ingresados son iguales.")
