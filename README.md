# Problema-Modulo-3---Prog4

🎯 Objetivo
Modificar la aplicación original de biblioteca personal para sustituir SQLite por MariaDB como motor de base de datos e integrar el uso de Object-Relational Mapping (ORM) mediante la biblioteca SQLAlchemy.

📝 Contexto
El objetivo de esta tarea es que los estudiantes adapten la aplicación previamente desarrollada para que funcione con una base de datos MariaDB, utilizando un enfoque moderno de programación orientada a objetos con un ORM.

Esto implica reemplazar el acceso directo a SQLite por una conexión a MariaDB y usar SQLAlchemy para definir y manipular los modelos de datos.

📌 Requisitos funcionales
La aplicación debe seguir ofreciendo las funcionalidades mínimas ya implementadas:

Agregar nuevo libro
➤ Añadir libros especificando título, autor, género y estado de lectura.

Actualizar información de un libro
➤ Modificar detalles como estado de lectura, título, autor o género.

Eliminar libro existente
➤ Borrar un libro registrado.

Ver listado de libros
➤ Mostrar todos los libros registrados.

Buscar libros
➤ Permitir búsquedas por título, autor o género.

Salir
➤ Terminar el programa de forma controlada.

🔄 Cambios y objetivos clave
Reemplazar SQLite con MariaDB como sistema de gestión de base de datos.

Utilizar una herramienta ORM como SQLAlchemy para manejar las operaciones con la base de datos.

Configurar correctamente la conexión a MariaDB, incluyendo usuario, contraseña, host y nombre de base de datos.

Incluir instrucciones claras para instalar y configurar MariaDB en el entorno de desarrollo.

Implementar manejo de excepciones para errores comunes (conexión fallida, integridad, etc.).

💡 Consideraciones técnicas
El proyecto debe utilizar SQLAlchemy como ORM.

Crear un archivo requirements.txt con todas las dependencias necesarias.

El archivo README.md debe incluir:

Instrucciones para instalar MariaDB en el sistema operativo correspondiente

Comandos para crear la base de datos y tabla(s)

Instrucciones para configurar la cadena de conexión

Comando para ejecutar la aplicación
