
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
   <div>
    <Catalogo/>
   </div>
  );
}

export default App;