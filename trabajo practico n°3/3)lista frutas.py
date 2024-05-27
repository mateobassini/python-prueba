frutas = ["banana", "manzana", "pera"]

print("ingrese 3 frutas adicionales:")
for i in range(3):
	frutas_nuevas = input("fruta {}:". format(i+1))
	frutas.append(frutas_nuevas)

print("\nLista completa de frutas: ")
for fruta in frutas:
	print(fruta)

print("\nFrutas nuevas: ")
for fruta in frutas [3:]:
	print(fruta)