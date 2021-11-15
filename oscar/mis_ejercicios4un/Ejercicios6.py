"""
Ejercicio 6 (Dificultad media)
Escriba un programa que pida la fecha según el formato 04/12/1973 
y lo retorne según el formato 1973/12/04
"""


fecha = input("Ingrese la fecha, con formato aaaa/mm/dd: ")
print(f"Nuevo formato {fecha[8:]}/{fecha[5:7]}/{fecha[:4]}")
