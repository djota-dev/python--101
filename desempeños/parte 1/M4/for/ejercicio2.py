# Consigna:
# Pedir al usuario cuántos productos va a comprar.
# Luego, por cada producto:
# - Pedir el nombre (solo para simular)
# - Pedir el precio
# - Sumar todos los precios
# Al final, mostrar el total a pagar y la cantidad total de productos.


c = int(input("¿Cuántos productos va a comprar? "))
total = 0

for i in range(c):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio  = float(input(f"Ingrese el precio del producto {i+1}: "))
    total = total + precio
    
print("total a pagar:", total)
print("cantidad de productos:", c)

