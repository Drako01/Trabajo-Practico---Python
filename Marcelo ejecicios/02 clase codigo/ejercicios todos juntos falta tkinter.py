#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:06:15 2021

@author: maromans
unidad 2


Python soporta números enteros, de punto flotante o complejos, básicamente el intérprete actúa como una calculadora, utilizando operadores de forma análoga a como lo haríamos en C, en donde tenemos la posibilidad de utilizar paréntesis para agrupar términos, pero teniendo en cuenta que el uso de paréntesis puede alterar el resultado. Veamos un ejemplo:"""


a="es un string"
print (type(a))




""" no entiendo muy bien cual seria la cuestion de hacer este codigo pero bueno ahi esta hecho y probado"""

valor1 = 5 - 2 *6 
valor2= (5 - 2) *6 
print(valor1) 
print(type(valor1)) 
print(valor2) 
print(type(valor2))


"""STRING para definir un string hay que poner entre comillas un serie de numeros letra o simbolos y son tomados como una variable no se cual seria el tamaño maximo de un string???"""

mi_string="5"

""" los strring son inmutables OJO AL PIOJO"""
""" lo interesante de un string es que lo puedo multiplica sin pasarlo a valor numero en este caso ejemplo """

mi_string="5"
mi_variable=mi_string*5 # que esperan que de 25 no señore no da 25
print (mi_variable)# elemental watson pone la cantidad de veces el 5 que le digamos en este caso le dijimos 5 veces el string 5


""" y si quisieramos multiplicarlo como si fuese un numero"""

#entonces habria que transformar el 5(string) a numero y despues multiplicarlo capishi como se hara esto 

mi_string="5"#este guion bajo me rompe los esquemas

mi_variable=5*(int(mi_string))
print (mi_variable)# que esperan 55555 no esta vez da 25
# asi es como cambia de un tipo a otro de variable



"""TRABAJOS A PRESENTAR EN EL FORO"""
"""Ejercicio 1 

Cree  una  lista de frutas  de  7 elementos,  
y  realice  un  programa que  muestre  el  tercer 
elemento de la lista en pantalla
"""
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3])

""" y si quisiera que mostrara desde el 3 al 7"""
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3:7])# que pasa si ponemos un numero mas grande que el final de la lista un 10 por ejemplo

lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3:10])# no pasa nada nos muestra hasta el que tiene eso es interesante

# y si los quisieramos salteados 
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3:6])# no pasa nada nos muestra hasta el que tiene eso es interesante

"""          
Ejercicio 2 
Para concatenar texto se utiliza el signo + 
Cree una lista de frutas de 2 elementos, y realice un programa con tkinter que muestre 
una oración conteniendo los 
formar una oración con sentido.  
"""

lista=["casa", "alpina"]
concatenar=(lista[0]+" para clima cordillerano "+lista[1])
print(lista)
print(concatenar)

"""
Ejercicio 3
Cree un diccionario con las claves:
· identificador
· nombre
· apellido
· telefono
Nota: al utilizar claves no utilice acentos u otros caracteres en español, por ejemplo no ponga “teléfono” sino “telefono”.
Realice un programa que a partir del diccionario creado retorne en una oración: 1) El número de elementos del diccionario
2) Las claves del diccionario
Pregunta:
¿Cree que para guardar y recuperar información es mejor un diccionario o una lista? Justifique su respuesta.
"""
print ("DICCIONARIO")
dic={"identificador":"documento","nombre":"marcelo","apellido":"mansilla","telefono":"02215025764"}
print (dic.keys())
print (dic.values())
a=len(dic)
print (f"numero de elementos del diccionario {a}")
#print (a) #esta linea la comento porque queda mejor que este en la misma linea
print ("las claves del diccionario son :")
print (dic.keys())
print ("para mi tienen sus ventajas y desventajas y dependeran de lo queramos hacer con ellas")


"""
Ejercicio 4
Para tomar texto por consola se utiliza el comando: input()
Tome un nombre por consola y presente en la pantalla de la consola la oración: Hola nombre bienvenido!
"""
nombre=input("ingrese su nombre:")
print("hola "+ nombre + " bienvenido" )



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


Ejercicio 6
Repita el ejercicio 5 pero en lugar de una lista utilice un diccionario.

sumando1=int(input("ingrese sumando1 "))
sumando2=int(input("ingrese sumando2 "))
resultado=sumando1+sumando2
print (sumando1)
print(sumando2)
print (resultado)

diccionario={"sumando1":sumando1,"sumando2":sumando2,"suma":resultado}

print (diccionario.keys())
print (diccionario.values())
a=len(diccionario)
print (f"numero de elementos del diccionario {a}")

"""
Ejercicio 7 OPCIONAL
Intente realizar los ejercicios 1, 2 y 3 con tkinter.
Nota: No hemos entrado aún a analizar esta interfaz gráfica por lo que NO se solicita que se busque información extra en internet. Solo se está pidiendo presentar los datos en pantalla como se realizo en el ejercicio presentado en la unidad 1
"""
"""   los 3  primero con tkinter """
"""Ejercicio 1 

Cree  una  lista de frutas  de  7 elementos,  
y  realice  un  programa que  muestre  el  tercer 
elemento de la lista en pantalla
"""
from tkinter import * 
root = Tk() 
e = Entry(root) 
e.pack() 
e.focus_set() 
#---------------------------
a = 5 
b = 2 
c = a * b 
#---------------------------
var = IntVar() 
e.config(textvariable=var) 
var.set(c) 
 
mainloop()







lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3])

""" y si quisiera que mostrara desde el 3 al 7"""
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3:7])# que pasa si ponemos un numero mas grande que el final de la lista un 10 por ejemplo

lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3:10])# no pasa nada nos muestra hasta el que tiene eso es interesante

# y si los quisieramos salteados 
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3:6])# no pasa nada nos muestra hasta el que tiene eso es interesante

"""          
Ejercicio 2 
Para concatenar texto se utiliza el signo + 
Cree una lista de frutas de 2 elementos, y realice un programa con tkinter que muestre 
una oración conteniendo los 
formar una oración con sentido.  
"""

lista=["casa", "alpina"]
concatenar=(lista[0]+" para clima cordillerano "+lista[1])
print(lista)
print(concatenar)

"""
Ejercicio 3
Cree un diccionario con las claves:
· identificador
· nombre
· apellido
· telefono
Nota: al utilizar claves no utilice acentos u otros caracteres en español, por ejemplo no ponga “teléfono” sino “telefono”.
Realice un programa que a partir del diccionario creado retorne en una oración: 1) El número de elementos del diccionario
2) Las claves del diccionario
Pregunta:
¿Cree que para guardar y recuperar información es mejor un diccionario o una lista? Justifique su respuesta.
"""
print ("DICCIONARIO")
dic={"identificador":"documento","nombre":"marcelo","apellido":"mansilla","telefono":"02215025764"}
print (dic.keys())
print (dic.values())
a=len(dic)
print (f"numero de elementos del diccionario {a}")
#print (a) #esta linea la comento porque queda mejor que este en la misma linea
print ("las claves del diccionario son :")
print (dic.keys())
print ("para mi tienen sus ventajas y desventajas y dependeran de lo queramos hacer con ellas")

