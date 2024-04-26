def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Ejemplo de uso
palabra = input("Ingresa un texto para verificar si es un palíndromo: ")
resultado = es_palindromo(palabra)
print(f"¿{palabra} es palíndromo? {resultado}")
