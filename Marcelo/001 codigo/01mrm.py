"""Ejercicio 1                             
Para pasar de un string a un número entero se utiliza el método int(), como se muestra a 
Realice un programa con Tkinter que tome dos valores, uno entero y el otro un string, 
realice la suma como enteros y lo presente en pantalla.                                                       """

from tkinter import * 
root = Tk() 
e = Entry(root) 
e.pack() 
e.focus_set() 
#---------------------------
a = 6 
b = "2" 
c = a *int(b)# transformo a b en entero
#---------------------------
var = IntVar() 
e.config(textvariable=var) 
var.set(c) 
 
mainloop() 