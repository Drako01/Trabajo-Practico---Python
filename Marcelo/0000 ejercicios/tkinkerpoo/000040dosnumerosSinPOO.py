"""Confeccionar un programa que permita ingresar dos números en controles 
de tipo Entry, luego sumar los dos valores ingresados y mostrar la suma 
en una Label al presionar un botón."""
#es el mismo ejemplo pero sin POO es lineal

import tkinter as tk

def sumar():
    suma=int(dato1.get()) + int(dato2.get())
    label3.configure(text=suma)

ventana1=tk.Tk()
ventana1.title("sumar")
label1=tk.Label(ventana1,text="Ingrese primer valor:")
label1.grid(column=0, row=0)
dato1=tk.StringVar()
entry1=tk.Entry(ventana1, width=20, textvariable=dato1)
entry1.grid(column=1, row=0)
label2=tk.Label(text="Ingrese segundo valor:")
label2.grid(column=0, row=1)
dato2=tk.StringVar()
entry2=tk.Entry(ventana1, width=20, textvariable=dato2)
entry2.grid(column=1, row=1)
boton1=tk.Button(ventana1, text="Sumar", command=sumar)
boton1.grid(column=1, row=2)
label3=tk.Label(ventana1,text="resultado")
label3.grid(column=1, row=3)
ventana1.mainloop()

