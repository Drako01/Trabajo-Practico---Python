## Control de Stock de un Almacen
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021

uno=0
dos=0
tres=0
cuatro=0
tres1=0
cuatro1=0



print ("Bienvenido al Almacen")
print ("Hagamos un Control del Stock")
print ("Ingrese la Cantidad Actual de Mayonesa: ")
uno=int(input())
print ("Ingrese la Cantidad Actual de Mostaza: ")
dos=int(input())
print("En este momento tenemos : ", "Cantidad de Mayonesa: ",uno,"y", "Cantidad de Mostaza: ", dos)
print ("Recientemente realizo una Venta")
print ("Ingrese la Cantidad de Mayonesa que vendio: ")
tres=int(input())
print ("Ingrese la Cantidad de Mostaza que vendio: ")
cuatro=int(input())
tres1=uno-tres
cuatro1=dos-cuatro
print("Luego de la Ultima Venta tenemos: ", "Cantidad de Mayonesa: ",tres1,"y", "Cantidad de Mostaza: ", cuatro1)