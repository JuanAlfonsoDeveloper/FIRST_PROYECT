import mysql.connector

print("✅ Script iniciado")

try:
    print("🔄 Intentando conectar a MySQL...")

    conexion = mysql.connector.connect(
        host="localhost",     # <-- cambia esto
        port=3306,            # <-- o prueba 3307
        user="root",
        password="",          # <-- vacío si no pusiste una
        database="db_first_proyect"
    )

    print("✅ Conexión establecida.")
    conexion.close()

except mysql.connector.Error as err:
    print("❌ Error de MySQL:", err)
except Exception as e:
    print("⚠️ Otro error:", e)
