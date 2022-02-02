"""Plantear una clase llamada Jugador. 
Definir en la clase Jugador los atributos nombre y puntaje, 
y los métodos __init__, imprimir y pasar_tiempo 
(que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase 
que indique cuantos minutos falta para el fin de juego 
(iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero."""

class Jugador:
    tiempo=30 #VARIABLE DE CLASE

    def __init__(self, nombre, puntaje):#Definir en la clase Jugador los atributos nombre y puntaje,
        self.nombre=nombre
        self.puntaje=puntaje

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Puntaje:",self.puntaje)
        print("Fin de juego en",Jugador.tiempo,"minutos")

    def pasar_minuto(self):
        Jugador.tiempo=Jugador.tiempo-1


# bloque principal

jugador1=Jugador("Juan",100)
jugador2=Jugador("Ana",50)
while Jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minuto()