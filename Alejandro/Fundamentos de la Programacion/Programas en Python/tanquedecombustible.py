## Tanque de Combustible
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021

litros=0
precio=0
total=0

print ("Ingrese la capacidad en Litros que tiene el Tanque de Combustible de su Auto: ")
litros=float(input())
print ("Ingrese el precio de la Nafta en: $")
precio=float(input())
total=litros*precio
print ("Usted deberá Abonar un total de: $", total, "Pesos Argentinos por llenar su Tanque de",
litros," Litros de Combustible")
