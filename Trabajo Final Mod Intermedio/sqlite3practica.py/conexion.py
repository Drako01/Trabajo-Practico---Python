import sqlite3 as sql # importo la libreria y cambio el nombre para acortar codigo

# funcion para crear base de datos
def crear_basedatos():
    conn = sql.connect("agenda.db")
    conn.commit()
    conn.close()
    
# funcion para crear tabla, al final el commit es para realizarpedido y cerramos conexion    
def crear_tabla():
    conn = sql.connect("agenda.db")    
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE agenda (
        name text,
        segudires integer,
        cantidad integer
        )"""
    )
    conn.commit()
    conn.close()

    

crearBaseDatos()
crearTabla()