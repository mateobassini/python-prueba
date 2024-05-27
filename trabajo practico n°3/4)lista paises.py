paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

print("Cantidad de elementos en la lista:", len(paises))

print("Primer elemento:", paises[0])
print("Último elemento:", paises[-1])

print("Resto de elementos:")
for pais in paises[1:-1]:
    print(pais)

pais_buscado = input("Ingrese un país para buscar en la lista: ")
if pais_buscado in paises:
    print("El país", pais_buscado, "se encuentra en la lista en el índice", paises.index(pais_buscado))
else:
    print("El país", pais_buscado, "no se encuentra en la lista.")

indice_a_eliminar = int(input("Ingrese un número igual o menor a la cantidad de elementos de la lista para eliminar el país en esa posición: "))
if indice_a_eliminar <= len(paises):
    del paises[indice_a_eliminar - 1]
    print("Elemento eliminado correctamente.")
else:
    print("El número ingresado excede la cantidad de elementos en la lista.")

print("Lista en orden inverso:")
for pais in reversed(paises):
    print(pais)

paises.clear()
print("La lista ha sido vaciada:", paises)
