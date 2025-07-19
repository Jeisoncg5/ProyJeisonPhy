# Jeison Cristancho Garcia
# Proyecto: Gestion de la Liga Betplay
# Fecha: 2025-17-07
# LigaBetplay ###
# Hacer un programa que permita gestionar la Liga Betplay,
# permitiendo registrar equipos, fechas, marcadores, goles a favor y en contra,
# y planteles de los equipos. El programa debe tener un menú que permita
# seleccionar las diferentes opciones de gestión.
""" 
    1. Registrar Equipo                          #Global
    2. Registrar Fecha                           #Global
    3. Registrar Marcador                        #Fecha
    4. Registrar Equipo con Mas Goles Contra     #Equipo
    5. Registrar Equipo con Mas Goles A Favor    #Equipo
    6. Registrar Plantel                         #Equipo
    7. Salir
"""

import os
from tabulate import tabulate

equipos = []
fechas = []



def agregarEquipo():                       #Funcion para registrar un equipo
    global equipos
    nombreEquipo = input("Ingrese el nombre del equipo que desea agregar: ").strip()
    if not nombreEquipo:
        print("Error: El nombre del equipo no puede estar vacío.")
    elif nombreEquipo in [e[0] for e in equipos]:
        print("Error: El equipo ya está registrado.")
    else:
        equipos.append([nombreEquipo, 0, 0, 0, 0, 0, 0, 0, jugador, plantel])  # Añade el equipo con estadísticas iniciales
                      # [nombre,    pj, pg, pe, pp, gf, gc, pts]
        print(f"¡Equipo '{nombreEquipo}' registrado con éxito!")

def agregarFecha():                     #Funcion para programar una fecha
    global equipos, fechas
    if len(equipos) < 2:               # Verificar si hay al menos dos equipos registrados
        print("Necesitas al menos dos equipos registrados para programar una fecha.")
        return
    print ("Equipos registrados:")
    for nombreEquipo in equipos:         # Mostrar los equipos registrados
        print(f"- {nombreEquipo[0]}")
    local = input("Ingrese el equipo Local: ")
    visitante = input("Ingrese el equipo visitante: ")
    if local not in [e[0] for e in equipos] or visitante not in [e[0] for e in equipos]:
        print("Error: Uno o ambos equipos no están registrados.")
    elif local == visitante:
        print("Error: Un equipo no puede jugar contra sí mismo.")
    else:
        seleccion = [local, visitante, None, None]  # [local, visitante, golLocal, golVisitante]
        fechas.append(seleccion)
        print(f"Partido '{local} vs {visitante}' programado.")


def agregarMarcador():                          #Funcion para registrar el marcador de un partido
    global equipos, fechas
    print("Partidos programados:")
    if not fechas:
        print("No hay partidos programados.")
        return

    for i in range(len(fechas)):
        local, visitante, golLocal, golVisitante = fechas[i]
        print(f"{i + 1}. {local} vs {visitante} - Marcador: {golLocal if golLocal is not None else '_'} : {golVisitante if golVisitante is not None else '_'}")

    try:
        seleccion = int(input("Seleccione el número del partido a registrar: "))
        if seleccion < 1 or seleccion > len(fechas):
            print("Selección inválida.")
            return

        golLocal = int(input("Ingrese los goles del equipo local: "))
        golVisitante = int(input("Ingrese los goles del equipo visitante: "))
        if golLocal < 0 or golVisitante < 0:
            print("Error: Los goles no pueden ser negativos.")
            return

        fechas[seleccion - 1][2] = golLocal
        fechas[seleccion - 1][3] = golVisitante                   # Actualizar los goles en la lista
        print("Marcador actualizado correctamente.")

        local, visitante = fechas[seleccion-1][0], fechas[seleccion-1][1]  # Actualizar estadísticas de los equipos
        for equipo in equipos:  # Busca el equipo local y visitante en la lista de equipos y actualiza sus estadísticas
            if equipo[0] == local: # Busca el equipo local en la lista de equipos
                equipo[1] += 1  # PJ  Sunma 1 partido jugado al equipo local
                equipo[5] += golLocal  # GF sunma los goles a favor del equipo local
                equipo[6] += golVisitante  # GC suma los goles en contra del equipo local
                if golLocal > golVisitante:
                    equipo[2] += 1  # PG suma 1 partido ganado al equipo local
                    equipo[7] += 3  # PTS suma 3 puntos al equipo local
                elif golLocal == golVisitante: # PE suma 1 partido empatado al equipo local
                    equipo[3] += 1  # PE suma 1 partido empatado al equipo local
                    equipo[7] += 1 # PTS suma 1 punto al equipo local
                else:
                    equipo[4] += 1  # PP  Partido perdido por parte de local                         #Busca el equipo local y visitante en la lista de equipos y actualiza sus estadísticas

            if equipo[0] == visitante:  # Busca el equipo visitante en la lista de equipos
                equipo[1] += 1  # PJ suma 1 partido jugado al equipo visitante
                equipo[5] += golVisitante  # GF suma los goles a favor del equipo visitante
                equipo[6] += golLocal  # GC suma los goles en contra del equipo visitante
                if golVisitante > golLocal:
                    equipo[2] += 1  # PG suma 1 partido ganado al equipo visitante
                    equipo[7] += 3  # PTS suma 3 puntos al equipo visitante
                elif golVisitante == golLocal: 
                    equipo[3] += 1  # PE suma 1 partido empatado al equipo visitante
                    equipo[7] += 1
                else:
                    equipo[4] += 1  # PP suma 1 partido perdido al equipo visitante

    except ValueError:
        print("Entrada inválida.")    


def equipoMasGolesFavor():  # Función para mostrar el equipo con más goles a favor
    global equipos
    if not equipos:
        print("No hay equipos registrados.")
        return

    maxgolFavor = -1
    mejorEquipo = None

    for equipo in equipos:   # Recorre la lista de equipos
        if len(equipo) >= 6:  # Asegura que tenga al menos hasta GF
            golesFavor = equipo[5]  # Goles a favor del equipo
            if golesFavor > maxgolFavor:  # Compara los goles a favor
                maxgolFavor = golesFavor
                mejorEquipo = equipo  # Guarda toda la fila del equipo

    if mejorEquipo:
        print(f"El equipo con más goles a favor es: {mejorEquipo[0]} ({mejorEquipo[5]} goles).")
    else:
        print("No hay datos de goles a favor disponibles.")

def equipoMasGolesContra():  # Función para mostrar el equipo con más goles en contra
    global equipos
    if not equipos:
        print("No hay equipos registrados.")
        return

    maxgolContra = -1
    peorEquipo = None

    for equipo in equipos:   # Recorre la lista de equipos
        if len(equipo) >= 7:  # Asegura que tenga al menos hasta GC
            golesContra = equipo[6]  # Goles en contra del equipo
            if golesContra > maxgolContra:  # Compara los goles en contra
                maxgolContra = golesContra
                peorEquipo = equipo  # Guarda toda la fila del equipo

    if peorEquipo:
        print(f"El equipo con mas goles en contra es: {peorEquipo[0]} ({peorEquipo[6]} goles).")
    else:
        print("No hay datos de goles en contra disponibles.")

   
def menuBetplay() -> int:               #Funcion para el menu principal de la Liga Betplay (Llamar desde el main)
    os.system('cls' if os.name == 'nt' else 'clear')
    global equipos, fechas
    print("+==============================================================+")
    print("||             Menú de gestión de la Liga Betplay             ||")
    print("+==============================================================+")
    print("1. Registrar Equipo")
    print("2. Programar Fecha")
    print("3. Registrar Marcador")
    print("4. Registrar Equipo con Más Goles A Favor")
    print("5. Registrar Equipo con Más Goles En Contra")
    print("6. Registrar Plantel")
    print("7. Salir")
    header = ["Equipo", "PJ", "PG", "PE", "PP", "GF", "GC", "PTS"]             
    print(tabulate(equipos, header, tablefmt="outline"))                # Imprime la tabla de estadísticas de los equipos (Haciendo uso de la libreria tabulate)
    header = ["Local", "Visitante", "Goles Local", "Goles Visitante"]   # Tabla improvisada para ir mirando como se guardan las listas de fechas
    print(tabulate(fechas, header, tablefmt="outline"))
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 7:
            print("Opción no válida. Intente de nuevo.")
            return menuBetplay()
        return opcion
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return menuBetplay()


def menuPlantel() -> int:   #Funcion para el menu del plantel  (llamar desde el caso 6 del menuBetplay)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("             Registro del Plantel")
    print("1. Registrar Jugador")
    print("2. Registrar Plantel")
    print("3. Salir")
   #print(tabulate(plantel, header, tablefmt="outline"))
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("Opción no válida. Intente de nuevo.")
            return menuPlantel()
        return opcion
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return menuPlantel()

def agregarJugador():
    global jugador
    Jugador = input("Ingrese el Nombre del jugador dorsal y posicion de juego (nombre/dorsal/posicion): ")
    print(f"Jugador registrado: {Jugador}")
    input("Presione Enter para continuar...")
    jugador.append(Jugador)

def agregarPlantel():
    global plantel
    input("Ingrese el Nombre de la persona del equipo tecnico y su cargo (nombre/cargo): ")
    print(f"Persona registrada: {plantel}")
    input("Presione Enter para continuar...")




if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de la Liga Betplay")
        opcion = menuBetplay()
        match opcion:
            case 1:
                agregarEquipo()
            case 2:
                agregarFecha()
            case 3:
                agregarMarcador()
            case 4:
                equipoMasGolesFavor()
            case 5:
                equipoMasGolesContra()
            case 6:
                while True:
                    opcion_plantel = menuPlantel()
                    match opcion_plantel:
                        case 1:
                            agregarJugador()          
                        case 2:
                            agregarPlantel()
                        case 3:
                            break
            case 7:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
        input("\nPresione Enter para continuar...")