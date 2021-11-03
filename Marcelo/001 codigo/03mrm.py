"""importando la libreria random
import random
"""
#importacion de librerias
import random

from tkinter import * 
root = Tk() 
e = Entry(root) 
e.pack() 
e.focus_set() 
#---------------------------
a = 6 
b = random.randrange(0,100) # utiliza 3 parametros start stop step IGUAL POR LO  VEO TAMBIEN ANDA CON 1 Y CON 2 PARAMETROS
c = a * b 
"""por lo que observo un metodo es como un
subprograma que necesita de parametros que
irian despues del punto para una cualidad
en particular(RANGO intervalo) de ese metodo 
en este caso.
V.g "generar numeros aleatorios entre 1 y 100"
lo que no comprendo es que haria el 3 parametro step
lo que observe es que SOLO DA PARES PORQUE?"""
#---------------------------
var = IntVar() 
e.config(textvariable=var) 
var.set(c) 
 
mainloop() 
