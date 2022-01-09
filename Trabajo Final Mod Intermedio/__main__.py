# Importamos las Bibliotecas de tkinter
from __view__ import *

# Funcion para conectar a la base de datos


def conect_sql():
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="Agenda_Contacto"
    )
    micursor = mibase.cursor()



# Funcion para cargar un contacto


def callback(x, dni, apellido, nombre, direccion, localidad, telefono, email):

    if comparar_dni(dni) == False:
        # Definimos la Validacion del EMail.!
        patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
        if re.match(patron, email.get()):
            conect_sql()
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
            colorNegro()
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
            limpiar_entries()
        else:
            colorRojo()
            x.set("La Direccion de Mail NO es Valida")
    else:
        colorRojo()
        x.set("Ya existe ese Registro")


# Funcion para buscar un contacto


def busqueda(x, dni):
    conect_sql()
    micursor = mibase.cursor()
    sql = "SELECT * FROM entidad WHERE DNI = {}".format(dni.get())
    micursor.execute(sql)
    registro = micursor.fetchall()

    if not registro == []:
        limpiar_tabla()
        x.set(f"{registro}")
        i = -1
        for dato in registro:
            i = i + 1
            tabla.insert("", i, text=registro[i][1:2], values=registro[i][2:8])
        colorNegro()
        x.set("Se encontraron los siguientes contactos.")

    else:
        colorRojo()
        x.set("No se encontro el contacto.")


# Funcion para modificar un contacto


def modificar_(x):
    patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
    if re.match(patron, email.get()):
        conect_sql()
        colorNegro()
        micursor = mibase.cursor()
        sql = "UPDATE entidad SET Apellido= %s, Nombre=%s, Direccion=%s, Localidad=%s, Telefono=%s, Email=%s WHERE DNI = %s"
        dato = (
            apellido.get(),
            nombre.get(),
            direccion.get(),
            localidad.get(),
            telefono.get(),
            email.get(),
            dni.get(),
        )
        micursor.execute(sql, dato)
        mibase.commit()
        listar(x)
        limpiar_entries()
        x.set(
            f"Se ha modificado el Contacto DNI: {dato[6]}, de Nombre: {dato[1]} {dato[0]}"
        )
    else:
        colorRojo()
        x.set("La Direccion de Mail NO es Valida")


# Funcion para borrar un contacto


def borrar(x):
    colorNegro()
    fila = tabla.selection()

    if len(fila) != 0:
        item = tabla.item(fila)
        valor = int(item["text"])

        conect_sql()
        micursor = mibase.cursor()
        sql = "DELETE FROM entidad WHERE dni = %s"
        dato = (valor,)

        micursor.execute(sql, dato)

        mibase.commit()
        x.set("Se ha borrado el Contacto")
        tabla.delete(fila)
        limpiar_entries()
    else:
        colorRojo()
        x.set("No se pudo Borrar el Contacto")


# Funcion para cargar todos los contacto


def listar(x):
    limpiar_tabla()
    conect_sql()
    micursor = mibase.cursor()
    sql = "SELECT * FROM entidad"
    micursor.execute(sql)
    registro = micursor.fetchall()

    if not registro == []:
        x.set(f"{registro}")
        i = -1
        for dato in registro:
            i = i + 1
            tabla.insert("", i, text=registro[i][1:2], values=registro[i][2:8])
        colorNegro()
        x.set("Se encontraron los siguientes contactos.")
    else:
        colorRojo()
        x.set("No se encontro el contacto.")


# Funcion para cargar en los entry el contacto seleccionado del treview "tabla"


def item_elegido(seleccion):
    for selec in tabla.selection():
        item = tabla.item(selec)
        record = item["values"]
        dni.set(item["text"])
        apellido.set(record[0])
        nombre.set(record[1])
        direccion.set(record[2])
        localidad.set(record[3])
        telefono.set(record[4])
        email.set(record[5])


# Funcion para limpiar los entry


def limpiar_entries():
    dni.set("")
    apellido.set("")
    nombre.set("")
    direccion.set("")
    localidad.set("")
    telefono.set("")
    email.set("")


# Funcion para limpiar la pantalla


def limpiar_tabla():
    ingreso.set("")
    tabla.delete(*tabla.get_children())
    limpiar_entries()


# Funcion compara DNI


def comparar_dni(dni):
    conect_sql()
    micursor = mibase.cursor()
    sql = "SELECT * FROM entidad WHERE DNI = {}".format(dni.get())
    micursor.execute(sql)
    registro = micursor.fetchall()

    if not registro == []:
        return True
    else:
        return False


# creacion de la base de datos

mibase = mysql.connector.connect(host="localhost", user="root", passwd="")
try:
    micursor = mibase.cursor()
    micursor.execute("CREATE DATABASE Agenda_Contacto")
except:
    print("Ya esta Creada la Base de Datos Agenda_Contactos")

# Creacion de la Tabla en la Base de Datos

mibase = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="Agenda_Contacto"
)
micursor = mibase.cursor()
micursor.execute(
    "CREATE TABLE IF NOT EXISTS entidad( ID int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, DNI INT(8) COLLATE utf8_spanish2_ci NOT NULL, Apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Direccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL , Localidad VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Telefono VARCHAR(15) COLLATE utf8_spanish2_ci NOT NULL, Email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)"
)




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
alta.grid(row=9, column=0, pady=12, columnspan=1, sticky=N)

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
buscar.grid(row=9, column=1, pady=12, columnspan=1, sticky=N)

# Definimos el Boton Listar Contactos
listar_ = Button(
    master,
    text="   Listar   ",
    command=lambda: listar(
        ingreso,
    ),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
listar_.grid(row=10, column=0, pady=12, columnspan=1, sticky=N)

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
borrar_.grid(row=10, column=1, pady=12, columnspan=1, sticky=N)

# Boton de Modificar Datos del Contacto
modificar = Button(
    master,
    text="Modificar",
    command=lambda: modificar_(ingreso),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
modificar.grid(row=11, column=0, pady=12, columnspan=1, sticky=N)

# Boton de Reset Datos del Contacto
reset = Button(
    master,
    text="    Reset    ",
    command=lambda: limpiar_tabla(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
reset.grid(row=11, column=1, pady=12, columnspan=1, sticky=N)

