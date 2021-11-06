print("secuencia fibonaci")
a=0
b=1
ant=a
pos=b
for i in range(100):
    suma=(ant+pos)
    inverso=(1/suma)
    
    print((suma),"secuencia fibonaci ",(i),"inverso fibonaci  ",(inverso))
    ant=pos
    pos=(suma)
    aureo=(pos/ant)
    antiaureo=(ant/pos)
    print(("aurea proporcion ",aureo, " antiaureo", antiaureo))
