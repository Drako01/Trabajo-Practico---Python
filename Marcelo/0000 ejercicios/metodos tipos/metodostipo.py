class MethodTypes:
    
    name = "tipo de metodo "

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "metodo de instancia"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "metodo de clase"
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("metodo estatico")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()