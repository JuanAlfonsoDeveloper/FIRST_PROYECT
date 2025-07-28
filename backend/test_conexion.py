import mysql.connector
print("✅ Script iniciado")

try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password=""   # ← vacío
    )
    print("✅ Conexión al servidor MySQL exitosa.")
    conexion.close()
except mysql.connector.Error as err:
    print("❌ Error de MySQL:", err)
except Exception as e:
    print("⚠️ Otro error:", e)
