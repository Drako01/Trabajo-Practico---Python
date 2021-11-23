l={"clave1":"val1","clave2":"val2","clave3":"val3"}

print("Ingrese el primer valor")
l["clave1"]=input()
print("ingrese el segundo valor")
l["clave2"]=input()
l["clave1"]=int(l["clave1"])
l["clave2"]=int(l["clave2"])
l["clave3"]=l["clave1"]+l["clave2"]

print(l)