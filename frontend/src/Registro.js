import React, { useState } from "react";


function Registro() {
  // Estado inicial del formulario
  const [form, setForm] = useState({
    nombre: "",
    apellido: "",
    correo: "",
    telefono: "",
    password: "", // Cambiado de 'contraseña' para evitar errores de codificación
    direccion: "",
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
      const respuesta = await fetch("http://localhost:5000/registro", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(form), // Enviamos el objeto 'form' completo
      });

      const data = await respuesta.json();
      console.log("Respuesta del servidor:", data);
      alert("Registro exitoso");
    } catch (error) {
      console.error("Error al conectar con el servidor:", error);
      alert("Hubo un error al registrar:", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Formulario de Registro</h2>
      <form onSubmit={handleSubmit}>
        <input name="nombre" placeholder="Nombre" onChange={handleChange} />
        <input name="apellido" placeholder="Apellido" onChange={handleChange} />
        <input name="correo" type="email" placeholder="Correo" onChange={handleChange} />
        <input name="telefono" placeholder="Teléfono" onChange={handleChange} />
        <input name="password" type="password" placeholder="Contraseña" onChange={handleChange} />
        <input name="direccion" placeholder="Dirección" onChange={handleChange} />
        
        <button type="submit">Enviar Registro</button>
      </form>
    </div>
  );
}

export default Registro;