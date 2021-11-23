""" 
Ejercicio 1
Cree una función lambda que compruebe si un número es par o impar.
"""


num = int(input("Ingrese un número: "))

funcion1 = (
    lambda x: (f"El número {x} es par") if (x % 2 == 0) else (f"El nùmero {x} es impar")
)
print(funcion1(num))
