# Importamos las Bibliotecas de tkinter
from tkinter import *
from tkinter import ttk

lista = {}
lista = set()

# Le asignamos valores para las dimensiones de la ventana
master = Tk()
master.geometry("450x350")
master.title("Trabajo Final")
master.resizable(False, False)
master.config(bd=20)

# Aca vamos a encontrarnos con el Encabezado de la Agenda
encabezado = Label(
    master,
    text="Ingrese sus datos",
    background="LightSteelBlue",
    foreground="black",
    width=60,
)
encabezado.grid(row=0, column=0, columnspan=2, pady=10)
# En esta seccion definimos los nombre de variables globales
agenda = {}

# En esta seccion estan los Label donde figura el Nombre de cada Campo
nombre = Label(master, text="Nombre(s)").grid(
    row=2, column=0, sticky=W, pady=3)
apellido = Label(master, text="Apellido").grid(
    row=3, column=0, sticky=W, pady=3)
direccion = Label(master, text="Dirección").grid(
    row=4, column=0, sticky=W, pady=3)
localidad = Label(master, text="Localidad").grid(
    row=5, column=0, sticky=W, pady=3)
telefono = Label(master, text="Telefono").grid(
    row=6, column=0, sticky=W, pady=3)
email = Label(master, text="Correo Electronico").grid(
    row=7, column=0, sticky=W, pady=3)
dni = Label(master, text="D.N.I.").grid(row=8, column=0, sticky=W, pady=3)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar
entrada_nombre = Entry(master, text="", width=30, bd=3)
entrada_nombre.grid(row=2, column=1, pady=3)
entrada_apellido = Entry(master, text="", width=30, bd=3)
entrada_apellido.grid(row=3, column=1, pady=3)
entrada_direccion = Entry(master, width=30, bd=3)
entrada_direccion.grid(row=4, column=1, pady=3)
entrada_localidad = Entry(master, width=30, bd=3)
entrada_localidad.grid(row=5, column=1, pady=3)
entrada_telefono = Entry(master, width=30, bd=3)
entrada_telefono.grid(row=6, column=1, pady=3)
entrada_email = Entry(master, width=30, bd=3)
entrada_email.grid(row=7, column=1, pady=3)
entrada_dni = Entry(master, width=30, bd=3)
entrada_dni.grid(row=8, column=1, pady=3)

# Definimos la Funcion callback para Agendar al Contacto


def callback():
    print("Nuevo Contacto en la Agenda")
    print(
        " El Apellido es: ",
        entrada_apellido.get(),
        "\n",
        "El Nombre es: ",
        entrada_nombre.get(),
        "\n",
        "La Direccion es: ",
        entrada_direccion.get(),
        "\n",
        "De la Localidad de: ",
        entrada_localidad.get(),
        "\n",
        "El Telefono es: ",
        entrada_telefono.get(),
        "\n",
        "El Correo Electronico es: ",
        entrada_email.get(),
        "\n",
        "El DNI es: ",
        entrada_dni.get(),
    )


# Definimos los Botones de llamada
alta = Button(
    master,
    text="Agendar",
    command=callback,
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
alta.grid(row=10, column=1, pady=8)
# alta = Button(master, text="Guardar", command=guardar, padx=10)
# alta.grid(row=12, column=1)

master.mainloop()
# fin del Programa
