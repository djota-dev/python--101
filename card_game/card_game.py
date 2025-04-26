import random
"""Se mezclan las cartas

Cada alumno recibe 2 cartas iniciales

Por turnos, cada alumno decide si tomar más cartas

Si un alumno se pasa de 21 puntos, queda eliminado

Al final se determina el ganador (mayor puntaje sin pasarse de 21)"""



# Lista de alumnos (diccionarios)
alumnos = [
    {"nombre": "Juan", "cartas": [], "puntaje": 0, "activo": True},
    {"nombre": "María", "cartas": [], "puntaje": 0, "activo": True},
    {"nombre": "Pedro", "cartas": [], "puntaje": 0, "activo": True},
    {"nombre": "Ana", "cartas": [], "puntaje": 0, "activo": True}
]

# Mazo de cartas (diccionarios)
cartas = [
    {"nombre": "As", "valor": 11, "palo": "Corazones"},
    {"nombre": "2", "valor": 2, "palo": "Corazones"},
    {"nombre": "3", "valor": 3, "palo": "Corazones"},
    {"nombre": "4", "valor": 4, "palo": "Corazones"},
    {"nombre": "5", "valor": 5, "palo": "Corazones"},
    {"nombre": "6", "valor": 6, "palo": "Corazones"},
    {"nombre": "7", "valor": 7, "palo": "Corazones"},
    {"nombre": "8", "valor": 8, "palo": "Corazones"},
    {"nombre": "9", "valor": 9, "palo": "Corazones"},
    {"nombre": "10", "valor": 10, "palo": "Corazones"},
    {"nombre": "Jota", "valor": 10, "palo": "Corazones"},
    {"nombre": "Reina", "valor": 10, "palo": "Corazones"},
    {"nombre": "Rey", "valor": 10, "palo": "Corazones"},
    # Podríamos añadir más palos pero por simplicidad usaremos solo uno
]

def mezclar_cartas():
    #Mezcla el mazo de cartas aleatoriamente
    random.shuffle(cartas)
    print("El mazo ha sido mezclado.")
    
    return cartas

def repartir_carta(alumno):
    #Reparte una carta a un alumno
    
    if cartas:
        carta = cartas.pop()
        alumno["cartas"].append(carta)
        alumno["puntaje"] = calcular_puntaje(alumno["cartas"])
        print(f"{alumno['nombre']} recibe: {carta['nombre']} de {carta['palo']}")
    else:
        print("No hay más cartas en el mazo.")

def calcular_puntaje(mano):
    #Calcula el puntaje total de una mano de cartas
    total = sum(carta["valor"] for carta in mano)
    #me volé un poquito xD
    num_ases = sum(1 for carta in mano if carta["nombre"] == "As")
    
    while total > 21 and num_ases:
        total -= 10
        num_ases -= 1
    
    return total

def comparar_cartas(c1, c2):
    #Compara dos cartas y devuelve la de mayor valor
    if c1["valor"] > c2["valor"]:
        return c1
    elif c2["valor"] > c1["valor"]:
        return c2
    else:
        return None  # Empate


def tomar_carta(alumno):
    #Un alumno toma una carta del mazo (no sé si falta algo aquí)!!!!
    repartir_carta(alumno)


def devolver_carta(alumno, indice):
    #Devuelve una carta al mazo
    if 0 <= indice < len(alumno["cartas"]):
        carta_devuelta = alumno["cartas"].pop(indice)
        cartas.append(carta_devuelta)
        
        alumno["puntaje"] = calcular_puntaje(alumno["cartas"])
        print(f"{alumno['nombre']} devuelve: {carta_devuelta['nombre']} de {carta_devuelta['palo']}")
    else:
        print("Índice de carta inválido.")

def tirar_carta(alumno, indice):
    #Tira una carta (la elimina del juego)
    if 0 <= indice < len(alumno["cartas"]):
        carta_tirada = alumno["cartas"].pop(indice)
        alumno["puntaje"] = calcular_puntaje(alumno["cartas"])
        print(f"{alumno['nombre']} tira: {carta_tirada['nombre']} de {carta_tirada['palo']}")
    else:
        print("Índice de carta inválido.")

def verificar_ganador(): #me volé otra vez acá xD2
    #Verifico si hay un ganador y muestra mensaje
    activos = [alumno for alumno in alumnos if alumno["activo"]]
    
    if not activos:
        print("No hay ganadores, todos han sido eliminados.")
        return None
    
    # Encontrar el puntaje más alto sin pasarse de 21
    max_puntaje = 0
    ganadores = []
    
    for alumno in activos:
        if alumno["puntaje"] <= 21 and alumno["puntaje"] >= max_puntaje:
            if alumno["puntaje"] > max_puntaje:
                max_puntaje = alumno["puntaje"]
                ganadores = [alumno]
            else:
                ganadores.append(alumno)
    
    if not ganadores:
        print("No hay ganadores, todos se pasaron de 21.")
    elif len(ganadores) == 1:
        print(f"¡El ganador es {ganadores[0]['nombre']} con {ganadores[0]['puntaje']} puntos!")
    else:
        nombres = ", ".join(alumno['nombre'] for alumno in ganadores)
        print(f"¡Empate entre {nombres} con {max_puntaje} puntos cada uno!")
    
    return ganadores

def mostrar_estado():
    #Muestra el estado actual del juego
    print("\n--- ESTADO DEL JUEGO ---")
    for alumno in alumnos:
        estado = "ACTIVO" if alumno["activo"] else "ELIMINADO"
        cartas_str = ", ".join(f"{c['nombre']} de {c['palo']}" for c in alumno["cartas"])
        print(f"{alumno['nombre']} ({estado}): {cartas_str} | Puntaje: {alumno['puntaje']}")
    print("-----------------------\n")


#====================programa principal===================#

def jugar():
    mezclar_cartas()
    
#repartimos 2 cartas a cada alumno

    for _ in range(2):
        for alumno in alumnos:
            repartir_carta(alumno)
    
    mostrar_estado()
    
    # Turnos de los alumnos
    for alumno in alumnos:
        print(f"\nTurno de {alumno['nombre']}")
        while True:
            decision = input("¿Quieres tomar otra carta? (s/n): ").lower()
            if decision == 's':
                tomar_carta(alumno)
                mostrar_estado()
                if alumno["puntaje"] > 21:
                    print(f"{alumno['nombre']} se ha pasado de 21 y queda eliminado!")
                    alumno["activo"] = False
                    break
            else:
                break
    
    # Determinar ganador
    verificar_ganador()

# Iniciar el juego
if __name__ == "__main__":
    jugar()