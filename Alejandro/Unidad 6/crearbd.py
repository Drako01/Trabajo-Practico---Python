import mysql.connector

mibase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
micursor = mibase.cursor()

micursor.execute("CREATE DATABASE mi_plantilla2")
