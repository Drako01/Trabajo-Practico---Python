class Automovil:
    def iniciar(self,marca,modelo,kilometros,dueno):
        self.marca = marca
        self.modelo = modelo
        self.kilometros = kilometros
        self.dueno = dueno
    def imprimir(self):
        print("marca",self.marca)
        print("modelo",self.modelo)
        print("kilometros",self.kilometros)
        print("dueno",self.dueno)
        print(self.marca,self.modelo,self.kilometros,self.dueno)
auto1=Automovil()
auto1.iniciar("peugeot","308","150000","marcelo")
auto1.imprimir()

        