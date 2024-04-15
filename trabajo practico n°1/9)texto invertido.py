def main():
    #Solicitar al usuario que ingrese un texto
    texto = input("ingresa un texto: ")

    #Invertir el texto
    texto_invertido = texto[::-1]

    #Mostrar el texto invertido
    print("El texto invertido es:", texto_invertido)

if __name__ == "__main__":
    main()