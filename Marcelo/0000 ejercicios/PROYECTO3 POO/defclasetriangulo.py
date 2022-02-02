class triangulos:
    def iniciar(self,ca,co,hip):
        self.ca=ca
        self.co=co
        self.hip=hip
    
    def perimetro(self):
        print (self.ca+self.co+self.hip)
    
    def suma(self,a,b):
        self.a=a
        self.b=b
        print (self.a+self.b)

triangua = triangulos()
triangua.iniciar(12,20,25)
triangua.perimetro()
triangua.suma(10,20)