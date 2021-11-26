# Importamos las Bibliotecas de tkinter
from tkinter import *
from tkinter import ttk
import shelve
import mysql.connector

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
encabezado.grid(row=14, column=0, columnspan=2, pady=10)

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

nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
localidad = StringVar()
telefono = IntVar()
email = StringVar()
dni = IntVar()
ingreso = StringVar()
entidad = StringVar()


# creacion de la base de datos

def Crear_Agenda():
    mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
    )
    micursor = mibase.cursor()

    micursor.execute("CREATE DATABASE Agenda_Contacto")

try:
    Crear_Agenda()
    print("Estamos Creando la BD")
except:
    print("Ya esta Creada la BD")

# Creacion de la Tabla en la Base de Datos

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Agenda_Contacto"
)
micursor = mibase.cursor()

micursor.execute("CREATE TABLE IF NOT EXISTS entidad( ID int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, DNI INT(8) COLLATE utf8_spanish2_ci NOT NULL, Apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Direccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL , Localidad VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Telefono INT(15) COLLATE utf8_spanish2_ci NOT NULL, Email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)")


# Definimos las Funciones para la Agendar de Contactos

def callback():        
    mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Agenda_Contacto"
    )
    micursor = mibase.cursor()

    sql = "INSERT INTO entidad (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    datos = ("DNI", "Apellido", "Nombre", "Direccion", "Localidad", "Telefono", "EMail" )
  
    micursor.execute(sql, datos)

    mibase.commit()

    print(micursor.rowcount, "Cantidad de registros agregados.")

def busqueda(x, du):
    if du.get() in entidad:
        aux = entidad[du.get()]
        x.set(
            "Ud. busco al Contacto : "
            + str(aux.get("Apellido"))
            + ", "
            + str(aux.get("Nombre"))
            + ", "
            + str(aux.get("Direccion"))
            + ", "
            + str(aux.get("Localidad"))
            + ", "
            + str(aux.get("Telefono"))
            + ", "
            + str(aux.get("Email"))
            + ", "
            + str(aux.get("DNI"))
            + "."
        )
    else:
        x.set("No se encuentra ese Contacto")

def borrar(x, du):
    if du.get() in entidad:
        aux = entidad[du.get()]
        x.set(
            "Ud. Eliminó al Contacto : "
            + str(aux.get("Apellido"))
            + ", "
            + str(aux.get("Nombre"))
            + ", "
            + str(aux.get("Direccion"))
            + ", "
            + str(aux.get("Localidad"))
            + ", "
            + str(aux.get("Telefono"))
            + ", "
            + str(aux.get("Email"))
            + ", "
            + str(aux.get("DNI"))
            + "."
        )
        entidad.pop(du.get())
    else:
        x.set("No se encuentra ese Contacto")
   
def modificar_():
        
    mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Agenda_Contacto"
    )
    micursor = mibase.cursor()

    sql = "UPDATE entidad SET titulo = 'Titulo 8' WHERE titulo = 'Tema 3'"

    micursor.execute(sql)
    mibase.commit()

    print(micursor.rowcount, "Cantidad de registros afectados.")
    
    
     
        
# Definimos el Boton de Agendado
alta = Button(
    master,
    text="Agendar", command=lambda: callback(),
    # command=lambda: callback(
    # ingreso, apellido, nombre, direccion, localidad, telefono, email, dni),
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
    command=lambda: borrar(ingreso, dni),
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
        ingreso, apellido, nombre, direccion, localidad, telefono, email, dni),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
modificar.grid(row=10, column=2, pady=12, columnspan=1, sticky=N)



# En esta seccion estan los Label donde figura el Nombre de cada Campo
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
dni_ = Label(frame, text="D.N.I.").grid(row=2, column=0, sticky=W, pady=3, padx=6)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar

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

entrada_dni = Entry(frame, textvariable=dni, width=30, bd=3)
entrada_dni.grid(row=2, column=1, pady=3, sticky=W, padx=6)


# defino la tabla donde se veran los datos

entrada3 = Entry(master, bd=4, textvariable=ingreso, state="disabled")
entrada3.grid(row=11, column=0, pady=4, columnspan=2, ipadx=300)



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

tabla.grid(row=15, column=0, pady=3, columnspan=2)

master.mainloop()
# fin del Programa
