## Promedio de Puntos por Temporada
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021

club=0
uno=0
dos=0
tres=0
suma=0
promedio=0


print ("Bienvenido al Fisture del Club!!")
print ("Ingrese el Nombre de su Club: ")
club=str(input())
print ("Puntaje de la Primer Temporada")
uno=int(input())
print ("Puntaje de la Segunda Temporada")
dos=int(input())
print ("Puntaje de la Tercera Temporada")
tres=int(input())
suma=uno+dos+tres
promedio=suma/3


print ("El Promedio de Puntos de", club,"es de: ",promedio)
