Ejercicio 6
Repita el ejercicio 5 pero en lugar de una lista utilice un diccionario.

sumando1=int(input("ingrese sumando1 "))
sumando2=int(input("ingrese sumando2 "))
resultado=sumando1+sumando2
print (sumando1)
print(sumando2)
print (resultado)

diccionario={"sumando1":sumando1,"sumando2":sumando2,"suma":resultado}

print (diccionario.keys())
print (diccionario.values())
a=len(diccionario)
print (f"numero de elementos del diccionario {a}")
