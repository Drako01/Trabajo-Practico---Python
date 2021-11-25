import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "INSERT INTO producto (titulo, ruta, descripcion) VALUES (%s, %s, %s)"
datos = ("Tema 3", "ruta3", "descripción 3")

micursor.execute(sql, datos)

mibase.commit()

print(micursor.rowcount, "Cantidad de registros agregados.")