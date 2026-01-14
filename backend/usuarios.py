from db import conectar
import hashlib


# -- CAMBIAR ROL DE USUARIO (SOLO ADMIN) -- 
def cambiar_rol_usuario(id_usuario_cambiar, nuevo_rol):
    conexion = conectar()
    if not conexion: 
        print(" X Error al conectar a la base de datos ")
        return
    
    try: 
        cursor = conexion.cursor()
        
        # Validacion ID usuario 
        if not id_usuario_cambiar.isdigit():
            print("X Error El ID del usuario debe ser numero")
            return
        
        # Validar rol 
        if nuevo_rol not in ("1","2","3"):
            print("X Error rol invalido")
            return
        
        # Verificar si el usuario existe
        cursor.execute(
            "SELECT nombre_usuario, id_rol FROM usuario WHERE id_usuario = %s", (id_usuario_cambiar,)
        )
        usuario = cursor.fetchone()
        
        if not usuario: 
            print("X Error el usuario no existe")
            return
        nombre, rol_actual = usuario 
        
        # Confirmacion
        print(f"Usuario: {nombre}")
        print(f"Rol Actual: {rol_actual}")
        confirmacion = input("Escriba CAMBIAR para confirmar el cambio del rol: ").strip()
        
        if confirmacion != "CAMBIAR":
            print("Cambio de rol cancelado")
            return
        
        # Actualizar rol 
        cursor.execute("UPDATE usuario SET id_rol = %s WHERE id_usuario = %s", (nuevo_rol, id_usuario_cambiar))
        conexion.commit()
        
        print("Rol Actualizado correctamente")
        
    except Exception as e:
        print("Error al cambiar rol:",e)
    finally:
        conexion.close()
    
        
#-- REGISTRAR USURIO --

def registrar_usuario(nombre, apellido, correo, telefono, contraseña, direccion, id_rol_nuevo):
    print("Registrar Usuario")
    conexion = conectar()
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        
        # --- VALIDACION DE DUPLICADOS ---
        cursor.execute(
            "SELECT id_usuario FROM usuario WHERE correo_usuario = %s",(correo,))
        if cursor.fetchone():
            print("X Error: El correo ya esta registrado. ")
            return
        
        cursor.execute(
            "SELECT id_usuario FROM usuario WHERE telefono_usuario = %s",(telefono,))
        if cursor.fetchone():
            print("X Error: El telefono ya esta registrado. ")
            return
        
        consulta = """
        INSERT INTO usuario ( 
            nombre_usuario, apellido_usuario, correo_usuario, 
            telefono_usuario, contraseña_usuario, direccion_usuario, id_rol
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        contraseña_cifrada = cifrar_contraseña(contraseña)
        datos = (nombre, apellido, correo, telefono, contraseña_cifrada, direccion, id_rol_nuevo)
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
        consulta = """ SELECT id_usuario , nombre_usuario, id_rol
        FROM usuario 
        WHERE  correo_usuario = %s AND contraseña_usuario = %s 
        
        """
        contraseña_cifrada = hashlib.sha256(contraseña.encode()).hexdigest()
        cursor.execute(consulta, (correo, contraseña_cifrada))
        usuario = cursor.fetchone()
        if usuario:
            print(f"Login Exitoso. Bienvenido {usuario[1]}")
            return usuario
        else: 
            print("correo o contraseña incorrectos")
    except Exception as e:
        print("Error al hacer login:", e)
    finally: 
        conexion.close()
        
#-- ACTUALIZAR DATOS DE UN USUARIO --
def actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, contraseña, direccion ):
    conexion = conectar()
    if not conexion: 
        print("Error a conectar a la base de datos.")
        return
    try:
        cursor = conexion.cursor()
        cifrar_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
        consulta = """
        UPDATE usuario SET nombre_usuario=%s, apellido_usuario=%s,
        correo_usuario=%s, contraseña_usuario=%s, telefono_usuario=%s, direccion_usuario=%s
        WHERE id_usuario=%s
        """
        datos = (nombre, apellido, correo, cifrar_contraseña, telefono,  direccion,  id_usuario)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Usuario actualizado correctamente")
    except Exception as e:
        print("Error al actualizar usuario:", e)
    finally:
        conexion.close()

#-- ELIMINAR USUARIO --

def eliminar_usuario(id_usuario):
    # Validacion de que no este vacio
    if not id_usuario.strip():
        print("Error El Id del usuario no puede estar vacio ")
        return 
    # Validacion de que sea un numero
    if not id_usuario.isdigit():
        print("Error El Id debe ser un numero valido")
    conexion = conectar()
    if not conexion:
        print("Error al conectar a la base de datos")
        return
    try:
        cursor = conexion.cursor()
        
        # Verificar si el usurio existe o no 
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s" , (id_usuario,))
        usuario = cursor.fetchone()
        if not usuario:
            print("No existe un usuario con ese ID")
            return
    
        
        print(f"¿Estas seguro de eliminar al usuario {usuario[1]} ")
        confirmacion = input("Para confirmar la eliminacion escribe exactamente `ELIMINAR` todo en mayusculas:  ").strip() 
        
        # Confirmacion de eliminacion
        if confirmacion.upper() != "ELIMINAR":
            print("Eliminacion cancelada")  
        cursor.execute("SELECT COUNT(*) FROM producto WHERE id_usuario = %s", (id_usuario,))
        productos = cursor.fetchone()[0]
        
        # Validacion que menciona que no se puede eliminar usuarios con productos apregados
        if productos > 0: 
            print("No puedes eliminar este usuario porque tiene productos registrados. ")
            return
        consulta = "DELETE FROM usuario WHERE id_usuario = %s"
        cursor.execute(consulta, (id_usuario,))
        conexion.commit()
        print("Usuario eliminado correctamente")  
    except Exception as e:
        print("Error al eliminar el usuario:", e)
    finally:
        conexion.close()