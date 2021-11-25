import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mi_plantilla2"
)
micursor = mibase.cursor()

micursor.execute("CREATE TABLE IF NOT EXISTS producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta varchar(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
