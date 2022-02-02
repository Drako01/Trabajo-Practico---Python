"""10 - Estructura repetitiva for

 
Cualquier problema que requiera una estructura repetitiva se puede resolver empleando la estructura while, pero hay otra estructura repetitiva cuyo planteo es más sencillo en ciertas situaciones que tenemos que recorrer una lista de datos.

En general, la estructura repetitiva for se usa en aquellas situaciones en las cuales queremos que una variable vaya tomando un valor de una lista definida de valores.

Veremos con una serie de ejemplos el empleo del for.
  range(inicio,fin,incremento)  """
for x in range(101):
    print(x)
"""La función range puede tener también tres parámetros, el primero indica el valor inicial que tomará la variable x, el segundo parámetro el valor final (que no se incluye) y el tercer parámetro indica cuanto se incrementa cada vuelta x."""

for x in range(1,100,2):
    print(x)
"""Problemas propuestos
Ha llegado nuevamente la parte fundamental, que es el momento donde uno desarrolla individualmente un algoritmo para la resolución de un problema.

Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie. 
b) La cantidad de triángulos cuya superficie es mayor a 12.
Ver video

Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
Ver video

Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)
Ver video

Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.
Ver video

Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
Ver video

Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
Ver video

Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
Ver video

Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
Ver video

"""

#ejercicio47.py

n=int(input("Cuantos triángulos procesará:"))
cantidad=0
for x in range(n):
    basetri=int(input("Ingrese el valor de la base:"))
    altura=int(input("Ingrese el valor de la altura:"))
    superficie=basetri*altura/2
    print("La superficie es")
    print(superficie)
    if superficie>12:
        cantidad=cantidad+1
print("La cantidad de triángulos con superficie superior a 12 son")
print(cantidad)




#ejercicio48.py

suma=0
for f in range(10):
    valor=int(input("Ingrese un valor:"))
    if f>4:
        suma=suma+valor
print("La suma de los últimos 5 valores es")
print(suma)




#ejercicio49.py

for f in range(5,51,5):
    print(f)




#ejercicio50.py

valor=int(input("Ingrese un valor entre 1 y 10:"))
for f in range(1,13):
    tabla=valor*f
    print(tabla)




#ejercicio51.py

cant1=0
cant2=0
cant3=0
n=int(input("Ingrese la cantidad de triángulos:"))
for f in range(n):
    lado1=int(input("Ingrese lado 1:"))
    lado2=int(input("Ingrese lado 2:"))
    lado3=int(input("Ingrese lado 3:"))
    if lado1==lado2 and lado1==lado3:
        print("Es un triángulo equilatero.")
        cant1=cant1+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Es un triángulo isósceles.")
            cant2=cant2+1
        else:
            print("Es un triángulo escaleno.")
            cant3=cant3+1

print("Cantidad de triángulos equilateros:")
print(cant1)
print("Cantidad de triángulos isósceles:")
print(cant2)
print("Cantidad de triángulos escalenos:")
print(cant3)




#ejercicio52.py

cant1=0
cant2=0
cant3=0
cant4=0
n=int(input("Cantidad de puntos:"))
for f in range(n):
    x=int(input("Ingrese coordenada x:"))
    y=int(input("Ingrese coordenada y:"))
    if x>0 and y>0:
        cant1=cant1+1
    else:
        if x<0 and y>0:
            cant2=cant2+1
        else:
            if x<0 and y<0:
                cant3=cant3+1
            else:
                if x>0 and y<0:
                    cant4=cant4+1

print("Cantidad de puntos en el primer cuadrante:")
print(cant1)
print("Cantidad de puntos en el segundo cuadrante:")
print(cant2)
print("Cantidad de puntos en el tercer cuadrante:")
print(cant3)
print("Cantidad de puntos en el cuarto cuadrante:")
print(cant4)




#ejercicio53.py

negativos=0
positivos=0
mult15=0
sumapares=0
for f in range(10):
    valor=int(input("Ingrese valor:"))
    if valor<0:
        negativos=negativos+1
    else:
        if valor>0:
            positivos=positivos+1
    if valor%15==0:
        mult15=mult15+1
    if valor%2==0:
        sumapares=sumapares+valor

print("Cantidad de valores negativos:")
print(negativos)
print("Cantidad de valores positivos:")
print(positivos)
print("Cantidad de valores múltiplos de 15:")
print(mult15)
print("Suma de los valores pares:")
print(sumapares)




#ejercicio54.py

suma1=0
suma2=0
suma3=0

for f in range(5):
    edad=int(input("Ingrese edad:"))
    suma1=suma1+edad
pro1=suma1/5
print("Promedio de edades del turno mañana:")
print(pro1)

for f in range(6):
    edad=int(input("Ingrese edad:"))
    suma2=suma2+edad
pro2=suma2/6
print("Promedio de edades del turno tarde:")
print(pro2)

for f in range(11):
    edad=int(input("Ingrese edad:"))
    suma3=suma3+edad
pro3=suma3/11
print("Promedio de edades del turno noche:")
print(pro3)
if pro1<pro2 and pro1<pro3:
    print("El turno mañana tiene un promedio menor de edades.")
else:
    if pro2<pro3:
        print("El turno tarde tiene un promedio menor de edades.")
    else:
        print("El turno noche tiene un promedio menor de edades.")
