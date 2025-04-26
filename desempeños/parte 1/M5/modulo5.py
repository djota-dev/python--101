# Desempeño 35
#Realizar la carga de dos nombres de personas distintos.
# Mostrar por pantalla luego ordenados en forma alfabética.

nombre1=input("Ingrese el primer nombre")
nombre2=input("Ingrese el segundo nombre")
print("Listado alfabetico")
if nombre1<nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)
    
#Desempeño 36
#Cargar una oración por teclado. Mostrar luego cuantos espacios en 
# blanco se ingresaron. Tené en cuenta que un espacio en blanco es 
# igual a ‘ ’, en cambio una cadena vacía es "."

oracion=input("Ingese una oracion")
cantidad=0
x=0
while x<len(oracion):
    if oracion[x]==" ":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de espacios en blanco ingresado son")
print(cantidad)


#Desempeño 37
#Ingresar una oración que puede tener letras tanto en mayúsculas como 
# minúsculas. Contar la cantidad de vocales. Crear un segundo string con
# toda la oración en minúsculas para que sea más fácil disponer la condición
# que verifica que es una vocal.


oracion=input("Ingrese una oracion")
oracionmin=oracion.lower()
cantidad=0
x=0
while x<len(oracionmin):
    if oracionmin[x]=="a" or oracionmin[x]=="e" or oracionmin[x]=="i" or oracionmin[x]=="o" or oracionmin[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de vocales de la oracion son")
print(cantidad)


#Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de
# caracteres. Controlá que el string ingresado tenga entre 10 y 20 caracteres
# para que sea válido, en caso contrario mostrar un mensaje de error."

clave=input("Ingrese una clave que tenga entre 10 y 20 caracteres:")
if len(clave)>=10 and len(clave)<=20:
    print("Largo correcto")
else:
    print("Largo incorrecto")