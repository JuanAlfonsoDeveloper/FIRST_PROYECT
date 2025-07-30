import pymysql

def conectar():
    try: 
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="db_first_proyect",
            port=3306
        )
        print("Conexion a la base de datos exitosa")
        return conexion
    except pymysql.MySQLError as e:
        print("Error al conectar la base de datos:", e)
        return None