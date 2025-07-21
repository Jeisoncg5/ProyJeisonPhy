#  Jeison Leonardo Cristancho Garcia
#  Ejercicios Taller
#  19/07/2025
#  Hacer Ejercicios del taller y ecxplicar cada uno de ellos
##  Ejercicio 7:  Verificar si una palabra es un palíndromo


palabra = input("Escribe una palabra: ").lower()   # Solicita al usuario una palabra y la convierte a minúsculas para una comparación uniforme
invertida = palabra[::-1]                          # Invierte la palabra usando slicing

if palabra == invertida:                           # Compara la palabra original con la invertida
    print("La palabra es un palíndromo.")          # Mensaje si la palabra es un palíndromo
else:  
    print("La palabra no es un palíndromo.")        # Mensaje si la palabra no es un palíndromo


# la función slicing [::-1] se utiliza para invertir la cadena de texto
# La comparación se hace entre la palabra original y la invertida para determinar si es un palíndromo
# El resultado se imprime en función de la comparación