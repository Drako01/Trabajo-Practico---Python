from tkinter import *

master = Tk()
master.geometry("400x150")
master.title("Trabajo Final")
master.resizable(False, False)


encabezado = Label(master, text="Ingrese sus datos",
                   background="#E0FFDA", foreground="black", width=60)
encabezado.grid(row=0, column=0, columnspan=2)

nombre = Label(master, text="Nombre").grid(row=1, column=0, sticky=W)
apellido = Label(master, text="Apellido").grid(row=2, column=0, sticky=W)
direccion = Label(master, text="Dirección").grid(row=3, column=0, sticky=W)
telefono = Label(master, text="Telefono").grid(row=4, column=0, sticky=W)


entrada_nombre = Entry(master, width=30)
entrada_nombre.grid(row=1, column=1)
entrada_apellido = Entry(master, width=30)
entrada_apellido.grid(row=2, column=1)
entrada_direccion = Entry(master, width=30)
entrada_direccion.grid(row=3, column=1)
entrada_telefono = Entry(master, width=30)
entrada_telefono.grid(row=4, column=1)


def callback():
    print("Nuevo Contacto en la Agenda")
    print(" El Nombre es: ", entrada_nombre.get(), '\n', "El Apellido es: ",
          entrada_apellido.get(), '\n', "La Direccion es: ", entrada_direccion.get(), '\n', "El Telefono es: ", entrada_telefono.get())


def colorchange():
    color = master.config(bg="#A3FF91")
    entrada_nombre = Entry(master, width=30, bg="Green")
    entrada_nombre.grid(row=1, column=1)
    entrada_apellido = Entry(master, width=30, bg="Green")
    entrada_apellido.grid(row=2, column=1)
    entrada_direccion = Entry(master, width=30, bg="Green")
    entrada_direccion.grid(row=3, column=1)
    entrada_telefono = Entry(master, width=30, bg="Green")
    entrada_telefono.grid(row=4, column=1)

    return color


alta = Button(master, text="Agendar", command=callback, padx=10)
alta.grid(row=10, column=1)


master.mainloop()
