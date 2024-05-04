def factura_iva(sin_iva, porcentaje_iva=21):
    con_iva=sin_iva * (porcentaje_iva / 100)

    total=sin_iva + con_iva

    return total

sin_iva=float(input("ingrese el monto de la factura: "))

try:
    porcentaje_iva= float(input("ingrese el iva aplicado a la factura:"))
except ValueError:
    porcentaje_iva=21


total_factura= factura_iva(sin_iva,porcentaje_iva)
print("el total de la factura con iva incluido es: {:2f}".format(total_factura))
