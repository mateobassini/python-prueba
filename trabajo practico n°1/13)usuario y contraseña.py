def generar_usuario_contraseña(nombre, apellido, año_nacimiento):
	# Generar el nombre de usuario
	usuario = nombre[0].lower() + apellido.lower()

	# Generar la contraseña
	contraseña = nombre[0].lower() + apellido[0].lower() + '.' + año_nacimiento

	return usuario, contraseña

def main():
	# Solicitar al usuario su nombre, apellido y año de nacimiento
	nombre = input("Ingrese su nombre: ")
	apellido = input("Ingrese su apellido: ")
	año = input("Ingrese su año de nacimiento: ")

	# Generar el nombre de usuario y la contraseña
	usuario, contraseña = generar_usuario_contraseña(nombre, apellido, año)

	# Imprimir el nombre de usuario y la contraseña sugeridos
	print("Usuario sugerido:", usuario)
	print("Contraseña sugerida:", contraseña)

if __name__ == "__main__":
	main()
