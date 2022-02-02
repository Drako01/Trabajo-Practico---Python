class Cliente:
    
    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto

    def __add__(self,objeto2):
        s=cli1.monto+objeto2.monto
        return s

cli1=Cliente('Ana',1700)
cli2=Cliente('Luis',1500)
print("El total depositado por los dos clientes es")
print(cli1+cli2)
