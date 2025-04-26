"""Leer 10 notas (valores entre 0 y 10). Validar que cada nota esté dentro del rango   permitido. Calcular y mostrar el promedio, y clasificarlo en:

Desaprobado si el promedio es menor a 4.

Regular si el promedio está entre 4 y 6.9.

Aprobado si el promedio es 7 o mayor."""

suma = 0
notas_validas = 0


while notas_validas < 10:
    nota = float(input("ingrese la nota: "))
    
    if 0 <= nota <=10: #valida que la notas este entre 0 y 10
        suma = suma + nota
        notas_validas = notas_validas + 1
    else:
        print("la nota no es valida")
        
    promedio =  suma /notas_validas
    print(f"el promedio es: {promedio}")
    

if promedio < 4:
    print("desaprobado")
elif promedio >= 4 and promedio < 7:
    print("regular")
else:
    print("aprobado")
    
    
    