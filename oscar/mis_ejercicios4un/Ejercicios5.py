""" 
Ejercicio 5 (Dificultad alta)
Escriba un programa que tome 5 números cualesquiera
y determine cuales son divisibles por 2.
"""


lista = []
i = 1

while i <= 5:
    lista.append(int(input("Ingrese un numero: ")))
    i = i + 1

for i in lista:
    if i % 2 == 0:
        print(f"El numero {i}, es divisible por 2.")
    else:
        print(f"El numero {i}, no es divisible por 2.")
