#Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia_semana = input("Por favor, ingresa un día de la semana: ")

dia_semana = dia_semana.lower()

if dia_semana == "lunes":
	print("¡Es el comienzo de la semana!")
elif dia_semana == "viernes":
	print("¡Por fin es viernes!")
elif dia_semana == "sábado" or dia_semana == "domingo":
	print("¡Es fin de semana, disfruta!")
else:
	print("Hoy no es un dia muy especial.")