from tkinter import *

root = Tk()
root.title("Entrada")
root.geometry("400x300")

nombre = StringVar()
apellido = StringVar()

nombre.set("Escribe aqui tu nombre")
apellido.set("Escribe aqui tu apellido")

def saludar():
    print("Hola "+nombre.get()+ " "+apellido.get())



etiqueta1 = Label(root, text="escribe aqui tu nombre: ")
etiqueta1.place(x=10, y=10)
entrada1 = Entry(root, textvariable=nombre)
entrada1.place(x=170, y=10)



etiqueta2 = Label(root, text="escribe aqui tu apellido: ")
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable=apellido)
entrada2.place(x=170, y=40)

boton1 = Button(root, text="saludar ahora", command=saludar)
boton1.place(x=10, y=100)








root.mainloop()