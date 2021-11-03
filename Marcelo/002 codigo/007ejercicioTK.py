#ejercicio 007
#ejercicio 1

"""TRABAJOS A PRESENTAR EN EL FORO"""
"""Ejercicio 1 

Cree  una  lista de frutas  de  7 elementos,  
y  realice  un  programa que  muestre  el  tercer 
elemento de la lista en pantalla
"""
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
print (lista[3])


#ejercicio 2

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



#ejercicio 3
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
