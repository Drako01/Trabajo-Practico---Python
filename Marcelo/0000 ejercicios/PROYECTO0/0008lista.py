"""14 - Estructura de datos tipo lista

 
Hasta ahora hemos trabajado con variables que permiten almacenar un único valor:

edad=12
altura=1.79
nombre="juan"
En Python existe un tipo de variable que permite almacenar una colección de datos y luego acceder por medio de un subíndice (similar a los string)

Creación de la lista por asignación
Para crear una lista por asignación debemos indicar sus elementos encerrados entre corchetes y separados por coma.
"""
lista1=[10, 5, 3]                       # lista de enteros
lista2=[1.78, 2.66, 1.55, 89,4]         # lista de valores float
lista3=["lunes", "martes", "miercoles"] # lista de string
lista4=["juan", 45, 1.92]               # lista con elementos de distinto tipo
"""Si queremos conocer la cantidad de elementos de una lista podemos llamar a la función len:
"""
lista1=[10, 5, 3]   # lista de enteros
print(len(lista1))  # imprime un 3
"""Problema 1:
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

Programa: ejercicio69.py

Ver video
"""
lista=[10,7,3,7,2]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("Los elementos de la lista son")
print(lista)
print("La suma de todos sus elementos es")    
print(suma)
"""   
lista python con valores por asignacion

Primero definimos una lista por asignación con 5 elementos:

lista=[10,7,3,7,2]
Definimos un acumulador para sumar los elementos de la lista y un contador para indicar que posición de la lista accedemos:

suma=0
x=0
Mediante un ciclo while recorremos y sumamos cada elementos de la lista:

while x<len(lista):
    suma=suma+lista[x]
    x=x+1
Cuando llamamos a la función print pasando como dato una lista luego se muestra en pantalla todos los elementos de la lista entre corchetes y separados por coma tal cual como la definimos:

print("Los elementos de la lista son")
print(lista)
Finalmente mostramos el acumulador:

print("La suma de todos sus elementos es")    
print(suma)    
Problema 2:
Definir una lista por asignación que almacene los nombres de los primeros cuatro meses de año. Mostrar el primer y último elemento de la lista solamente.

Programa: ejercicio70.py

Ver video
"""
meses=["enero", "febrero", "marzo", "abril"]
print(meses[0]) # se muestra enero
print(meses[3]) # se muestra abril
"""Como queremos imprimir solo el primer y último elemento de la lista indicamos entre corchetes la posición de la lista del cual queremos rescatar el valor.

Si llamamos a print y pasamos solo el nombre de la lista luego se nos muestra todos los elementos:

print(meses) # se muestra ["enero", "febrero", "marzo", "abril"]
Problema 3:
Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.

Programa: ejercicio71.py

Ver video
"""
lista=["ana", 7, 9]
print("Nombre del alumno:")
print(lista[0])
promedio=(lista[1]+lista[2])//2
print("Promedio de sus dos notas:")
print(promedio)
"""Como vemos en este problema los elementos de una lista pueden ser de distinto tipo, aquí tenemos el primer elemento de tipo string y los dos siguientes de tipo int.

Recordemos que el operador // se utiliza para dividir dos valores y retornar solo la parte entera.

Problemas propuestos
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.
Ver video

Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
Ver video

Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.
Ver video"""
#ejercicio72.py

lista=[1000, 6000, 400, 23, 130, 400, 60, 2000]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1
    
print("La lista esta constituida por los elementos:")
print(lista)
print("La cantidad de valores mayores a 100 en la lista son:")
print(cantidad)




#ejercicio73.py

lista=[8,1,9,2,10]
x=0
print("Elementos de la lista con valores iguales o superiores a 7")
while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1




#ejercicio74.py

nombres=["juan", "ana", "marcos", "carlos", "luis"]
cantidad=0
x=0
while x<len(nombres):
    if len(nombres[x])>=5:
        cantidad=cantidad+1
    x=x+1

print("Todos los nombres son")
print(nombres)
print("Cantidad de nombres con 5 o mas caracteres")
print(cantidad)