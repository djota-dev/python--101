# ================================
#  Ejercicios de Variables y Estructuras Secuenciales
# ================================

# 📌 Conceptos Claves
# Una estructura secuencial en Python ejecuta las instrucciones de manera lineal.
# Las variables almacenan valores y pueden ser de distintos tipos: enteros, flotantes, strings, etc.
# Python detecta automáticamente el tipo de variable, pero podemos convertirlo con int(), float(), str(), etc.

# ================================

# 1⃣ Conversión de Temperatura
# Escribe un programa que solicite al usuario una temperatura en grados Celsius 
# y la convierta a Fahrenheit usando la fórmula:
# F = C * (9 / 5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))

# Convertir C a F
F = celsius * (9/5) + 32
print(f"La temperatura en Fahrenheit es: {F:.2f}°F")

# ================================

# 2⃣ Cálculo de Promedio
# Crea un programa que solicite al usuario tres números y calcule el promedio de los mismos.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular promedio
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números es: {promedio:.2f}")

# ================================

# 3⃣ Cálculo del Área de un Círculo
# Escribe un programa que pida el radio de un círculo y calcule su área usando la fórmula:
# Área = π * r^2
# (Usaremos `math.pi` para el valor de π.)

import math

radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área
area = math.pi * (radio ** 2)
print(f"El área del círculo es: {area:.2f}")

# ================================

# 4⃣ Operaciones Básicas con Dos Números
# Escribe un programa que solicite dos números y muestre la suma, resta, 
# multiplicación y división entre ellos.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

division = num1 / num2 if num2 != 0 else "Indefinida"  # Evitar división por cero

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# ================================
#  Ejercicios con if-else + Estructuras Secuenciales
# ================================

# 📌 Tabla de Operadores de Comparación
# | Operador | Ejemplo        | Descripción        |
# |---------|--------------|------------------|
# | ==      | 5 == 5 → True  | Igualdad         |
# | !=      | 5 != 3 → True  | Diferente        |
# | >       | 10 > 5 → True  | Mayor que        |
# | <       | 3 < 8 → True   | Menor que        |
# | >=      | 7 >= 7 → True  | Mayor o igual    |
# | <=      | 2 <= 5 → True  | Menor o igual    |

# 📌 Tabla de Operadores Lógicos
# | Operador | Ejemplo           | Descripción               |
# |---------|----------------|-------------------------|
# | and     | True and False → False | Ambos deben ser True  |
# | or      | True or False  → True  | Al menos uno es True  |
# | not     | not True → False    | Invierte el valor      |

# ================================

# 5⃣ Número Par o Impar
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# ================================

# 6⃣ Clasificación de Edad
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")

# ================================

# 7⃣ Cálculo de Descuento
monto = float(input("Ingrese el valor de la compra: "))
if monto > 100:
    descuento = monto * 0.10
    total = monto - descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
else:
    total = monto
print(f"Total a pagar: ${total:.2f}")

# ================================

# 8⃣ Cálculo del Mayor de Tres Números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num3:
    mayor = num2
else:
    mayor = num3
print(f"El número mayor es: {mayor}")



# ================================
# 💡 Desafío EXTRA:
# ¿QUE HACE EL PROGRAMA?

edad = int(input("Ingrese su edad: "))
ingreso = float(input("Ingrese su ingreso mensual: "))

if edad >= 18:
    if edad > 50 and ingreso >= 5000:
        print("¡Felicidades! Calificas para el préstamo.")
    elif edad <= 50 and ingreso >= 2000:
        print("¡Felicidades! Calificas para el préstamo.")
    else:
        print("Lo sentimos, no cumples con los requisitos.")
else:
    print("Debes ser mayor de 18 años para solicitar un préstamo.")

# ================================
# THE END. 🚀
