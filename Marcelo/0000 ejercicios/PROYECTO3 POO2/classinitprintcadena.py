"""Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si es principiante (menos de 1000 puntos) o experto (1000 o más puntos)"""

class Jugador:
    
    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def __str__(self):
        cadena=self.nombre+"-"
        if self.puntaje<1000:
            cadena=cadena+"principiante"
        else:
            cadena=cadena+"experto"
        return cadena


# bloque principal

jugador1=Jugador("Juan",750)
jugador2=Jugador("Ana",1200)
print(jugador1)
print(jugador2)
