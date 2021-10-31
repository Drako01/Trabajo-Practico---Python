print("Hola mundo")
print(2)
print("Hola a Todos")
# hola a todos
print(12112)
print("dejen de joder y entren por la pagina no hagamos tanto lio por favor se los pido")
print("HOla juan carlo")


#lista
from tkinter import*
ventana = Tk()
ventana.title("2.Ejercicio")
ventana.geometry("400x50")

lista1 = ["pera" ,"manzana"]
lista2 = [ "Al mediodia comi una " , " y en la facultad una " ]
ventana1 = (Label(text= lista2[0] + lista1[0] + lista2[1] + lista1[1])).pack()

mainloop()

#holalaaaaaaa

from tkinter import *
ventana = Tk()
ventana.title("2.Ejercicio")
ventana.geometry("400x50")

datos={"identificador":"val1","nombre":"juan","apellido":"labajian","telefono":"123456"}

ventana1=(Label(text="los elementos del diccionario son: "+(datos)+" y las claves son: "+(datos.keys))).pack()

mainloop()
