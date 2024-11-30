<?php
session_start();  // Iniciar la sesión
include 'conexion.php';  

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    
    if (isset($_POST['email']) && isset($_POST['password'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];

        
        $stmt = $conexion->prepare("SELECT id, usuario, email, password FROM usuarios WHERE email = ?");
        $stmt->bind_param('s', $email);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result && $result->num_rows > 0) {
            $usuario = $result->fetch_assoc();

            
            if (password_verify($password, $usuario['password'])) {
                
                $_SESSION['usuario'] = $usuario['usuario'];  
                $_SESSION['user_id'] = $usuario['id'];       
                $_SESSION['email'] = $usuario['email'];      

                
                header("Location: index.php");  
                exit();
            } else {
                echo "Contraseña incorrecta.";
            }
        } else {
            echo "Usuario no encontrado.";
        }
        $stmt->close();
    } else {
        echo "Por favor, complete todos los campos.";
    }
}


$conexion->close();
?>
