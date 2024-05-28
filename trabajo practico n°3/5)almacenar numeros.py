def obtener_numeros():
    numeros = []
    while True:
        entrada = input("Ingrese un número entero o escriba 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero válido.")
    return numeros

def maximo(numeros):
    return max(numeros)

def segundo_maximo(numeros):
    numeros_ordenados = sorted(set(numeros), reverse=True)
    if len(numeros_ordenados) > 1:
        return numeros_ordenados[1]
    else:
        return None

def minimo(numeros):
    return min(numeros)

def multiplicacion(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def contar_pares_impares(numeros):
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = sum(1 for num in numeros if num % 2 != 0)
    return pares, impares

def remover_repetidos(numeros):
    return list(set(numeros))

# Solicitar números al usuario
numeros = obtener_numeros()

# a. Determinar el máximo.
maximo_numero = maximo(numeros)
print("Máximo:", maximo_numero)

# b. Obtener segundo valor máximo.
segundo_maximo_numero = segundo_maximo(numeros)
print("Segundo máximo:", segundo_maximo_numero)

# c. Determinar el mínimo.
minimo_numero = minimo(numeros)
print("Mínimo:", minimo_numero)

# d. Calcular la multiplicación de todos los números de la lista.
resultado_multiplicacion = multiplicacion(numeros)
print("Multiplicación de todos los números:", resultado_multiplicacion)

# e. Contar los valores pares e impares.
num_pares, num_impares = contar_pares_impares(numeros)
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)

# f. Remover los elementos repetidos.
numeros_sin_repetir = remover_repetidos(numeros)
print("Números sin repetir:", numeros_sin_repetir)