import React, { useEffect, useState } from "react";

function App() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/productos")
      .then(response => response.json())
      .then(data => {
        console.log("Datos del bakend:", data);
        setProductos(data);
      })
      .catch(error => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h1>Mi proyecto</h1>
      <pre>{JSON.stringify(productos, null, 2)}</pre>
    </div>
  );
}

export default App;