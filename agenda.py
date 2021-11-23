# Importamos las Bibliotecas de tkinter
from tkinter import *
from tkinter import ttk
import shelve

# Le asignamos valores para las dimensiones de la ventana
master = Tk()

# Definimos Variables

nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
localidad = StringVar()
telefono = StringVar()
email = StringVar()
dni = StringVar()


# creacion de la base de datos
entidad = shelve.open("Agenda_Contacto")


lista = {}
lista = set()


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
imagen = PhotoImage(file="agenda2.gif")
Label(master, image=imagen).grid(row=2, column=1, sticky=E)

frame = Frame(master)
frame.grid(row=2, column=0)
frame.config(bg="LightSteelBlue")


# En esta seccion estan los Label donde figura el Nombre de cada Campo
nombre_ = Label(frame, text="Nombre(s)").grid(row=2, column=0, sticky=W, pady=3, padx=6)

apellido_ = Label(frame, text="Apellido").grid(
    row=3, column=0, sticky=W, pady=3, padx=6
)

direccion_ = Label(frame, text="Dirección").grid(
    row=4, column=0, sticky=W, pady=3, padx=6
)
localidad_ = Label(frame, text="Localidad").grid(
    row=5, column=0, sticky=W, pady=3, padx=6
)
telefono_ = Label(frame, text="Telefono").grid(
    row=6, column=0, sticky=W, pady=3, padx=6
)
email_ = Label(frame, text="Correo Electronico").grid(
    row=7, column=0, sticky=W, pady=3, padx=6
)
dni_ = Label(frame, text="D.N.I.").grid(row=8, column=0, sticky=W, pady=3, padx=6)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar
entrada_nombre = Entry(frame, textvariable=nombre, width=30, bd=3)
entrada_nombre.grid(row=2, column=1, pady=3, sticky=E, padx=6)

entrada_apellido = Entry(frame, textvariable=apellido, width=30, bd=3)
entrada_apellido.grid(row=3, column=1, pady=3, sticky=W, padx=6)

entrada_direccion = Entry(frame, textvariable=direccion, width=30, bd=3)
entrada_direccion.grid(row=4, column=1, pady=3, sticky=W, padx=6)

entrada_localidad = Entry(frame, textvariable=localidad, width=30, bd=3)
entrada_localidad.grid(row=5, column=1, pady=3, sticky=W, padx=6)

entrada_telefono = Entry(frame, textvariable=telefono, width=30, bd=3)
entrada_telefono.grid(row=6, column=1, pady=3, sticky=W, padx=6)

entrada_email = Entry(frame, textvariable=email, width=30, bd=3)
entrada_email.grid(row=7, column=1, pady=3, sticky=W, padx=6)

entrada_dni = Entry(frame, textvariable=dni, width=30, bd=3)
entrada_dni.grid(row=8, column=1, pady=3, sticky=W, padx=6)

# Definimos la Funcion callback para Agendar al Contacto


# def callback():
#     print("Nuevo Contacto en la Agenda")
#     print(
#         " El Apellido es: ",
#         entrada_apellido.get(),
#         "\n",
#         "El Nombre es: ",
#         entrada_nombre.get(),
#         "\n",
#         "La Direccion es: ",
#         entrada_direccion.get(),
#         "\n",
#         "De la Localidad de: ",
#         entrada_localidad.get(),
#         "\n",
#         "El Telefono es: ",
#         entrada_telefono.get(),
#         "\n",
#         "El Correo Electronico es: ",
#         entrada_email.get(),
#         "\n",
#         "El DNI es: ",
#         entrada_dni.get(),
#     )


def callback(ID, a, n, d, l, t, e, du):
    # ID.set(
    #     +a.get
    # )
    entidad[du.get()] = {
        "Apellido": a.get(),
        "Nombre": n.get(),
        "Direccion": d.get(),
        "Localidad": l.get(),
        "Telefono": t.get(),
        "Email": e.get(),
        "DNI": du.get(),
    }


def busqueda(x, du):
    if du.get() in entidad:
        aux = entidad[du.get()]
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


# Definimos los Botones de llamada
alta = Button(
    master,
    text="Agendar",
    command=lambda: callback(
        tabla, apellido, nombre, direccion, localidad, telefono, email, dni
    ),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
alta.grid(row=10, column=0, pady=12, columnspan=2, sticky=N)

buscar = Button(
    master,
    text="Consultar",
    command=lambda: busqueda(tabla, dni),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
alta.grid(row=10, column=1, pady=12, columnspan=3, sticky=N)
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

tabla.grid(row=11, column=0, pady=3, columnspan=2)

master.mainloop()
# fin del Programa
