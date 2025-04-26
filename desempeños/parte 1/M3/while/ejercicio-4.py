"""Ingresar la cantidad de productos comprados. Para cada producto, leer su precio, calcular el total gastado y, si el total supera $1000, aplicar un descuento del 10%. Mostrar el total final (con o sin descuento)."""

productos = int(input("Ingrese la cantidad de productos comprados: "))
total_gastado = 0
contador = 0

while contador < productos:
    precio = float(input(f"ingrese el precio del producto {contador +1}:"))
    total_gastado = total_gastado + precio
    contador = contador + 1
    
    print(f"el total gastado sin descuento es : {total_gastado }")
    
    if total_gastado > 1000:
        descuento = total_gastado * 0.10
        total_con_descuento = total_gastado - descuento
        print(f"el total gastado con descuento es: {total_con_descuento}")
    else:
        print("no se aplica descuento")
        
    
        
    
    