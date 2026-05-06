import Catalogo from './Catalago';
import React, { useState, useEffect } from 'react';
import Login from './Login';

function App() {
  const [usuarioActivo, setUsuarioActivo] = useState(null);

  useEffect(() => {
    const usuarioGuardado = localStorage.getItem("usuario");
    if (usuarioGuardado) {
      setUsuarioActivo(JSON.parse(usuarioGuardado));
    }
  }, []);

  const finalizarLogin = (datosUsuario) => {
    setUsuarioActivo(datosUsuario);
    // OJO: Cambié "user" por "usuario" para que coincida con tu useEffect de arriba
    localStorage.setItem("usuario", JSON.stringify(datosUsuario));
  };

  const cerrarSesion = () => {
    setUsuarioActivo(null);
    localStorage.removeItem("usuario");
  };

  return (
    <div>
      {/* CONDICIÓN LÓGICA:
          ¿Hay usuario activo? 
          SI: Muestra Bienvenida y Catálogo
          NO: Muestra el Login
      */}
      {usuarioActivo ? (
        <>
          <nav style={{ padding: "10px", background: "#eee" }}>
            <span>Bienvenido, <b>{usuarioActivo.nombre}</b> </span>
            <button onClick={cerrarSesion}>Cerrar Sesión</button>
          </nav>
          <Catalogo />
        </>
      ) : (
        <Login alLoguear={finalizarLogin} /> 
      )}
    </div>
  );
}

export default App;