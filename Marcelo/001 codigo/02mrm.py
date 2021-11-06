"""Ejercicio 2                             
a pasar de un entero a un string se utiliza el método str(). Realice un programa con 
Tkinter que tome dos valores uno entero y el otro un string, concatene ambos como un 
string y presente el resultado en pantalla                                                """
from tkinter import * 
root = Tk() 
e = Entry(root) 
e.pack() 
e.focus_set() 
#---------------------------
a = "5" 
b = 2 
c = a + str(b) #paso a string b
#---------------------------
var = IntVar() 
e.config(textvariable=var) 
var.set("concatenacion "+c) #agrego la palabra para saber luego de que se trata ya que es muy parecido al anterior
 
mainloop() 