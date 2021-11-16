"""
Ejercicio 2 (Dificultad alta)
Escribir un programa que permita ingresar un número y calcule el factorial
"""
numero = int(input("Ingrese un numero entero mayor a 0: "))


def factorial(num):
    if num >= 1:
        return num * factorial(num - 1)
    else:
        return 1


print(factorial(numero))
