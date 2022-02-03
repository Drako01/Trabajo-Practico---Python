from tkinter import *
root = Tk()
# Obtenga el tamaño de la pantalla para que la ventana esté en el centro de la pantalla
width = 380
heigh = 300
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))

mainloop()