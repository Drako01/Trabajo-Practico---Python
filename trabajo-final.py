
print("Hola mundo")
print(2)


print("Hola mundo")

print("Hola a Todos")

print(12112)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 15:47:56 2021
todo tkinter explicado paso a paso lo que voy entendiendo
@author: maromans
"""


#IMPORTO TKINTER QUE VIENE POR DEFECTO
import tkinter



#DEFINICION DE FUNCIONES
"""las funciones se colocan siempre despues del llamado de los modulos por lo que estuve viendo"""
def prueba():
    print("esta es la funcion prueba")



"""PROGRAMA PROPIAMENTE DICHO"""
#Hola a todos




#ARRANCO DEFINIENDO LAS CLASES DE OBJETOS QUE VAMOS A USAR
#DEFINO UNA CLASE(capaz que es objeto) DENTRO DE TKINTER


#LO MAS GENERAL ES DECIR DONDE VAN ESTAR LAS COSAS ES VENTANA

ventana = tkinter.Tk()# clase dentro del modulo tkinter y le aplico el metodo tk creo

#ALGUNAS COSAS MANEJABLES EN LA VENTANA

ventana.geometry("400x500")#tamaño inicial de ventana
ventana.resizable(width=False,height=False)#habilito que solo se pueda cambiar en un sentido la ventana


"""DEFINIMOS UN ELEMENTO QUE VAN A ESTAR DENTRO DE LA VENTANA QUE PODRIA SER LA ETIQUETA, BOTON CAJA DE TEXTO ETC ETC"""


#ETIQUETA
etiqueta = tkinter.Label(ventana, text ="esto es una prueba", bg = "red" )# PARA QUE LA ETIQUETA SEA ETIQUETA EL METODO ES LABEL

"""a la etiqueta le paso un argumento texto para ponerlo en pantalla y defino el color de fondo en rojo"""


#BOTON
boton1 = tkinter.Button (ventana, text = "aprete aca",  bg = "red" , command =prueba)




#CAJA DE TEXTO



#METODO DE COLOCACION POR GRILLA





#POSISIONADO LAS COSAS EN LA PANTALLA
""" este que sigue es un metodo de posicionamiento PACK hay otros GRID """
boton1.pack()
etiqueta.pack()
"""este metodo posiciona la etiqueta en pantalla centro arriba acepta otros parametros lo que esta entre los parentesis, va entre los parentesis
(side=tkinter,RIGHT) por ejemplo lo pone a la derecha etc /BOTH/LEFT/UP
(fill = tkinter.X) estira en eje x la etiqueta /X/Y  (ojo en el caso de usarlo al y se debe agregar , expand = true)
"""
"""DEFINIENDO BOTONES"""
ventana.mainloop()
# esto mantiene la ventana corriendo y registra todo lo que le pasa

