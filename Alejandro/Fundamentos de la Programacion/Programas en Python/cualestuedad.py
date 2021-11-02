## Cual es mi Edad actual
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021


from datetime import date

def calcular_años(fecha_naciento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_naciento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_naciento.month, fecha_naciento.day))
    return resultado
ano=0
mes=0
dia=0
print ("Calculemos su Edad")
print ("Ingrese el Año de su Nacimiento: ")
ano=int(input())
print ("Ingrese el Mes de su Nacimiento: ")
mes=int(input())
print ("Ingrese el Día de su Nacimiento: ")
dia=int(input())
fecha_nacimiento = date(ano, mes, dia )
edad = calcular_años(fecha_nacimiento)

print(f"Usted tiene: {edad}", "Años de Edad")