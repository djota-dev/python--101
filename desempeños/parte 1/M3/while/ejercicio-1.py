"""Leer 15 números enteros. Mostrar aquellos que sean múltiplos de 3 y mayores a 50. Finalmente, mostrar la cantidad total de números que cumplieron con esa condición."""

contador = 0

cumplen = 0

while contador < 15:
    numero = int(input("ingrese el numero: "))
    
    # Verificar si el número es múltiplo de 3 y mayor a 50
    if numero % 3 == 0 and numero > 50:
        print(f"{numero} es multiplo de 3 y mayor a 50")
        cumplen = cumplen + 1
    contador = contador + 1
    
print(f"la cantidad de numeros que cumplen la condicion es: {cumplen}")


        