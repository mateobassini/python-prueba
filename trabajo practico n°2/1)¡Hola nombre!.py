#Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.
def saludar(nombre):
	print("¡Hola {}!".format(nombre))

nombre = input("Ingresa tu nombre: ")
saludar(nombre)
