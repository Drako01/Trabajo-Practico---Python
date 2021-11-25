import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "INSERT INTO producto (titulo, ruta, descripcion) VALUES (%s, %s, %s)"
datos = [("Tema 4", "ruta4", "descripción 4"),
    ("Tema 5", "ruta5", "descripción 5"),
    ("Tema 6", "ruta6", "descripción 6"),
]

micursor.executemany(sql, datos)

mibase.commit()

print(micursor.rowcount, "Cantidad de registros agregados.")