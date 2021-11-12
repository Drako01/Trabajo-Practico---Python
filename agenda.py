# Importamos las Bibliotecas de tkinter
from tkinter import *
from tkinter import ttk

lista = {}
lista = set()

# Le asignamos valores para las dimensiones de la ventana
master = Tk()

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

# imagen opcional para acomodar los entry
imagen = PhotoImage(file="agenda.gif")
Label(master, image=imagen).grid(row=2, column=1, sticky=E)

frame = Frame(master)
frame.grid(row=2, column=0)
frame.config(bg="cyan2")


# En esta seccion estan los Label donde figura el Nombre de cada Campo
nombre = Label(frame, text="Nombre(s)").grid(row=2, column=0, sticky=W, pady=3)
apellido = Label(frame, text="Apellido").grid(row=3, column=0, sticky=W, pady=3)
direccion = Label(frame, text="Dirección").grid(row=4, column=0, sticky=W, pady=3)
localidad = Label(frame, text="Localidad").grid(row=5, column=0, sticky=W, pady=3)
telefono = Label(frame, text="Telefono").grid(row=6, column=0, sticky=W, pady=3)
email = Label(frame, text="Correo Electronico").grid(row=7, column=0, sticky=W, pady=3)
dni = Label(frame, text="D.N.I.").grid(row=8, column=0, sticky=W, pady=3)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar
entrada_nombre = Entry(frame, text="", width=30, bd=3)
entrada_nombre.grid(row=2, column=1, pady=3, sticky=E)
entrada_apellido = Entry(frame, text="", width=30, bd=3)
entrada_apellido.grid(row=3, column=1, pady=3, sticky=W)
entrada_direccion = Entry(frame, width=30, bd=3)
entrada_direccion.grid(row=4, column=1, pady=3, sticky=W)
entrada_localidad = Entry(frame, width=30, bd=3)
entrada_localidad.grid(row=5, column=1, pady=3, sticky=W)
entrada_telefono = Entry(frame, width=30, bd=3)
entrada_telefono.grid(row=6, column=1, pady=3, sticky=W)
entrada_email = Entry(frame, width=30, bd=3)
entrada_email.grid(row=7, column=1, pady=3, sticky=W)
entrada_dni = Entry(frame, width=30, bd=3)
entrada_dni.grid(row=8, column=1, pady=3, sticky=W)

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

# defino la tabla donde se veran los datos


tabla = ttk.Treeview(
    master, columns=("uno", "dos", "tres", "cuatro", "cinco", "seis", "siete")
)


tabla.column("#0", width=20, minwidth=40)
tabla.column("uno", width=100, minwidth=70)
tabla.column("dos", width=100, minwidth=70)
tabla.column("tres", width=100, minwidth=50)
tabla.column("cuatro", width=100, minwidth=50)
tabla.column("cinco", width=100, minwidth=50)
tabla.column("seis", width=120, minwidth=50)
tabla.column("siete", width=100, minwidth=50)


tabla.heading("#0", text="ID", anchor="w")
tabla.heading("uno", text="Nombre", anchor="w")
tabla.heading("dos", text="Apellido", anchor="w")
tabla.heading("tres", text="Dirección", anchor="w")
tabla.heading("cuatro", text="Localidad", anchor="w")
tabla.heading("cinco", text="Telefono", anchor="w")
tabla.heading("seis", text="Correo Electronico", anchor="w")
tabla.heading("siete", text="D.N.I", anchor="w")

tabla.grid(row=11, column=0, pady=3)

master.mainloop()
# fin del Programa
