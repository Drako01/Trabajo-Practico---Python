from tkinter import*
ventana = Tk()
ventana.title("ejercicio 7b")
ventana.geometry("300x50")

lista1 = ["manzana" ,"banana"]
lista2 = [ "Fui a comprar una  " , " y una " ]
ventana1 = (Label(text= lista2[0] + lista1[0] + lista2[1] + lista1[1])).pack()

mainloop()