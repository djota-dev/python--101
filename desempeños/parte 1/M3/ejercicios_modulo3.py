# Desempeño 17
#dado el programa:

x=1
while x<=100:
 print(x) 
 x=x+1
 
#a| Imprimir los números del 1 al 500.
    #Modificar la condición del while para que sea x <= 500.
    
#b| Imprimir los números del 50 al 100.
    # b. Inicializar la variable x con 50.

#c| Imprimir los números del -50 al 0.
    # c. Inicializar la variable x con -50.# c. Inicializar x en -50 y usar la condición x <= 0.

#d| Imprimir los números del 2 al 100 pero de 2 en 2 (2,4,6,8 ....100)
    # d. Inicializar x con 2 e incrementar de a 2 (x = x + 2) dentro del while.


# Desempeño 18
# Leer 10 notas de alumnos. Contar cuántas son mayores o iguales a 7 y cuántas menores. Mostrar ambas cantidades.
cant_notas = 0
cantidad_mayores = 0
cantidad_menores = 0

while cant_notas < 10:
    nota = int(input("ingresar nota:"))
    cant_notas = cant_notas + 1
    
    if nota >= 7:
        cantidad_mayores = cantidad_mayores + 1
    else:
        cantidad_menores = cantidad_menores + 1
    
    
print("\nResultados:")
print("Cantidad de notas mayores o iguales a 7:", cantidad_mayores)
print("Cantidad de notas menores a 7:", cantidad_menores)

# Desempeño 19
# Leer la cantidad de personas y luego ingresar sus alturas.
# Calcular y mostrar el promedio de altura.

cant = int(input("ingresar cantidad de personas:"))
total = 0
contador = 0

while contador  < cant:
    altura = float(input("ingresar altura:"))
    total = total + altura
    contador = contador + 1

prom = total / cant
print("el promedio de altura es:", prom)

# Desempeño 20
# Leer la cantidad de empleados de una empresa. Ingresar sus sueldos.
# Contar cuántos ganan entre 100 y 300 y cuántos más de 300. Calcular el gasto total en sueldos.
cant_empleados = int(input("ingresar cantidad de empleados"))

cant_mas_300 = 0
cant_100_300  =0
total_Sueldos = 0
contador = 0

while contador < cant_empleados:
    sueldo = float(input("ingresar sueldo del empleado: "))
    contador += 1
    total_Sueldos = total_Sueldos + sueldo
    

    if sueldo >=100 and sueldo <= 300:
        cant_100_300 = cant_100_300 + 1
    elif sueldo > 300:
        cant_mas_300 = cant_mas_300 + 1
    else:
        print("sueldo menor a 100$")


print("empleados que ganan mas de 300$:", cant_mas_300,"$")
print("empleados que ganan entre 100$ y 300$:", cant_100_300,"$")
print("total gasto en sueldos:", total_Sueldos, "$")


# Desempeño 21
# Imprimir los primeros 25 múltiplos de 11.

num = 11
multiplos = 0
contador = 0

while contador < 25:
    multiplos = num * (contador + 1)
    print(multiplos)
    contador = contador + 1


# Desempeño 22
# Imprimir todos los múltiplos de 8 que sean menores o iguales a 500.
num = 8
multiplos = 0
contador = 0

while multiplos <= 500:
    multiplos = num * (contador + 1)
    
    if multiplos <=500:
        print(multiplos)
    contador = contador + 1
    
#---------- Desempeño 22 (Alternativa)--------------
num = 8
contador = 1

while (multiplo := num * contador) <= 500:  # Usando el operador walrus (Python 3.8+)
    print(multiplo)
    contador += 1
#----------------------------------------------------

# Desempeño 23
# Leer dos listas de 15 números cada una. Calcular la suma de cada lista y mostrar cuál tiene mayor suma, o si son iguales.
total_L1 = 0
total_L2 = 0
x  = 1

print("lista uno")

while x <= 15:
    valores_lista1 = int(input("ingresar numeros de la lista uno: "))
    total_L1 += valores_lista1 # eso es lo mismo que: total_L1 = total_L1 + valores_lista1
    x+=1


print("lista dos")

x = 1

while x <= 15:
    valores_lista2 = int(input("ingresar numeros de la lista dos: "))
    total_L2 +=valores_lista2 # eso es lo mismo que: total_L2 = total_L2 + valores_lista2
    x+=1



if total_L1 > total_L2:
    print("lista uno mayor")
else:
    if total_L1 < total_L2:
        print("lista dos mayor")
    else:
        print("las listas son iguales")
        
#version alternativa usando listas (no lo vimos en clases todavia, 
# solo lo hice para practicar un poco)
#--------------------------------------------------------#
# # Leer la primera lista de 15 números                  #
print("Ingrese 15 números para la primera lista:")       #
lista1 = []                                              #
for i in range(15):                                      #
    num = float(input(f"Ingrese el número {i+1}: "))     #
    lista1.append(num)                                   #
                                                         #
# Leer la segunda lista de 15 números                    #
print("\nIngrese 15 números para la segunda lista:")     #
lista2 = []                                              #   
for i in range(15):                                      #               
    num = float(input(f"Ingrese el número {i+1}: "))     #
    lista2.append(num)                                   #   
                                                         # 
# Calcular sumas                                         #
suma1 = sum(lista1)                                      #               
suma2 = sum(lista2)                                      #   
                                                         #
# Comparar y mostrar resultados                          #
print(f"\nSuma de la lista 1: {suma1}")                  #
print(f"Suma de la lista 2: {suma2}")                    #
                                                         #   
                                                         #
if suma1 > suma2:                                        #
    print("La primera lista tiene mayor suma")           #
elif suma2 > suma1:                                      #
    print("La segunda lista tiene mayor suma")           #
else:                                                    #   
    print("Ambas listas tienen sumas iguales")           #
                                                         #           
#--------------------------------------------------------#

# Desempeño 24
# Leer una cantidad n de números enteros. Contar cuántos son pares y cuántos impares. Mostrar ambas cantidades.

cant = int(input("ingresar cantidad de numeros: "))
contador = 0

cant_pares = 0
cant_impares = 0

while contador < cant:
    num = int(input("ingresar numero: "))
    contador += 1
    
    if num % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1
        
print("cantidad de pares:", cant_pares)
print("cantidad de impares:", cant_impares)
print("fin del programa")