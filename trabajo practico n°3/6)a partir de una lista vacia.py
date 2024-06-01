class ListaInteractiva:
    def __init__(self):
        self.lista = []

    def agregar_final(self, elemento):
        self.lista.append(elemento)

    def agregar_inicio(self, elemento):
        self.lista.insert(0, elemento)

    def quitar_final(self):
        return self.lista.pop() if self.lista else None

    def quitar_inicio(self):
        return self.lista.pop(0) if self.lista else None

    def imprimir_lista(self):
        print("Lista actual:", self.lista)


def mostrar_menu():
    print("\nOpciones:")
    print("a. Agregar un elemento al final.")
    print("b. Agregar un elemento al principio.")
    print("c. Quitar un elemento al final.")
    print("d. Quitar un elemento al principio.")
    print("e. Salir.")


def obtener_opcion():
    opcion = input("Ingrese su opción: ").lower()
    while opcion not in {'a', 'b', 'c', 'd', 'e'}:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        opcion = input("Ingrese su opción: ").lower()
    return opcion


def ejecutar_opcion(opcion, lista):
    if opcion == 'e':
        print("¡Hasta luego!")
        exit()
    elif opcion in {'c', 'd'}:
        elemento = lista.quitar_final() if opcion == 'c' else lista.quitar_inicio()
        if elemento is not None:
            print(f"Elemento eliminado: {elemento}")
        else:
            print("La lista está vacía.")
    else:
        elemento = input("Ingrese el elemento: ")
        lista.agregar_final(elemento) if opcion == 'a' else lista.agregar_inicio(elemento)
    lista.imprimir_lista()


def main():
    lista_interactiva = ListaInteractiva()

    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        ejecutar_opcion(opcion, lista_interactiva)


if __name__ == "__main__":
    main()
