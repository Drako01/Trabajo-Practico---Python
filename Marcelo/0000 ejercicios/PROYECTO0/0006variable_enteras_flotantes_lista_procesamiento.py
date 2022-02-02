"""Variables enteras, flotantes y cadenas de caracteres

 
Hasta este momento hemos visto como definir variables enteras y flotantes. Realizar su carga por asignación y por teclado.

Para iniciarlas por asignación utilizamos el operador =

#definición de una variable entera
cantidad=20
#definición de una variable flotante
altura=1.92
Como vemos el intérprete de Python diferencia una variable flotante de una variable entera por la presencia del caracter punto.

Para realizar la carga por teclado utilizando la función input debemos llamar a la función int o float para convertir el dato devuelto por input:

cantidad=int(input("Ingresar la cantidad de personas:"))
altura=float(input("Ingresar la altura de la persona en metros ej:1.70:"))
A estos dos tipos de datos fundamentales (int y float) se suma un tipo de dato muy utilizado que son las cadenas de caracteres.

Una cadena de caracteres está compuesta por uno o más caracteres. También podemos iniciar una cadena de caracteres por asignación o ingresarla por teclado.

Inicialización de una cadena por asignación:

#definición e inicio de una cadena de caracteres
dia="lunes"
Igual resultado obtenemos si utilizamos la comilla simple:

#definición e inicio de una cadena de caracteres
dia='lunes'
Para la carga por teclado de una cadena de caracteres utilizamos la función input que retorna una cadena de caracteres:

nombre=input("ingrese su nombre:")
"""
#quien es mas alto, ingreso entero, string, float,
print("Datos de la primer persona")
nombre1=input("Ingrese nombre:")
edad1=int(input("Ingrese la edad:"))
altura1=float(input("Ingrese la altura Ej 1.75:"))
print("Datos de la segunda persona")
nombre2=input("Ingrese nombre:")
edad2=int(input("Ingrese la edad:"))
altura2=float(input("Ingrese la altura Ej 1.75:"))
print("La persona mas alta es:")
if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)
    
#opcion por teclado luego de un ingreso interesante
opcion="si"
suma=0
while opcion=="si":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    opcion=input("Desea cargar otro numero (si/no):")
print("La suma de valores ingresados es")
print(suma)


#orden alfabetico de 2 nombres
"""Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética.
"""
nombre1=input("Ingrese el primer nombre:")
nombre2=input("Ingrese el segundo nombre:")
print("Listado alfabetico:")
if nombre1<nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)
