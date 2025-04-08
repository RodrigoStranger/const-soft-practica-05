USE biblioteca;

-- POST
DELIMITER $$
CREATE PROCEDURE CrearLibro (
    IN p_titulo VARCHAR(255),
    IN p_fecha_publicacion DATE,
    IN p_descripcion TEXT
)
BEGIN
    DECLARE libro_existente INT;
    SELECT COUNT(*) INTO libro_existente FROM Libros WHERE titulo = p_titulo;
    IF libro_existente > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro ya existe en la base de datos.';
    ELSE
        INSERT INTO Libros (titulo, fecha_publicacion, descripcion)
        VALUES (p_titulo, p_fecha_publicacion, p_descripcion);
    END IF;
END $$
DELIMITER ;

-- GET ID
DELIMITER $$
CREATE PROCEDURE ObtenerLibroPorId (IN p_id_libro INT)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Libros WHERE id_libro = p_id_libro) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    END IF;

    SELECT 
        L.titulo AS titulo_libro,
        L.descripcion,
        GROUP_CONCAT(DISTINCT A.nombre SEPARATOR ', ') AS autores,
        GROUP_CONCAT(DISTINCT G.nombre SEPARATOR ', ') AS generos
    FROM Libros L
    LEFT JOIN Libros_Autores LA ON L.id_libro = LA.id_libro
    LEFT JOIN Autores A ON LA.id_autor = A.id_autor
    LEFT JOIN Libros_Generos LG ON L.id_libro = LG.id_libro
    LEFT JOIN Generos G ON LG.id_genero = G.id_genero
    WHERE L.id_libro = p_id_libro
    GROUP BY L.id_libro;
END $$
DELIMITER ;

-- GET ALL
DELIMITER $$
CREATE PROCEDURE ObtenerLibros()
BEGIN
    SELECT 
        L.id_libro,
        L.titulo AS titulo_libro,
        L.descripcion,
        GROUP_CONCAT(DISTINCT A.nombre SEPARATOR ', ') AS autores,
        GROUP_CONCAT(DISTINCT G.nombre SEPARATOR ', ') AS generos
    FROM Libros L
    LEFT JOIN Libros_Autores LA ON L.id_libro = LA.id_libro
    LEFT JOIN Autores A ON LA.id_autor = A.id_autor
    LEFT JOIN Libros_Generos LG ON L.id_libro = LG.id_libro
    LEFT JOIN Generos G ON LG.id_genero = G.id_genero
    GROUP BY L.id_libro
    ORDER BY L.titulo ASC;
END $$
DELIMITER ;

-- PUT
DELIMITER $$
CREATE PROCEDURE ActualizarLibro (
    IN p_id_libro INT,
    IN p_nuevo_titulo VARCHAR(255),
    IN p_fecha_publicacion DATE,
    IN p_descripcion TEXT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Libros WHERE id_libro = p_id_libro) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    END IF;
    UPDATE Libros
    SET titulo = p_nuevo_titulo,
        fecha_publicacion = p_fecha_publicacion,
        descripcion = p_descripcion
    WHERE id_libro = p_id_libro;
END $$
DELIMITER ;

-- PUT
DELIMITER $$
CREATE PROCEDURE DesactivarLibro (IN p_id_libro INT)
BEGIN
    DECLARE estado_actual BOOLEAN;
    SELECT disponible INTO estado_actual FROM Libros WHERE id_libro = p_id_libro;
    IF estado_actual IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    ELSEIF estado_actual = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro ya está marcado como no disponible.';
    ELSE
        UPDATE Libros SET disponible = 0 WHERE id_libro = p_id_libro;
    END IF;
END $$
DELIMITER ;

-- PUT
DELIMITER $$
CREATE PROCEDURE ActivarLibro (IN p_id_libro INT)
BEGIN
    DECLARE estado_actual BOOLEAN;
    SELECT disponible INTO estado_actual FROM Libros WHERE id_libro = p_id_libro;
    IF estado_actual IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    ELSEIF estado_actual = 1 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro ya está marcado como disponible.';
    ELSE
        UPDATE Libros SET disponible = 1 WHERE id_libro = p_id_libro;
    END IF;
END $$
DELIMITER ;

-- POST
DELIMITER $$
CREATE PROCEDURE CrearAutor (
    IN p_nombre VARCHAR(255),
    IN p_fecha_nacimiento DATE,
    IN p_nacionalidad VARCHAR(100)
)
BEGIN
    DECLARE autor_existente INT;
    SELECT COUNT(*) INTO autor_existente FROM Autores WHERE nombre = p_nombre;
    IF autor_existente > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor ya existe en la base de datos.';
    ELSE
        INSERT INTO Autores (nombre, fecha_nacimiento, nacionalidad)
        VALUES (p_nombre, p_fecha_nacimiento, p_nacionalidad);
    END IF;
END $$
DELIMITER ;

-- GET ID
DELIMITER $$
CREATE PROCEDURE ObtenerAutorPorId (
    IN p_id_autor INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Autores WHERE id_autor = p_id_autor) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor no existe en la base de datos.';
    END IF;
    SELECT nombre, fecha_nacimiento, nacionalidad
    FROM Autores
    WHERE id_autor = p_id_autor;
END $$
DELIMITER ;

-- GET ALL
DELIMITER $$
CREATE PROCEDURE ObtenerAutores()
BEGIN
    SELECT nombre, fecha_nacimiento, nacionalidad
    FROM Autores
    ORDER BY nombre ASC;
END $$
DELIMITER ;

-- PUT
DELIMITER $$
CREATE PROCEDURE ActualizarAutor (
    IN p_id_autor INT,
    IN p_nombre VARCHAR(255),
    IN p_fecha_nacimiento DATE,
    IN p_nacionalidad VARCHAR(100)
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Autores WHERE id_autor = p_id_autor) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor no existe en la base de datos.';
    END IF;
    UPDATE Autores
    SET nombre = p_nombre,
        fecha_nacimiento = p_fecha_nacimiento,
        nacionalidad = p_nacionalidad
    WHERE id_autor = p_id_autor;
END $$
DELIMITER ;

-- POST
DELIMITER $$
CREATE PROCEDURE AsignarAutorALibro (
    IN p_id_autor INT,
    IN p_id_libro INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Autores WHERE id_autor = p_id_autor) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor no existe en la base de datos.';
    ELSEIF NOT EXISTS (SELECT 1 FROM Libros WHERE id_libro = p_id_libro) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    ELSEIF EXISTS (
        SELECT 1 FROM Libros_Autores 
        WHERE id_autor = p_id_autor AND id_libro = p_id_libro
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor ya está asignado a este libro.';
    ELSE
        INSERT INTO Libros_Autores (id_libro, id_autor)
        VALUES (p_id_libro, p_id_autor);
    END IF;
END $$
DELIMITER ;

-- POST
DELIMITER $$
CREATE PROCEDURE CrearGenero (
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT
)
BEGIN
    DECLARE genero_existente INT;
    SELECT COUNT(*) INTO genero_existente FROM Generos WHERE nombre = p_nombre;
    IF genero_existente > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El género ya existe en la base de datos.';
    ELSE
        INSERT INTO Generos (nombre, descripcion)
        VALUES (p_nombre, p_descripcion);
    END IF;
END $$
DELIMITER ;

-- GET ID
DELIMITER $$
CREATE PROCEDURE ObtenerGeneroPorId (
    IN p_id_genero INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Generos WHERE id_genero = p_id_genero) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El género no existe en la base de datos.';
    END IF;

    SELECT nombre, descripcion
    FROM Generos
    WHERE id_genero = p_id_genero;
END $$
DELIMITER ;

-- GET ALL
DELIMITER $$
CREATE PROCEDURE ObtenerGeneros()
BEGIN
    SELECT nombre, descripcion
    FROM Generos
    ORDER BY nombre ASC;
END $$
DELIMITER ;

-- PUT
DELIMITER $$
CREATE PROCEDURE ActualizarGenero (
    IN p_id_genero INT,
    IN p_nombre VARCHAR(255),
    IN p_descripcion TEXT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Generos WHERE id_genero = p_id_genero) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El género no existe en la base de datos.';
    END IF;

    UPDATE Generos
    SET nombre = p_nombre,
        descripcion = p_descripcion
    WHERE id_genero = p_id_genero;
END $$
DELIMITER ;

-- POST
DELIMITER $$
CREATE PROCEDURE AsignarGeneroALibro (
    IN p_id_genero INT,
    IN p_id_libro INT
)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Generos WHERE id_genero = p_id_genero) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El género no existe en la base de datos.';
    ELSEIF NOT EXISTS (SELECT 1 FROM Libros WHERE id_libro = p_id_libro) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    ELSEIF EXISTS (
        SELECT 1 FROM Libros_Generos 
        WHERE id_genero = p_id_genero AND id_libro = p_id_libro
    ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El género ya está asignado a este libro.';
    ELSE
        INSERT INTO Libros_Generos (id_libro, id_genero)
        VALUES (p_id_libro, p_id_genero);
    END IF;
END $$
DELIMITER ;

-- TAREA: 
-- LISTAR LOS LIBROS DE UN AUTOR
-- GET
DELIMITER $$
CREATE PROCEDURE ObtenerLibrosPorAutor (IN p_id_autor INT)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Autores WHERE id_autor = p_id_autor) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor no existe en la base de datos.';
    END IF;
    IF NOT EXISTS (SELECT 1 FROM Libros_Autores WHERE id_autor = p_id_autor) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El autor no tiene libros asociados.';
    END IF;
    SELECT 
        L.id_libro, 
        L.titulo, 
        L.fecha_publicacion, 
        L.descripcion 
    FROM 
        Libros L
    JOIN 
        Libros_Autores LA ON L.id_libro = LA.id_libro
    WHERE 
        LA.id_autor = p_id_autor;
END $$
DELIMITER ;

-- LISTAR LOS AUTORES DE UN LIBRO
-- GET
DELIMITER $$
CREATE PROCEDURE ObtenerAutoresPorLibro (IN p_id_libro INT)
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Libros WHERE id_libro = p_id_libro) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no existe en la base de datos.';
    END IF;
    IF NOT EXISTS (SELECT 1 FROM Libros_Autores WHERE id_libro = p_id_libro) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El libro no tiene autores asociados.';
    END IF;
    SELECT 
        A.id_autor, 
        A.nombre, 
        A.fecha_nacimiento, 
        A.nacionalidad 
    FROM 
        Autores A
    JOIN 
        Libros_Autores LA ON A.id_autor = LA.id_autor
    WHERE 
        LA.id_libro = p_id_libro;
END $$
DELIMITER ;