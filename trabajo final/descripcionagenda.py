""" QUE CORNNO ARMAMOS DE TODO ESTO
<<<<<<< HEAD

agenda

deficinicion de agenda
=======
ENTREGA TRABAJO DIPLOMATURA PYTHON NIVEL INICIAL
NOS QUEDAMOS CORTOS SI SOLO HACEMOS LA PARTE DE CONTACTOS... RECALCULANDO.... CORTOS

DESARROLLO DE UNA AGENDA:



Deficinicion de agenda: // OJO SIEMPRE AGENDA HABLA DE CALENDARIO ADEMAS DE CONTACTOS
1.
Libro o cuaderno donde se apuntan, para no olvidarlas, las cosas que se han de hacer en determinadas fechas; generalmente sus hojas llevan impresos los días del año ordenados por meses y por semanas con un espacio para escribir.
2.
Programa de actividades o de trabajo que pretende realizar una persona en un período determinado de tiempo.
"tener una agenda muy apretada"

Qué es Agenda:
Como agenda se denomina el programa que contiene, ordenadamente, un conjunto de temas, tareas o actividades para su realización en un periodo de tiempo determinado. Como tal, la palabra proviene del latín agenda, que significa ‘cosas que se han de hacer’.

OTRA DEFICINICION
Como agenda electrónica o digital se denomina el dispositivo electrónico de bolsillo 
que funciona como una agenda personal. Como tal, posee múltiples funciones orientadas 
a la gestión del tiempo, y tiene la capacidad de almacenar todo tipo datos, 
así como de organizar tareas y actividades. 
Combina programación de actividades, 
lista de contactos, 
bloc de notas, alarmas y recordatorios. 
Hoy día, no obstante, han sido desplazadas por aplicaciones que
se integran en el sistema operativo de computadoras personales, tablets y teléfonos inteligentes.






llave key logearse:

OBJETIVO DAR DE ALTA UN USUARIO Y UNA CLAVE PARA LA AGENDA

objetivo del proyecto:

en que se diferencia a una agenda comun y silvestre 
porque usaria esta un publico objetivo
segmentacion de los clientes
generaria codigo qr para discado automatico
generaria codigo qr para transferencia de datos a telefonia
>>>>>>> 43c82d9fdaca9e43512b0ff3b5f6f1455b9e05cd

* contactos


<<<<<<< HEAD
* cargar datos (tirarlos en un archivo de texto)
apellido, nombre, email, telefono,dni
=======

* cargar datos (tirarlos en un archivo de base de datos SQL)
apellido, nombre, email, telefono,dni, trabajo, direccion, localidad partido, sexo, fecha de naciminento

>>>>>>> 43c82d9fdaca9e43512b0ff3b5f6f1455b9e05cd

* PROCESO DE VERIFICACION a prueba de boludos
QUE PASA SI ES VACIO NO TOMO DATOS
QUE PASA SI INGRESA UN NUMERO TELEFONICO DE MAS DE 10 DIGITOS O CON ESPACIOS
QUE PASA SI INGRESA EN BLANCO UN CAMPO FUNDAMENTAL APELLIDO
O NOMBRE O DNI
QUE PASA SI ELMAIL NO TIENEN @

* PROCESO DE VERIFICACION a prueba de hijos de puta
* PROCESO DE NO DUPLICACION DE DATOS
    SI DATO DUPLICADO QUE HAGO? UNIFICO, ELIMINO
    REEMPLAZO SEGMENTO DEL DATO POR OTRO MAS NUEVO ACTUALIZO EL TELEFONO
    COMPLETO LO QUE FALTABA
    QUE PASA SI TIENE MAS DE UN TELEFONO
    QUE PASA SI TIENE MAS DE UN EMAIL
 
 
 funciones   
* almacenarlos (ALMACENAMIENTO CON FECHA Y HORA ASI PODEMOS VER DESDE CUANDO ES CONTACTO)
<<<<<<< HEAD
* actualizarlos
* buscarlos
    ULTIMOS CONTACTOS INGRESADOS
    POR FECHAS POR EJEMPLO EN EL ULTIMO MES. (NUEVOS CLIENTES)
=======
* editarlos
* buscarlos
    ULTIMOS CONTACTOS INGRESADOS (10 ultimos)
    POR FECHAS POR EJEMPLO EN EL ULTIMO MES. (NUEVOS CLIENTES) checkbox
>>>>>>> 43c82d9fdaca9e43512b0ff3b5f6f1455b9e05cd
    CONTACTOS CUYA CARACTERISTICA TELEFONICA SEA X
    CONTACTOS FEM MAS BIN TRIN ETC ETC
    CONTACTOS   POR APELLIDO 
                POR NOMBRE
    SEGMENTACION ETAREA POR EDADES O RANGOS ETAREOS
<<<<<<< HEAD
    y todos estos convinables tipo con checkbox
    y que por supuesto tire un listado tipo txt etc 

FRUTILLAS DEL POSTRE
 IMPORTACION Y EXPORTACION DE DATOS A OTRA AGENDA O TIPO DE AGENDAS
=======
    localidades etc etc
    YO COMO MEDICO AGREGARIA OBRA SOCIALLLLLLLLL JEJJEJEJJEEJJEJ
    
    y todos estos convinables tipo con checkbox
    y que por supuesto tire un listado tipo txt etc 

FRUTILLAS DEL POSTRE:

 generacion de codigo qr para discado automatico o transferencia a telefono celular
 
 IMPORTACION Y EXPORTACION DE DATOS A OTRA AGENDA O TIPO DE AGENDAS
 y lo que se me ocurrio se acuerdan vsc (formato de transferencia de contactos entre telefonos
 por ahi podemos hacer algo para esa funcionalidad extra)
>>>>>>> 43c82d9fdaca9e43512b0ff3b5f6f1455b9e05cd
 ESTO ES PARA VOS TINCHO PANDASSSSSSSSS



"""
<<<<<<< HEAD
print("saludos maromans")
=======
print("cagamos una agenda es mas jodida que un libro de contactos")


"""
TRABAJO FINAL DIPLOMATURA PYTHON UTN  elearning NIVEL INICIAL
------------------------------------------------------------------------------------------------------------

OBJETIVO DEL TRABAJO “Desarrollo de un aplicativo en python que utiliza  o no interfaz gráfica ( tkinter) cuya funcionalidad sea la de una agenda de datos que se vincule con tablas externas al programa, creadas por este, aplicando todo lo conocido y visto en el curso inicial de la diplomatura
 
------------------------------------------------------------------------------------------------------------
INTEGRANTES DEL TRABAJO
Nosotros

------------------------------------------------------------------------------------------------------------ 
DEFINICIÓN DE AGENDA:
 
Etimologia: la palabra agenda proviene de latin “agendum” (lo que se debe hacer), es su plural neutro (“cosas para hacer”) es la forma neutra del participio de futuro pasivo, es decir lo que esta en una agenda es algo a realizarse desde su etimología. Implica futuro de realización.
 
------------------------------------------------------------------------------------------------------------
 
DESARROLLO:
LA AGENDA DESARROLLADA CONSTA DE VARIOS MÓDULOS INTERRELACIONADOS

1. 	CONTACTOS
2. 	TAREAS
3. 	RECORDATORIOS
4. 	CALENDARIOS (CITAS DE CALENDARIO)
5. 	NOTAS CON ALARMA

------------------------------------------------------------------------------------------------------------
 
1) SENTANDO BASES DEFINIENDO ESTRUCTURAS TABLAS
 
2) INTERRELACIONADO  LAS ESTRUCTURAS

Con el fin de contestar estas dos premisas desarrollaremos cada uno de los módulos separadamente (forma de adquisición de datos), y luego accederemos a ellas desde una pantalla principal de nuestra aplicación. Realizado esto tendremos definidos los campos y las validaciones necesarias
 ------------------------------------------------------------------------------------------------------------

3) INGRESO DE DATOS (que definirán tablas)
4) VALIDACION DE LOS MISMOS ANTES DE INTEGRAR LAS TABLAS

------------------------------------------------------------------------------------------------------------
CONTACTOS
1. 	INGRESO DE DATOS: NOMBRE, APELLIDO, FECHA NAC, GENERO, DIRECCION, LOCALIDAD, TELEFONO, EMAIL
2. 	VERIFICACIÓN DE CAMPOS EN BLANCO
3. 	VERIFICACIÓN DE DUPLICACIÓN DE DATOS
4. 	VERIFICACIÓN TELEFONO SUPERIOR A 10 CIFRAS
5. 	VERIFICACIÓN DE EMAIL CONTENIENDO @
------------------------------------------------------------------------------------------------------------
        	           
TAREAS
1. 	VERIFICACIÓN DE INGRESO DE TAREAS
2. 	VERIFICACIÓN DE DATOS NO EN BLANCO
3. 	VERIFICACIÓN DE CAMPO DE FECHA MAYOR QUE CAMPO HOY
4. 	PRIORIDAD DE LA TAREA CREADA EN ESCALA DE 1 A 3
5. 	PORCENTAJE DE TAREA COMPLETADA
 ------------------------------------------------------------------------------------------------------------
RECORDATORIO
1. 	INGRESO DE DATOS
2. 	VERIFICACIÓN DE DATOS NO EN BLANCO
3. 	VERIFICACIÓN DE INCONSISTENCIAS
4. 	VERIFICACIÓN DE FECHAS MAYOR A LA FECHA ACTUAL
5. 	VERIFICACIÓN DE RECORDATORIO NO DUPLICADO
6. 	COLOCACIÓN O NO DE ALARMA
 ------------------------------------------------------------------------------------------------------------
NOTAS
1. 	INGRESO DE DATOS
2. 	VERIFICACIÓN DE DATOS NO EN BLANCO
3. 	VERIFICACIÓN DE INCONSISTENCIAS
4. 	VERIFICACIÓN DE FECHAS MAYOR A LA FECHA ACTUAL
5. 	VERIFICACIÓN DE RECORDATORIO NO DUPLICADO
6. 	COLOCACIÓN O NO DE ALARMA

------------------------------------------------------------------------------------------------------------


5) BÚSQUEDA DE DATOS POR:

CONTACTOS (APELLIDO, LOCALIDADES SEGMENTACIÓN (RANGO ETARIOS)
TAREAS (NOMBRE TAREA, UBICACION, FECHA TERMINACIÓN % DE REALIZACIÓN)
RECORDATORIOS (ASUNTO, FECHAS, PALABRAS CLAVE)
CALENDARIO (FECHAS)
NOTAS (ASUNTO, FECHA, PALABRAS CLAVE)
------------------------------------------------------------------------------------------------------------
           



"""
>>>>>>> 43c82d9fdaca9e43512b0ff3b5f6f1455b9e05cd
