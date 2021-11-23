"""
Ejercicio 4
Crear una función lambda que sea equivalente a la siguiente función:

def sumar(valor1, valor2):
        res = valor1 + valor2    # se puede llegar a usar return valor1 + valor2
        return res               # para no crear la variable res?     

"""

x = 4
y = 7

sumar = lambda valor1, valor2: valor1 + valor2

print(sumar(x, y))
