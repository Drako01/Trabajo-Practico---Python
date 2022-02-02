class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def imprimir(self):
        print ("nombre: ",self.nombre)
        print ("nota: ",self.nota)
    def mostrar_estado(self):
        if self.nota>=6:
            print("aprobado")
        else:
            print("desaprobado")

alumno1=Alumno()
alumno1.inicializar("juan",8)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("celeste",5)
alumno2.imprimir()
alumno2.mostrar_estado()