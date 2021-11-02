## Producto con IVA
## Autor: Alejandro Di Stefano
## Fecha 21/08/2021

uno=0
dos=0
tres=0
iva=0


print ("Ingrese el Precio que pago por el Producto en $: ")
uno=float(input())
print ("Ingrese el Porcentaje de IVA del Producto: ")
iva=float(input())
print ("Usted esta pagando de IVA: ")
dos=uno*(iva/100)
print("$",dos)
print ("El Valor Real del Producto mas el IVA es: $",uno)
tres=uno-dos
print("Valor Real del Producto: $",tres, "y lo que pago de IVA es: $",dos,)
