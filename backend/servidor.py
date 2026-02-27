# Flask
from flask import Flask, jsonify
from flask_cors import CORS
from db import conectar

from usuarios import (
    registrar_usuario,
    obtener_usuario,
    obtener_usuario_por_correo,
    obtener_usuario_por_telefono,
    login_usuario,
    actualizar_usuario,
    eliminar_usuario,
    cambiar_rol_usuario
)

from productos import(
    registrar_producto,
    obtener_productos,
    buscar_producto_por_nombre,
    actualizar_productos,
    eliminar_productos,
    validar_numerodecimal
)

from carrito import(
    agregar_al_carrito,
    mostrar_carrito_por_usuario,
    actualizar_cantidad_carrito,
    eliminar_producto_carrito,
    vaciar_carrito_usuario,
    confirmar_compra
)

app = Flask(__name__)
CORS(app)

@app.route("/productos")
def productos():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM PRODUCTO")
    productos = cursor.fetchall()
    
    return jsonify(productos)


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
            print("7. Cambiar rol de usuario")
            print("8. Registrar producto: ")
            print("9. Mostrar productos: ")
            print("10. Buscar productos: ")
            print("11. Actualizar productos: ")
            print("12. Eliminar productos: ")
            print("13. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            #  Opcion 1. Registrar Usuario
            if opcion == "1":
                print("\n--- REGISTRAR USUARIOS ---")
                nombre = input("Digite su nombre: ").strip()
                apellido = input("Digite su apellido: ").strip()
                correo = input("Digite su correo: ").strip()
                telefono = input("Digite su telefono: ").strip()
                contraseña = input("Digite su contraseña: ").strip()
                direccion = input("Digite su direccion: ").strip()
                id_rol_nuevo = input("Digite su codigo del rol: ").strip()
                registrar_usuario(nombre, apellido, correo, telefono, contraseña, direccion, id_rol_nuevo)
                    
            
            # Opcion 2. Mostrar todos los usuarios:
            elif opcion == "2":
                print("\n--- MOSTRAR USUARIOS ---")
                obtener_usuario()
            
            # Opcion 3. Buscar usuarios por correo:
            elif opcion == "3":
                print("\n--- BUSCAR USUARIO POR CORREO ---")
                correo = input("Correo a buscar: ")
                usuario = obtener_usuario_por_correo(correo)
                
                
            # Opcion 4. Buscar usuarios por telefono:
            elif opcion == "4":
                print("\n--- BUSCAR USUARIO POR TELEFONO ---")
                telefono = input("Telefono a buscar: ")
                usuario = obtener_usuario_por_telefono(telefono)
                
                
            # Opcion 5. Actualizar usuario: 
            elif opcion == "5":
                print("\n--- ACTUALIZAR USUARIO ---")
                id_usuario = input("ID del usuario a actualizar: ").strip()
                nombre = input("Nuevo nombre: ").strip()
                apellido = input("Nuevo apellido: ").strip()
                correo = input("Nuevo correo: ").strip()
                telefono = input("Nuevo telefono: ").strip()
                contraseña = input("Nueva contraseña ").strip()
                direccion = input("Nueva direccion: ").strip()  
                actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, contraseña, direccion,)
            
            # Opcion 6. Eliminar usuario:
            elif opcion == "6":
                print("\n--- ELIMINAR USUARIO ---")
                id_usuario = input("ID del usuario a eliminar: ")
                eliminar_usuario(id_usuario)
                
            # Opcion 7. Cambiar rol a usuario
            elif opcion == "7":
                print("\n-- CAMBIAR ROL DE USUARIO --")
                id_usuario_cambiar = input("ID del usuario: ").strip()
                nuevo_rol = input("Nuevo Rol (1 - Admin, 2 - Vendedor, 3 - Cliente ): ").strip()
                cambiar_rol_usuario(id_usuario_cambiar , nuevo_rol)
            
            # Opcion 8. Registrar producto:
            elif opcion == "8":
                print("\n-- REGISTRA PRODUCTOS ---")
                titulo = input("Titulo del producto: ").strip()
                precio_input = input("Precio del producto: ").strip()
                imagen = input("Ruta o nombre de la imagen ").strip()
                descripcion = input("Descripcion del producto: ").strip()
                stock = input("Cantidad en el stock: ").strip()
                id_usuario = usuario[0]
                registrar_producto(titulo, precio_input, imagen, descripcion, stock, id_usuario)
                
            # Opcion 9. Mostrar productos:
            elif opcion == "9":
                obtener_productos()
                
            # Opcion 10. Buscar productos:
            elif opcion == "10":
                print("\n-- BUSCAR PRODUCTOS ---")
                nombre = input("Nombre del producto: ")
                buscar_producto_por_nombre(nombre)
            
            # Opcion 11. Actualizar productos:
            elif opcion == "11":
                print("\n-- ACTUALIZAR PRODUCTOS ---")
                id_producto = input("ID del producto a actualizar: ").strip()
                titulo = input("Nuevo titulo: ").strip()
                precio_input = input("Nuevo precio: ").strip()
                imagen = input("Nueva ruta de la imagen / URL: ").strip()
                descripcion = input("Nueva descripcion: ").strip()
                stock = input("Nuevo stock: ").strip()
                id_usuario = usuario[0]   
                actualizar_productos(id_producto, titulo, precio_input, imagen, descripcion, stock, id_usuario)
                
            # Opcion 12. Eliminar productos:
            elif opcion == "12":
                print("\n-- ELIMINAR PRODUCTOS ---")
                id_producto = input("ID del producto a eliminar: ")
                eliminar_productos(id_producto)
            
            # Opcion 13. Cerrar sesion:
            elif opcion == "13":
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
                print("\n-- REGISTRA PRODUCTOS ---")
                titulo = input("Titulo del producto: ").strip()
                precio_input = input("Precio del producto: ").strip()
                imagen = input("Ruta o nombre de la imagen ").strip()
                descripcion = input("Descripcion del producto: ").strip()
                stock = input("Cantidad en el stock: ").strip()
                id_usuario = usuario[0]
                registrar_producto(titulo, precio_input, imagen, descripcion, stock, id_usuario)
                
            # Opcion 2. Mostrar productos:
            elif opcion == "2":
                obtener_productos()
                
            # Opcion 3. Buscar productos:
            elif opcion == "3":
                print("\n-- BUSCAR PRODUCTOS ---")
                nombre = input("Nombre del producto: ")
                buscar_producto_por_nombre(nombre)
            
            # Opcion 4. Actualizar productos:
            elif opcion == "4":
                print("\n-- ACTUALIZAR PRODUCTOS ---")
                id_producto = input("ID del producto a actualizar: ").strip()
                titulo = input("Nuevo titulo: ").strip()
                precio_input = input("Nuevo precio: ").strip()
                imagen = input("Nueva ruta de la imagen / URL: ").strip()
                descripcion = input("Nueva descripcion: ").strip()
                stock = input("Nuevo stock: ").strip()
                id_usuario = usuario[0]   
                actualizar_productos(id_producto, titulo, precio_input, imagen, descripcion, stock, id_usuario)
                        
            # Opcion 5. Eliminar productos:
            elif opcion == "5":
                print("\n-- ELIMINAR PRODUCTOS ---")
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
            print("\n --- MENU PRINCIPAL CLIENTE ---")
            print("1. Ver productos: ")
            print("2. Agregar al carrito: ")
            print("3. Ver carrito: ")
            print("4. Actualizar cantidad del carrito: ")
            print("5. Actualizar datos de usuario")
            print("6. Eliminar producto carrito: ")
            print("7. Vaciar carrito: ")
            print("8. Comfirmar compra: ")
            print("9. Cerrar sesion: ")
            opcion = input("Seleccione una opcion: ")
            
            # Opcion 1. Ver productos 
            if opcion == "1":
                print("\n-- PRODUCTOS EN EL CARRITO --")
                obtener_productos()
            
            # Opcion 2. Agregar productos al carrito 
            elif opcion == "2":
                print("\n--AGREGAR PRODUCTOS AL CARRITO--")
                id_producto = input("ID del producto a agregar: ")                
                cantidad_carrito = input("Cantidad: ")
                agregar_al_carrito(id_usuario,id_producto,cantidad_carrito)
            
            # Opcion 3. Mostrar carrito
            elif opcion == "3":
                print("\n--MOSTRAR CARRITO--")
                mostrar_carrito_por_usuario(id_usuario)
            
            # Opcion 4. Actualizar cantidad del carrito
            elif opcion == "4":
                print("\n--ACTUALIZAR CANTIDAD DEL CARRITO--")
                id_carrito = input("Ingrese el ID del carrito: ")
                nueva_cantidad = input("Ingrese la nueva cantidad: ")
                actualizar_cantidad_carrito(id_carrito, nueva_cantidad)
                
            # Opcion 5. Actualizar datos de usuario 
            elif opcion == "5":
                print("\n--ACTUALIZAR DATOS DE USUARIO--")
                
                nombre = input("Nuevo nombre: ").strip()
                apellido = input("Nuevo apellido: ").strip()
                correo = input("Nuevo correo: ").strip()
                telefono = input("Nuevo telefono: ").strip()
                contraseña = input("Nueva contraseña ").strip()
                direccion = input("Nueva direccion: ").strip()  
                actualizar_usuario(id_usuario, nombre, apellido, correo, telefono, contraseña, direccion,)
                
            # Opcion 6. Eliminar productos del carrito
            elif opcion == "6":
                print("\n--ELIMINAR PRODUCTOS DEL CARRITO--")
                id_carrito = input("Digite el ID del carrito a eliminar: ")
                eliminar_producto_carrito(id_carrito)
            
            # Opcion 7. Vaciar carrito
            elif opcion == "7":
                print("\n--VACIAR CARRITO--")
                vaciar_carrito_usuario(id_usuario)
                
            # Opcion 8. Confirmar compra
            elif opcion == "8":
                print("\n--CONFIRMAR COMPRA--")
                confirmar_compra(id_usuario)
            
            # Opcion 9. Agregar productos al carrito 
            elif opcion == "9":
                print("Cerrando sesion ...")
                break
            else:
                print("Opcion no valida")

                
                
                
                
                
                
                
    
            
            
# -------------------------- MENU PRINCIPAL --------------------------
def menu_principal():
    while True:
        print("\n --- MENU  PRINCIPAL ---")
        print("1. Login: ")
        print("2. Crear cuenta")
        print("3. Salir: ")

        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            usuario = login_usuario(correo, contraseña)
            if usuario: 
                mostrar_menu_por_rol(usuario)
        elif opcion == "2":
            print("\n--- REGISTRAR USUARIOS ---")
            nombre = input("Digite su nombre: ").strip()
            apellido = input("Digite su apellido: ").strip()
            correo = input("Digite su correo: ").strip()
            telefono = input("Digite su telefono: ").strip()
            contraseña = input("Digite su contraseña: ").strip()
            direccion = input("Digite su direccion: ").strip()
            id_rol_nuevo = 3
            registrar_usuario(nombre, apellido, correo, telefono, contraseña, direccion, id_rol_nuevo)
        elif opcion == "3":
            break
        else: 
            print("Opcion no valida. ")
            
if __name__ == "__main__":
    app.run(debug=True, port=5000)







