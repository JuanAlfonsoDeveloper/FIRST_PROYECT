from db import conectar

# -- REGISTRAR PRODUCTOS --
def registrar_producto():
    print("REGISTRAR PRODUCTO")
    titulo = input("Titulo del producto: ")
    precio = input("Precio del producto: ")
    imagen = input("Ruta o nombre de la imagen ")
    descripcion = input("Descripcion del producto: ")
    stock = input("Cantidad en el stock: ")
    id_usuario = input("ID del uuaurio que publica: ")

    conexion = conectar
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
        print("Producto registrado correctamente")
    except Exception as e: 
        print("Error al registrar producto, e")
    finally:
        conexion.close()


# -- OBTENER PRODUCTOS --
