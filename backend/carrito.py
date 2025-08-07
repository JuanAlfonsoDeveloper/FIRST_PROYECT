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
