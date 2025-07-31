from db import conectar
import hashlib

#-- REGISTRAR USURIO --

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


#-- OBTENER USUARIOS --
def obtener_usuario():
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        for usuario in usuarios:
            print(usuario)
    except Exception as e:
        print("Error al obtener usuarios: ", e)
    finally: 
        conexion.close()


#-- OBTENER USUARIO POR CORREO --
def obtener_usuario_por_correo(correo):
    conexion = conectar()
    if not conexion:
        return
    try: 
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuario WHERE correo_usuario = %s"
        cursor.execute(consulta, (correo,))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        print("Error al obtener usuario:", e)
    finally:
        conexion.close()

#-- OBTENER USUARIO POR TELEFONO --
def obtener_usuario_por_telefono(telefono):
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuario WHERE telefono_usuario = %s"
        cursor.execute(consulta, (telefono))
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        print("Error al obtener usuario por telefono:", e)
    finally:
        conexion.close()


#-- VALIDAR LOGIN --
import hashlib

def login_usuario(correo, contraseña):
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuario WHERE correo_usuario = %s AND contraseña_usuario = %s"
        contraseña_cifrada = hashlib.sha256(contraseña.encode()).hexdigest()
        cursor.execute(consulta, (correo, contraseña_cifrada))
        usuario = cursor.fetchone()
        if usuario:
            print("Login exitoso")
            return usuario
        else: 
            print("correo o contraseña incorrectos")
    except Exception as e:
        print("Error al hacer login:", e)
    finally: 
        conexion.close()
        
#-- ACTUALIZAR DATOS DE UN USUARIO --
def actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, direccion):
    conexion = conectar()
    if not conexion: 
        return
    try:
        cursor = conexion.cursor()
        consulta = """
        UPDATE usuario SET nombre_usuario=%s, apellido_usuario=%s,
        correo_usuario=%s, telefono_usuario=%s, direccion_usuario=%s
        WHERE id_usuario=%s
        """
        datos = (nombre, apellido, correo, telefono, direccion, id_usuario)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Usuario actualizado correctamente")
    except Exception as e:
        print("Error al actualizar usuario:", e)
    finally:
        conexion.close()

#-- ELIMINAR USUARIO --

def eliminar_usuario(id_usuario):
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        consulta = "DELETE FROM usuario WHERE id_usuario = %s"
        cursor.execute(consulta, (id_usuario,))
        conexion.commit()
        print("Usuario eliminado correctamente")
    except Exception as e:
        print("Error al elminar el usuario:", e)
    finally:
        conexion.close()