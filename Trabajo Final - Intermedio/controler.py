from tkinter import *
from vista import Aplicacion
"""hola Soy Marce el del Paraguas"""

class AppPrincipal:
    def __init__(self, ventana):
        objeto = Aplicacion(ventana)


if __name__ == "__main__":
    root = Tk()
    miapp = AppPrincipal(root)
    root.mainloop()
