from usuarios import (
    registrar_usuario,
    obtener_usuario,
    obtener_usuario_por_correo,
    obtener_usuario_por_telefono,
    login_usuario,
    actualizar_usuario,
    eliminar_usuario
)

from productos import(
    registrar_producto,
    obtener_productos,
    buscar_producto_por_nombre,
    actualizar_productos,
    eliminar_productos
)

from carrito import(
    agregar_al_carrito,
    mostrar_carrito_por_usuario,
    actualizar_cantidad_carrito,
    eliminar_producto_carrito,
    vaciar_carrito_usuario,
    confirmar_compra
)


# -------------------------- MENU ROLES --------------------------

def mostrar_menu_por_rol(usuario):
    id_usuario, nombre_usuario, id_rol = usuario
    while True:
        if id_rol == 1: #Administrador
            print("\n --- MENU PRINCIPAL ADMINISTRADOR ---")
            print("1. Registrar Usuario: ")
            print("2. Mostrar todos los usuarios: ")
            print("3. Buscar usuario por correo: ")
            print("4. Buscar usuario por telefono: ")
            print("5. Actualizar usuario: ")
            print("6. Eliminar usuario: ")
            print("7. Registrar producto: ")
            print("8. Mostrar productos: ")
            print("9. Buscar productos: ")
            print("10. Actualizar productos: ")
            print("11. Eliminar productos: ")
            print("12. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            #  Opcion 1. Registrar Usuario
            if opcion == "1":
                print("--- REGISTRAR USUARIOS ---")
                nombre = input("Digite su nombre: ").strip()
                apellido = input("Digite su apellido: ").strip()
                correo = input("Digite su correo: ").strip()
                telefono = input("Digite su telefono: ").strip()
                contraseña = input("Digite su contraseña: ").strip()
                direccion = input("Digite su direccion: ").strip()
                id_rol_nuevo = input("Digite su codigo del rol: ").strip()
                
                
                if not (nombre and apellido and correo and telefono and contraseña and direccion and id_rol_nuevo):
                    print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
                else: 
                    registrar_usuario(nombre, apellido, correo, telefono, contraseña, direccion, id_rol_nuevo)
                    
            
            # Opcion 2. Mostrar todos los usuarios:
            elif opcion == "2":
                print("--- MOSTRAR USUARIOS ---")
                obtener_usuario()
            
            # Opcion 3. Buscar usuarios por correo:
            elif opcion == "3":
                print("--- BUSCAR USUARIO POR CORREO ---")
                correo = input("Correo a buscar: ")
                usuario = obtener_usuario_por_correo(correo)
                print("Resultado", usuario if usuario else "Usuario no encontrado")
                
            # Opcion 4. Buscar usuarios por telefono:
            elif opcion == "4":
                print("--- BUSCAR USUARIO POR TELEFONO ---")
                telefono = input("Telefono a buscar: ")
                usuario = obtener_usuario_por_telefono(telefono)
                print("Resultado", usuario if usuario else "Usuario no encontrado")
                
            # Opcion 5. Actualizar usuario: 
            elif opcion == "5":
                print("--- ACTUALIZAR USUARIO ---")
                id_usuario = input("ID del usuario a actualizar: ").strip()
                nombre = input("Nuevo nombre: ").strip()
                apellido = input("Nuevo apellido: ").strip()
                correo = input("Nuevo correo: ").strip()
                telefono = input("Nuevo telefono: ").strip()
                contraseña = input("Nueva contraseña ").strip()
                direccion = input("Nueva direccion: ").strip()  
                if not (id_usuario and nombre and apellido and correo and telefono and contraseña and  direccion  ):
                    print("X ERROR: Todos los campos son obligatorios. Intente nuevamente")
                else: 
                    actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, contraseña, direccion,)
            
            # Opcion 6. Eliminar usuario:
            elif opcion == "6":
                id_usuario = input("ID del usuario a eliminar: ")
                eliminar_usuario(id_usuario)
                
            # Opcion 7. Registrar producto:
            elif opcion == "7":
                registrar_producto()
                
            # Opcion 8. Mostrar productos:
            elif opcion == "8":
                obtener_productos()
                
            # Opcion 9. Buscar productos:
            elif opcion == "9":
                nombre = input("Nombre del producto: ")
                buscar_producto_por_nombre(nombre)
            
            # Opcion 10. Actualizar productos:
            elif opcion == "10":
                id_producto = input("ID del producto a actualizar: ")
                titulo = input("Nuevo titulo: ")
                precio = input("Nuevo precio: ")
                imagen = input("Nueva ruta de la imagen / URL: ")
                descripcion = input("Nueva descripcion: ")
                stock = input("Nuevo stock: ")
                id_usuario = input("ID del usuario que publica: ")
                actualizar_productos(id_producto, titulo, precio, imagen, descripcion, stock, id_usuario)
                
            # Opcion 11. Eliminar productos:
            elif opcion == "11":
                id_producto = input("ID del producto a eliminar: ")
                eliminar_productos(id_producto)
            
            # Opcion 12. Cerrar sesion:
            elif opcion == "12":
                print("Cerrando sesion ...")
                break
            # VALIADACION POR PONER DIGITOS QUE NO SON 
            else:
                print("Error opcion invalida:")
            
        
        
        elif id_rol == 2: #Vendedor
            print("\n --- MENU PRINCIPAL VENDEDORES ---")
            print("1. Registrar producto: ")
            print("2. Mostrar productos: ")
            print("3. Buscar productos: ")
            print("4. Actualizar productos: ")
            print("5. Eliminar productos: ")
            print("6. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            # Opcion 1. Registrar producto:
            if opcion == "1":
                registrar_producto()
                
            # Opcion 2. Mostrar productos:
            elif opcion == "2":
                obtener_productos()
                
            # Opcion 3. Buscar productos:
            elif opcion == "3":
                nombre = input("Nombre del producto: ")
                buscar_producto_por_nombre(nombre)
            
            # Opcion 4. Actualizar productos:
            elif opcion == "4":
                id_producto = input("ID del producto a actualizar: ")
                titulo = input("Nuevo titulo: ")
                precio = input("Nuevo precio: ")
                imagen = input("Nueva ruta de la imagen / URL: ")
                descripcion = input("Nueva descripcion: ")
                stock = input("Nuevo stock: ")
                id_usuario = input("ID del usuario que publica: ")
                actualizar_productos(id_producto, titulo, precio, imagen, descripcion, stock, id_usuario)
                
            # Opcion 5. Eliminar productos:
            elif opcion == "5":
                id_producto = input("ID del producto a eliminar: ")
                eliminar_productos(id_producto)
            
            # Opcion 6. Cerrar sesion:
            elif opcion == "6":
                print("Cerrando sesion ...")
                break
            # VALIADACION POR PONER DIGITOS QUE NO SON 
            else:
                print("Error opcion invalida")
           
                
            
                
        elif id_rol == 3: #Cliente
            print("1. Ver productos : ")
            print("2. Agregar al carrito: ")
            print("3. Ver carrito")
            print("4. Eliminar producto carrito")
            print("5. Vaciar carrito")
            print("6. Comfirmar compra")
            print("7. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                obtener_productos()
            elif opcion == "2":
                id_producto = input("ID del producto a agregar: ")
                try: 
                    cantidad = int(input("Cantidad: "))
                except ValueError:
                    print("Error la cantidad debe ser un numero entero. ")                
                agregar_al_carrito(id_usuario,id_producto,cantidad)
            elif opcion == "3":
                mostrar_carrito_por_usuario(id_usuario)
            elif opcion == "4":
                eliminar_producto_carrito(id_usuario)
            elif opcion == "5":
                vaciar_carrito_usuario(id_usuario)
            elif opcion == "6":
                confirmar_compra(id_usuario)
            elif opcion == "7":
                print("Cerrando sesion ...")
                break
            else: 
                print("Opcion no valida")


            
# -------------------------- MENU PRODUCTOS --------------------------

# def menu_productos():
#     while True:
#         print("\n --- MENU DE PRODUCTOS ---")
#         print("1. Registrar producto")
#         print("2. Mostrar productos")
#         print("3. Buscar producto por nombre")
#         print("4. Actualizar producto")
#         print("5. Eliminar producto")
#         print("0. Volver al menu principal")

#         opcion = input("Elige una opcion: ")
        
#         
#         elif opcion == "2":
#             
#         
#         elif opcion == "4":
#             
#         elif opcion == "5":
#            
#         elif opcion == "0":
#             break
#         else:
#             print("Opcion no valida. ")

# -------------------------- MENU CARRITO --------------------------
       
def menu_carrito():
    while True:
        print("\n --- MENU DE CARRITO ---")
        print("1. Agregar producto al carrito")
        print("2. Mostrar productos del carrito")
        print("3. Actualizar cantidad del carrito")
        print("4. Eliminar producto del carrito")
        print("5. Vaciar carrito")
        print("6. Confirmar compra")
        print("0. Volver al menu principal")
        
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            agregar_al_carrito()
        elif opcion == "2":
            mostrar_carrito_por_usuario()
        elif opcion == "3":
            actualizar_cantidad_carrito()
        elif opcion == "4":
            eliminar_producto_carrito()
        elif opcion == "5":
            vaciar_carrito_usuario()
        elif opcion == "6":
            confirmar_compra()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. ")
            
            
# -------------------------- MENU PRINCIPAL --------------------------
def menu_principal():
    while True:
        print("\n --- MENU  PRINCIPAL ---")
        print("1. Login: ")
        print("2. Salir: ")

        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            usuario = login_usuario(correo, contraseña)
            if usuario: 
                mostrar_menu_por_rol(usuario)
        elif opcion == "2":
            break
        else: 
            print("Opcion no valida. ")
            
if __name__ == "__main__":
    menu_principal()
    


                
                
# ------------------ Se empezo pruebas de administrador, faltan todas menos registrar usuario -----------------------------------







