## Calculo de la Hipotenusa
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021

from math import sqrt

print ("Bienvenidos a la Trigonometria")
a = float (input("Ingrese el Valor del Cateto A: "))
b = float (input("Ingrese el Valor del Cateto B: "))

c = sqrt (a ** 2 + b ** 2)

print("El Cateto A mide : ", a,"y", "el Cateto B mide: ", b)
print ("Por lo Tanto el Valor de la Hipotenusa es: {}".format(c))