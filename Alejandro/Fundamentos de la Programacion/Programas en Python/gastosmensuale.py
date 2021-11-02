## Calculadora de Gastos mensuales
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021

bruto=0
luz=0
gas=0
celular=0
alquiler=0
escuela=0

print ("Bienvenido!!")
print ("Ingrese Su Sueldo Bruto Actual : $")
bruto=int(input())
print ("Cuanto gasto de Luz: $")
luz=int(input())
print ("Cuanto gasto de Gas: $")
gas=int(input())
print ("Cuanto gasto de Celular: $")
celular=int(input())
print ("Cuanto gasto de Alquiler: $")
alquiler=int(input())
print ("Cuanto gasto de Escuela de los Chicos: $")
escuela=int(input())

suma=luz+gas+celular+alquiler+escuela
total=bruto-suma
print ("El saldo Neto en su Cuenta es de: $",total)