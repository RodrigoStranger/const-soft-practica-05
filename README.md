# Autores y Libros - Nivel 2

Este repositorio, almacena la mejora y el funcionamiento de un pequeño sistema bibliotecario usando las practicas de programacion usados en el curso de Construccion de Software 25 - I

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
└── mysql
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
## Instalar dependencias
```bash
pip install -r requirements.txt
```
