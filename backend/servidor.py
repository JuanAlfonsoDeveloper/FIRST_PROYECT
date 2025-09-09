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
    eliminar_productos_carrio,
    vaciar_carrito_usuario
)



def menu():
    while True:
        print("")
        print("")
        print(" --MENU DE USUARIOS-- ")
        print("1. Registar usuario")
        print("2. Mostrar todos los usuarios")
        print("3. Buscar usuario por correo")
        print("4. Buscar usuario por telefono")
        print("5. Login de usuario")
        print("6. Actualizar usuario")
        print("7. Eliminar usuario")
        print("")
        print("")
        print("-- MENU DE PRODUCTOS --")
        print("8. Registrar productos: ")
        print("9. Mostrar los productos: ")
        print("10. Buscar productos por nombre: ")
        print("11. Actualizar producto: ")
        print("12. Eliminar producto: ")
        print("")
        print("")
        print("-- MENU DEL CARRITO --")
        print("13. Agregar producto al carrito")
        print("14. Mostrar carrito del usuario")
        print("15. Actualizar carrito")
        print("16. Eliminar producto del carrito carrito")
        print("17. Vaciar Carrito")

        print("50. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            registrar_usuario()
        
        elif opcion == "2":
            obtener_usuario()

        elif opcion == "3":
            correo = input("Correo a buscar ")
            usuario = obtener_usuario_por_correo(correo)
            if usuario: 
                print("Usuario encontrado:", usuario)
            else: 
                print("Usuario no encntrado. ")


        elif opcion == "4":
            telefono = input("Numero de telefono a buscar ")
            usuario = obtener_usuario_por_telefono(telefono)
            if usuario: 
                print("Usuario encontrado:", usuario)
            else: 
                print("Usuario no encntrado. ")

        elif opcion == "5":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            login_usuario(correo, contraseña)
        
        elif opcion == "6":
            id_usuario = input("Digie el ID del usuario que desea utilizar: ")
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            correo = input("Nuevo correo: ")
            telefono = input("Nuevo telefono: ")
            direccion = input("Nueva direccion: ")
            actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, direccion)

        elif opcion == "7":
            id_usuario = input("Id del usuario a eliminar: ")
            eliminar_usuario(id_usuario)

        elif opcion == "8":
            registrar_producto()


        elif opcion == "9":
            obtener_productos()

        
        elif opcion == "10":
            nombre = input("Nombre del producto a buscar: ")
            buscar_producto_por_nombre(nombre)

        elif opcion == "11":
            print("--ACTUALIZAR PRODUCTO--")
            id_producto = input("Digite el ID del producto a actulizar: ")
            titulo_producto = input("Digite el nuevo titulo: ")
            precio_producto = input("Digite el nuevo precio: ")
            imagen_producto = input("Digite el nuevo nombre o ruta de la imagen: ")
            descripcion_producto = input("Digite la nueva descripcion: ")
            stock_producto = input("Digite el nuevo stock del producto: ")
            id_usuario = input("Digite el nuevo ID del usuario que publica: ")
            actualizar_productos(id_producto, titulo_producto, precio_producto, imagen_producto, descripcion_producto, stock_producto, id_usuario)
        
        elif opcion == "12":
            print("ELIMINAR PRODUCTO")
            id_producto = input("Digite el ID del producto a eliminar: ")
            eliminar_productos(id_producto)

        elif opcion == "13":
            agregar_al_carrito()

        elif opcion == "14":
            mostrar_carrito_por_usuario()
            
        elif opcion == "15":
            actualizar_cantidad_carrito()
            
        elif opcion == "16":
            eliminar_productos_carrio()
            
        elif opcion == "17":
            vaciar_carrito_usuario()

        elif opcion == "50":
            print("Saliendo del sistema ")
            break

        else:
            print("Opcion no valida. Intente de nuevo")

menu()

