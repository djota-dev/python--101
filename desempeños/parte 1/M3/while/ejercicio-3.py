"""Leer n números enteros, donde n es definido por el usuario. Contar cuántos de los números son positivos, cuántos negativos y cuántos son ceros."""

n = int(input("Ingrese la cantidad de números a leer: "))

contador= 0
positivos = 0
negativos = 0
ceros = 0

while contador < n:
    numero = int(input("ingrese el numero: "))
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1
        
    contador += 1
    
    
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")