programa: CuentoDeVotos
inicio
	//tienen que se globales, porque sino se pierden cada vez que sale de la funcion
	var integer pA
	var integer pB
	var integer pC

    funcion principal ()
        var string partidoElegido //Esta variable se utiliza para ingresar el partido elegido
        var string siONo //Esta variable se utiliza para saber si quedan votos por contar o no

        mostrar: "Ingrese SI si hay votos por contar. De lo contrario, ingrese NO"
        ingresar: siONO

        mientras siONo = "SI" hacer
            mostrar: "Por favor, ingrese el nombre del partido seleccionado en mayusculas"
            ingresar: partidoElegido
            cuentoDeVotos (partidoElegido)
            ingresar: siONo
        fin mientras

		mostrar: "El recuento de votos ha terminado"
		//los votos ya est�n contados, no hace falta ir a contarlos de nuevo
		//mostrar: "Los votos del PARTIDO A fueron" + cuentoDeVotos (pA)
		//mostrar: "Los votos del PARTIDO B fueron" + cuentoDeVotos (pB)
		//mostrar: "Los votos del PARTIDO B fueron" + cuentoDeVotos (pC)
		mostrar: "Los votos del PARTIDO A fueron" + pA
		mostrar: "Los votos del PARTIDO B fueron" + pB
		mostrar: "Los votos del PARTIDO B fueron" + pC

    fin funcion

    funcion cuentoDeVotos(string pE) //no es necesario que devuelve nada
        //var string pE  variable duplicada
        en caso de pE hacer
            caso pE = "PARTIDO A"
            	pA = pA + 1
            fin caso
            caso pE = "PARTIDO B"
                pB = pB + 1
            fin caso
            caso pE = "PARTIDO C"
                pC = pC + 1
            fin caso
        fin en caso de

 	fin funcion
fin