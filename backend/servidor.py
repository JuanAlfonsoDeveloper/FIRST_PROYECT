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
    eliminar_producto_carrio,
    vaciar_carrito_usuario,
    confirmar_compra
)


# -------------------------- MENU ROLES --------------------------

def mostrar_menu_por_rol(usuario):
    id_usuario, nombre_usuario, id_rol = usuario
    while True:
        print("\n --- MENU PRINCIPAL ---")
        if id_rol == 1: #Administrador
            print("1. Gestionar Usuarios: ")
            print("2. Gestionar productos: ")
            print("3. Ver reportes: ")
            print("4. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                print("Aqui iria la gestion de usuarios...")
            elif opcion == "2":
                print("Aqui iria la gestion de productos...")
            elif opcion == "3":
                print("Aqui se ven los reportes...")
            elif opcion == "4":
                print("Cerrando sesion ...")
                break
            else: 
                print("Opcion no valida")
        
        elif id_rol == 2: #Administrador
            print("1. Agregar producto: ")
            print("2. Actualizar productos: ")
            print("3. Eliminar producto ")
            print("4. Ver productos")
            print("5. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                print("Funcion agregar producto")
            elif opcion == "2":
                print("Funcion actualizar productos")
            elif opcion == "3":
                print("Funcion Eliminar productos")
            elif opcion == "4":
                print("Funcion ver productos")
            elif opcion == "5":
                print("Cerrando sesion ...")
                break
            else: 
                print("Opcion no valida")
                
        elif id_rol == 3: #Cliente
            print("1. Ver productos : ")
            print("2. Agregar al carrito: ")
            print("3. Ver carrito")
            print("4. Comfirmar compra")
            print("5. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                print("Funcion ver productos: ")
            elif opcion == "2":
                print("Funcion agregar al carrito")
            elif opcion == "3":
                print("Funcion ver carrito")
            elif opcion == "4":
                print("Funcion comfirmar compra")
            elif opcion == "5":
                print("Cerrando sesion ...")
                break
            else: 
                print("Opcion no valida")

# -------------------------- MENU USUARIOS --------------------------

def menu_usuario():
    while True:
        print("\n --- MENU DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Mostrar todos los usuarios")
        print("3. Buscar usuario por correo")
        print("4. Buscar usuario por telefono")
        print("5. Login de usuario")
        print("6. Actulizar usuario")
        print("7. Eliminar usuario")
        print("0. Volver al menu principal")
        
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            obtener_usuario()
        elif opcion == "3":
            correo = input("Correo a buscar: ")
            usuario = obtener_usuario_por_correo(correo)
            print("Resultado", usuario if usuario else "Usuario no encontrado")
        elif opcion == "4":
            telefono = input("Telefono a buscar: ")
            usuario = obtener_usuario_por_telefono(telefono)
            print("Resultado", usuario if usuario else "Usuario no encontrado")
        elif opcion == "5":
            correo = input("Correo :")
            contraseña = input("Contraseña :")
            usuario = login_usuario(correo, contraseña)
            if usuario: 
                mostrar_menu_por_rol(usuario)
        elif opcion == "6":
            id_usuario = input("ID del usuario a actualizar: ")
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            correo = input("Nuevo correo: ")
            telefono = input("Nuevo telefono: ")
            direccion = input("Nueva direccion: ")
            actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, direccion)
        elif opcion == "7":
            id_usuario = input("ID del usuario a eliminar: ")
            eliminar_usuario(id_usuario)
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. ")
            
# -------------------------- MENU PRODUCTOS --------------------------

def menu_productos():
    while True:
        print("\n --- MENU DE PRODUCTOS ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto por nombre")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("0. Volver al menu principal")

        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            obtener_productos()
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            buscar_producto_por_nombre(nombre)
        elif opcion == "4":
            id_producto = input("ID del producto a actualizar: ")
            titulo = input("Nuevo titulo: ")
            precio = input("Nuevo precio: ")
            imagen = input("Nueva ruta de la imagen / URL: ")
            descripcion = input("Nueva descripcion: ")
            stock = input("Nuevo stock: ")
            id_usuario = input("ID del usuario que publica: ")
            actualizar_productos(id_producto, titulo, precio, imagen, descripcion, stock, id_usuario)
        elif opcion == "5":
            id_producto = input("ID del producto a eliminar: ")
            eliminar_productos(id_producto)
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. ")

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
            eliminar_producto_carrio()
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
        print("1. Usuarios")
        print("2. Productos")
        print("3. Carrito")
        print("0. Salir")

        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            menu_usuario()
        elif opcion == "2":
            menu_productos()
        elif opcion == "3":
            menu_carrito()
        elif opcion == "0":
            break
        else: 
            print("Opcion no valida. ")
            
if __name__ == "__main__":
    menu_principal()
    


                
                
# ------------------ QUEDA PENDIENTE HACER LAS PREUBAS A LOS MENUS 2 Y 3 DE LOS ROLES -----------------------------------








# def menu():
#     while True:
#         print("")
#         print("")
#         print(" --MENU DE USUARIOS-- ")
#         print("1. Registar usuario")
#         print("2. Mostrar todos los usuarios")
#         print("3. Buscar usuario por correo")
#         print("4. Buscar usuario por telefono")
#         print("5. Login de usuario")
#         print("6. Actualizar usuario")
#         print("7. Eliminar usuario")
#         print("")
#         print("")
#         print("-- MENU DE PRODUCTOS --")
#         print("8. Registrar productos: ")
#         print("9. Mostrar los productos: ")
#         print("10. Buscar productos por nombre: ")
#         print("11. Actualizar producto: ")
#         print("12. Eliminar producto: ")
#         print("")
#         print("")
#         print("-- MENU DEL CARRITO --")
#         print("13. Agregar producto al carrito")
#         print("14. Mostrar carrito del usuario")
#         print("15. Actualizar carrito")
#         print("16. Eliminar producto del carrito ")
#         print("17. Vaciar Carrito")
#         print("18. Confirmar compra")

#         print("50. Salir")

#         opcion = input("Elige una opcion: ")

#         if opcion == "1":
#             registrar_usuario()
        
#         elif opcion == "2":
#             obtener_usuario()

#         elif opcion == "3":
#             correo = input("Correo a buscar ")
#             usuario = obtener_usuario_por_correo(correo)
#             if usuario: 
#                 print("Usuario encontrado:", usuario)
#             else: 
#                 print("Usuario no encntrado. ")


#         elif opcion == "4":
#             telefono = input("Numero de telefono a buscar ")
#             usuario = obtener_usuario_por_telefono(telefono)
#             if usuario: 
#                 print("Usuario encontrado:", usuario)
#             else: 
#                 print("Usuario no encntrado. ")

#         elif opcion == "5":
#             correo = input("Correo: ")
#             contraseña = input("Contraseña: ")
#             login_usuario(correo, contraseña)
        
#         elif opcion == "6":
#             id_usuario = input("Digie el ID del usuario que desea utilizar: ")
#             nombre = input("Nuevo nombre: ")
#             apellido = input("Nuevo apellido: ")
#             correo = input("Nuevo correo: ")
#             telefono = input("Nuevo telefono: ")
#             direccion = input("Nueva direccion: ")
#             actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, direccion)

#         elif opcion == "7":
#             id_usuario = input("Id del usuario a eliminar: ")
#             eliminar_usuario(id_usuario)

#         elif opcion == "8":
#             registrar_producto()


#         elif opcion == "9":
#             obtener_productos()

        
#         elif opcion == "10":
#             nombre = input("Nombre del producto a buscar: ")
#             buscar_producto_por_nombre(nombre)

#         elif opcion == "11":
#             print("--ACTUALIZAR PRODUCTO--")
#             id_producto = input("Digite el ID del producto a actulizar: ")
#             titulo_producto = input("Digite el nuevo titulo: ")
#             precio_producto = input("Digite el nuevo precio: ")
#             imagen_producto = input("Digite el nuevo nombre o ruta de la imagen: ")
#             descripcion_producto = input("Digite la nueva descripcion: ")
#             stock_producto = input("Digite el nuevo stock del producto: ")
#             id_usuario = input("Digite el nuevo ID del usuario que publica: ")
#             actualizar_productos(id_producto, titulo_producto, precio_producto, imagen_producto, descripcion_producto, stock_producto, id_usuario)
        
#         elif opcion == "12":
#             print("ELIMINAR PRODUCTO")
#             id_producto = input("Digite el ID del producto a eliminar: ")
#             eliminar_productos(id_producto)

#         elif opcion == "13":
#             agregar_al_carrito()

#         elif opcion == "14":
#             mostrar_carrito_por_usuario()
            
#         elif opcion == "15":
#             actualizar_cantidad_carrito()
            
#         elif opcion == "16":
#             eliminar_producto_carrio()
            
#         elif opcion == "17":
#             vaciar_carrito_usuario()
        
#         elif opcion == "18":
#             confirmar_compra()

#         elif opcion == "50":
#             print("Saliendo del sistema ")
#             break

#         else:
#             print("Opcion no valida. Intente de nuevo")

# menu()
# if __name__ == "__main__":
#     menu
