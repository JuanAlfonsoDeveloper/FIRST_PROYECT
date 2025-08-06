from db import conectar

# -- REGISTRAR PRODUCTOS --
def registrar_producto():
    print("REGISTRAR PRODUCTO")

    titulo = input("Titulo del producto: ")
    precio = input("Precio del producto: ")
    imagen = input("Ruta o nombre de la imagen ")
    descripcion = input("Descripcion del producto: ")
    stock = input("Cantidad en el stock: ")
    id_usuario = input("ID del usuario que publica: ")

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
            print("Productos eontrados con  '{nombre_producto}':")
            for producto in productos: 
                print(producto)
        else:
            print("No se encontraron productos con ese con ese nombre.")
    except Exception as e:
        print("Error al buscar producto: ", e)
    finally:
        conexion.close()    