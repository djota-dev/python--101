# Consigna:
# Pedir al usuario cuántos días quiere registrar.
# Luego, por cada día, pedir la temperatura.
# Al final, mostrar:
# - El promedio de las temperaturas
# - La temperatura más alta registrada
# - La temperatura más baja registrada

dias = int(input("¿Cuántos días quieres registrar? "))
suma = 0;
max_tmp = None
min_tmp = None

for i in range(dias):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    suma = suma + temp
    
    if max_tmp == None or temp > max_tmp:
        max_tmp = temp
    if min_tmp == None or temp < min_tmp:
        min_tmp = temp
    
promedio = suma / dias
print("promedio:", promedio)
print("temperatura más alta:", max_tmp)
print("temperatura más baja:", min_tmp)


"""
¿QUÉ SIGNIFICA None EN ESTE CÓDIGO?

None es un valor especial en Python que representa "nada" o "ausencia de valor".
Es diferente a cero o a una cadena vacía, y se usa comúnmente para inicializar
variables cuando no tenemos un valor inicial significativo.

¿POR QUÉ USAMOS mayor = None y menor = None?

INICIALIZACIÓN:
mayor = None
menor = None

- Al principio no tenemos temperaturas registradas
- No podemos inicializar con 0 porque sería un valor válido de temperatura
- None indica claramente que aún no tenemos valores registrados

LÓGICA DE COMPARACIÓN:

Para la temperatura MÁXIMA:
if mayor == None or temp > mayor:
    mayor = temp

- En la primera iteración (mayor es None), asignamos automáticamente
  la primera temperatura como valor máximo
- En iteraciones posteriores, solo actualizamos si la nueva temperatura
  es mayor que el máximo registrado

Para la temperatura MÍNIMA:
if menor == None or temp < menor:
    menor = temp

- Misma lógica que para el máximo, pero buscando el valor más bajo
"""