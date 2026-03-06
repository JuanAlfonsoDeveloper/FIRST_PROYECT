import Registro from "./pages/registro"

function App() {

  const handleSubmit = async (e) => {
    e.preventDefault();
    const datos = {
      nombre: nombre,
      apellido: apellido,
      correo: correo,
      telefono: telefono,
      contraseña: contraseña,
      direccion: direccion
    };

    const respuesta = await
  fetch("http://127.0.0.1:5000/registro", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(datos)
  });

  const data = await respuesta.json();

  console.log(data);

  };
  return (
    <div>
      < Registro />
    </div>
  )
}

export default App;
