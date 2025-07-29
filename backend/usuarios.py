from db import conectar
def registrar_usuario(nombre, apellido, correo, telefono, contraseña, direccion, id_rol):
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO usuario ( 
            nombre_usuario, apellido_usuario, correo_usuario, 
            telefono_usuario, contraseña_usuario, direccion_usuario, id_rol
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        datos = (nombre, apellido, correo, telefono, contraseña, direccion, id_rol)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Usurio registrado correctamente")
    except Exception as e:
        print("Error al registrar Usuario", e)
    finally:
        conexion.close()