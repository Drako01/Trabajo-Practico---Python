"""aca me surgio un problema en este ejercio que no me permitia ver una proporcion de pares e impares estadistica por lo que desarrolle e hice la comprovacion estadistica sumando los pare es impares para ver que estaba fallando"""""""DEFINICION DE METODO SACADA DE LOS PELOSpor lo que observo un metodo es como unsubprograma que necesita de parametros queirian despues del punto para una cualidaden particular(RANGO intervalo) de ese metodo en este caso.V.g "generar numeros aleatorios entre 1 y 100"lo que no comprendo es que haria el 3 parametro steplo que observe es que SOLO DA PARES PORQUE?"""print(" the ramdon crazy man")import randompar=0#para contar los paresimpar=0#para contar los imparescont=0# para contar las operacioneswhile cont<100:# busque algun metodo de ejecutar controlado el programa 100 veces mientras cont sea menor que 100 se ejecuta    #a = 1#asigne a a el valor 1 AHI ES DONDE VARIA     b = random.randrange(0,100,1) # segui usando los 3 parametros    #c = a * b     #print (c)    print(b) #imprimo b    if b % 2 == 0: # si el resto de la division (2) da resto cero es par        par=par +1 #incremento contador de pares    else: # si el resto de la division fue distinto de cero        impar=impar+1#incremento contador de pares    cont=cont+1 # aumento el contador una unidad que ejecuta el programaprint(f"pares {par}  impares {impar}")#imprimo la suma de los pares y los imparesprint("finalizado")#terminado""" las lineas que eran codigo en el anterior las comente asi por las dudas habia que volverlas a escribir no perdia mucho tiempo"""        """LUEGO DE MUCHAS PRUEBAS LLEGUE A LA CONCLUSION QUE EL TERCER PARAMETRO, ES PARA VER CUANTOS CALCULOS ESTADISTICOS HACE ANTES DE ASIGNAR AL NUMERO ESTADISTICO, IGUAL NO ESTOY CONVENCIDO DE ESTO DE TODAS MANERAS HABRA QUE INVESTIGARLOPIDO DISCULPAS A LOS QUE SE LES VALLA DE LAS MANOS EL PROGRAMA PERO ME VI EN EL DESAFIO DE VER SI LA ESTADISTICA ERA REAL YA QUE AL PRINCIPIO SOLO ME DABA PARES"""