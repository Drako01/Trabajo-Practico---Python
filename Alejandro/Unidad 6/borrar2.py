import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mi_plantilla2"
)
micursor = mibase.cursor()
a = input()
sql = "DELETE FROM producto WHERE id = %s"
dato = (a,)

micursor.execute(sql, dato)

mibase.commit()

print(micursor.rowcount, "Registro borrado")
