<?php
$conexion = new mysqli(
    'localhost',
    'root', '',
    'proyectoutd'
);

if ($conexion->connect_error) {
    die("Conexión fallida: " . $conexion->connect_error);
}
?>
