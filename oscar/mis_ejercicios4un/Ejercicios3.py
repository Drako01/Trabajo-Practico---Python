""" 
Ejercicio 3 (Dificultad media)
Escribir un programa que permita tomar un número por consola
e imprima los números entre cero 
y el número de menor a mayor separados por coma 
y luego de mayor a menor separado por coma.  

Ejemplo de salida para 5
0, 1, 2, 3, 4, 5
5, 4, 3, 2, 1, 0
 """

num = int(input("Ingrese un numero entero: "))


def ascendente(i):
    for x in range(i + 1):
        yield str(x)


def descendente(i):
    for x in range(i, -1, -1):
        yield str(x)


print(" ".join(ascendente(num)))
print(" ".join(descendente(num)))
