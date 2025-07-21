#  Jeison Leonardo Cristancho Garcia
#  Ejercicios Taller
#  19/07/2025
#  Hacer Ejercicios del taller y ecxplicar cada uno de ellos
##  Ejercicio 1: Contar caracteres y espacios en una frase


 
frase = input("Escribe una frase: ")  # Solicita al usuario que ingrese una frase
total_caracteres = len(frase) # Calcula el número total de caracteres en la frase (Cada letra, espacio y símbolo cuenta como un carácter)
espacios = frase.count(" ") # Cuenta el número de espacios en la frase

print(f"La frase tiene {total_caracteres} caracteres en total.")  # Imprime el número total de caracteres
print(f"La frase tiene {espacios} espacios.") # Imprime el número de espacios en la frase

# la función len() se utiliza para contar el número total de caracteres en la frase, incluyendo letras, espacios y símbolos
# la función count() se utiliza para contar el número de espacios en la frase

