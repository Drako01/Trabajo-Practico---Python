""" 
EJERCICIO ADICIONAL

Modifique el ejercicio desafío de la unidad 3, para que los parámetros sean
pasados a la función que imprime los datos en pantalla, mediante una función
lambda agregada al botón


EJERCICIO DESAFIO (NIVEL DE DIFICULTAD MUY ALTO)

En la siguiente unidad vamos a comenzar a trabajar con bases de datos, para ir
ingresando en el tema, realice un trabajo de investigación sobre el tipo de
base shelve de python e intente realizar un alta de registro y consulta de
registro a partir de la aplicación desafío de la unidad 3.  
"""

import random
from tkinter import *
from tkinter import ttk
import shelve


root = Tk()
root.title("Peliculas")
root.geometry("700x350")
root.resizable(0, 0)

# creacion de la base de datos
tabla = shelve.open("Peliculas")


fondo = "cyan2"
fondo2 = "cyan3"
colores = [
    "lime green",
    "ivory2",
    "LightSteelBlue1",
    "CadetBlue2",
    "DarkSeaGreen2",
    "OliveDrab2",
    "cyan2",
    "Khaki1",
    "tan2",
    "orchid3",
    "SpringGreen2",
]
letra = "Tahoma 10"
titulo = StringVar()
año = StringVar()
director = StringVar()
ingreso = StringVar()


titulo.set("...")
año.set("...")
director.set("...")

# quice definir sorpresa como:
# def sorpresa ():
#     fondo = random.choice(colores)
#     fondo2 = random.choice(colores)
# "pero no funciono el boton"
def sorpresa():
    root.config(background=random.choice(colores))
    etiqueta1.config(background=random.choice(colores))
    etiqueta2.config(background=random.choice(colores))
    etiqueta3.config(background=random.choice(colores))
    etiqueta4.config(background=random.choice(colores))
    boton1.config(background=random.choice(colores))
    boton2.config(background=random.choice(colores))
    boton3.config(background=random.choice(colores))
    boton4.config(background=random.choice(colores))


def alta(x, y, z, w):
    x.set(
        "Ud. registro la pelicula: "
        + y.get()
        + ", del año "
        + z.get()
        + ", dirigida por "
        + w.get()
        + "."
    )
    tabla[y.get()] = {"titulo": y.get(), "año": z.get(), "director": w.get()}


# cree la variable auxiliar, por que no sabia otra manera de ver mas prolijo los datos.
def busqueda(x, y):
    if y.get() in tabla:
        aux = tabla[y.get()]
        x.set(
            "Ud. busco la pelicula : "
            + str(aux.get("titulo"))
            + ", del año "
            + str(aux.get("año"))
            + ", dirigida por "
            + str(aux.get("director"))
            + "."
        )
    else:
        x.set("No se encuentra ese titulo")


# cree un boton para borrar.
def borrar(x, y):
    if y.get() in tabla:
        aux = tabla[y.get()]
        x.set(
            "Ud. borro la pelicula : "
            + str(aux.get("titulo"))
            + ", del año "
            + str(aux.get("año"))
            + ", dirigida por "
            + str(aux.get("director"))
            + "."
        )
        tabla.pop(y.get())
    else:
        x.set("No se encuentra ese titulo")


etiqueta1 = Label(root, text="Titulo: ", bd=4, bg=fondo, font=(letra))
etiqueta1.place(x=10, y=10)
entrada1 = Entry(root, textvariable=titulo, bd=3)
entrada1.place(x=170, y=10)


etiqueta2 = Label(root, text="Año: ", bd=4, bg=fondo, font=(letra))
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable=año, bd=3)
entrada2.place(x=170, y=40)


etiqueta3 = Label(root, text="Director: ", bd=4, bg=fondo, font=(letra))
etiqueta3.place(x=10, y=70)
entrada3 = Entry(root, textvariable=director, bd=3)
entrada3.place(x=170, y=70)

etiqueta4 = Label(
    root,
    text="Ingrese el titulo de la pelicula que desea:",
    bd=4,
    bg=fondo,
    font=(letra),
)
etiqueta4.place(x=10, y=160)


boton1 = Button(
    root,
    text="Alta",
    command=lambda: alta(ingreso, titulo, año, director),
    bd=5,
    bg=fondo2,
    font=(letra),
    cursor="hand2",
)
boton1.place(x=10, y=120)

boton2 = Button(
    root,
    text="Buscar",
    command=lambda: busqueda(ingreso, titulo),
    bd=5,
    bg=fondo2,
    font=(letra),
    cursor="hand2",
)
boton2.place(x=280, y=155)

boton3 = Button(
    root,
    text="Borrar",
    command=lambda: borrar(ingreso, titulo),
    bd=5,
    bg=fondo2,
    font=(letra),
    cursor="hand2",
)
boton3.place(x=350, y=155)

boton4 = Button(
    root,
    text="Sorpresa!",
    command=sorpresa,
    bd=5,
    bg=fondo2,
    font=(letra),
    cursor="hand2",
)
boton4.place(x=200, y=300)

entrada3 = Entry(root, bd=4, font=(letra), textvariable=ingreso, state="disabled")
entrada3.place(x=10, y=230, relwidth=0.95)

root.mainloop()
