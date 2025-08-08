from db import conectar

# -- AGRAGAR PRODUCTOS AL CARRITO -- 
def agregar_al_carrito():
    print("--AGREGAR PRODUCTOS AL CARRITO--")
    id_usuario = input("Id del usuario: ")
    id_producto = input("Id del producto: ")
    cantidad_carrito = input("Cantidad deseada : ")

    conexion = conectar()
    if not conectar:
        print("Error al conectar con la base de datos")
        return
    
    try: 
        cursor = conexion.cursor()
        consulta = """
        INSERT INTO carrito (id_usuario, id_producto, cantidad_carrito) 
        VALUES (%s, %s, %s)

        """
        datos = (id_usuario, id_producto, cantidad_carrito )
        cursor.execute(consulta, datos)
        conexion.commit()
        print("Producto agragado al carrito exitosamente. ")
    except Exception as e: 
        print("Error al agregar poducto al carrito:", e)
    finally:
        conexion.close()


# -- MOSTRAR CARRITO --
def mostrar_carrito_por_usuario():
    print("-- VER CARRITO DEL USUARIO --")
    id_usuario = input("Ingrese el ID del usuario: ")
    conexion = conectar()
    if not conexion:
        print("Error al conectar con la base de datos")
        return
    try: 
        cursor = conexion.cursor()
        consulta = """
        SELECT 
            carrito.id_carrito, 
            producto.titulo_producto, 
            carrito.cantidad_carrito, 
            carrito.metodo_pago_carrito
        FROM carrito
        INNER JOIN producto ON carrito.id_producto = producto.id_producto
        WHERE carrito.id_usuario = %s
        """
        cursor.execute(consulta, (id_usuario,))
        resultados = cursor.fetchall()

        if resultados:
            print("-- PRODUCTOS EN EL CARRITO --")
            for fila in resultados:
                print(f"ID Carrito: {fila[0]} | Producto: {fila[1]} | Cantidad: {fila[2]} | Método de Pago: {fila[3]}")
        else: 
            print("El carrito está vacío o el usuario no existe.")
    except Exception as e: 
        print("Error al mostrar el carrito:", e)
    finally:
        conexion.close()