<?php
session_start();  // Iniciar sesión
include 'conexion.php';  

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    
    if (isset($_POST['usuario'], $_POST['nombre'], $_POST['apellido_paterno'], $_POST['email'], $_POST['password'], $_POST['confirm_password'])) {
        $usuario = $_POST['usuario'];
        $nombre = $_POST['nombre'];
        $apellido_paterno = $_POST['apellido_paterno'];
        $apellido_materno = $_POST['apellido_materno'];
        $email = $_POST['email'];
        $password = $_POST['password'];
        $confirm_password = $_POST['confirm_password'];

        
        if ($password !== $confirm_password) {
            echo "Las contraseñas no coinciden.";
            exit();
        }

        
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        
        $stmt = $conexion->prepare("SELECT id FROM usuarios WHERE email = ?");
        $stmt->bind_param('s', $email);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result && $result->num_rows > 0) {
            echo "El correo electrónico ya está registrado.";
            exit();
        }

        
        $stmt = $conexion->prepare("INSERT INTO usuarios (usuario, nombre, apellido_paterno, apellido_materno, email, password) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->bind_param('ssssss', $usuario, $nombre, $apellido_paterno, $apellido_materno, $email, $hashed_password);

        if ($stmt->execute()) {
            echo "Registro exitoso. Por favor, inicie sesión.";
            
            header("Location: ../inicio_sesion.php");
            exit();
        } else {
            echo "Hubo un error al registrar el usuario. Intente nuevamente.";
        }

        $stmt->close();
    } else {
        echo "Por favor, complete todos los campos.";
    }
}

// Cerrar la conexión
$conexion->close();
?>
