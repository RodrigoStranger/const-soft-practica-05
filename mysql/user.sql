CREATE DATABASE IF NOT EXISTS user;

USE user;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

INSERT INTO users (nombre, contraseña) VALUES ('rodrigo', 'admin');
INSERT INTO users (nombre, contraseña) VALUES ('angela', 'admin');
INSERT INTO users (nombre, contraseña) VALUES ('daniel', 'admin');
INSERT INTO users (nombre, contraseña) VALUES ('esthephany', 'admin');