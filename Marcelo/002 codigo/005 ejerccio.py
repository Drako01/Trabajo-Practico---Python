"""
ejercicio numero 5
Para pasar un valor de string a entero se utiliza el comando int(), así:
Int(“2”)
Tome dos valores por consola, y guarde en una lista:
[primer_valor, segundo_valor, la_suma_de_los_valores]
Muestre en pantalla la lista.
"""

#lista=[]# esta demas
a=input("ingrese un primer valor ")
b=input("ingrese un segundo valor ")
lista=[a,b]
suma=int(a)+int(b)
lista.append(suma)
print(lista)