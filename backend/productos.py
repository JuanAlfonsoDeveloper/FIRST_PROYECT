from db import conectar

# -- VALIDAR NUMEROS DECIMALES()
def validar_numerodecimal(precio_input):
    try:
        numero = float(precio_input)
        return numero
    except ValueError:
        return None
     

# -- REGISTRAR PRODUCTOS --
def registrar_producto(titulo, precio_input, imagen, descripcion, stock, id_usuario,):

    # Validacion de que no haya espacios en blanco
    if not (titulo and precio_input and imagen and descripcion and stock and id_usuario ):
        print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
        return
    else: 
        
    # Funcion de que los rectifique que son decimales 
        precio = validar_numerodecimal(precio_input)
        if precio is None:
            print("X Error debe ingresar valores numericos enteros o decimales validos en el campo del precio")
            return
                    

    # Validacion stock numerico
    if not stock.isdigit():
        print("X Error El stock debe ser un valor numerico")
        return

    conexion = conectar()
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        consulta = """
          INSERT INTO producto (
            titulo_producto, precio_producto, imagen_producto,
            descripcion_producto, stock_producto, id_usuario
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos = (titulo, precio, imagen, descripcion, stock, id_usuario)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Producto registrado correctamente")
    except Exception as e: 
        print("Error al registrar producto", e)
    finally:
        conexion.close()


# -- OBTENER PRODUCTOS --
def obtener_productos():
    print("-- LISTADO DE PRODUCTOS DISPONIBLES --")

    conexion = conectar()
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM producto")
        productos = cursor.fetchall()
        if productos:
            for producto in productos:
                print(producto)
        else: 
            print("No hay productos registrados. ")
    except Exception as  e:
        print("Error al obtener productos:", e)
    finally: 
        conexion.close()

# -- BUSCADOR DE PRODUCTOS --
def buscar_producto_por_nombre(nombre):
    conexion = conectar()
    if not conexion:
        return
    try:
        # Validacion de que no haya espacios en blanco
        if not (nombre):
            print("X ERROR: No has puesto ningun nombre")
            return
        
        nombre_producto = nombre        
        cursor = conexion.cursor()
        consulta = "SELECT * FROM  producto WHERE titulo_producto LIKE %s"
        valor = f"%{nombre_producto}%"
        cursor.execute(consulta, (valor,))
        productos = cursor.fetchall()

        if productos:
            print(f"Productos encontrados con  {nombre_producto}:")
            for producto in productos: 
                print(producto)
        else:
            print("No se encontraron productos con ese con ese nombre.")
    except Exception as e:
        print("Error al buscar producto: ", e)
    finally:
        conexion.close()    


# -- ACTUALIZAR PRODUCTOS --
def actualizar_productos(id_producto, titulo, precio_input, imagen, descripcion, stock, id_usuario):
    conexion = conectar()
    if not conexion:
        print("No se pudo establecer conexión con la base de datos.")
        return
    try:
        # Validacion de que no hayan espacios vacios 
        if not (id_producto and titulo and precio_input and imagen and descripcion and stock and id_usuario ):
            print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
            return
        else:
            # Validacion de id numerico
            if not id_producto.isdigit():
                print("X Error el Id debe ser valor numerico")
                return
            else: 
                # Validacion de precio que sea float 
                precio = validar_numerodecimal(precio_input)
                if precio is None:
                    print("X Error debe ingresar valores numericos enteros o decimales validos en el campo del precio")
                    return
                # Validacion stock numerico
                if not stock.isdigit():
                    print("X Error El stock debe ser un valor numerico")
                    return
        
        cursor = conexion.cursor()
        # Validacion de que el id exista 
        
        cursor.execute("SELECT * FROM producto WHERE id_producto = %s" , (id_producto,))
        usuario = cursor.fetchone()
        if not usuario:
            print("No existe un producto con ese ID")
            return
        
         
        
        consulta = """
        UPDATE producto 
        SET titulo_producto = %s,
            precio_producto = %s,
            imagen_producto = %s,
            descripcion_producto = %s,
            stock_producto = %s,
            id_usuario = %s
        WHERE id_producto = %s
        """
        datos = (titulo, precio, imagen, descripcion, stock, id_usuario, id_producto)
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Producto actualizado correctamente")
    except Exception as e:
        print("Error al actualizar el producto:", e)
    finally: 
        conexion.close()


# -- ELIMINAR PRODUCTOS --
def eliminar_productos(id_producto):
    conexion = conectar()
    if not conexion:
        print("No se pudo establecer conexión con la base de datos.")
        return
    
    try: 
        cursor = conexion.cursor()
        
        # Validacion de que no hayan espacios vacios 
        if not (id_producto):
            print("X ERROR: No deber haber campo vacio")
            return

        # Validacion de que el id sea numerico
        if not id_producto.isdigit():
            print("X Error El id debe ser un valor numerico")
            return
        
        # Validacion de que el id exista 
        cursor.execute("SELECT * FROM producto WHERE id_producto = %s" , (id_producto,))
        producto = cursor.fetchone()
        if not producto:
            print("No existe un producto con ese ID")
            return
        
        # Confirmacion de eliminacion
        print(f"¿Estas seguro de eliminar al producto:  {producto[1]} ")
        confirmacion = input("Para confirmar la eliminacion escribe exactamente `ELIMINAR` todo en mayusculas:  ").strip() 
        
        if confirmacion != "ELIMINAR":
            print("Eliminacion cancelada") 
            return
        
        consulta = "DELETE FROM producto WHERE id_producto = %s"
        cursor.execute(consulta, (id_producto,))
        conexion.commit()
        print("Producto eliminado correctamente ")
    except Exception as e:
        print("Error al eliminar el producto: ", e)
    finally: 
        conexion.close()



