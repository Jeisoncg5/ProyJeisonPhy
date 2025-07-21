#  Jeison Leonardo Cristancho Garcia
#  Ejercicios Taller
#  19/07/2025
#  Hacer Ejercicios del taller y ecxplicar cada uno de ellos
#  Ejercicio 2: Validar un nombre completo


nombre = input("Escribe tu nombre completo: ")  # Solicitar al usuario que ingrese su nombre completo

if nombre.replace(" ", "").isalpha():   # Verificar si el nombre contiene solo letras y espacios
    if nombre.istitle():                # Verificar si el nombre comienza con mayúscula
        print("El nombre es válido.")   # Imprimir mensaje de nombre válido
    else:
        print("El nombre debe comenzar con mayúscula.")     # Imprimir mensaje si el nombre no comienza con mayúscula
else:
    print("El nombre solo debe contener letras.")           # Imprimir mensaje si el nombre contiene caracteres no permitidos


#la función replace() se utiliza para eliminar los espacios del nombre antes de verificar si contiene solo letras
#la función isalpha() se utiliza para verificar si el nombre contiene solo letras
#la función istitle() se utiliza para verificar si el nombre comienza con mayúscula