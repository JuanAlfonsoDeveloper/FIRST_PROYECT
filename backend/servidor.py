from usuarios import (
    registrar_usuario,
    obtener_usuario,
    obtener_usuario_por_correo,
    obtener_usuario_por_telefono,
    login_usuario,
    actualizar_usuario,
    eliminar_usuario
)

def menu():
    while True:
        print(" --MENU DE USUARIOS-- ")
        print("1. Registar usuario")
        print("2. Mostrar todos los usuarios")
        print("3. Buscar usuario por correo")
        print("4. Buscar usuario por telefono")
        print("5. Login de usuario")
        print("6. Actualizar usuario")
        print("7. Eliminar usuario")
        print("8. Salir")

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
            print("Saliendo del sistema ")
            break

        else:
            print("Opcion no valida. Intente de nuevo")

menu()