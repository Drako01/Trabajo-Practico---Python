# Importamos las Bibliotecas de tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter.messagebox import *

# Le asignamos valores para las dimensiones de la ventana
master = Tk()

# Aca vamos a encontrarnos con el Encabezado de la Agenda
encabezado = Label(
    master,
    text="Ingrese los datos del Nuevo Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=0, column=0, columnspan=2, pady=10)

encabezado = Label(
    master,
    text="Ingrese el DNI para Buscar o Eliminar al Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=9, column=0, columnspan=2, pady=10)

encabezado = Label(
    master,
    text="INTEGRANTES: Alejandro Di Stefano - Oscar Quintana - Nora Nardi - Marcelo Mansilla - Federico Iaccono - Juan Alberto Labajian",
    background="LightSteelBlue",
    foreground="black",
    width=100,
)
encabezado.grid(row=15, column=0, columnspan=2, pady=10)

master.title("Trabajo Final - Nivel Inicial - Diplomatura en Python")
master.resizable(False, False)
master.config(bd=20)

# imagen opcional para acomodar los entry
imagen = PhotoImage(file="agenda2.gif")
Label(master, image=imagen).grid(row=2, column=1, sticky=E)

frame = Frame(master)
frame.grid(row=2, column=0)
frame.config(bg="LightSteelBlue")

# Definimos Variables

dni = IntVar()
dni.set("")
nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
localidad = StringVar()
telefono = IntVar()
telefono.set("")
email = StringVar()
ingreso = StringVar()
entidad = StringVar()


# creacion de la base de datos

mibase = mysql.connector.connect(host="localhost", user="root", passwd="")
try:
    micursor = mibase.cursor()
    micursor.execute("CREATE DATABASE Agenda_Contacto")
except:
    print("Ya esta Creada la BD")

# Creacion de la Tabla en la Base de Datos

mibase = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="Agenda_Contacto"
)
micursor = mibase.cursor()

micursor.execute(
    "CREATE TABLE IF NOT EXISTS entidad( ID int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, DNI INT(8) COLLATE utf8_spanish2_ci NOT NULL, Apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Direccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL , Localidad VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Telefono INT(15) COLLATE utf8_spanish2_ci NOT NULL, Email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)"
)


# Definimos las Funciones para la Agendar de Contactos


def callback(x, dni, apellido, nombre, direccion, localidad, telefono, email):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="Agenda_Contacto"
    )
    micursor = mibase.cursor()

    sql = "INSERT INTO entidad (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    datos = (
        dni.get(),
        apellido.get(),
        nombre.get(),
        direccion.get(),
        localidad.get(),
        telefono.get(),
        email.get(),
    )
    micursor.execute(sql, datos)
    mibase.commit()

    x.set("Ud. Agrego al siguiente Contacto:")
    tabla.insert(
        "",
        "end",
        text=dni.get(),
        values=[
            apellido.get(),
            nombre.get(),
            direccion.get(),
            localidad.get(),
            telefono.get(),
            email.get(),
        ],
    )


def busqueda(x, dni):  # , nombre, direccion, localidad, telefono, email):
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="Agenda_Contacto"
    )
    micursor = mibase.cursor()
    sql = "SELECT * FROM entidad WHERE DNI = {}".format(dni.get())
    micursor.execute(sql)
    registro = micursor.fetchall()

    if not registro == []:
        x.set(f"{registro}")
        i = -1
        for dato in registro:
            i = i + 1
            tabla.insert("", i, text=registro[i][1:2], values=registro[i][2:7])
        x.set("Se encontraron los siguientes contactos.")
    else:
        x.set("No se encontro el contacto.")


# def item_elegido(seleccion):
#     x = tabla.focus()
#     item = tabla.item(x)
#     valor = item["values"][0]
# showinfo(title="Information", message=",".join(valor))


def borrar(x):
    fila = tabla.selection()

    if len(fila) != 0:
        item = tabla.item(fila)
        valor = int(item["text"])
        print(valor)

        mibase = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="Agenda_Contacto"
        )
        micursor = mibase.cursor()
        sql = "DELETE FROM entidad WHERE dni = %s"

        micursor.execute(sql, valor)

        mibase.commit()
        x.set("Se ha borrado el Contacto")
        tabla.delete(fila)
    else:
        x.set("No se pudo Borrar el Contacto")


def item_elegido(seleccion):
    """x = tabla.focus()
    item = tabla.item(x)
    print(item)
    data = tabla.item(x)
    nombre_borar = data["text"]
    return nombre_borar"""
    for selec in tabla.selection():
        item = tree.item(selec)
        record = item["text"]


def modificar_():
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="Agenda_Contacto"
    )
    micursor = mibase.cursor()

    sql = "UPDATE entidad SET titulo = 'Titulo 8' WHERE titulo = 'Tema 3'"

    micursor.execute(sql)
    mibase.commit()

    print(micursor.rowcount, "Cantidad de registros afectados.")


def limpiar_tabla():
    tabla.delete(*tabla.get_children())
    dni.set("")
    apellido.set("")
    nombre.set("")
    direccion.set("")
    localidad.set("")
    telefono.set("")
    email.set("")
    ingreso.set("")


# Definimos el Boton de Agendado
alta = Button(
    master,
    text="Agendar",
    command=lambda: callback(
        ingreso, dni, apellido, nombre, direccion, localidad, telefono, email
    ),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
alta.grid(row=10, column=0, pady=12, columnspan=1, sticky=N)

# Definimos el Boton de Consulta
buscar = Button(
    master,
    text="Consultar",
    command=lambda: busqueda(ingreso, dni),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
buscar.grid(row=10, column=1, pady=12, columnspan=1, sticky=N)

# Definimos el Boton de Borrar Contacto
borrar_ = Button(
    master,
    text="   Borrar   ",
    command=lambda: borrar(ingreso),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
borrar_.grid(row=9, column=2, pady=12, columnspan=1, sticky=N)

# Boton de Modificar Datos del Contacto
modificar = Button(
    master,
    text="Modificar",
    command=lambda: modificar_(
        ingreso, apellido, nombre, direccion, localidad, telefono, email, dni
    ),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
modificar.grid(row=10, column=2, pady=12, columnspan=1, sticky=N)

# Boton de Reset Datos del Contacto
modificar = Button(
    master,
    text="Reset",
    command=lambda: limpiar_tabla(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
modificar.grid(row=14, column=2, pady=12, columnspan=1, sticky=N)


# En esta seccion estan los Label donde figura el Nombre de cada Campo
dni_ = Label(frame, text="D.N.I.").grid(row=2, column=0, sticky=W, pady=3, padx=6)

nombre_ = Label(frame, text="Nombre(s)").grid(row=3, column=0, sticky=W, pady=3, padx=6)

apellido_ = Label(frame, text="Apellido").grid(
    row=4, column=0, sticky=W, pady=3, padx=6
)

direccion_ = Label(frame, text="Dirección").grid(
    row=5, column=0, sticky=W, pady=3, padx=6
)
localidad_ = Label(frame, text="Localidad").grid(
    row=6, column=0, sticky=W, pady=3, padx=6
)
telefono_ = Label(frame, text="Telefono").grid(
    row=7, column=0, sticky=W, pady=3, padx=6
)
email_ = Label(frame, text="Correo Electronico").grid(
    row=8, column=0, sticky=W, pady=3, padx=6
)


# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar

entrada_dni = Entry(frame, textvariable=dni, width=30, bd=3)
entrada_dni.grid(row=2, column=1, pady=3, sticky=W, padx=6)

entrada_nombre = Entry(frame, textvariable=nombre, width=30, bd=3)
entrada_nombre.grid(row=3, column=1, pady=3, sticky=E, padx=6)

entrada_apellido = Entry(frame, textvariable=apellido, width=30, bd=3)
entrada_apellido.grid(row=4, column=1, pady=3, sticky=W, padx=6)

entrada_direccion = Entry(frame, textvariable=direccion, width=30, bd=3)
entrada_direccion.grid(row=5, column=1, pady=3, sticky=W, padx=6)

entrada_localidad = Entry(frame, textvariable=localidad, width=30, bd=3)
entrada_localidad.grid(row=6, column=1, pady=3, sticky=W, padx=6)

entrada_telefono = Entry(frame, textvariable=telefono, width=30, bd=3)
entrada_telefono.grid(row=7, column=1, pady=3, sticky=W, padx=6)

entrada_email = Entry(frame, textvariable=email, width=30, bd=3)
entrada_email.grid(row=8, column=1, pady=3, sticky=W, padx=6)


# defino la tabla donde se veran los datos

entrada3 = Entry(master, bd=4, textvariable=ingreso, state="disabled")
entrada3.grid(row=11, column=0, pady=4, columnspan=2, ipadx=300)


tabla = ttk.Treeview(master, columns=("uno", "dos", "tres", "cuatro", "cinco", "seis"))

tabla.column("#0", width=100, minwidth=70)
tabla.column("uno", width=100, minwidth=70)
tabla.column("dos", width=100, minwidth=70)
tabla.column("tres", width=100, minwidth=70)
tabla.column("cuatro", width=100, minwidth=70)
tabla.column("cinco", width=100, minwidth=70)
tabla.column("seis", width=120, minwidth=70)


tabla.heading("#0", text="D.N.I", anchor="w")
tabla.heading("uno", text="Nombre", anchor="w")
tabla.heading("dos", text="Apellido", anchor="w")
tabla.heading("tres", text="Dirección", anchor="w")
tabla.heading("cuatro", text="Localidad", anchor="w")
tabla.heading("cinco", text="Telefono", anchor="w")
tabla.heading("seis", text="Correo Electronico", anchor="w")


tabla.grid(row=14, column=0, pady=3, columnspan=2)

# tabla.bind("<<TreeviewSelect>>", item_elegido)


master.mainloop()
# fin del Programa
