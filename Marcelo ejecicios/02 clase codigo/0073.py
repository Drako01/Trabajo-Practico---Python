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
