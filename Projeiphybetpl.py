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

equipos = []
fechas = []
jugador = []
plantel = []


def agregarEquipo():
    global equipos
    nombreEquipo = input("Ingrese el nombre del equipo que desea agregar: ").strip()
    if not nombreEquipo:
        print("Error: El nombre del equipo no puede estar vacío.")
    elif nombreEquipo in [e[0] for e in equipos]:
        print("Error: El equipo ya está registrado.")
    else:
        equipos.append([nombreEquipo])
        print(f"¡Equipo '{nombreEquipo}' registrado con éxito!")

def agregarFecha():
    global equipos, fechas
    if len(equipos) < 2:
        print("Necesitas al menos dos equipos registrados para programar una fecha.")
        return
    print ("Equipos registrados:")
    for nombreEquipo in equipos:
        print(f"- {nombreEquipo[0]}")
    local = input("Ingrese el equipo Local: ")
    visitante = input("Ingrese el equipo visitante: ")
    if local not in [e[0] for e in equipos] or visitante not in [e[0] for e in equipos]:
        print("Error: Uno o ambos equipos no están registrados.")
    elif local == visitante:
        print("Error: Un equipo no puede jugar contra sí mismo.")
    else:
        seleccion = [local, visitante, None, None]  # [local, visitante, marcador_local, marcador_visitante]
        fechas.append(seleccion)
        print(f"Partido '{local} vs {visitante}' programado.")



def agregarMarcador():
    global fechas
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


    except ValueError:
        print("Entrada inválida.")    


def equipomasgolesfavor():
    global equipos, fechas
    if not equipos:
        print("No hay equipos registrados.")
        return

    mejor_ataque = None
    max_goles_favor = -1

    for nombreEquipo in equipos:
        if len(nombreEquipo) < 2:
            continue
        goles_favor = nombreEquipo[1]
        if goles_favor > max_goles_favor:
            max_goles_favor = goles_favor
            mejor_ataque = nombreEquipo[0]

    if mejor_ataque:
        print(f"El equipo con más goles a favor es: {mejor_ataque} ({max_goles_favor} goles).")
    else:
        print("No hay datos de goles a favor disponibles.")


#def agregarMarcador():
#    global equipos, fechas
#    print("Partidos programados:")
#    if not fechas:
#        print("No hay partidos programados.")
#        return
#    for i in range(len(fechas)):
#        print(f"{i + 1}. {fechas[i][0]} vs {fechas[i][1]}")
#    golLocal = int(input("Ingrese Los Goles del equipo Local: "))
#    golVisitante = int(input("Ingrese Los Goles del equipo Visitante: "))
#    if golLocal < 0 or golVisitante < 0:
#        print("Error: Los goles no pueden ser negativos.")
#        return  
    
   
def menuBetplay() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("              Menú de gestión de la Liga Betplay")
    print("1. Registrar Equipo")
    print("2. Programar Fecha")
    print("3. Registrar Marcador")
    print("4. Registrar Equipo con Más Goles Contra")
    print("5. Registrar Equipo con Más Goles A Favor")
    print("6. Registrar Plantel")
    print("7. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 7:
            print("Opción no válida. Intente de nuevo.")
            return menuBetplay()
        return opcion
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return menuBetplay()


def menuPlantel() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("             Registro del Plantel")
    print("1. Registrar Jugador")
    print("2. Registrar Plantel")
    print("3. Salir")
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
                print("Registrar Equipo con Más Goles Contra")
            case 5:
                print("Registrar Equipo con Más Goles A Favor")
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