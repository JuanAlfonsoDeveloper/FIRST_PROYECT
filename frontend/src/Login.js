import React, { useState } from "react";

function Login({ alLoguear }){
    const[form, setForm] = useState({
        correo: "",
        password: "",
    });
  
    // Función para capturar lo que el usuario escribe
  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({
      ...form,
      [name]: value,
    });
  };

  
  // Función para enviar los datos al backend (Flask)
  const handleSubmit = async (e) => {
    e.preventDefault(); // Evita que la página se recargue

    try {
      const respuesta = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form), // Enviamos el objeto 'form' completo
      });

      const data = await respuesta.json();
      if (respuesta.ok) {
        // Guardamos los datos en el navegador
        localStorage.setItem("usuario", JSON.stringify(data.usuario));
        
        // ¡ESTO ES LO NUEVO! 
        // Avisamos a App.js que ya tenemos usuario para que cambie la pantalla
        alLoguear(data.usuario); 

        alert(`Bienvenido de nuevo, ${data.usuario.nombre}`);
    }
    } catch (error) { 
        console.error("Error de red:", error);
        alert("No se pudo conectar con el servidor");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Iniciar seccion</h2>
      <form onSubmit={handleSubmit}>
        <input name="correo" type="email" placeholder="Correo" onChange={handleChange} />
        <input name="password" type="password" placeholder="Contraseña" onChange={handleChange} />
        <button type="submit">Enviar Registro</button>
      </form>
    </div>
  );
}

export default Login;