from tkinter import *
import random

#Creamos la ventana
root = Tk()
root.title("Desafio")
root.geometry("300x200")
# Creamos las variables para tomar por entry
titulo = StringVar()
ruta = StringVar()
descrip = StringVar()
# Creamos las funciones
def imprimir():
    print(titulo.get()+" "+ruta.get()+" "+descrip.get())

def cambiarFondo():
    colores = ["blue","yellow","red","browm","black","pink","white","green","grey","cyan"]
    coloresAleatorios = random.choice(colores)
    root.config(background=coloresAleatorios)
# Creamos las etiquetas
etiqueta1 = Label(root, text="Título")
etiqueta1.grid(row=0, column=0)
etiqueta2 = Label(root, text="Ruta")
etiqueta2.grid(row=1, column=0)
etiqueta3= Label(root, text="Descripción")
etiqueta3.grid(row=2, column=0)
# Creamos las entrys
entrada1 = Entry(root, textvariable=titulo)
entrada1.grid(row=0, column=1)
entrada2 = Entry(root,textvariable=ruta)
entrada2.grid(row=1, column=1)
entrada3 = Entry(root, textvariable=descrip)
entrada3.grid(row=2, column=1)
#Creamos los botones de accion vinclados a las funciones
boton1 = Button(root, text="Alta", command=imprimir)
boton1.grid(row=3, column=1)
boton2 = Button(root, text="Sorpresa", command=cambiarFondo)
boton2.grid(row=3, column=2)

mainloop()