#ejercicio 007
#ejercicio 1
"""TRABAJOS A PRESENTAR EN EL FORO"""
"""Ejercicio 007-1 USE TK 

Cree  una  lista de frutas  de  7 elementos,  
y  realice  un  programa que  muestre  el  tercer 
elemento de la lista en pantalla
"""
#importacion de librerias
import tkinter as tk #libreria de ventana
from tkinter import ttk #libreria de escritura
#definicion de objetos
ventana=tk.Tk()
#definicion variable y constantes
lista=["cero","uno","dos","tres","cuatro","cinco","seis","siete"]
a=(lista[3])
#titulo de la ventana
ventana.title("EJERCICIO 7.1 EN TK")
#tamaño de la ventana
#ventana.resizable ( height=400,weight= 1000)
# L A B E L S etiquetas
ttk.Label(ventana,text=a).grid(column=0,row=1)#inserto la variable
#activar ventana
ventana.mainloop()

