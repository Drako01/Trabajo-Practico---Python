"""Se define el modulo modelo   ."""

import sqlite3
from sqlite3 import Error
import re
from tkinter import TclError


class Conectando:
    """En la clase Conectando se definen 4 metodos:
    metodo conectar: para la base de datos Agenda_Contacto con motor sqlite3
    metodo crear_bbdd: realiza la conecion a la base, con Regex
    metodo cursor_obj: se define cursor
    metodo crear_tabla: metodo que llama al cursor para crear la tabla Entidad,
    en caso de no existir no la crea."""

    def conectar(self):
        """Metodo que define la conexion en sqlite3."""

        con = sqlite3.connect("Agenda_Contacto")
        return con

    def crear_bbdd(self):
        """Metodo que crea la Base de Dato Agenda_Contacto."""

        try:
            self.conectar()
            print("Base de Dato Agenda_Contacto")
        except IndexError as error:
            print(error)
            excepcion = IndexError("La Base de Datos no fue creada.!")
            raise excepcion
        finally:
            self.conectar().close()

    def cursor_obj(self):
        """Metodo que define el cursor a partir del metodo conectar."""

        return self.conectar().cursor()

    def crear_tabla_usuario(self):
        """Metodo que crea la base usuario."""

        self.cursorObj().execute(
            "CREATE TABLE IF NOT EXISTS usuario_app(id INTEGER PRIMARY KEY AUTOINCREMENT, usuario VARCHAR(128) NOT NULL, contraseña VARCHAR(128) NOT NULL)"
        )
        self.conectar().commit()
        self.conectar().close()
        
        
    def crear_tabla(self):
        """Metodo que crea la base tabla entidad."""

        self.cursor_obj().execute(
            "CREATE TABLE IF NOT EXISTS entidad(id INTEGER PRIMARY KEY AUTOINCREMENT, DNI integer(8) NOT NULL, Apellido VARCHAR(128) NOT NULL, Nombre VARCHAR(128) NOT NULL, Direccion VARCHAR(128) NOT NULL, Localidad VARCHAR(128) NOT NULL, Telefono VARCHAR(15) NOT NULL, Email VARCHAR(128) NOT NULL)"
        )
        self.conectar().commit()
        self.conectar().close()

class control_usuario:
    """Clase de loguin """
    def __init__(
        self, 
        usuario,
        contraseña,  
        tabla0,
    ):
        self.usuario = usuario
        self.contraseña = contraseña
        self.tabla0 = tabla0

class Control:
    """Clase que le da funcionalidad a los Widget Button.
    En la clase Control se definen 12 metodos."""

    def __init__(
        self,
        entrada3,
        ingreso,
        con,
        dni,
        apellido,
        nombre,
        direccion,
        localidad,
        telefono,
        email,
        tabla,
    ):
        self.entrada3 = entrada3
        self.mensaje = ingreso
        self.con = con
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.telefono = telefono
        self.email = email
        self.tabla = tabla
        self.patron_email = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
        self.patron_telefono = (
            r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"
        )

    def color_negro(self):
        """Metodo para cambiar las Caracteristicas del mensaje de texto a negro."""

        self.entrada3.config(
            fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6
        )

    def colo_rojo(self):
        """Metodo para cambiar las Caracteristicas del mensaje de texto a rojo."""

        self.entrada3.config(
            fg="red", bg="Yellow", font=("Verdana", 10, "bold"), width=6
        )

    # Funcion para cargar un usuario
    def logueo(self):
        micursor = con.cursor()
        sql = "INSERT INTO usuario_app (usuario, contraseña) VALUES (?,?)"
        datos = (
            self.usuario.get(),
            self.contraseña.get(),
        )
        micursor.execute(sql, datos)
        con.commit()
        self.tabla.insert(
        "",
        "end",
        )        

    def callback(self):
        """Definimos el metodo callback para cargar un contacto,
        verificando las siguientes condiciones:
        Que el campo DNI sea un valor entero.
        Que el registro no exista en la base.
        Definimos la Validacion del EMail.
        Definimos la Validacion del Telefono iniciando con +5411111111
        Excepciones: dni.get != IntVar."""

        try:
            if self.dni.get() != "":
                if self.comparar_dni() is False:
                    if re.match(self.patron_email, self.email.get()):
                        if re.match(self.patron_telefono, self.telefono.get()):
                            micursor = self.con.cursor()
                            sql = "INSERT INTO entidad (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail) VALUES (?,?,?,?,?,?,?)"
                            datos = (
                                self.dni.get(),
                                self.apellido.get(),
                                self.nombre.get(),
                                self.direccion.get(),
                                self.localidad.get(),
                                self.telefono.get(),
                                self.email.get(),
                            )
                            micursor.execute(sql, datos)
                            self.con.commit()
                            self.color_negro()
                            self.mensaje.set(
                                "Ud. Agrego al siguiente Contacto:")
                            self.tabla.delete(*self.tabla.get_children())
                            self.tabla.insert(
                                "",
                                "end",
                                text=self.dni.get(),
                                values=[
                                    self.apellido.get(),
                                    self.nombre.get(),
                                    self.direccion.get(),
                                    self.localidad.get(),
                                    self.telefono.get(),
                                    self.email.get(),
                                ],
                            )
                            self.limpiar_entries()
                        else:
                            self.colo_rojo()
                            self.mensaje.set(
                                "El Telefono Ingresado no es Valido")
                    else:
                        self.colo_rojo()
                        self.mensaje.set("La Direccion de Mail NO es Valida")
                else:
                    self.colo_rojo()
                    self.mensaje.set("Ya existe ese Registro")
        except TclError:
            self.colo_rojo()
            self.mensaje.set("Ud. no ingreso ningun DNI")

    # Metodo para buscar un contacto

    def busqueda(self):
        """Definimos el metodo busqueda,
        verificando la existencia del contacto e
        informando mediante un mensaje si se haya o no."""

        try:
            self.micursor = self.con.cursor()
            self.micursor.execute(
                "SELECT * FROM entidad WHERE DNI =:documento",
                {"documento": self.dni.get()},
            )
            self.registro = self.micursor.fetchall()
            if not self.registro == []:
                self.limpiar_tabla()
                self.mensaje.set(f"{self.registro}")
                i = -1
                for dato in self.registro:
                    i = i + 1
                    self.tabla.insert(
                        "", i, text=self.registro[i][1:2], values=self.registro[i][2:8]
                    )
                self.color_negro()
                self.mensaje.set("Se encontraron los siguientes contactos.")

            else:
                self.colo_rojo()
                self.mensaje.set("No se encontro el contacto.")
        except TclError:
            self.colo_rojo()
            self.mensaje.set("No ingreso ningun DNI.")

    # Metodo para modificar un contacto

    def modificar(self):
        """Definimos el metodo modificar,
        verificando la existencia del contacto e
        informando mediante un mensaje si se haya o no."""

        self.patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
        if re.match(self.patron, self.email.get()):
            self.micursor = self.con.cursor()
            self.color_negro()
            sql = "UPDATE entidad SET (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail)=(?,?,?,?,?,?,?)WHERE DNI=?"
            dato = (
                self.dni.get(),
                self.apellido.get(),
                self.nombre.get(),
                self.direccion.get(),
                self.localidad.get(),
                self.telefono.get(),
                self.email.get(),
                self.dni.get(),
            )
            self.micursor.execute(sql, dato)
            self.con.commit()
            self.listar()
            self.limpiar_entries()
            self.mensaje.set(
                f"Se ha modificado el Contacto DNI: {dato[0]}, de Nombre: {dato[2]} {dato[1]}"
            )
        else:
            self.colo_rojo()
            self.mensaje.set("La Direccion de Mail NO es Valida")

    # Metodo para borrar un contacto

    def borrar(self):
        """Definimos el metodo modificar."""

        self.color_negro()
        self.fila = self.tabla.selection()

        if len(self.fila) != 0:
            self.item = self.tabla.item(self.fila)
            self.valor = int(self.item["text"])

            self.micursor = self.con.cursor()
            sql = "DELETE FROM entidad WHERE DNI=?"
            self.micursor.execute(sql, (self.valor,))

            self.con.commit()
            self.mensaje.set("Se ha borrado el Contacto")
            self.tabla.delete(self.fila)
            self.limpiar_entries()
        else:
            self.colo_rojo()
            self.mensaje.set("No se pudo Borrar el Contacto")

    # Metodo para cargar todos los contacto

    def listar(self):
        """Definimos el metodo listar."""

        self.limpiar_tabla()
        self.micursor = self.con.cursor()
        self.sql = "SELECT * FROM entidad"
        self.micursor.execute(self.sql)
        self.registro = self.micursor.fetchall()

        if not self.registro == []:
            self.mensaje.set(f"{self.registro}")
            i = -1
            for dato in self.registro:
                i = i + 1
                self.tabla.insert(
                    "", i, text=self.registro[i][1:2], values=self.registro[i][2:8]
                )
            self.color_negro()
            self.mensaje.set("Se encontraron los siguientes contactos.")
        else:
            self.colo_rojo()
            self.mensaje.set("No se encontro el contacto.")

    # Metodo para cargar en los entry el contacto seleccionado del treview "tabla"

    def item_elegido(
        self, tabla, dni, apellido, nombre, direccion, localidad, telefono, email
    ):
        """Definimos el metodo item_elegido."""

        for selec in tabla.selection():
            item = tabla.item(selec)
            record = item["values"]
            dni.set(item["text"])
            apellido.set(record[0])
            nombre.set(record[1])
            direccion.set(record[2])
            localidad.set(record[3])
            telefono.set(record[4])
            email.set(record[5])

    def limpiar_entries(self):
        """Metodo para limpiar los entry."""

        self.dni.set("")
        self.apellido.set("")
        self.nombre.set("")
        self.direccion.set("")
        self.localidad.set("")
        self.telefono.set("")
        self.email.set("")

    # Metodo para limpiar la pantalla

    def limpiar_tabla(self):
        """Metodo para limpiar la tabla."""

        self.mensaje.set("")
        self.tabla.delete(*self.tabla.get_children())
        self.limpiar_entries()

    def comparar_dni(self):
        """Metodo para comparar los DNI."""

        con = sqlite3.connect("Agenda_Contacto")
        self.micursor = con.cursor()
        self.micursor.execute(
            "SELECT * FROM entidad WHERE DNI =:documento", {
                "documento": self.dni.get()}
        )
        self.registro = self.micursor.fetchall()

        if not self.registro == []:
            return True
        else:
            return False
