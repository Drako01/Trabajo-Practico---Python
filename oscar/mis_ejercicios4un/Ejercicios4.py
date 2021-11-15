""" 
Ejercicio 4 (Dificultad alta)
Escriba un programa que permita tomar una palabra,
 retorne las vocales que contenga, junto con la cantidad de veces que se repite. 
 """

frase = input("Ingrese una palabra o texto: ")
frase = frase.lower()
vocales = ["a", "e", "i", "o", "u"]


def programa(item):
    for i in vocales:
        contador = 0
        for e in frase:
            if i == e:
                contador += 1
        yield (f"La vocal: {i}, aparece {contador} veces.")


for x in programa(vocales):
    print(x)
