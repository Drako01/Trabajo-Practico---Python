"""Implementaremos una clase llamada Persona 
que tendrá como atributo (variable) su nombre
y dos métodos (funciones), uno de dichos 
métodos inicializará el atributo nombre y el
siguiente método mostrará en la pantalla el
contenido del mismo."""
class Persona:
    
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()

persona3=Persona()
persona3.inicializar("jose")
persona3.imprimir()