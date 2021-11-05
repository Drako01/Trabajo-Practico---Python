num = int(input("Ingrese un numero positivo entero: "))


if num > 0:
    fact = 1
    x = num
    for i in range(x):
        fact *= x
        x -= 1
    print("El factorial de ", num, "es ", fact, ".")
else:
    num <= 0
    print("No es posible obtener factorial de un numero menor a 1")
