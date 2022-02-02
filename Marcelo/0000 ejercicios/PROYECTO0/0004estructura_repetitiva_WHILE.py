#while
"""
Estructura repetitiva while

 
Hasta ahora hemos empleado estructuras SECUENCIALES y CONDICIONALES. Existe otro tipo de estructuras tan importantes como las anteriores que son las estructuras REPETITIVAS.

Una estructura repetitiva permite ejecutar una instrucción o un conjunto de instrucciones varias veces.

Una estructura repetitiva se caracteriza por:
- La sentencia o las sentencias que se repiten.
- El test o prueba de condición antes de cada repetición, que motivará que se repitan o no las instrucciones."""

#escribir los numeros del 1 al 100
x=1
while x<=100:
    print(x)
    x=x+1
#concepto de acumulador y de contador

x=1
suma=0
while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("La suma de los 10 valores es")
print(suma)
print("El promedio es")
print(promedio)

"""
Problemas propuestos
Ha llegado la parte fundamental, que es el momento donde uno desarrolla individualmente un algoritmo para la resolución de problemas.

El tiempo a dedicar a esta sección EJERCICIOS PROPUESTOS debe ser mucho mayor que el empleado a la sección de EJERCICIOS RESUELTOS.
La experiencia dice que debemos dedicar el 80% del tiempo a la resolución individual de problemas y el otro 20% al análisis y codificación de problemas ya resueltos por otras personas.
Es de vital importancia para llegar a ser un buen PROGRAMADOR poder resolver problemas en forma individual.

Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
Ver video

Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
Ver video

En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
Ver video

Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)
Ver video

Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
Ver video

Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
Ver video

Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
	if valor%2==0:         
Ver video
"""
#ejercicio32.py

x=1
conta1=0
conta2=0
while x<=10:
    nota=int(input("Ingrese nota:"))
    if nota>=7:
        conta1=conta1+1
    else:
        conta2=conta2+1
    x=x+1
print("Cantidad de alumnos con notas mayores o iguales a 7")
print(conta1)
print("Cantidad de alumons con notas menores a 7")
print(conta2)




#ejercicio33.py

n=int(input("Cuantas personas hay:"))
x=1
suma=0
while x<=n:
    altura=float(input("Ingrese la altura:"))
    suma=suma+altura
    x=x+1
promedio=suma/n
print("Altura promedio")
print(promedio)




#ejercicio34.py

n=int(input("Cuantos empleados tiene la empresa:"))
x=1
conta1=0
conta2=0
gastos=0
while x<=n:
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    if sueldo<=300:
        conta1=conta1+1
    else:
        conta2=conta2+1
    gastos=gastos+sueldo
    x=x+1
print("Cantidad de empleados con sueldos entre 100 y 300")
print(conta1)
print("Cantidad de empleados con sueldos mayor a 300")
print(conta2)
print("Gastos total de la empresa en sueldos")
print(gastos)




#ejercicio35.py

x=1
termino=11
while x<=25:
    print(termino)
    x=x+1
    termino=termino+11




#ejercicio36.py

mult8=8
while mult8<=500:
    print(mult8)
    mult8=mult8+8




#ejercicio37.py

x=1
suma1=0
suma2=0
print("primer lista")
while x<=15:
    valor=int(input("Ingrese valor:"))
    suma1=suma1+valor
    x=x+1
print("Segunda lista")
x = 1
while x<=15:
    valor=int(input("Ingrese valor:"))
    suma2=suma2+valor
    x=x+1
if suma1>suma2:
    print("Lista 1 mayor.")
else:
    if suma2>suma1:
        print("Lista2 mayor.")
    else:
        print("Listas iguales.")




#ejercicio38.py

x=1
pares=0
impares=0
n=int(input("Cuantos números ingresará:"))
while x<=n:
    valor=int(input("Ingrese el valor:"))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print("Cantadad de pares")
print(pares)
print("Cantidad de impares")
print(impares)

