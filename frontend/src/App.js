
import Registro from './Registro'; // Importas el que ya tenías
import React, { useState, useEffect } from 'react';
import Login from './Login';

function App() {
  const [usuarioActivo, setUsuarioActivo] = useState(null);
        // Esta función la creamos para que Login la pueda usar

  useEffect(() => {
    const usuarioGuardado = localStorage.getItem("usuario");
    if (usuarioGuardado) {
      setUsuarioActivo(JSON.parse(usuarioGuardado));
    }
  }, []);


  const finalizarLogin = (datosUsuario) => {
    setUsuarioActivo(datosUsuario);
};

  return (
   <div style={{ padding: "20px" }}>
      {usuarioActivo ? (
        <div>
          <h2>¡Hola de nuevo, {usuarioActivo.nombre}! 👋</h2>
          <button onClick={() => {
            localStorage.removeItem("usuario"); // Borramos la sesión
            setUsuarioActivo(null); // Actualizamos la pantalla
          }}>
            Cerrar Sesión
          </button>
        </div>
      ) : (
        <Login alLoguear={finalizarLogin} />
      )}
    </div>
  );
}

export default App;