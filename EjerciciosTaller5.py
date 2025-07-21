#  Jeison Leonardo Cristancho Garcia
#  Ejercicios Taller
#  19/07/2025
#  Hacer Ejercicios del taller y ecxplicar cada uno de ellos
##  Ejercicio 5: Contar vocales en una frase



frase = input("Escribe una frase: ")      # Solicita al usuario una frase

a = frase.count("a") + frase.count("A")   # Cuenta las vocales minúsculas y mayúsculas
e = frase.count("e") + frase.count("E")   # Cuenta las vocales minúsculas y mayúsculas
i = frase.count("i") + frase.count("I")   # Cuenta las vocales minúsculas y mayúsculas
o = frase.count("o") + frase.count("O")   # Cuenta las vocales minúsculas y mayúsculas
u = frase.count("u") + frase.count("U")   # Cuenta las vocales minúsculas y mayúsculas

total_vocales = a + e + i + o + u         # Suma el total de vocales

print(f"La frase tiene {total_vocales} vocales.")   # Imprime el total de vocales


# la función count() se utiliza para contar las ocurrencias de cada vocal en la frase