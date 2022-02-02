"""Desarrollar una clase que represente un Cuadrado
y tenga los siguientes métodos:
    inicializar el valor del lado 
    llegando como parámetro al método
    __init__ (definir un atributo llamado
lado), imprimir su perímetro y su superficie."""

class Cuadrado:
    def __init__ (self,lado):
        self.lado=int(input("el valor de lado "))
    def perimetro(self):
        print(("perimetro "),self.lado*4)
    def superficie(self):
        print(("superficie "),self.lado*self.lado)

cuad1 = Cuadrado(0)
cuad1.perimetro()
cuad1.superficie()
print("programa finalizado")

