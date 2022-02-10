#%% ejemplo tk checkbutton 
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Python", variable=self.seleccion1)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="C++", variable=self.seleccion2)
        self.check2.grid(column=0, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1,text="Java", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana1, text="Verificar", command=self.verificar)
        self.boton1.grid(column=0, row=4)
        self.label1=tk.Label(self.ventana1,text="cantidad:")
        self.label1.grid(column=0, row=5)
        self.ventana1.mainloop()

    def verificar(self):
        cant=0
        if self.seleccion1.get()==1:
            cant+=1
        if self.seleccion2.get()==1:
            cant+=1
        if self.seleccion3.get()==1:
            cant+=1
        self.label1.configure(text="cantidad:"+str(cant))


aplicacion1=Aplicacion()
#%% otro ejemplo

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="¿Está de acuerdo con los términos y condiciones?", variable=self.seleccion, command=self.cambiarestado)
        self.check1.grid(column=0, row=0)
        self.boton1=tk.Button(self.ventana1, text="Entrar", state="disabled", command=self.ingresar)
        self.boton1.grid(column=0, row=1)        
        self.ventana1.mainloop()

    def cambiarestado(self):
        if self.seleccion.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion.get()==0:
            self.boton1.configure(state="disable")

    def ingresar(self):
        self.ventana1.title("Ingresando...")

aplicacion1=Aplicacion() 



#%% seleccionar varios items

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Chrome", variable=self.seleccion1, command=self.cambiartitulo)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="FireFox", variable=self.seleccion2, command=self.cambiartitulo)
        self.check2.grid(column=1, row=0)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1,text="Edge", variable=self.seleccion3, command=self.cambiartitulo)
        self.check3.grid(column=2, row=0)
        self.seleccion4=tk.IntVar()
        self.check4=tk.Checkbutton(self.ventana1,text="Opera", variable=self.seleccion4, command=self.cambiartitulo)
        self.check4.grid(column=3, row=0)
        self.ventana1.mainloop()

    def cambiartitulo(self):
        cadena='';
        if self.seleccion1.get()==1:
            cadena+="Chrome - "
        if self.seleccion2.get()==1:
            cadena+="Firefox - "
        if self.seleccion3.get()==1:
            cadena+="Edge - "
        if self.seleccion4.get()==1:
            cadena+="Opera"
        self.ventana1.title(cadena)

aplicacion1=Aplicacion()