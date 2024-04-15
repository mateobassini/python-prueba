def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar los espacios en blanco
    texto = texto.lower().replace(" ", "")
    # Verificar si el texto es igual al revés
    return texto == texto[::-1]

def main():
    # Solicitar al usuario que ingrese un texto
    texto = input("Ingresa un texto para verificar si es un palíndromo: ")

    # Verificar si el texto es un palíndromo
    if es_palindromo(texto):
        print("El texto ingresado es un palíndromo.")
    else:
        print("El texto ingresado no es un palíndromo.")

if __name__ == "__main__":
    main()
