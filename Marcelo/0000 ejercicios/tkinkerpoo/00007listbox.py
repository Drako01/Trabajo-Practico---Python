#%% lista de elementos
"""Problema: SELECCION DE UN ELEMENTO
Disponer un Listbox con una serie de nombres de frutas. Permitir la selección solo de uno de ellos. Cuando se presione un botón recuperar la fruta seleccionada y mostrarla en una Label."""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(self.ventana1,text="Seleccionado:")
        self.label1.grid(column=0, row=2)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()  


#%% lista de SELECCION VARIOS ELEMENTOS

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE)#MULTIPLES ELEMENTOS
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1,"manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)
        self.label1=tk.Label(self.ventana1,text="Seleccionado:")
        self.label1.grid(column=0, row=2)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion1=Aplicacion()


#%% nombre lista de paises

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese nombre")
        self.label1.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=40, textvariable=self.nombre)
        self.entry1.grid(column=0, row=1)
        self.label2=tk.Label(self.ventana1,text="Seleccione país")
        self.label2.grid(column=0, row=2)
        self.listbox1=tk.Listbox(self.ventana1,selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=3)
        self.listbox1.insert(0,"Argentina")
        self.listbox1.insert(1,"Chile")
        self.listbox1.insert(2,"Bolivia")
        self.listbox1.insert(3,"Paraguay")
        self.listbox1.insert(4,"Brasil")
        self.listbox1.insert(5,"Uruguay")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.mostrardatos)
        self.boton1.grid(column=0, row=4)        
        self.ventana1.mainloop()

    def mostrardatos(self):
         if len(self.listbox1.curselection())!=0:
            self.ventana1.title("Nombre:"+self.nombre.get()+" Pais:"+self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()