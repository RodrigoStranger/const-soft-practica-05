USE biblioteca;

INSERT INTO Generos (nombre, descripcion)
VALUES
('Ficción', 'Narrativa que describe eventos y personajes que no corresponden a la realidad, pero que pueden estar inspirados en hechos reales.'),
('No Ficción', 'Obras literarias que se basan en hechos reales, investigaciones, biografías y relatos verídicos.'),
('Ciencia Ficción', 'Género que imagina futuros avances científicos y tecnológicos, así como sus impactos en la sociedad, el espacio o el tiempo.'),
('Fantasía', 'Narrativa que presenta mundos imaginarios con elementos sobrenaturales, como magia, criaturas fantásticas y mundos alternativos.'),
('Misterio', 'Obras que giran en torno a resolver enigmas, crímenes o sucesos inexplicables, y cuya trama se desarrolla a través de la investigación.'),
('Romántico', 'Historias centradas en relaciones amorosas, explorando el amor, los sentimientos y las complejidades de las relaciones románticas.'),
('Biografía', 'Relato de la vida de una persona, escrito por otro autor, generalmente con un enfoque histórico, social o emocional.'),
('Historia', 'Género que estudia y narra hechos y eventos pasados de la humanidad, interpretando su relevancia y contexto a lo largo del tiempo.'),
('Terror', 'Género literario cuyo objetivo es generar miedo, horror y tensión en el lector a través de situaciones macabras o sobrenaturales.'),
('Autoayuda', 'Libros que buscan mejorar la vida del lector proporcionando consejos prácticos sobre bienestar, desarrollo personal y emocional.');

INSERT INTO Autores (nombre, fecha_nacimiento, nacionalidad)
VALUES
('Gabriel García Márquez', '1927-03-06', 'Colombia'),
('Plinio Apuleyo Mendoza', '1932-01-01', 'Colombia'),
('Mario Vargas Llosa', '1936-03-28', 'Perú'),
('Jorge Luis Borges', '1899-08-24', 'Argentina'),
('Adolfo Bioy Casares', '1914-09-15','Argentina'),
('Pablo Neruda', '1904-07-12', 'Chile'),
('Julio Cortázar', '1914-08-26', 'Argentina'),
('Isabel Allende', '1942-08-02', 'Chile'),
('Carlos Fuentes', '1928-11-11', 'México'),
('Octavio Paz', '1914-03-31', 'México'),
('Laura Esquivel', '1950-09-30', 'México'),
('Rubén Darío', '1867-01-18', 'Nicaragua'),
('Mario Benedetti', '1920-09-14', 'Uruguay'),
('Vicente Huidobro', '1893-01-10', 'Chile'),
('Alejo Carpentier', '1904-12-26', 'Cuba'),
('Juan Rulfo', '1917-05-16', 'México'),
('Sor Juana Inés de la Cruz', '1648-11-12', 'México'),
('Horacio Quiroga', '1878-12-31', 'Uruguay'),
('Eduardo Galeano', '1940-09-03', 'Uruguay'),
('María Dueñas', '1960-01-01', 'España'),
('Ricardo Piglia', '1941-12-24', 'Argentina'),
('César Vallejo', '1892-03-16', 'Perú'),
('José María Arguedas', '1911-01-18', 'Perú'),
('Alfredo Bryce Echenique', '1939-02-19', 'Perú'),
('Ricardo Palma', '1833-02-07', 'Perú');

INSERT INTO Libros (titulo, fecha_publicacion, descripcion, disponible)
VALUES
-- Gabriel García Márquez
('Cien Años de Soledad', '1967-06-05', 'Una obra maestra de Gabriel García Márquez que narra la historia de la familia Buendía en el mítico pueblo de Macondo, explorando el realismo mágico y las complejidades del tiempo.', 1),
('El Amor en los Tiempos del Cólera', '1985-06-05', 'Una novela de Gabriel García Márquez que narra la historia de un amor que sobrevive a través del tiempo, la enfermedad y la guerra.', 1),
('Crónica de una Muerte Anunciada', '1981-06-01', 'Un relato de Gabriel García Márquez sobre un asesinato premeditado en un pequeño pueblo, explorando el destino y la inevitabilidad.', 1), -- Tiene doble autor que es Plinio Apuleyo Mendoza
-- Mario Vargas Llosa
('La Fiesta del Chivo', '2000-01-01', 'Una obra de Mario Vargas Llosa que describe la dictadura de Trujillo en la República Dominicana a través de una trama de terror y opresión.', 1),
('Conversación en La Catedral', '1969-01-01', 'Una novela de Mario Vargas Llosa que relata la historia de un periodista que busca la verdad sobre la corrupción política en Perú durante la dictadura de Odría.', 1),
('La Casa Verde', '1966-01-01', 'Una novela compleja de Mario Vargas Llosa que explora la vida en una ciudad peruana ficticia y las tensiones políticas y sociales de la época.', 1),
-- Jorge Luis Borges
('Ficciones', '1944-01-01', 'Un conjunto de relatos de Borges que exploran laberintos, realidades alternativas, y lo infinito en el marco del realismo fantástico.', 1),
('El Aleph', '1949-06-01', 'Un libro de Jorge Luis Borges que presenta una colección de cuentos con temas de infinito, tiempo y el concepto de universos paralelos.', 1), -- Tiene doble autor que es Adolfo Bioy Casares
('Labyrinths', '1962-01-01', 'Una colección de cuentos y ensayos de Jorge Luis Borges que explora temas de lo imposible, los laberintos, la identidad y la eternidad.', 1),
-- Pablo Neruda
('Veinte Poemas de Amor y Una Canción Desesperada', '1924-01-01', 'Una colección de poemas románticos y apasionados escritos por Pablo Neruda, que exploran el amor y la pérdida.', 1),
('Canto General', '1950-01-01', 'Un extenso poema épico de Pablo Neruda que describe la historia de América Latina y sus luchas sociales, políticas y culturales.', 1),
('Confieso que he Vivido', '1974-01-01', 'Una autobiografía de Pablo Neruda en la que reflexiona sobre su vida, su poesía y su compromiso político.', 1),
-- Julio Cortázar
('Rayuela', '1963-06-28', 'Una novela innovadora de Julio Cortázar que presenta múltiples formas de lectura, rompiendo las convenciones de la narrativa tradicional.', 1),
('Bestiario', '1951-01-01', 'Una colección de cuentos de Julio Cortázar que mezcla lo real con lo surreal y lo extraño, donde las fronteras entre lo humano y lo animal se disipan.', 1),
('Final del Juego', '1956-01-01', 'Un conjunto de relatos de Julio Cortázar que explora los límites de la realidad y la fantasía, con su característico estilo experimental.', 1),
-- Isabel Allende
('La Casa de los Espíritus', '1982-11-01', 'La novela debut de Isabel Allende, que narra la historia de una familia a través de generaciones, explorando el realismo mágico y los cambios sociales en Chile.', 1),
('Eva Luna', '1987-01-01', 'Una obra de Isabel Allende que narra la historia de Eva Luna, una mujer que, mediante su capacidad de contar historias, da voz a su pueblo.', 1),
('Paula', '1994-03-01', 'Una novela autobiográfica de Isabel Allende en la que narra la vida de su hija Paula y la enfermedad que la llevó a la muerte.', 1),
-- Carlos Fuentes
('La Muerte de Artemio Cruz', '1962-01-01', 'Una de las obras más destacadas de Carlos Fuentes, que narra la vida de Artemio Cruz a través de su lecho de muerte, reflexionando sobre el poder y la corrupción.', 1),
('Terra Nostra', '1975-01-01', 'Una novela épica de Carlos Fuentes que abarca la historia de España y América Latina, explorando temas de poder, cultura y memoria.', 1),
('Aura', '1962-01-01', 'Una novela corta de Carlos Fuentes que mezcla lo sobrenatural y lo psicológico, narrando la historia de una joven que vive en un mundo de misterio y secretos.', 1),
-- Octavio Paz
('El Laberinto de la Soledad', '1950-01-01', 'Una obra de Octavio Paz que analiza la identidad mexicana, la historia y la soledad del individuo en la cultura mexicana.', 1),
('Piedra de Sol', '1957-01-01', 'Un largo poema de Octavio Paz que explora temas como el tiempo, la vida, el amor y la muerte, usando la forma del soneto.', 1),
('El Arco y la Lira', '1956-01-01', 'Un ensayo de Octavio Paz en el que reflexiona sobre el papel de la poesía en la vida humana y la cultura.', 1),
-- Laura Esquivel
('Como Agua para Chocolate', '1989-01-01', 'Una novela de Laura Esquivel que mezcla recetas de cocina y relatos de amor, abordando la vida de una familia en el México revolucionario.', 1),
('La Ley del Amor', '1995-01-01', 'Una novela de Laura Esquivel que explora el amor en sus diversas formas a lo largo del tiempo, entrelazando ciencia ficción y realismo mágico.', 1),
('Tan Veloz como el Deseo', '1995-01-01', 'Una novela de Laura Esquivel que narra las historias de varias mujeres en un contexto de amores, pasiones y secretos familiares.', 1),
-- Rubén Darío
('Azul', '1888-01-01', 'Un libro de Rubén Darío que marca el inicio del modernismo en la poesía latinoamericana, con sus innovadoras formas y ritmos poéticos.', 1),
('Cantos de Vida y Esperanza', '1905-01-01', 'Una obra poética de Rubén Darío que explora el sufrimiento humano, el amor y la muerte desde un enfoque modernista.', 1),
('Los Raros', '1896-01-01', 'Una colección de ensayos de Rubén Darío donde reflexiona sobre la vida de diversos personajes destacados en la historia, la cultura y el arte.', 1),
-- Mario Benedetti
('La Tregua', '1960-01-01', 'Una novela de Mario Benedetti que relata la historia de un hombre que, en medio de su rutina diaria, se encuentra con un amor inesperado.', 1),
('Gracias por el Fuego', '1965-01-01', 'Una obra de Mario Benedetti que narra la historia de un joven que busca dar sentido a su vida en medio de una sociedad desigual.', 1),
('El Otro Yo', '1965-01-01', 'Una novela de Mario Benedetti que explora las emociones, los sentimientos y las dificultades de un hombre atrapado en su vida cotidiana.', 1),
-- Vicente Huidobro
('Altazor', '1931-01-01', 'Un poema vanguardista de Vicente Huidobro, que explora la ruptura de las estructuras lingüísticas y literarias convencionales.', 1),
('Poemas Árticos', '1918-01-01', 'Una colección de poemas de Vicente Huidobro que refleja su estilo innovador y experimental, y sus preocupaciones sobre la naturaleza y el ser humano.', 1),
('La Poesía', '1936-01-01', 'Un ensayo de Vicente Huidobro que analiza la creación poética y la búsqueda del sentido a través de la palabra.', 1),
-- Alejo Carpentier
('El Reino de Este Mundo', '1949-01-01', 'Una novela de Alejo Carpentier que explora la historia de Haití, mezclando lo histórico y lo fantástico.', 1),
('Los Pasos Perdidos', '1953-01-01', 'Una novela de Alejo Carpentier que narra la experiencia de un músico cubano que viaja a América Latina, enfrentando sus propios dilemas existenciales.', 1),
('El Siglo de las Luces', '1962-01-01', 'Una novela de Alejo Carpentier que explora el impacto de la Revolución Francesa en Cuba y América Latina.', 1),
-- Juan Rulfo
('Pedro Páramo', '1955-01-01', 'Una novela de Juan Rulfo que explora la historia de un joven que viaja a Comala, un pueblo donde descubre las voces de los muertos.', 1),
('El Llano en Llamas', '1953-01-01', 'Una colección de cuentos de Juan Rulfo que capturan las luchas sociales y existenciales de los habitantes de un pueblo mexicano en el campo.', 1),
-- Sor Juana Inés de la Cruz
('Inundación Castálida', '1689-01-01', 'Una obra literaria de Sor Juana Inés de la Cruz que refleja su profundo conocimiento de la teología, la poesía y la filosofía.', 1),
('Carta Atenagórica', '1700-01-01', 'Una carta escrita por Sor Juana Inés de la Cruz en la que defiende el derecho de las mujeres a la educación y la intelectualidad.', 1),
-- Horacio Quiroga
('Cuentos de la Selva', '1918-01-01', 'Una colección de cuentos de Horacio Quiroga que reflejan la vida y los peligros de la selva misionera en Argentina y Uruguay.', 1),
('Los Buques Suicidantes', '1937-01-01', 'Una obra de Horacio Quiroga que narra los misterios y las tragedias de un hombre que se enfrenta a la muerte a través de la literatura.', 1),
-- Eduardo Galeano
('Las Venas Abiertas de América Latina', '1971-01-01', 'Una obra de Eduardo Galeano que describe las injusticias económicas y sociales sufridas por América Latina a lo largo de su historia.', 1),
('Memoria del Fuego', '1986-01-01', 'Una trilogía de Eduardo Galeano que relata la historia de América Latina, desde sus inicios hasta el siglo XX, mediante una mirada crítica y poética.', 1),
-- María Dueñas
('La Templanza', '2015-03-17', 'Una novela de María Dueñas que narra la historia de un hombre que se ve envuelto en el mundo del vino y el comercio durante el siglo XIX en México.', 1),
('El Tiempo entre Costuras', '2009-06-25', 'Una novela de María Dueñas que relata la historia de una joven costurera durante la Guerra Civil Española, entrelazando amor y espionaje.', 1),
('Las Hijas del Capitán', '2018-06-14', 'Una historia sobre tres hermanas que luchan por salir adelante después de la muerte de su padre, un capitán de barco.', 1),
-- Ricardo Piglia
('Artificial Respiration', '1980-01-01', 'Una novela de Ricardo Piglia que explora la historia de un joven argentino y su relación con el arte, la política y la historia del país.', 1),
('The Absent City', '1992-01-01', 'Una novela de Ricardo Piglia sobre la historia de un hombre que busca entender la ciudad de Buenos Aires a través de los ojos de otros.', 1),
-- César Vallejo
('Los Heraldos Negros', '1919-01-01', 'Un libro de poesía de César Vallejo que aborda el sufrimiento, la muerte y la angustia existencial, con un estilo profundamente emocional.', 1),
('Trilce', '1922-01-01', 'Una obra innovadora de César Vallejo que mezcla simbolismo, vanguardismo y surrealismo para explorar la vida humana, el sufrimiento y el amor.', 1),
('Poemas Humanos', '1939-01-01', 'Una colección de poemas de César Vallejo en los que el autor reflexiona sobre la injusticia social, la guerra y las dificultades humanas.', 1),
-- José María Arguedas
('Los Ríos Profundos', '1958-01-01', 'Una novela de José María Arguedas que relata la vida de un joven en los Andes peruanos y su relación con la cultura indígena y mestiza.', 1),
('El Zorro de Arriba y el Zorro de Abajo', '1965-01-01', 'Una novela de José María Arguedas que narra el conflicto entre la tradición andina y la modernidad urbana en Perú.', 1),
-- Alfredo Bryce Echenique
('Un Mundo para Julius', '1970-01-01', 'Una novela de Alfredo Bryce Echenique que cuenta la vida de un niño en Lima, explorando la desconexión de la clase alta peruana con la realidad social.', 1),
('La Amistad', '2002-01-01', 'Una obra de Alfredo Bryce Echenique que explora las relaciones personales y la vida cotidiana de un hombre que busca un sentido en su existencia.', 1),
('El Huésped', '2001-01-01', 'Una novela de Alfredo Bryce Echenique sobre un hombre que trata de comprender la soledad y las conexiones humanas en un mundo cada vez más alienante.', 1),
-- Ricardo Palma
('Peruana', '1872-01-01', 'Una colección de relatos y leyendas de Ricardo Palma que exploran mitos, supersticiones y misterios populares del Perú.', 1),
('Cuentos de la Abuela', '1890-01-01', 'Una serie de cuentos populares peruanos recopilados y adaptados por Ricardo Palma, explorando la cultura popular de su país.', 1);