#DESEMPEÑOS DE LA SEMANA 2 (ESTRUCTURAS CONDICIONALES)
#=====================================================

# Desempeño 9

# a. Leer tres números enteros e imprimir el mayor.

num1 = int(input("ingresar numero"))
num2 = int(input("ingresar numero"))
num3 = int(input("ingresar numero"))

if num1 > num2 and num1 > num3:
           
    print("num1 es mas grande")
           
elif num2 > num3:
    
    print("num2 es mas grande")
    
else:
    print("num3 es mas grande")




        
# b. Pedir un número entero e informar si es cero, positivo o negativo.

num= int(input("ingresar un numero"))

if num == 0:         
  print("es cero")
         
elif num < 0:  
  print("es negativo")
  
else:
  print("es positivo")




# c. Leer un número entero positivo de hasta tres cifras e informar cuántos dígitos tiene.
#    Si tiene más de tres dígitos, mostrar un mensaje de error.


num = int(input("ingresar valor de hasta 3 digitos"))

if num < 10:
    print("tiene un digito")
elif num < 100:
    print("tiene dos digitos")
elif num < 1000:
    print("tiene 3 digitos")
else:
    print("ERROR: fuera de nivel")





# d. Ingresar cantidad total de preguntas de un examen y cantidad correctas.
#    Calcular el porcentaje y mostrar el nivel:
#    - 90% o más: Nivel máximo
#    - 75% a 89%: Nivel medio
#    - 50% a 74%: Nivel regular
#    - Menos de 50%: Fuera de nivel


total_preguntas = int(input("ingresar la cantidad de preguntas: "))
total_correctas = int(input("ingresar cantidad de preguntas correctas: "))

porcent = total_correctas * 100 / total_preguntas #con eso sacamos el porcentaje!

if porcent >= 90:
    print("Nivel máximo")
    
elif porcent >= 75:                   #elif porcent >= 75 or porcent <= 89:
    print("Nivel médio")
    
elif porcent >= 50:
    print("nivel regular")
    
else:
    print ("fuera de nivel")




# Desempeño 10
# Leer día, mes y año. Mostrar si la fecha corresponde al 25 de diciembre (Navidad).

dd = int(input("igresar día"))
mm = int(input("igresar mes"))
aa = int(input("igresar anio"))

if dd > 0 and dd <= 31:
    if mm >0 and mm <= 12:
        if mm == 12 and dd == 25:
            print("es navidad")
        else:
            print("no es navidad")
    else:
        print("no existe el mes", mm)
else:
    print("ESO NO EXISTE BRO!!!")

    


# Desempeño 11
# Leer tres números. Si son iguales, sumar el primero y el segundo, luego
# multiplicar el resultado por el tercero. Mostrar ambos resultados.

num1 = int(input("ingresar numero"))#control C + control V 
num2 = int(input("ingresar numero"))
num3 = int(input("ingresar numero"))

if num1 == num2 and num1  == num3:
        suma = num1 + num2
        print("La suma del primero y segundo:")
        print(suma)

        producto = suma * num3
        print("La suma del primero y segundo multiplicado por el tercero:")
        print(producto)
else:
    print("los numeros no son iguales")
    


# Desempeño 12
# Leer tres números enteros. Informar si todos son menores que 10.
num1 = int(input("ingresar numero"))#control C + control V 
num2 = int(input("ingresar numero"))
num3 = int(input("ingresar numero"))

if num1 < 10 and num2 < 10 and num3 < 10:
    print("todos los numeros son menores que 10")
else:
    print("ERROR")




# Desempeño 13
# Leer tres números enteros. Informar si alguno es menor que 10.

num1 = int(input("ingresar numero"))#control C + control V 
num2 = int(input("ingresar numero"))
num3 = int(input("ingresar numero"))

if num1 < 10 or  num2 < 10 or num3 < 10:
    print("todos los numeros son menores que 10")
else:
    print("ERROR")


    
# Desempeño 14
# Leer dos números (coordenadas x e y). Mostrar en qué cuadrante del plano cartesiano se encuentran.

x = int(input("ingresar coordenada x:"))
y = int(input("ingresar coordenada y:"))

if x > 0 and y > 0:
    print("primer cuadrante")
else:
    if x < 0 and y > 0:
        print("segundo cuadrante")
    else:
        if x <0 and y < 0:
            print("tercer cuadrante")
        else:
            print("cuarto cuadrante")




# Desempeño 15
# Leer sueldo y antigüedad. Si el sueldo < 500 y antigüedad > 10, aumentar 20%.
# Si sueldo < 500 y antigüedad <= 10, aumentar 5%.
# Si no, no hay aumento. Mostrar sueldo final.

sueldo = float(input("ingresar sueldo del empleado"))
antiguedad = int(input("ingresar antiguedad del empleado"))

#Si el sueldo < 500 y antigüedad > 10, aumentar 20%.
if sueldo < 500 and antiguedad > 10:
    aumento = sueldo * 0.20
    sueldo_total = sueldo + aumento
    print("sueldo a pagar:")
    print(sueldo_total)
else:
    if sueldo < 500 and antiguedad <= 10:
        aumento = sueldo * 0.05
        sueldo_total = sueldo + aumento
        print("sueldo a pagar:")
        print(sueldo_total)
    else:
        sueldo_total = sueldo
        print("sueldo a pagar:")
        print(sueldo_total)

# Desempeño 16
# Leer tres números enteros. Mostrar el menor y luego el mayor de los tres.

num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: '))
num3=int(input('Ingrese el tercer numero: '))

if num1<num2 and num2<num3:
    print('El Primer numero es menor, y el tercero es el mayor')
else:
    if num1>num2 and num1<num3:
        print('El Segundo numero es menor y el tercero es el mayor')
    else:
        if num3<num2 and num2<num1:
            print('El Tercer numero es el menor y el primero es el mayor')
        else:
            if num3>num2 and num2<num1:
                print('El Segundo numero es el menor y el primero es el mayor')
            else:
                if num1<num3 and num3<num2:
                    print('El Primer numero es el menor y el segundo es mayor')
                else:
                    print('El Tercer numero es el menor y el segundo es el mayor')





















































