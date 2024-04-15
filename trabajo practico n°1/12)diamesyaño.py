def main():
    # Solicitar al usuario que ingrese una fecha
    fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")

    # Dividir la fecha en día, mes y año
    partes_fecha = fecha.split('/')

    # Extraer el día, mes y año
    dia = partes_fecha[0]
    mes = partes_fecha[1]
    año = partes_fecha[2]

    # Imprimir el día, mes y año
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", año)

if __name__ == "__main__":
    main()
