import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("titulo de la ventana")
        self.label1=tk.Label(self.ventana1, text="etiqueta n 1")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="etiqueta 2")
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="boton 1 finalizar", command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.resizable(False, False)
        self.ventana1.mainloop()


    def finalizar(self):
        sys.exit(0)

aplicacion1=Aplicacion()