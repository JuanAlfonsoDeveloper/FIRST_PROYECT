from db import conectar

# -- AGRAGAR PRODUCTOS AL CARRITO -- 
def agregar_al_carrito(id_usuario, id_producto, cantidad_carrito):
    
    # Validacion de que no hayan espacios vacios 
    if not (id_usuario and id_producto and cantidad_carrito ):
        print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
        return
    
    # Validacion de id numerico 
    if not id_producto.isdigit():
        print("X Error el Id debe ser valor numerico")
        return

    # Validacion de cantidad de carrito 
    if not cantidad_carrito.isdigit():
        print("X Error la cantidad debe ser valor numerico")
        return
    
    # Validacion de cantidad de carrito no sea cero
    if int(cantidad_carrito) == 0:
        print("X Error la cantidad debe ser mayor a cero")
        return
    

    conexion = conectar()
    if not conexion:
        print("Error al conectar con la base de datos")
        return
    
    try:
        cantidad_carrito = int(cantidad_carrito)
        cursor = conexion.cursor()
        # 1. Verificar stock disponible del producto
        consulta_stock = " SELECT stock_producto FROM producto WHERE id_producto = %s"
        cursor.execute(consulta_stock, (id_producto,))
        resultado = cursor.fetchone()
        
        if not resultado:
            print("El producto no existe. ")
            return
        stock_disponible = int(resultado[0])
        
        # 2. Verificar si el producto ya esta en el carrito
        consulta_carrito = """
        SELECT cantidad_carrito FROM carrito WHERE id_usuario = %s AND id_producto = %s
        """
        cursor.execute(consulta_carrito,(id_usuario, id_producto))
        producto_en_carrito = cursor.fetchone()
        
        if producto_en_carrito:
            cantidad_actual = int(producto_en_carrito[0])
            nueva_cantidad = cantidad_actual + cantidad_carrito
            
            if nueva_cantidad > stock_disponible:
                print(f"No hay suficiente stock. Stock disponible: {stock_disponible}")
                return
            
            consulta_update = """
            UPDATE carrito SET cantidad_carrito = %s WHERE id_usuario = %s AND id_producto = %s
            """
            
            cursor.execute(consulta_update, (nueva_cantidad, id_usuario, id_producto))
            conexion.commit()
            print("Cantidad del producto actualizada en el carrito ")
            
        else:
            if cantidad_carrito > stock_disponible:
                print(f"No hay suficiente stock. Stock disponible: {stock_disponible}")
                return
            
            consulta_insert = """
            INSERT INTO carrito (metodo_pago_carrito, cantidad_carrito, id_usuario, id_producto)
            VALUES (%s, %s, %s, %s)
            """
            datos = ("pendiente", cantidad_carrito, id_usuario, id_producto)
            cursor.execute(consulta_insert, datos)
            conexion.commit()
            print("Producto agregado al carrito exitosamente. ")
        
   
    except Exception as e: 
        print("Error al agregar producto al carrito:", e)
    finally:
        conexion.close()

# -- MOSTRAR CARRITO DEL USUARIO -- 
def mostrar_carrito_por_usuario(id_usuario):
    
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
            producto.precio_producto, 
            carrito.cantidad_carrito, 
            carrito.metodo_pago_carrito
        FROM carrito
        INNER JOIN producto ON carrito.id_producto = producto.id_producto
        WHERE carrito.id_usuario = %s
        """
        cursor.execute(consulta, (id_usuario,))
        resultados = cursor.fetchall()

        if resultados:
            
            total_general = 0  
            total_cantidad = 0  
            for fila in resultados:
                id_carrito = fila[0]
                nombre_producto = fila[1]
                precio = float(fila[2])  
                cantidad = int(fila[3])  
                metodo_pago = fila[4]
                total = precio * cantidad
                total_general += total  
                total_cantidad += cantidad  

                print(f"ID Carrito: {id_carrito} | Producto: {nombre_producto} | "
                      f"Precio: {precio:.2f} | Cantidad: {cantidad} | "
                      f"Total: {total:.2f} | Método de Pago: {metodo_pago}")
            
            print("\n-----------------------------------")
            print(f"TOTAL DE PRODUCTOS: {total_cantidad}")
            print(f"TOTAL GENERAL DEL CARRITO: {total_general:.2f}")
            print("-----------------------------------")
        else: 
            print("El carrito está vacío o el usuario no existe.")
    except Exception as e: 
        print("Error al mostrar el carrito:", e)
    finally:
        conexion.close()


# -- ACTUALIZAR CARRITO -- 
def actualizar_cantidad_carrito(nueva_cantidad, id_carrito):
    
     # Validacion de que no hayan espacios vacios 
    if not (nueva_cantidad and id_carrito ):
        print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
        return
    
    # Validacion de id numerico 
    if not nueva_cantidad.isdigit():
        print("X Error la cantidad debe ser valor numerico") 
        return

    # Validacion de cantidad de carrito 
    if not id_carrito.isdigit():
        print("X Error el Id debe ser valor numerico")
        return
    
    # Validacion de cantidad de carrito no sea cero
    if int(nueva_cantidad) == 0:
        print("X Error la cantidad debe ser mayor a cero")
        return
    
    conexion = conectar()
    if not conexion:
        print("Error al conectar con la base de datos")
        return
    try:
        cursor = conexion.cursor()
        consulta = """
        UPDATE carrito 
        SET cantidad_carrito = %s
        WHERE id_carrito = %s
        """
        cursor.execute(consulta, (nueva_cantidad, id_carrito))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print("Cantidad actualizada exitosamente ")
        else:
            print("No se encontro el carrito con ese ID ")
    except Exception as e:
        print("Error al actulizar la cantidad: ", e)
    finally: 
        conexion.close()

# -- ELIMINAR PRODUCTOS DEL CARRITO --
def eliminar_producto_carrito(id_carrito):
   
    
    
    # Validacion de que no hayan espacios vacios 
    if not (id_carrito ):
        print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
        return
    
    # Validacion de id numerico 
    if not id_carrito.isdigit():
        print("X Error el Id debe ser valor numerico")
        return

    
    conexion = conectar()
    if not conexion:
        print("Error al conectar con la base de datos")
        return
    try: 
        cursor = conexion.cursor()
        consulta = """ DELETE FROM carrito WHERE id_carrito = %s """
        cursor.execute(consulta,(id_carrito,))
        conexion.commit()
        if cursor.rowcount > 0:
            print("Producto eliminado exitosamente del carrito")
        else:
            print("No se encontro producto con ese ID en el carrito")
    except Exception as e:
        print("Error al eliminar producto del carrito", e)
    finally:
        conexion.close()


# -- VACIAR CARRITO  --
def vaciar_carrito_usuario(id_usuario):
    print("-- VACIAR CARRITO --")
    conexion = conectar()
    if not conexion:
        print("Error al conectar con la base de datos ")
        return
    try:
        cursor = conexion.cursor()
        consulta = """ DELETE FROM carrito WHERE id_usuario = %s """
        cursor.execute(consulta,(id_usuario, ))
        conexion.commit()
        if cursor.rowcount > 0:
                print(f"Carrito del usuario {id_usuario} vaciado exitosamente ")
        else:
            print("El carrito ya esta vacio o el usuario no existe ")
    except Exception as e:
        print("Error al vaciar el carrito ", e)
    finally:
        conexion.close()
        

# -- CONFIRMAR COMPRA  --
def confirmar_compra(id_usuario):
   
    if not id_usuario:
        id_usuario = input("Ingrese el ID del usuario:")
    
    
    metodo_pago = input("Metodo de Pago (Tarjeta / Efectivo  / PSE / ): ")
    
    
    
    
    conexion = conectar()
    if not conexion:
        print("Error al conectar con la base de datos ")
        return
    try:
        cursor = conexion.cursor()
        
        # 1. Obtener productos pendientes del carrito
        consulta_carrito = """
        SELECT id_producto, cantidad_carrito FROM carrito WHERE id_usuario = %s AND metodo_pago_carrito = 'pendiente'
        """
        cursor.execute(consulta_carrito, (id_usuario,))
        productos = cursor.fetchall()
        
        if not productos:
            print("No hay productos pendientes en el carrito")
            return
        
        # 2. Verificar stock y descontarlo
        for producto in productos:
            id_producto = producto[0]
            cantidad_carrito = int(producto[1])
            
            # Obtener stock actual
            cursor.execute("SELECT stock_producto FROM producto WHERE id_producto = %s",(id_producto)) 
            
            resultado = cursor.fetchone()
            
            if not resultado:
                print(f"Producto con ID {id_producto} no existe")
                return
            
            stock_actual = int(resultado[0])
            
            if cantidad_carrito > stock_actual:
                print(f"No hay suficiente stock paa el producto {id_producto}")
                return
            
            # Descontar el stock
            nuevo_stock = stock_actual - cantidad_carrito
            cursor.execute("UPDATE producto SET stock_producto = %s WHERE id_producto = %s", (nuevo_stock, id_producto))
            
        # 3. Confirmar compra
        consulta = """ 
        UPDATE carrito 
        SET metodo_pago_carrito = %s
        WHERE id_usuario = %s AND metodo_pago_carrito = 'pendiente'
        """
        cursor.execute(consulta,(metodo_pago, id_usuario, ))
        conexion.commit()
        if cursor.rowcount > 0:
                print(f"Compra confirmada con metodo de pago:  {metodo_pago} ")
        else:
            print("No hay productos pendientes en el carrito para confirmar")
    except Exception as e:
        print("Error al confirmar la compra ", e)
    finally:
        conexion.close()
