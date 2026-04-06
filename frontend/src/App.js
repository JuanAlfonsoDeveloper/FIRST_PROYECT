
import Catalogo from './Catalago';
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
    localStorage.setItem("user", JSON.stringify(datosUsuario));
};

  return (
   <div className="App">
      {/* 3. La Lógica del Portero: */}
      { !usuarioActivo ? (
          // Si NO hay usuario, muestra el Login y pásale la función
          <Login alLoguear={finalizarLogin} />
      ) : (
          // Si HAY usuario, muestra el Catálogo y un saludo
          <div>
            <h1>¡Hola, {usuarioActivo.nombre}!</h1>
            <button onClick={() => setUsuarioActivo(null)}>Cerrar Sesión</button>
            <Catalogo />
          </div>
      )}
    </div>
  );
}

export default App;