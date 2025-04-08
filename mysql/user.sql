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

DELIMITER $$
CREATE PROCEDURE validar_usuario(IN p_username VARCHAR(255), IN p_password VARCHAR(255))
BEGIN
    DECLARE user_exists INT;
    SELECT 1 INTO user_exists
    FROM user
    WHERE username = p_username AND password = p_password
    LIMIT 1;
    IF user_exists IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Credenciales no válidas';
    END IF;
END $$
DELIMITER ;