"""TRABAJOS A PRESENTAR EN EL FORO"""
"""Ejercicio 7.2"""
"""
Ejercicio USE TK
Para concatenar texto se utiliza el signo + 
Cree una lista de frutas de 2 elementos, y realice un programa con tkinter que muestre 
una oración conteniendo los 
formar una oración con sentido.  
"""
#importacion de librerias
import tkinter as tk #libreria de ventana
from tkinter import ttk #libreria de escritura

#definicion de objetos
ventana=tk.Tk()
#definicion variable y constantes
lista=["casa", "alpina"]
concatenar=(lista[0]+" para clima cordillerano "+lista[1])
#titulo de la ventana
ventana.title("EJERCICIO 7.2 EN TK")
#tamaño de la ventana
#ventana.resizable ( height=400,weight= 1000)
# L A B E L S etiquetas
ttk.Label(ventana,text=lista).grid(column=0,row=0)#inserto la variable
ttk.Label(ventana,text=concatenar).grid(column=0,row=1)#inserto la variable
#activar ventana
#vicios propios lo queria ver por la pantalla de terminal tambien
print(lista)
print(concatenar)
ventana.mainloop()


