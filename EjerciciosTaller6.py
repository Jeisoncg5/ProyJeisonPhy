#  Jeison Leonardo Cristancho Garcia
#  Ejercicios Taller
#  19/07/2025
#  Hacer Ejercicios del taller y ecxplicar cada uno de ellos
##  Ejercicio 6: Formatear un número de teléfono


telefono = input("Escribe un número de teléfono de 10 dígitos: ")            # Solicita al usuario un número de teléfono de 10 dígitos
if len(telefono) == 10 and telefono.isdigit():                               # Verifica que el número tenga exactamente 10 dígitos y sea numérico
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}" # Formatea el número en el estilo (XXX) XXX-XXXX
    print(f"El número formateado es: {telefono_formateado}")                 # Imprime el número formateado
else:
    print("El número debe tener exactamente 10 dígitos.")                    # Mensaje de error si el número no es válido



# la función isdigit() se utiliza para verificar que la cadena contenga solo dígitos
# La función len() se utiliza para verificar conn el == 10 la longitud de la cadena

#f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}  Esta parte recoge [:3][3:6][6:] lo que significa que en un ejemplo si el número es 1234567890, [:3] recogerá los primeros 3 dígitos, [3:6] recogerá los siguientes 3 dígitos y [6:] recogerá el resto de la cadena.