from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import __main__
from __main__ import *

# Definimos Variables

dni = IntVar()
dni.set("")
nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
localidad = StringVar()
telefono = StringVar()
email = StringVar()
ingreso = StringVar()
entidad = StringVar()

# Definimos una Funcion para cambiar las Caracteristicas del Label

color_fuente = "Black"

def colorNegro():
    entrada3.config(fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6)


def colorRojo():
    entrada3.config(
        fg="red", bg="Yellow", font=("Verdana", 10, "bold"), width=6
    )
    

# Asignacion de la ventana

master = Tk()
master.title("Trabajo Final - Nivel Inicial - Diplomatura en Python")
master.resizable(False, False)
master.config(bd=20)

# Encabezado de la Agenda

encabezado = Label(
    master,
    text="Ingrese los datos del Nuevo Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=0, column=0, columnspan=2, pady=10)

# Imagen opcional

imagen = PhotoImage(file="agenda2.gif")
Label(master, image=imagen).grid(row=2, column=1, sticky=E)

# Etiqueta con referencia a la busqueda

encabezado = Label(
    master,
    text="Ingrese el DNI para Buscar o Eliminar al Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=3, column=0, columnspan=2, pady=10)

# Frame donde se ubican los entry y label

frame = Frame(master)
frame.grid(row=2, column=0)
frame.config(bg="LightSteelBlue")


# En esta seccion estan los Label donde figura el Nombre de cada Campo

dni_ = Label(frame, text="D.N.I.", bg="LightSteelBlue").grid(
    row=2, column=0, sticky=W, pady=3, padx=6
)

apellido_ = Label(frame, text="Apellido", bg="LightSteelBlue").grid(
    row=3, column=0, sticky=W, pady=3, padx=6
)
nombre_ = Label(frame, text="Nombre(s)", bg="LightSteelBlue").grid(
    row=4, column=0, sticky=W, pady=3, padx=6
)
direccion_ = Label(frame, text="Dirección", bg="LightSteelBlue").grid(
    row=5, column=0, sticky=W, pady=3, padx=6
)
localidad_ = Label(frame, text="Localidad", bg="LightSteelBlue").grid(
    row=6, column=0, sticky=W, pady=3, padx=6
)
telefono_ = Label(frame, text="Telefono", bg="LightSteelBlue").grid(
    row=7, column=0, sticky=W, pady=3, padx=6
)
email_ = Label(frame, text="Correo Electronico", bg="LightSteelBlue").grid(
    row=8, column=0, sticky=W, pady=3, padx=6
)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar

entrada_dni = Entry(frame, textvariable=dni, width=30, bd=3)
entrada_dni.grid(row=2, column=1, pady=3, sticky=W, padx=6)

entrada_apellido = Entry(frame, textvariable=apellido, width=30, bd=3)
entrada_apellido.grid(row=3, column=1, pady=3, sticky=W, padx=6)

entrada_nombre = Entry(frame, textvariable=nombre, width=30, bd=3)
entrada_nombre.grid(row=4, column=1, pady=3, sticky=E, padx=6)

entrada_direccion = Entry(frame, textvariable=direccion, width=30, bd=3)
entrada_direccion.grid(row=5, column=1, pady=3, sticky=W, padx=6)

entrada_localidad = Entry(frame, textvariable=localidad, width=30, bd=3)
entrada_localidad.grid(row=6, column=1, pady=3, sticky=W, padx=6)

entrada_telefono = Entry(frame, textvariable=telefono, width=30, bd=3)
entrada_telefono.grid(row=7, column=1, pady=3, sticky=W, padx=6)

entrada_email = Entry(frame, textvariable=email, width=30, bd=3)
entrada_email.grid(row=8, column=1, pady=3, sticky=W, padx=6)


# entry registro de acciones del usuario

entrada3 = Label(master, bd=4, textvariable=ingreso)
entrada3.config(
    fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6
)  # Foreground  # Background
entrada3.grid(row=12, column=0, pady=4, columnspan=2, ipadx=300)

# defino la tabla donde se veran los datos

tabla = ttk.Treeview(master, columns=("uno", "dos", "tres", "cuatro", "cinco", "seis"))

tabla.column("#0", width=100, minwidth=70)
tabla.column("uno", width=100, minwidth=70)
tabla.column("dos", width=100, minwidth=70)
tabla.column("tres", width=100, minwidth=70)
tabla.column("cuatro", width=100, minwidth=70)
tabla.column("cinco", width=100, minwidth=70)
tabla.column("seis", width=120, minwidth=70)

tabla.heading("#0", text="D.N.I", anchor="w")
tabla.heading("uno", text="Apellido", anchor="w")
tabla.heading("dos", text="Nombre", anchor="w")
tabla.heading("tres", text="Dirección", anchor="w")
tabla.heading("cuatro", text="Localidad", anchor="w")
tabla.heading("cinco", text="Telefono", anchor="w")
tabla.heading("seis", text="Correo Electronico", anchor="w")

tabla.grid(row=14, column=0, pady=3, columnspan=2)
tabla.bind("<<TreeviewSelect>>", item_elegido)

estilo = ttk.Style(master)
estilo.theme_use("alt")
estilo.configure(".", font=("Helvetica", 12, "bold"), foreground="black")
estilo.configure(
    "Treeview", font=("Helvetica", 10), foreground="black", background="white"
)
estilo.map(
    "Treeview",
    background=[("selected", "LightSteelBlue")],
    foreground=[("selected", "black")],
)

# etiqueta al pie con los integrantes

encabezado = Label(
    master,
    text="INTEGRANTES: Alejandro Di Stefano - Oscar Quintana - Nora Nardi - Marcelo Mansilla - Federico Iaccono - Juan Alberto Labajian",
    background="LightSteelBlue",
    foreground="black",
    width=100,
)
encabezado.grid(row=15, column=0, columnspan=2, pady=10)

master.mainloop()

micursor.close()

# fin del Programa