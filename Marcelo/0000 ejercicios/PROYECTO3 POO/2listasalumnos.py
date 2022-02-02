"""Plantear una clase que administre dos 
listas de 5 nombres de alumnos y sus notas.
Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa."""


class carga:
    def __init__(self,a1,a2,b1,b2,c1,c2,d1,d2,e1,e2):#ingresa los nombres y las nota
        self.a1=input("ingrese alumno 1 ")
        self.a2=int(input("nota alumno 1 "))
        self.b1=input("ingrese alumno 2 ")
        self.b2=int(input("nota alumno 2 "))
        self.c1=input("ingrese alumno 3 ")
        self.c2=int(input("nota alumno 3 "))
        self.d1=input("ingrese alumno 4 ")
        self.d2=int(input("nota alumno 4 "))
        self.e1=input("ingrese alumno 5 ")
        self.e2=int(input("nota alumno 5 "))
    def present(self):
        print(self.a1,self.a2)
        print(self.b1,self.b2)
        print(self.c1,self.c2)
        print(self.d1,self.d2)
        print(self.e1,self.e2)
    def sobre7(self):
        if self.a2>6:
            print("alumno "),self.a1,(" con buena nota "),self.a2,self
        else:
            print("alumno "),self.a1,(" con baja nota "),self.a2,self
        if self.b2>6:
            print("alumno "),self.b1,(" con buena nota "),self.b2,self
        else:
            print("alumno "),self.b1,(" con baja nota "),self.b2,self
        if self.c2>6:
            print("alumno "),self.c1,(" con buena nota "),self.c2,self
        else:
            print("alumno "),self.c1,(" con baja nota "),self.c2,self
        if self.d2>6:
            print("alumno "),self.d1,(" con buena nota "),self.d2,self
        else:
            print("alumno "),self.d1,(" con baja nota "),self.d2,self
        if self.e2>6:
            print("alumno "),self.e1,(" con buena nota "),self.e2,self
        else:
            print("alumno "),self.e1,(" con baja nota "),self.e2,self
                
obj1=carga(0,0,0,0,0,0,0,0,0,0,)
obj2=carga(0,0,0,0,0,0,0,0,0,0,)
obj1.present()
obj2.present()
obj1.sobre7()
obj2.sobre7()