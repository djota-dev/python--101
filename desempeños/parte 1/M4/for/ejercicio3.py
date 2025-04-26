# Consigna:
# Pedir al usuario cuántas notas va a cargar.
# Luego, por cada nota:
# - Pedir la nota
# - Acumular las notas para calcular el promedio
# - Contar cuántas son mayores o iguales a 6 (aprobados)
# Al final, mostrar el promedio general y la cantidad de aprobados.

cant = int(input("¿Cuántas notas va a cargar? "))
suma = 0
aprobados = 0


for i in range(cant):
    nota = float(input("ingresá la nota"))
    suma = suma + nota
    
    if nota >= 6:
        aprobados = aprobados +1 #aprobados += 1
        
promedio = suma / cant
print("promedio:", promedio)
print("cantidad de aprobados:", aprobados)

