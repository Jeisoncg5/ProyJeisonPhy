### **Ejercicio 1: Contando caracteres**

#### **Instrucción:**

Escribe un programa que solicite al usuario una frase y muestre:

1. La cantidad total de caracteres en la frase.
2. La cantidad de espacios en la frase.

#### **Código base:**

```python
frase = input("Escribe una frase: ")  # Solicita al usuario que ingrese una frase
total_caracteres = len(frase) # Calcula el número total de caracteres en la frase (Cada letra, espacio y símbolo cuenta como un carácter)
espacios = frase.count(" ") # Cuenta el número de espacios en la frase

print(f"La frase tiene {total_caracteres} caracteres en total.")  # Imprime el número total de caracteres
print(f"La frase tiene {espacios} espacios.") # Imprime el número de espacios en la frase

# la función len() se utiliza para contar el número total de caracteres en la frase, incluyendo letras, espacios y símbolos
# la función count() se utiliza para contar el número de espacios en la frase
```

------

- La función len() se puede utilizar en diversos casos para poder contar lo que le pidamos a la función, en este caso le pedimos que cuente la cantidad de letras que hayan en la frase
- Mientras que con la función count() le pedimos que cuente específicamente los espacios





### **Ejercicio 2: Validando nombres**

#### **Instrucción:**

Crea un programa que solicite al usuario su nombre completo y verifique:

1. Que solo contenga letras.
2. Que comience con mayúscula.

#### **Código base:**

```python
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
```

------

- En este caso la función replace() se utiliza para para identificar si contiene solo letras y espacios junto con isalpha() la cual sirve para ver solo las letras
- Con la función istitle() sirve para ver si la primera letra fue escrita con mayuscula





### **Ejercicio 3: Invirtiendo palabras**

#### **Instrucción:**

Escribe un programa que pida al usuario una palabra y muestre la palabra invertida.

#### **Código base:**

```python
palabra = input("Escribe una palabra: ")        # Solicita al usuario una palabra
invertida = palabra[::-1]                       # Invierte la palabra usando slicing
print(f"La palabra invertida es: {invertida}")  # Imprime la palabra invertida

# la función slicing [::-1] se utiliza para invertir la cadena de texto
# El resultado se almacena en la variable 'invertida' y se imprime 
```

------

- En esta situación se usa la función slicing ( [::-1]  ) para hacer que la palabra que se escriba desde el input se reescriba pero invertida
- invertida es donde se almacena la palabra invertida, y se pide que se imprima



### **Ejercicio 4: Cifrando texto**

#### **Instrucción:**

Crea un programa que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*).

#### **Código base:**

```python
frase = input("Escribe una frase: ")                                                                                      # Solicita al usuario una frase

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")           # Reemplaza las vocales minúsculas
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")   # Reemplaza las vocales mayúsculas

print(f"La frase cifrada es: {frase_cifrada}")


# la función replace() se utiliza para reemplazar, en este caso las vocales por asteriscos
```

------

- En este caso usamos replace() que hace que las vocales que se especifican en las paréntesis se cambien por un asterisco

- Para luego invertir la frase o la palabra que se solicito pero ahora con las vocales ya sean mayúsculas o minúsculas por *

### **Ejercicio 5: Contador de vocales**

#### **Instrucción:**

Escribe un programa que cuente cuántas vocales hay en una frase ingresada por el usuario.



#### **Código base:**

```python
frase = input("Escribe una frase: ")      # Solicita al usuario una frase

a = frase.count("a") + frase.count("A")   # Cuenta las vocales minúsculas y mayúsculas
e = frase.count("e") + frase.count("E")   # Cuenta las vocales minúsculas y mayúsculas
i = frase.count("i") + frase.count("I")   # Cuenta las vocales minúsculas y mayúsculas
o = frase.count("o") + frase.count("O")   # Cuenta las vocales minúsculas y mayúsculas
u = frase.count("u") + frase.count("U")   # Cuenta las vocales minúsculas y mayúsculas

total_vocales = a + e + i + o + u         # Suma el total de vocales

print(f"La frase tiene {total_vocales} vocales.")   # Imprime el total de vocales


# la función count() se utiliza para contar las ocurrencias de cada vocal en la frase
```

------

- Eb este ejercicio se usa la función count() la cual cuenta la cantidad de vocales en este caso y que imprima cuantas vocales tiene la frase o palabra al final



### **Ejercicio 6: Formateando cadenas**

#### **Instrucción:**

Escribe un programa que tome un número de teléfono ingresado por el usuario (10 dígitos) y lo formatee como `(XXX) XXX-XXXX`.

#### **Código base:**

```python
telefono = input("Escribe un número de teléfono de 10 dígitos: ")            # Solicita al usuario un número de teléfono de 10 dígitos
if len(telefono) == 10 and telefono.isdigit():                               # Verifica que el número tenga exactamente 10 dígitos y sea numérico
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}" # Formatea el número en el estilo (XXX) XXX-XXXX
    print(f"El número formateado es: {telefono_formateado}")                 # Imprime el número formateado
else:
    print("El número debe tener exactamente 10 dígitos.")                    # Mensaje de error si el número no es válido



# la función isdigit() se utiliza para verificar que la cadena contenga solo dígitos
# La función len() se utiliza para verificar conn el == 10 la longitud de la cadena

#f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}  Esta parte recoge [:3][3:6][6:] lo que significa que en un ejemplo si el número es 1234567890, [:3] recogerá los primeros 3 dígitos, [3:6] recogerá los siguientes 3 dígitos y [6:] recogerá el resto de la cadena.
```

------

- En este ejercicio hacemos uso de la función len() la cual en este caso pide que teléfono la cual es una variable que se pida por medio de un input lea que sea igual a 10 numero si es así procede a isdigit() la cual verifica si lo que se escribió son números 
- Luego de eso se formatea el número en el estilo (XXX) XXX-XXXX

### **Ejercicio 7: Detectando palíndromos**

#### **Instrucción:**

Escribe un programa que determine si una palabra ingresada por el usuario es un palíndromo (se lee igual al derecho y al revés).

#### **Código base:**

```python
palabra = input("Escribe una palabra: ").lower()   # Solicita al usuario una palabra y la convierte a minúsculas para una comparación uniforme
invertida = palabra[::-1]                          # Invierte la palabra usando slicing

if palabra == invertida:                           # Compara la palabra original con la invertida
    print("La palabra es un palíndromo.")          # Mensaje si la palabra es un palíndromo
else:  
    print("La palabra no es un palíndromo.")        # Mensaje si la palabra no es un palíndromo


# la función slicing [::-1] se utiliza para invertir la cadena de texto
# La comparación se hace entre la palabra original y la invertida para determinar si es un palíndromo
# El resultado se imprime en función de la comparación
```

- En este ejercicio hacemos uso de la función slicing [::-1]  la cual ya vimos anteriormente para invertir la palabra que se solicita por medio del input para comparar la palabra que se escribió y luego el resultado del slicing. if palabra == invertida: esto significa que si la palabra escrita es igual al resultado de la palabra invertida que imprima que es un palíndromo(palabra que al invertirse se lee igual que la palabra original)