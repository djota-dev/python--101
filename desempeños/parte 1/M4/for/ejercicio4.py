# Consigna:
# Pedir al usuario cuántos productos hay en stock.
# Luego, por cada producto:
# - Pedir el nombre (solo para simular)
# - Pedir la cantidad de unidades disponibles
# - Sumar todas las unidades
# Al final, mostrar el total de unidades en el depósito.

cantidad = int(input("¿Cuántos productos hay en stock? "))
total_unidades = 0

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    unidades = int(input(f"Ingrese la cantidad de unidades del producto {i+1}: "))
    total_unidades = total_unidades + unidades
    
    
    print("total de unidades en el depósito:", total_unidades)