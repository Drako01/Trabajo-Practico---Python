import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "SELECT * FROM producto"


micursor.execute(sql)
resultado = micursor.fetchall()
print(resultado)
for x in resultado:
    print(x)
