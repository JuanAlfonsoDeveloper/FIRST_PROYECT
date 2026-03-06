import { useState } from "react";

function Registro() {
    const [nombre, setNombre] = useState("");
    const [apellido, setApellido] = useState("");
    const [correo, setCorreo] = useState("");
    const [telefono, setTelefono] = useState("");
    const [contraseña, setContraseña] = useState("");
    const [direccion, setDireccion] = useState("");
    
    return(
    <div>
        <h2>Registro</h2>

        {/* Este es un comentario en JSX */}
        <form onSubmit={handleSubmit}>
            <input placeholder="Nombre" type="text"/>
            <input placeholder="Apellido" type="text"/>
            <input placeholder="Correo" type="email"/>
            <input placeholder="Telefono" type="text"/>
            <input placeholder="Contraseña" type="password"/>
            <input placeholder="Direccion" type="text"/>
            
            <button type="submit">Registrar</button>
        </form>
        

    </div>
    )
}
export default Registro;

