import { useEffect, useState } from "react";

function App() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/productos")
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setProductos(data);
      })
      .catch(error => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h1>Mi proyecto</h1>
      <h2>{JSON.stringify(productos)}</h2>
      <ul>
        {productos.map(producto => (
          <li key={producto.id}>
            {producto.nombre} - ${producto.precio}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;