#EJERCIO 7 3
"""
Ejercicio 7.3 USE TK
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

#importacion de librerias
import tkinter as tk #libreria de ventana
from tkinter import ttk #libreria de escritura

#definicion de objetos
ventana=tk.Tk()

#definicion variable y constantes
dic={"identificador":"documento","nombre":"marcelo","apellido":"mansilla","telefono":"02215025764"}
kEys= " ".join(dic.keys())
vAlues= " ".join(dic.values())
lOngi=len(dic)

#titulo de la ventana
ventana.title("EJERCICIO 7.3 diccionario EN TK")
#tamaño de la ventana
#ventana.resizable ( height=400,weight= 1000)
# L A B E L S etiquetas
ttk.Label(ventana,text=kEys).grid(column=0,row=0)#inserto la variable
ttk.Label(ventana,text=vAlues).grid(column=0,row=1)#inserto la variable
ttk.Label(ventana,text=lOngi).grid(column=0,row=2)#inserto la variable
#activar ventana
ventana.mainloop()


""" DICCIONARIO nos permite buscar por clave o por valor """
""" LISTA nos permite iterar con ella sin conocer nada de la misma porque tiene lugares o casillas"""
""" LA LOGICA ME DICE QUE UNO SON MEJORES PARA UNAS COSAS
 Y OTROS MEJORES PARA OTRAS, Y SI LOS DOS ESTAN SERA:
PORQUE ALGO SE DEBE PODER HACER CON UNO QUE CON EL OTRO NO Y BICEVERSA"""
