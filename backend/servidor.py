from db import conectar
conexion = conectar()
if conexion:
    cursor = conexion.cursor()
    cursor.execute("SHOW TABLES;")
    tablas = cursor.fetchall()
    print("Tablas encontradas en la base de datos")
    for tabla in tablas:
        print("-", tabla[0])