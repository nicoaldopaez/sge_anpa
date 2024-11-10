### PR0401: Ejercicios básicos en Python
## 1. Lectura de un número válido:Crea un programa que solicite un número por pantalla al usuario y siga pidiéndolo hasta que el usuario introduzca un número válido.
'''
	n=int(input("Introduce un numero n"))

k=int(input("Introuce un numero k"))

c=1
while c<=k:
    resultado = n*c
    print(n*c)
    c += 1
'''
## 2. Tabla de multiplicar
Crea un programa que solicite un número n y un valor k y que muestre por la terminal los primeros k elementos de la tabla de multiplicar de n.
'''
	n = int(input("Introduce n: "))
k = int(input("Introduce k "))
for linea in range(k):
    resultado = n * linea
    print(str(n)+"*"+str(linea)+" = "+str(resultado))
'''
## 3. Triángulo de asteriscos
Crea un programa que solicite un número al usuario y dibuje un triángulo con asteriscos cuya base sea el número introducido.
'''
	base = int(input("introduce un numero"))
while(base % 2 == 0):
    print("Debes introducir un número impar")
    base = int(input("introduce un número impar"))
for i in range(1,base+1,2):
    espacios = (base-i)//2
    print(" "*espacios+ "*" * i)
'''
## 4. Pirámide de asteriscos
Modifica el programa anterior para que en lugar de crear un triángulo cree una pirámide. Si el usuario introduce un número par se lo volverá a pedir hasta que introduzca un número par.
'''
	base = int(input("Introduce un número impar: "))
while base % 2 == 0:
    print("Debes introducir un número impar.")
    base = int(input("Introduce un número impar: "))
for i in range(1, base + 1, 2):
    espacios = (base - i) // 2
    print(" " * espacios + "*" * i + " " * espacios)
'''
## 5. Número mayor y menor
Crea un programa que pida al usuario que introduzca 5 números y luego le diga cuál es el mayor y el menor de todos ellos de la forma: El número mayor es <mayor> y el menor es <menor>.
'''
	import math

mayor=-math.inf
menor=math.inf
for a in range(5):
    numero=int(input("introduce un número"))
    if(numero > mayor):
        mayor = numero
    if(numero<menor):
        menor = numero
print("el mayor número es: ")
print(mayor)
print("el menor número es:")
print(menor)
'''
## 7. 7. Acierta el número
Crea un programa que genere un número aleatorio entre 0 y 100 y el usuario tenga que adivinarlo. Cada vez que el usuario introduzca un número el programa le dirá si el número es más alto o más bajo.

Para generar un número aleatorio puedes utilizar la función randint(a, b) que devuelve un entero aleatorio entre a y b. Para poder utilizar esta función antes tienes que importar la librería con la orden from random import *
'''
	import random
aleatorio = random.randint(0, 100)
intento = int(input("Adivina el número"))
while(intento != aleatorio):
    if (intento > aleatorio):
        print("Mas bajo")
    elif(intento < aleatorio):
        print("Mas alto")
    intento = int(input("Adivina el número"))
print("Has adivinado el número")
'''