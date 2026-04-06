import React, {useState, useEffect } from "react";
import Login from "./Login";

function Catalogo() {
    const [usuarioActivo, setUsuario] = useState(null);

    useEffect(() => {
        const usuarioGuardado = localStorage.getItem("usuario");

        if (usuarioGuardado) {
            setUsuario(JSON.parse(usuarioGuardado));
        }
    }, []);
    return (
    <div style={{ padding: "20px" }}>
      <h1>Mi Tienda Virtual</h1>
      <hr />

      {usuarioActivo ? (
        <div>
          <h2>¡Hola de nuevo, {usuarioActivo.nombre}! 👋</h2>
          <p>Tu ID es: {usuarioActivo.id_usuario}</p>
          <button onClick={() => {
            localStorage.removeItem("usuario"); // Para cerrar sesión
            window.location.reload(); // Recarga para volver al login
          }}>
            Cerrar Sesión
          </button>
        </div>
      ) : (
        <Login />
      )}
    </div>
  );
}

export default Catalogo;