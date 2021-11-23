"""
Ejercicio 3
Crear una función lambda que tome como parámetro una frase y la escriba al revés. 
"""

frase = input("Ingrese una frase: ")

esarf = lambda valor: "".join(reversed(valor))  # Otra opcion seria valor [::-1]

print(esarf(frase))
