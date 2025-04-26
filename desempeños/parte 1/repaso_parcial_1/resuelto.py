# ---------------------------------------------------
# EJERCICIOS CON WHILE (Estructuras básicas)
# ---------------------------------------------------

# 1. Suma de múltiplos de 5 menores a 50
print("\n** Ejercicio 1: Suma de múltiplos de 5 menores a 50 **")
suma_multiplos = 0
multiplo_actual = 5

while multiplo_actual < 50:
    suma_multiplos += multiplo_actual
    multiplo_actual += 5
print("Resultado:", suma_multiplos)

# 2. Suma de múltiplos de 5 hasta un límite ingresado
print("\n** Ejercicio 2: Suma de múltiplos con límite personalizado **")
limite_superior = int(input("Ingrese el límite superior: "))
suma_multiplos = 0
multiplo_actual = 5

while multiplo_actual < limite_superior:
    suma_multiplos += multiplo_actual
    multiplo_actual += 5
print(f"Suma hasta {limite_superior}: {suma_multiplos}")

# 3. Tabla de multiplicar del 7
print("\n** Ejercicio 3: Tabla del 7 **")
tabla_del = 7
multiplicador = 1

while multiplicador <= 10:
    print(f"{tabla_del} x {multiplicador} = {tabla_del * multiplicador}")
    multiplicador += 1

# 4. Tabla de multiplicar personalizada
print("\n** Ejercicio 4: Tabla personalizada **")
numero_tabla = int(input("Ingrese el número para la tabla: "))
limite_tabla = int(input("Ingrese el límite: "))
multiplicador = 1

while multiplicador <= limite_tabla:
    print(f"{numero_tabla} x {multiplicador} = {numero_tabla * multiplicador}")
    multiplicador += 1

# 5. Suma y cantidad de pares en un rango

print("\n** Ejercicio 5: Pares en rango **")
inicio_rango = int(input("Ingrese el primer número: "))
fin_rango = int(input("Ingrese el segundo número: "))
if inicio_rango > fin_rango:
    inicio_rango, fin_rango = fin_rango, inicio_rango  # Ajuste de orden

suma_pares = 0
contador_pares = 0

numero_actual = inicio_rango
while numero_actual <= fin_rango:
    if numero_actual % 2 == 0:
        suma_pares += numero_actual
        contador_pares += 1
    numero_actual += 1
print(f"Suma: {suma_pares}, Cantidad: {contador_pares}")

# 6. Validación de edad (5-100 años)
print("\n** Ejercicio 6: Validación de edad **")
edad_usuario = int(input("Ingrese edad (5-100): "))

while edad_usuario < 5 or edad_usuario > 100:
    edad_usuario = int(input("Inválida. Ingrese edad (5-100): "))
print("Edad válida:", edad_usuario)

# 7. Sumatoria hasta ingresar 0
print("\n** Ejercicio 7: Sumatoria hasta 0 **")
suma_total = 0
numero_ingresado = int(input("Ingrese número (0 para terminar): "))

while numero_ingresado != 0:
    suma_total += numero_ingresado
    numero_ingresado = int(input("Ingrese otro número (0 para terminar): "))
print("Sumatoria total:", suma_total)

# 8. Sumatoria de positivos hasta 0
print("\n** Ejercicio 8: Suma de positivos **")
suma_positivos = 0
numero_ingresado = int(input("Ingrese número (0 para terminar): "))

while numero_ingresado != 0:
    if numero_ingresado > 0:
        suma_positivos += numero_ingresado
   # numero_ingresado = int(input("Ingrese otro número (0 para terminar): "))
print("Suma de positivos:", suma_positivos)




# 9. Mayor número hasta ingresar 0
print("\n** Ejercicio 9: Mayor número ingresado **")
mayor_numero = 0
numero_ingresado = int(input("Ingrese número positivo (0 para terminar): "))

while numero_ingresado != 0:
    if numero_ingresado > mayor_numero:
        mayor_numero = numero_ingresado
    numero_ingresado = int(input("Ingrese otro número (0 para terminar): "))
print("Mayor número:", mayor_numero)

# 10. Suma de dígitos de un número
print("\n** Ejercicio 10: Suma de dígitos **")
numero_original = int(input("Ingrese un número positivo: "))
suma_digitos = 0
copia_numero = numero_original
while copia_numero > 0:
    digito = copia_numero % 10
    suma_digitos += digito
    copia_numero = copia_numero // 10
print(f"Suma de dígitos de {numero_original}: {suma_digitos}")

# 11. Suma de dígitos y conteo de pares (hasta -1)
print("\n** Ejercicio 11: Suma de dígitos y pares **")
contador_pares = 0
numero_ingresado = int(input("Ingrese número (-1 para terminar): "))
while numero_ingresado != -1:
    # Suma de dígitos
    suma_digitos = 0
    temp = abs(numero_ingresado)
    while temp > 0:
        suma_digitos += temp % 10
        temp = temp // 10
    print(f"Suma de dígitos: {suma_digitos}")
    
    # Conteo de pares
    if numero_ingresado % 2 == 0:
        contador_pares += 1
    
    numero_ingresado = int(input("Ingrese otro número (-1 para terminar): "))
print("Total números pares:", contador_pares)

# 12. Menú interactivo
print("\n** Ejercicio 12: Menú interactivo **")
opcion_seleccionada = ""
while opcion_seleccionada != "3":
    print("\n--- Menú ---")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")
    opcion_seleccionada = input("Elija una opción: ")
    
    if opcion_seleccionada == "1":
        print("Ejecutando programa...")
    elif opcion_seleccionada == "2":
        print("Listado:\n- Item 1\n- Item 2\n- Item 3")
    elif opcion_seleccionada == "3":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")

# 13. Total de compras con descuento
print("\n** Ejercicio 13: Total de compras **")
total_compras = 0.0
monto_ingresado = float(input("Ingrese monto (0 para terminar): "))

while monto_ingresado != 0:
    if monto_ingresado > 0:
        total_compras += monto_ingresado
    else:
        print("Error: Ingrese monto positivo.")
    monto_ingresado = float(input("Ingrese otro monto (0 para terminar): "))

if total_compras > 1000:
    total_compras *= 0.9  # 10% de descuento
    print("¡Descuento aplicado!")
print(f"Total a pagar: ${total_compras:.2f}")

# 14. Conteo de dígitos pares/impares
print("\n** Ejercicio 14: Dígitos pares/impares **")
total_pares = 0
total_impares = 0
numero_ingresado = int(input("Ingrese número positivo (0 para terminar): "))

while numero_ingresado != 0:
    if numero_ingresado > 0:
        pares_en_numero = 0
        impares_en_numero = 0
        temp = numero_ingresado
        while temp > 0:
            digito = temp % 10
            if digito % 2 == 0:
                pares_en_numero += 1
            else:
                impares_en_numero += 1
            temp = temp // 10
        total_pares += pares_en_numero
        total_impares += impares_en_numero
        
        print(f"Número {numero_ingresado}: {pares_en_numero} par(es), {impares_en_numero} impar(es)")
    numero_ingresado = int(input("Ingrese otro número (0 para terminar): "))
print(f"\nTotal dígitos pares: {total_pares}, impares: {total_impares}")

# ---------------------------------------------------
# EJERCICIOS SIN WHILE (Condicionales y operaciones)
# ---------------------------------------------------

# 1. Incremento salarial para profesores
print("\n** Ejercicio 1 (sin while): Incremento salarial **")
salario_profesor = float(input("Ingrese salario del profesor: "))
if salario_profesor <= 100000:
    nuevo_salario = salario_profesor * 1.12
elif salario_profesor <= 120000:
    nuevo_salario = salario_profesor * 1.08
elif salario_profesor <= 150000:
    nuevo_salario = salario_profesor * 1.07
else:
    nuevo_salario = salario_profesor * 1.06
print(f"Nuevo salario: ${nuevo_salario:.2f}")

# 2. Verificar si un número es divisor de otro
print("\n** Ejercicio 2 (sin while): Divisor **")
numero_a = int(input("Ingrese primer número: "))
numero_b = int(input("Ingrese segundo número: "))
if numero_a % numero_b == 0:
    print(f"{numero_b} es divisor de {numero_a}")
elif numero_b % numero_a == 0:
    print(f"{numero_a} es divisor de {numero_b}")
else:
    print("No son divisores entre sí")

# 3. Verificar si tres números están en orden creciente
print("\n** Ejercicio 3 (sin while): Orden creciente **")
num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
num3 = int(input("Ingrese tercer número: "))
if num1 < num2 < num3:
    print("Están en orden creciente")
else:
    print("NO están en orden creciente")

print("\n--- Todos los ejercicios completados ---")