import React, {useState, useEffect } from "react";
import Login from "./Login";

function Catalogo() {
    const [usuarioActivo, setUsuario] = useState(null);
    const [productos, setProductos] = useState([]);
    

    useEffect(() => {
        const usuarioGuardado = localStorage.getItem("usuario");
        if (usuarioGuardado) {
            setUsuario(JSON.parse(usuarioGuardado));
        }
        fetch("http://localhost:5000/productos")
        .then(res => res.json())
        .then(data => {
          setProductos(data);
        })
        .catch(err => console.error("Error al traer productos:", err));
    }, []);
    return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
            <h1>Mi Tienda Virtual</h1>
            <hr />

            {usuarioActivo ? (
                <div>
                    <h2>¡Hola, {usuarioActivo.nombre}! 👋</h2>
                    <button onClick={() => { 
                        localStorage.removeItem("usuario"); 
                        window.location.reload(); 
                    }}>Cerrar Sesión</button>

                    {/* --- GRILLA DE PRODUCTOS --- */}
                    <div style={{ 
                        display: "grid", 
                        gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", 
                        gap: "20px", 
                        marginTop: "20px" 
                    }}>
                        {productos.map((p) => (
                            <div key={p.id} style={{ 
                                border: "1px solid #ccc", 
                                borderRadius: "8px", 
                                padding: "10px", 
                                textAlign: "center" 
                            }}>
                                {/* Mostramos la imagen (asegurate que el link en la DB sea válido) */}
                                <img src={p.imagen} alt={p.nombre} style={{ width: "100%", height: "150px", objectFit: "cover" }} />
                                <h3>{p.nombre}</h3>
                                <p>{p.descripcion}</p>
                                <p><strong>${p.precio}</strong></p>
                                <button style={{ cursor: "pointer", padding: "5px 10px" }}>
                                    Añadir al Carrito 🛒
                                </button>
                            </div>
                        ))}
                    </div>
                </div>
            ) : (
                <Login />
            )}
        </div>
    );
}

export default Catalogo;