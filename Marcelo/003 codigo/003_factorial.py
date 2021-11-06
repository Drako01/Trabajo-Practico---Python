"""Cree un script que permita calcular el factorial 
de un número, intente utilizar funciones o un 
bucle for/in. """
print (" VAMOS A HACER UN FACTORIAL BUCLE FOR")
aFactor = int(input("ingrese un numero positivo y entero "))
if aFactor >0:
    a=1
    for x in range(aFactor,0,-1):
        a=a*x
    print(f" el Factorial de {aFactor} es {a}")
else:
    print(" el numero ingresado es incorrecto ")
