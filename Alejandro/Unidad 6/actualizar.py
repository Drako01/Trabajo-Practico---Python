import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "UPDATE producto SET titulo = 'Titulo 8' WHERE titulo = 'Tema 3'"

micursor.execute(sql)
mibase.commit()

print(micursor.rowcount, "Cantidad de registros afectados.")