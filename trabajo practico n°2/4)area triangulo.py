#Que dada la base y altura de un triángulo nos calcule su área.
def calcular_area_triangulo(base, altura):
	area=(base*altura)/2
	return area
try:
	base=float(input("ingresa la basse del triangulo"))
	altura=float(input("inresa la altura del triangulo"))
finally:
	area_triangulo=calcular_area_triangulo(base,altura)
	print("el area del triangulo es: ", area_triangulo)