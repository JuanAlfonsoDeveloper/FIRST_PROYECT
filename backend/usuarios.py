from db import conectar
import hashlib

def registrar_usuario():
    print("Registrar Usuario")

    nombre = input("Digite su nombre: ")
    apellido = input("Digite su apellido: ")
    correo = input("Digite su correo: ")
    telefono = input("Digite su telefono: ")
    contraseña = input("Digite su contraseña: ")
    direccion = input("Digite su direccion: ")
    id_rol = input("Digite su codigo del rol: ")

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

        contraseña_cifrada = cifrar_contraseña(contraseña)
        datos = (nombre, apellido, correo, telefono, contraseña_cifrada, direccion, id_rol)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Usuario registrado correctamente")
    except Exception as e:
        print("Error al registrar usuario:", e)
    finally:
        conexion.close()

def cifrar_contraseña(contraseña):
    sha256 = hashlib.sha256()
    sha256.update(contraseña.encode("utf-8"))
    return sha256.hexdigest()
