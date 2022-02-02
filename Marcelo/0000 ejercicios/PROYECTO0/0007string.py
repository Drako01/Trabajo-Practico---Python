""" Procesar cadenas de caracteres

 
Ya hemos visto que podemos cargar una cadena de caracteres por asignación:

#con doble comillas
cadena1="juan"
#el resultado es igual con simple comillas
cadena2='ana'
También podemos cargarla por teclado:

nombre=input("Ingrese su nombre:")
Podemos utilizar los operadores relacionales para identificar si dos cadenas son iguales, distintas o cual es la mayor alfabética:

== Igualdad

!= Desigualdad

< menor

<= menor o igual

> mayor

>= mayor o igual
Como su nombre lo indica una cadena de caracteres está formada generalmente por varios caracteres (de todos modos podría tener solo un caracter o ser una cadena vacía)
Podemos acceder en forma individual a cada caracter del string mediante un subíndice:
"""
nombre='juan'
print(nombre[0])   #se imprime una j
if nombre[0]=="j": #verificamos si el primer caracter del string es una j
    print(nombre)
    print("comienza con la letra j")

"""Los subíndices comienzan a numerarse a partir del cero.

Si queremos conocer la longitud de un string en Python disponemos de una función llamada len que retorna la cantidad de caracteres que contiene:
"""
nombre='juan'
print(len(nombre))
"""
El programa anterior imprime un 4 ya que la cadena nombre almacena 'juan' que tiene cuatro caracteres.

Problema 1:
Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que lo componen.

Programa: ejercicio62.py
"""
nombre=input("Ingrese su nombre:")
print("Primer caracter")
print(nombre[0])
print("Cantidad de letras del nombre:")
print(len(nombre))
"""
Problema 2:
Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre.

Programa: ejercicio63.py

Ver video
"""
nombre=input("Ingrese su nombre:")
if nombre[0]=="a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print("El nombre ingresado comienza con vocal")
else:
    print("El nombre ingresado no comienza con vocal")
#Con que una de las condiciones del if sea verdadera luego se ejecuta el bloque del verdadero.
"""
Problema 3:
Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".

Programa: ejercicio64.py

Ver video
"""
mail=input("Ingrese un mail:")
cantidad=0
x=0
while x<len(mail):
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")
"""
Para analizar cada caracter del string ingresado disponemos una estructura while utilizando un contador llamado x que comienza con el valor cero y se repetirá tantas veces como caracteres tenga la cadena (mediante la función len obtenemos la cantidad de caracteres):

while x<len(mail):
Dentro del ciclo while verificamos cada caracter mediante un if y contamos la cantidad de caracterers "@":

    if mail[x]=="@":
        cantidad=cantidad+1
Cuando sale del ciclo while procedemos a verificar si el contador tiene almacenado el valor 1 y mostramos el mensaje respectivo:

if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")
Los string en Python son inmutables, esto quiere decir que una vez que los inicializamos no podemos modificar su contenido:
"""
nombre="juan"
#nombre[0]="m" #esto no se puede
#string inmutables python

#No hay que confundir cambiar parte del string con realizar la asignación de otro string a la misma variable, luego si es correcto asignar otro valor a un string:

nombre="juan"
print(nombre)
nombre="ana"
print(nombre)
#string inmutables python

#Métodos propios de las cadenas de caracteres.
#Los string tienen una serie de métodos (funciones aplicables solo a los string) que nos facilitan la creación de nuestros programas.

#Los primeros tres métodos que veremos se llaman: lower, upper y capitalize.
"""
upper() : devuelve una cadena de caracteres convertida todos sus caracteres a mayúsculas.
lower() : devuelve una cadena de caracteres convertida todos sus caracteres a minúsculas.
capitalize() : devuelve una cadena de caracteres convertida a mayúscula solo su primer caracter y todos los demás a minúsculas.
Problema 4:
Inicializar un string con la cadena "mAriA" luego llamar a sus métodos upper(), lower() y capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla.

Programa: ejercicio65.py

Ver video
"""
nombre1="mAriA"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4)
"""El resultado de ejecutar este programa es:

string python metodos upper(), lower() y capitalize()

Para llamar a un método del string debemos disponer entre el nombre del string y el método el caracter punto:

nombre2=nombre1.upper()
Es importante decir que el string nombre1 no se modifica su contenido (recordar que un string es inmutable) pero el método upper() retorna el contenido de la variable nombre1 pera convertida a mayúsculas. El dato devuelto se almacena en la variable nombre2.

Problemas propuestos
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es ""
Ver video

Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.
Ver video

Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.
Ver video

"""
#ejercicio66.py

oracion=input("Ingrese una oracion:")
cantidad=0
x=0
while x<len(oracion):
    if oracion[x]==" ":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de espacios en blanco ingresado son")
print(cantidad)




#ejercicio67.py


oracion=input("Ingrese una oracion:")
oracionmin=oracion.lower()
cantidad=0
x=0
while x<len(oracionmin):
    if oracionmin[x]=="a" or oracionmin[x]=="e" or oracionmin[x]=="i" or oracionmin[x]=="o" or oracionmin[x]=="u":
        cantidad=cantidad+1
    x=x+1
print("La cantidad de vocales de la oracion son")
print(cantidad)




#ejercicio68.py

clave=input("Ingrese una clave que tenga entre 10 y 20 caracteres:")
if len(clave)>=10 and len(clave)<=20:
    print("Largo correcto")
else:
    print("Largo incorrecto")

