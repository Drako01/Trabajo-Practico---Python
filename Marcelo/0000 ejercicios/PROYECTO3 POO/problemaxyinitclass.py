"""Problema 2:
Desarrollar una clase que represente un punto
en el plano y tenga los siguientes métodos:
inicializar los valores de x e y que llegan
como parámetros, imprimir en que cuadrante 
se encuentra dicho punto (concepto matemático
, primer cuadrante si x e y son positivas,
si x<0 e y>0 segundo cuadrante, etc.)"""

class Cuadrante:
    def __init__(self,x,y):
        self.x=int(input("el valor de x "))
        self.y=int(input("el valor de y "))
    
    def cuadrante1(self):
        if self.x>0 and self.y>0:
            print ("esta en cuadrante 1")
        else:
            print ("NO ESTA EN CUADRANTE 1")
    def cuadrante2(self):
        if self.x>0 and self.y<0:
            print ("esta en cuadrante 2")
        else:
            print ("NO ESTA EN CUADRANTE 2")
    def cuadrante3(self):
        if self.x<0 and self.y<0:
            print ("esta en cuadrante 3")
        else:
            print ("NO ESTA EN CUADRANTE 3")
    def cuadrante4(self):
        if self.x<0 and self.y>0:
            print ("esta en cuadrante 4")
        else:
            print ("NO ESTA EN CUADRANTE 4")

cuad1=Cuadrante(0,0)
cuad1.cuadrante4()
cuad1.cuadrante3()
cuad1.cuadrante2()
cuad1.cuadrante1()
        