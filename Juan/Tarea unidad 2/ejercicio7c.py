from tkinter import *
root = Tk()
root.config(bd=100)
e=Entry(root)
e.pack()
e.focus_set()


dic= {'Identificador': 'valor1', 'Nombre':'valor2', 'Apellido':'valor3', 'Telefono':'valor4'}

longitud = len(dic)  
longitud = str(longitud)  
claves = list(dic.keys()) 
claves = " - ".join(claves) 

texto = "los elementos del diccionario son : " 
texto01 = " y Las Claves son: "
c = texto + longitud + texto01 + claves

mensaje = Label(e, text=c)
mensaje.grid(row=1, column=2, columnspan=2)

var = IntVar()
e.config(textvariable=var)
var.set(c)

mainloop()