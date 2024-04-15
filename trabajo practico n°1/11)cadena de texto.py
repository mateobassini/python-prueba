def main():
    # Solicitar al usuario que ingrese una cadena de texto
    texto = input("Ingrese una cadena de texto: ")

    # Tomar los primeros 5 caracteres de la cadena
    prim5caract = texto[:5]

    # Mostrar los primeros 5 caracteres
    print("Los primeros 5 caracteres son:", prim5caract)

if __name__ == "__main__":
    main()