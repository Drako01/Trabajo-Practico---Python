# Importamos las Bibliotecas de tkinter
from tkinter import *

# Le asignamos valores para las dimensiones de la ventana
master = Tk()
master.geometry("400x250")
master.title("Trabajo Final")
master.resizable(False, False)

# Aca vamos a encontrarnos con el Encabezado de la Agenda
encabezado = Label(master, text="Ingrese sus datos",
                   background="#E0FFDA", foreground="black", width=60)
encabezado.grid(row=0, column=0, columnspan=2)
# En esta seccion definimos los nombre de variables globales
agenda=[]

# En esta seccion estan los Label donde figura el Nombre de cada Campo
nombre = Label(master, text="Nombre(s)").grid(row=2, column=0, sticky=W)
apellido = Label(master, text="Apellido").grid(row=1, column=0, sticky=W)
direccion = Label(master, text="Dirección").grid(row=3, column=0, sticky=W)
localidad = Label(master, text="Localidad").grid(row=4, column=0, sticky=W)
telefono = Label(master, text="Telefono").grid(row=5, column=0, sticky=W)
email = Label(master, text="Correo Electronico").grid(row=6, column=0, sticky=W)
dni = Label(master, text="D.N.I.").grid(row=7, column=0, sticky=W)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar
entrada_nombre = Entry(master, width=30)
entrada_nombre.grid(row=2, column=1)
entrada_apellido = Entry(master, width=30)
entrada_apellido.grid(row=1, column=1)
entrada_direccion = Entry(master, width=30)
entrada_direccion.grid(row=3, column=1)
entrada_localidad = Entry(master, width=30)
entrada_localidad.grid(row=4, column=1)
entrada_telefono = Entry(master, width=30)
entrada_telefono.grid(row=5, column=1)
entrada_email = Entry(master, width=30)
entrada_email.grid(row=6, column=1)
entrada_dni = Entry(master, width=30)
entrada_dni.grid(row=7, column=1)

lista = []

# Definimos la Funcion callback para Agendar al Contacto
def callback():
    print("Nuevo Contacto en la Agenda")
    print(" El Nombre es: ", entrada_nombre.get(), '\n', "El Apellido es: ",
          entrada_apellido.get(), '\n', "La Direccion es: ", entrada_direccion.get(),  '\n', "De la Localidad de: ", 
          entrada_localidad.get(), '\n', "El Telefono es: ", entrada_telefono.get(), '\n', "El Correo Electronico es: ", 
          entrada_email.get(), '\n', "El DNI es: ", entrada_dni.get())


def guardar():
    
    lista.append(apellido)
    lista.append(nombre)
    lista.append(direccion)
    lista.append(localidad)
    lista.append(telefono)
    lista.append(email)
    lista.append(dni)
    print(lista)
 
    
    

    
            

alta = Button(master, text="Agendar", command=callback, padx=10)
alta.grid(row=10, column=1)
alta = Button(master, text="Guardar", command=guardar, padx=10)
alta.grid(row=12, column=1)

master.mainloop()
# fin del Programa
