# LigaBetplay
# Hacer un programa que permita gestionar la Liga Betplay,
# permitiendo registrar equipos, fechas, marcadores, goles a favor y en contra,
# y planteles de los equipos. El programa debe tener un menú que permita
# seleccionar las diferentes opciones de gestión.
""" 
    1. Registrar Equipo
    2. Registrar Fecha
    3. Registrar Marcador
    4. Registrar Equipo con Mas Goles Contra
    5. Registrar Equipo con Mas Goles A Favor
    6. Registrar Plantel
    7. Salir
"""

import os

equipos = []
fechas = []



def agregarEquipo():
    global equipos
    equipo = input("Ingrese el nombre del equipo que desea agregar: ")
    print(f"Equipo '{equipo}' agregado correctamente.")
    equipos.append(([equipo]))
    print(f"Equipos registrados: {equipos}")
    input("Presione Enter para continuar...")


def agregarFecha():
    global equipos
    fecha = input("Ingrese la fecha del partido (DD/MM/AAAA): ")
    print(f"Fecha '{fecha}' registrada correctamente.")
    fechas.append(fecha)
    print(f"Fechas registradas: {fechas}")
    input("Presione Enter para continuar...")

def agregarMarcador():
    marcadorLo = input("Ingrese el Equipo Local: ")
    print(f"Marcador '{marcadorLo}' registrado correctamente.")
    



def menuBetplay() -> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menú de gestión de la Liga Betplay")
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




if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de alumnos")
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
                menuPlantel()
            case 7:
                print("Saliendo del sistema. ¡Hasta luego!")
                break