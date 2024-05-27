materias_carrera = ["Introducción a la Informática", "Programación I", "Diseño Gráfico", "Arquitectura de Computadoras", "Programación II", "Sistemas Operativos", "Introducción al Desarrollo Web", "Bases de Datos", "Redes de Datos", "Programación III", "Ingeniería de Software", "Desarrollo de Aplicaciones Web", "Desarrollo para Móviles", "Multimedia y Juegos en Web"]

def mostrar_materias(materias):
	print("Materias de la carrera:")
	for materia in materias:
		print("-", materia)

mostrar_materias(materias_carrera)
