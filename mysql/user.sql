CREATE DATABASE IF NOT EXISTS usuariosbiblioteca;

USE usuariosbiblioteca;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

INSERT INTO usuarios (nombre, contraseña) VALUES ('rodrigo', 'admin');
INSERT INTO usuarios (nombre, contraseña) VALUES ('angela', 'admin');
INSERT INTO usuarios (nombre, contraseña) VALUES ('daniel', 'admin');
INSERT INTO usuarios (nombre, contraseña) VALUES ('esthephany', 'admin');