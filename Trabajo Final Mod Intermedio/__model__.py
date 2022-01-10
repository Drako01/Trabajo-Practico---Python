# Base datos
import sqlite3
from sqlite3 import Error

# creacion de la base de datos
def conectar():
    try:
        con = sqlite3.connect("Agenda_Contacto.db")
        return con
    except Error:
        print(Error)

def crear_bbdd():
    try:
        con = sqlite3.connect("Agenda_Contacto.db")
    except Error:
        print(Error)
    finally:
        con.close()    

# Creacion de la Tabla en la Base de Datos
def crear_tabla(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS entidad( id INTEGER PRIMARY KEY " + \
            "AUTOINCREMENT, DNI INT(8) COLLATE utf8_spanish2_ci NOT NULL " + \
            "Apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, " + \
            "Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Direccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,  " + \
            "Localidad VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,  Telefono VARCHAR(15) COLLATE utf8_spanish2_ci NOT NULL, " + \
            "Email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)"
    )
