from tkinter import *
from tkinter import ttk
#hola
master = Tk()
master.title("Tabla de datos")
master.config(bd=20)


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

tabla.pack()


tabla.insert("", "end", iid=None, text="casa", values=("23-Jun-17 11:28", "PNG file"))
tabla.insert("", "end", text="", values=("23-Jun-17 11:28", "PNG file"))
tabla.insert("", "end", text="", values=("23-Jun-17 11:28", "PNG file"))
tabla.insert("", "end", text="", values=("23-Jun-17 11:28", "PNG file"))


master.mainloop()
# hola juan
