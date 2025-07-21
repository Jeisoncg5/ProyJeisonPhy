#  Jeison Leonardo Cristancho Garcia
#  Ejercicios Taller
#  19/07/2025
#  Hacer Ejercicios del taller y ecxplicar cada uno de ellos
##  Ejercicio 4: Cifrar una frase reemplazando vocales por asteriscos


frase = input("Escribe una frase: ")                                                                                      # Solicita al usuario una frase

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")           # Reemplaza las vocales minúsculas
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")   # Reemplaza las vocales mayúsculas

print(f"La frase cifrada es: {frase_cifrada}")


# la función replace() se utiliza para reemplazar, en este caso las vocales por asteriscos
