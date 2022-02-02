#CONDICIONAL SIMPLE solo rama verdad

#si el sueldo que ingresamos supera 3000 dolares se mostrará por pantalla el mensaje "Esta persona debe abonar impuestos"
sueldo=int(input("Ingrese cual es su sueldo:"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")


#CONDICIONAL COMPLEJA  una rama verdad una rama falso

num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)
"""
                Operadores Relacionales:
== Igualdad
!= Desigualdad
< menor
<= menor o igual
> mayor
>= mayor o igual

                Operadores Matemáticos
+ suma
- resta
* multiplicación
/ división de flotantes
// división de enteros
% resto de una división
** exponenciación  
    """


#ejercicio11.py

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
if num1>num2:
    suma=num1+num2
    print("La suma de los dos valores es")
    print(suma)
    resta=num1-num2
    print("La diferencia de los dos valores es")
    print(resta)
else:
    producto = num1*num2;
    print("El producto de los dos valores es")
    print(producto)
    division = num1/num2;
    print("La división de los dos valores es")
    print(division)




#ejercicio12.py

nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("INgrese la tercer nota:"))
promedio=(nota1 + nota2 + nota3)/3
if promedio>=7:
    print("Promocionado")




#ejercicio13.py

num=int(input("Ingrese un valor entero de 1 o 2 dígitos:"))
if num<10:
    print("Tiene un dígito")
else:
    print("Tiene dos dígitos")


#CONDICIONAL ANIDADA un condicional dentro de otro


# numero cero o positivo o negativo

num=int(input("Ingrese un valor:"))
if num==0:
    print("Se ingresó el cero")
else:
    if num>0:
        print("Se ingresó un valor positivo")
    else:
        print("Se ingresó un valor negativo")
            