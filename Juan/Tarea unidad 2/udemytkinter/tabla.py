from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tabla de datos")
root.geometry("400x300")

tabla = ttk.Treeview(root)


tabla.column("cero")
tabla.column("cero", width=270, minwidth=270, stretch=None)
tabla.column("uno", width=150, minwidth=150, stretch=None)



tabla.heading("cero", text="ID", anchor="W")
tabla.heading("una", text="Nombre", anchor="W")
tabla.heading("dos", text="Apellido", anchor="W")


tabla.pack()
root.mainloop()