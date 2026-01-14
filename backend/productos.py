from db import conectar

# -- VALIDAR NUMEROS DECIMALES()
def validar_numerodecimal(precio_input):
    try:
        numero = float(precio_input)
        return numero
    except ValueError:
        return None
     

# -- REGISTRAR PRODUCTOS --
def registrar_producto(titulo, precio, imagen, descripcion, stock, id_usuario):

    print("REGISTRAR PRODUCTO")

    # Validacion ID usuario 
    

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
def buscar_producto_por_nombre(nombre_producto):
    conexion = conectar()
    if not conexion:
        return
    try:
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
def actualizar_productos(id_producto, titulo, precio, imagen, descripcion, stock, id_usuario):
    conexion = conectar()
    if not conexion:
        print("No se pudo establecer conexión con la base de datos.")
        return
    try:
        cursor = conexion.cursor()
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
        consulta = "DELETE FROM producto WHERE id_producto = %s"
        cursor.execute(consulta, (id_producto,))
        conexion.commit()
        print("Producto eliminado correctamente ")
    except Exception as e:
        print("Error al eliminar el producto: ", e)
    finally: 
        conexion.close()



