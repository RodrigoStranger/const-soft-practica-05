# Autores y Libros - Nivel 2

📚 **Curso**: Construcción de Software  
📅 **Ciclo Académico:** 2025 - I  
🎓 **Semestre:** VII  
👨‍🏫 **Profesor:** Vicente Enrique Machaca Arceda

---

### ✍️ Autores  
- 👨‍💻 [Rodrigo Emerson Infanzón Acosta](https://github.com/rodrigostranger)  
- 👩‍💻 [Esthephany Erika Choquehuanca Layme](https://github.com/Esthephany24)  
- 👨‍💻 [Carlos Daniel Aguilar Chirinos](https://github.com/CDanielAg)  
- 👩‍💻 [Angela Milagros Quispe Huanca](https://github.com/Mila21xy)

---

## Estructura del proyecto

```bash
const-soft-practica-05
├── backend
│   ├── blueprints
│   │   └── autores_blueprint.py
│   │   └── generos_blueprint.py
│   │   └── libros_blueprint.py
│   │   └── server_blueprint.py
│   └── models
│       └── mysql_connection_pool.py
│       └── mysql_autores_model.py
│       └── mysql_generos_model.py
│       └── mysql_libros_model.py
├── mysql
│   └── biblioteca-datos.sql
│   └── biblioteca-diagrama.mwb
│   └── biblioteca-modelo-fisico.PNG
│   └── biblioteca-procedimientos-almacenados.sql
│   └── biblioteca.sql
│   └── usuariosbiblioteca-modelo-fisico.PNG
│   └── usuariosbiblioteca.sql
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

---

## Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## Bases de datos
**Base de datos de la biblioteca:**


<p align="center">
  <img src="https://github.com/RodrigoStranger/const-soft-practica-05/blob/main/mysql/biblioteca-modelo-fisico.PNG?raw=true" alt="Base de datos de la biblioteca" width="570"/>
</p>


**Base de datos de los usuarios:**


<p align="center">
  <img src="https://github.com/RodrigoStranger/const-soft-practica-05/blob/main/mysql/usuariosbiblioteca-modelo-fisico.PNG?raw=true" alt="Base de datos de los usuarios" width="250"/>
</p>

---

## Variables de entorno

👨‍🏫 **Video de referencia:** https://www.youtube.com/watch?v=oIbiHiNL0yc

### Variables de entorno usadas

```bash
MYSQL_DATABASE: Es el nombre de la base de datos principal que vas a utilizar en tu aplicación.
MYSQL_DATABASE_2: Es el nombre de una segunda base de datos, en caso de que necesites acceder a otra base de datos adicional.
MYSQL_HOST: Es la dirección del servidor donde está alojada tu base de datos MySQL, que puede ser una IP o un nombre de dominio.
MYSQL_PASSWORD: Es la contraseña correspondiente al usuario de la base de datos MySQL que se usará para autenticarte.
MYSQL_USER: Es el nombre de usuario que utilizarás para conectarte a la base de datos MySQL.
MYSQL_PORT: Es el puerto en el que el servidor MySQL está escuchando; el puerto por defecto es generalmente el 3306.
SECRET_KEY: Es una clave secreta utilizada para la autenticación y la seguridad de tu aplicación, importante para proteger datos sensibles.
```



---

## Ejecución

Corren dos servidores:

```bash
python app.py
```

```bash
python backend_server.py
```
