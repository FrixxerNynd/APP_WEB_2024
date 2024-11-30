<?php
// session_start();

// Verificar si el usuario está autenticado
function verificarAutenticado() {
    if (!isset($_SESSION['user_id'])) {
        header('Location: index.php');  // Redirigir a la página de login si no está autenticado
        exit();
     }
 }


$isLoggedIn = isset($_SESSION['user_id']);


if ($isLoggedIn) {
    $user_name = $_SESSION['usuario'];  // Nombre de usuario
    $user_email = $_SESSION['email'];  // Email del usuario
} else {
    $user_name = '';  
    $user_email = '';  
}

?>
