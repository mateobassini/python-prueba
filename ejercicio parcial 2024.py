def main():
	calificaciones = []

	while True:
		calificacion = input("Ingrese una calificación (o escriba 'FIN' para terminar): ")
		if calificacion.upper() == 'FIN':
			break
		try:
			calificacion = float(calificacion)
			calificaciones.append(calificacion)
		except ValueError:
			print("Error: Por favor, ingrese un número válido o escriba 'FIN' para terminar.")

	if not calificaciones:
		print("No se ingresaron calificaciones.")
		return

	calificaciones.sort()

	print("Calificaciones ordenadas de menor a mayor:")
	for calif in calificaciones:
		if calif.is_integer():  
			print(int(calif), end=' ')
		else:
			print(f"{calif:.2f}", end=' ')
	print()  

	promedio = sum(calificaciones) / len(calificaciones)
	print(f"El promedio de las calificaciones es: {promedio:.2f}")

	cantidad_calificaciones = len(calificaciones)
	print(f"Se ingresaron un total de {cantidad_calificaciones} calificaciones.")

	calificaciones_str = ', '.join(map(str, calificaciones))
	print(f"Calificaciones como cadena separada por comas: {calificaciones_str}")

	aprobados = sum(1 for calif in calificaciones if calif >= 6)
	print(f"Número de alumnos que han aprobado: {aprobados}")

	calif_minima = min(calificaciones)
	calif_maxima = max(calificaciones)
	print(f"La calificación más baja fue {calif_minima} y la más alta fue {calif_maxima}.")

	calificaciones.clear()
	print("La lista de calificaciones ha sido vaciada.")


if __name__ == "__main__":
	main()
