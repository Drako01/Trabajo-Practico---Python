#Condiciones compuestas con operadores lógicos

"""   
Hasta ahora hemos visto los operadores:

relacionales (>, <, >=, <= , ==, !=)
matemáticos (+, -, *, /, //, **, %)
pero nos están faltando otros operadores imprescindibles:

lógicos (and y or)
Estos dos operadores se emplean fundamentalmente en las estructuras condicionales para agrupar varias condiciones simples.
    """
"""DADOS 3 NUMEROS QUE NOS DEVUELVA EL MAYOR and"""
#AND
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
print("El mayor de los tres valores es")
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
"""DADA UNA FECHA NOS DEVUELVE SI PERTENECE AL PRIMER TRIMESTRE OR"""
#OR
dia=int(input("Ingrese nro de día:"))
mes=int(input("Ingrese nro de mes:"))
año=int(input("Ingrese nro de año:"))
if mes==1 or mes==2 or mes==3:
    print("Corresponde al primer trimestre")
    
    """Problemas propuestos
Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad.
Ver video

Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda "Todos los números son menores a diez".
Ver video

Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor a diez".
Ver video

Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.
Ver video

Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
Ver video

De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.
Ver video

Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)
Ver video
"""
#ejercicio21.py

dd=int(input("Ingrese nro de día:"))
mm=int(input("Ingrese nro de mes:"))
aa=int(input("Ingrese nro de año:"))
if mm==12 and dd==25:
    print("La fecha ingresada corresponde a navidad.")




#ejercicio22.py

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1<10 and num2<10 and num3<10:
    print("Todos los números son menores a diez")




#ejercicio23.py

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1<10 or num2<10 or num3<10:
    print("Alguno de los números es menor a diez")




#ejercicio24.py

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1==num2 and num1==num3:
    suma=num1+num2
    print("La suma del primero y segundo:")
    print(suma)
    producto=suma*num3;
    print("La suma del primero y segundo multiplicado por el tercero:")
    print(producto)



#ejercicio25.py

x=int(input("Ingrese coordenada x:"))
y=int(input("Ingrese coordenada y:"))
if x>0 and y>0:
    print("Se encuentra en el primer cuadrante")
else:
    if x<0 and y>0:
        print("Se encuentra en el segundo cuadrante")
    else:
        if x<0 and y<0:
            print("Se encuentra en el tercer cuadrante")
        else:
            print("Se encuentra en el cuarto cuadrante")
    



#ejercicio26.py

sueldo=int(input("Ingrese sueldo del empleado:"))
antiguedad=int(input("Ingrese su antiguedad en años:"))
if sueldo<500 and antiguedad>10:
    aumento=sueldo*0.20
    sueldototal=sueldo+aumento
    print("Sueldo a pagar")
    print(sueldototal)
else:
    if sueldo<500:
        aumento=sueldo*0.05
        sueldototal=sueldo+aumento
        print("Sueldo a pagar")
        print(sueldototal)
    else:
        print("Sueldo a pagar")
        print(sueldo)




#ejercicio27.py

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese tercer valor:"))
num3=int(input("Rango de valores:"))
if num1<num2 and num1<num3:
    print(num1)
else:
    if num2<num3:
        print(num2)
    else:
        print(num3)
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
