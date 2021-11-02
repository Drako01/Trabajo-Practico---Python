//Autor: Alejandro Di Stefano
//Fecha: 08/09/2021
//Descripcion del Programa: Desarrollar un programa en pseudocódigo que permita ingresar 
//los resultados de una (UNA) urna electoral para las elecciones del domingo en Argentina.

programa: VotacionesDelDomingo

Inicio
     funcion contarVotos ()   //Se define la funcion "contar los votos"
        var string partido
        var integer partido_a = 0
        var integer partido_b = 0
        var integer partido_c = 0
        var string voto 
        
        mostrar: "En caso que haya Votos para contar, Ingresar si o no: "
        ingresar: voto
        mientras  voto = "si" hacer 
            mostrar: "Que partido esta Ingresando?: "
            contarVotos (partido)
                si partido = "Partido A" entonces
                    partido_a = partido_a + 1                                       
                sino contarVotos ()
                    si partido  = "Partido B" entonces                       
                        partido_b = partido_b + 1                                                                
                    sino contarVotos ()
                        si partido  = "Partido C" entonces                       
                            partido_c = partido_c + 1                                                                      
                        sino contarVotos ()
                        fin si
                    fin si     
                fin si
        sino
            mostrar: "Fin de recuento"           

        fin mientras
        mostrar: "Se contabilizaron :" + partido_a + "de Votos"
        mostrar: "Se contabilizaron :" + partido_b + "de Votos"
        mostrar: "Se contabilizaron :" + partido_c + "de Votos"  
    fin funcion
Fin
