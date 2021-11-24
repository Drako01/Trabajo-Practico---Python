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
ingreso = StringVar()

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
    width=80,
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

# Definimos la Funcion callback para Agendar al Contacto

encabezado = Label(
    master,
    text="Ingrese el DNI para Buscar al Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=9, column=0, columnspan=2, pady=10)

def callback(x, a, n, d, l, t, e, du): 
    
    x.set(
        "Ud. ingreso al Contacto : "
        + str(a.get())
        + ", "
        + str(n.get())
        + ", "
        + str(d.get())
        + ", "
        + str(l.get())
        + ", "
        + str(t.get())
        + ", "
        + str(e.get())
        + ", "
        + str(du.get())
        + "."
    )
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
        
        
# Definimos el Boton de Agendado
alta = Button(
    master,
    text="Agendar",
    command=lambda: callback(
        ingreso, apellido, nombre, direccion, localidad, telefono, email, dni),
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
buscar.grid(row=10, column=0, pady=12, columnspan=2, sticky=N)

# Definimos el Boton de Borrar Contacto
borrar_ = Button(
    master,
    text="Borrar",
    command=lambda: borrar(ingreso, dni),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
borrar_.grid(row=10, column=1, pady=12, columnspan=3, sticky=N)


# defino la tabla donde se veran los datos

entrada3 = Entry(master, bd=4, textvariable=ingreso, state="disabled")
entrada3.grid(row=11, column=0, pady=4, columnspan=2, ipadx=300)

master.mainloop()
# fin del Programa
