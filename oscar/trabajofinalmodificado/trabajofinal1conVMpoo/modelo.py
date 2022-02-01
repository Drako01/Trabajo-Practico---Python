import mysql.connector
import re


class conectar:
    def __init__(self) -> None:
        pass

    # creacion de la base de datos
    def crearBaseDatos(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost", user="root", passwd=""
            )
            self.miprimercursor = self.conexion.cursor()
            self.miprimercursor.execute("CREATE DATABASE Agenda_Contacto")
        except:
            print("La base Agenda_Contacto ya esta creada")

    # Creacion de la Tabla en la Base de Datos
    def crearTabla(self):
        self.conexion = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="Agenda_Contacto"
        )
        self.conexion.cursor().execute(
            "CREATE TABLE IF NOT EXISTS entidad( ID int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, DNI INT(8) COLLATE utf8_spanish2_ci NOT NULL, Apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Direccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL , Localidad VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Telefono VARCHAR(15) COLLATE utf8_spanish2_ci NOT NULL, Email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)"
        )

    # Funcion para conectar a la base de datos
    def conect_sql(self):
        self.mibase = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="Agenda_Contacto"
        )
        return self.mibase


class control:
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
        self.x = ingreso
        self.con = con
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.telefono = telefono
        self.email = email
        self.tabla = tabla

    # Definimos una Funcion para cambiar las Caracteristicas del Label
    def colorNegro(self):
        self.entrada3.config(
            fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6
        )

    def colorRojo(self):
        self.entrada3.config(
            fg="red", bg="Yellow", font=("Verdana", 10, "bold"), width=6
        )

    # Funcion para cargar un contacto
    def callback(self):
        try:

            if self.comparar_dni() == False:
                # Definimos la Validacion del EMail.!
                patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
                if re.match(patron, self.email.get()):
                    micursor = self.con.cursor()
                    sql = "INSERT INTO entidad (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
                    self.colorNegro()
                    self.x.set("Ud. Agrego al siguiente Contacto:")
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
                    self.colorRojo()
                    self.x.set("La Direccion de Mail NO es Valida")
            else:
                self.colorRojo()
                self.x.set("Ya existe ese Registro")
        except:
            self.colorRojo()
            self.x.set("Ud. no ingreso ningun Dni")

    # Funcion para buscar un contacto

    def busqueda(self):
        try:
            self.micursor = self.con.cursor()
            self.sql = "SELECT * FROM entidad WHERE DNI = {}".format(self.dni.get())
            self.micursor.execute(self.sql)
            self.registro = self.micursor.fetchall()
            if not self.registro == []:
                self.limpiar_tabla()
                self.x.set(f"{self.registro}")
                i = -1
                for dato in self.registro:
                    i = i + 1
                    self.tabla.insert(
                        "", i, text=self.registro[i][1:2], values=self.registro[i][2:8]
                    )
                self.colorNegro()
                self.x.set("Se encontraron los siguientes contactos.")

            else:
                self.colorRojo()
                self.x.set("No se encontro el contacto.")
        except:
            self.colorRojo()
            self.x.set("No se encontro el contacto.")

    # Funcion para modificar un contacto

    def modificar(self):
        self.patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
        if re.match(self.patron, self.email.get()):
            self.micursor = self.con.cursor()
            self.colorNegro()
            sql = "UPDATE entidad SET Apellido= %s, Nombre=%s, Direccion=%s, Localidad=%s, Telefono=%s, Email=%s WHERE DNI = %s"
            dato = (
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
            self.x.set(
                f"Se ha modificado el Contacto DNI: {dato[6]}, de Nombre: {dato[1]} {dato[0]}"
            )
        else:
            self.colorRojo()
            self.x.set("La Direccion de Mail NO es Valida")

    # Funcion para borrar un contacto

    def borrar(self):
        self.colorNegro()
        self.fila = self.tabla.selection()

        if len(self.fila) != 0:
            self.item = self.tabla.item(self.fila)
            self.valor = int(self.item["text"])

            self.micursor = self.con.cursor()
            self.sql = "DELETE FROM entidad WHERE dni = %s"
            self.dato = (self.valor,)

            self.micursor.execute(self.sql, self.dato)

            self.con.commit()
            self.x.set("Se ha borrado el Contacto")
            self.tabla.delete(self.fila)
            self.limpiar_entries()
        else:
            self.colorRojo()
            self.x.set("No se pudo Borrar el Contacto")

    # Funcion para cargar todos los contacto

    def listar(self):
        self.limpiar_tabla()
        self.micursor = self.con.cursor()
        self.sql = "SELECT * FROM entidad"
        self.micursor.execute(self.sql)
        self.registro = self.micursor.fetchall()

        if not self.registro == []:
            self.x.set(f"{self.registro}")
            i = -1
            for dato in self.registro:
                i = i + 1
                self.tabla.insert(
                    "", i, text=self.registro[i][1:2], values=self.registro[i][2:8]
                )
            self.colorNegro()
            self.x.set("Se encontraron los siguientes contactos.")
        else:
            self.colorRojo()
            self.x.set("No se encontro el contacto.")

    # Funcion para cargar en los entry el contacto seleccionado del treview "tabla"

    def item_elegido(
        self, tabla, dni, apellido, nombre, direccion, localidad, telefono, email
    ):
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

    # Funcion para limpiar los entry

    def limpiar_entries(self):
        self.dni.set("")
        self.apellido.set("")
        self.nombre.set("")
        self.direccion.set("")
        self.localidad.set("")
        self.telefono.set("")
        self.email.set("")

    # Funcion para limpiar la pantalla

    def limpiar_tabla(self):
        self.x.set("")
        self.tabla.delete(*self.tabla.get_children())
        self.limpiar_entries()

    # Funcion compara DNI

    def comparar_dni(self):
        self.micursor = self.con.cursor()
        self.sql = "SELECT * FROM entidad WHERE DNI = {}".format(self.dni.get())
        self.micursor.execute(self.sql)
        self.registro = self.micursor.fetchall()

        if not self.registro == []:
            return True
        else:
            return False
