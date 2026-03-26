CREATE DATABASE db_first_proyect;







CREATE TABLE ROL(
	id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol varchar(50) NOT NULL
);




CREATE TABLE USUARIO(
	id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario varchar(50) NOT NULL,
    apellido_usuario varchar(50) NOT NULL,
    correo_usuario varchar(60) NOT NULL,
    telefono_usuario varchar(30) NOT NULL,
    contraseña_usuario varchar(200) NOT NULL,
    direccion_usuario varchar(100) NOT NULL,
    id_rol INT,
    FOREIGN KEY (id_rol) REFERENCES ROL(id_rol)
);



CREATE TABLE PRODUCTO(
	id_producto INT AUTO_INCREMENT PRIMARY KEY,
    titulo_producto varchar(100) NOT NULL,
    precio_producto DECIMAL(10,2) NOT NULL,
    imagen_producto varchar(300),
    descripcion_producto text,
    stock_producto INT NOT NULL DEFAULT 0,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
    
    
);



CREATE TABLE CARRITO(
	id_carrito INT AUTO_INCREMENT PRIMARY KEY,
    metodo_pago_carrito varchar(100) NOT NULL,
    cantidad_carrito varchar(100) NOT NULL,
    id_usuario INT,
    id_producto INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

-- Inserccion de datos del rol
INSERT INTO `rol`VALUES (1,'cliente');
INSERT INTO `rol`VALUES (2,'empleado');
INSERT INTO `rol`VALUES (3,'cliente');


-- Inserccion de productos 
INSERT INTO `producto` VALUES (1,'Pesas','10000','url','Texto','59',1);
INSERT INTO `producto` VALUES (2,'Saco de Box','50000','url','Texto','100',2);