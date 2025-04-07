CREATE DATABASE IF NOT EXISTS biblioteca;

USE biblioteca;

CREATE TABLE Generos (
    id_genero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (nombre)
);

CREATE TABLE Autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    nacionalidad VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (nombre)
);

CREATE TABLE Libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    fecha_publicacion DATE,
    descripcion TEXT,
    disponible BOOLEAN DEFAULT TRUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (titulo)
);

CREATE TABLE Libros_Autores (
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro) ON UPDATE CASCADE,
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor) ON UPDATE CASCADE
);

CREATE TABLE Libros_Generos (
    id_libro INT,
    id_genero INT,
    PRIMARY KEY (id_libro, id_genero),
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro) ON UPDATE CASCADE,
    FOREIGN KEY (id_genero) REFERENCES Generos(id_genero) ON UPDATE CASCADE
);