class Operaciones:
    def __init__(self,x,y):#dentro del constructor puedo llamar otros metodos de la misma clase
        self.x=int(input("ingrese x "))
        self.y=int(input("ingrese y "))
        self.suma()
        self.resta()
        self.mult()
        self.division()

    def suma(self):
        print(("suma "),self.x+self.y)
    def resta(self):
        print(("resta "),self.x-self.y)
    def mult(self):
        print(("multip "),self.x*self.y)
    def division(self):
        print(("division "),self.x/self.y)

obj1=Operaciones(0,0)
obj1.suma()
obj1.resta()
obj1.mult()
obj1.division()