from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tabla de datos")
root.geometry("400x300")

tabla = ttk.Treeview(root)


tabla["columnas"] = ("cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete")
tabla.column("cero", width=270, minwidth=270, stretch=None)
tabla.column("uno", width=150, minwidth=150, stretch=None)
tabla.column("dos", width=400, minwidth=200, stretch=None)
tabla.column("tres", width=80, minwidth=50, stretch=None)
tabla.column("cuatro", width=80, minwidth=50, stretch=None)
tabla.column("cinco", width=80, minwidth=50, stretch=None)
tabla.column("seis", width=80, minwidth=50, stretch=None)
tabla.column("siete", width=80, minwidth=50, stretch=None)


tabla.heading("cero", text="ID", anchor="W")
tabla.heading("una", text="Nombre", anchor="W")
tabla.heading("dos", text="Apellido", anchor="W")
tabla.heading("tres", text="Dirección", anchor="W")
tabla.heading("cuatro", text="Localidad", anchor="W")
tabla.heading("cinco", text="Telefono", anchor="W")
tabla.heading("seis", text="Correo Electronico", anchor="W")
tabla.heading("siete", text="D.N.I", anchor="W")

tabla.pack()
root.mainloop()
