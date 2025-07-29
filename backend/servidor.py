import pymysql

print("🔍 Probando conexión a MariaDB de XAMPP con PyMySQL...")

try:
    conexion = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",     # Vacío por defecto en XAMPP
        database="db_first_proyect"  # Cambia por el nombre de tu base de datos
    )
    print("✅ Conexión exitosa a la base de datos")
    conexion.close()

except pymysql.MySQLError as e:
    print("❌ Error de conexión:", e)
