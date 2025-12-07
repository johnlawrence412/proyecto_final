# Sistema de Control de Biblioteca

Proyecto final desarrollado en Python utilizando Flet para la gestión de una biblioteca.

## Estado del Proyecto

Actualmente se ha completado la primera fase del desarrollo.

| Módulo | Estado | Descripción |
| :--- | :--- | :--- |
| **Gestión de Libros** | Completado | Módulo funcional para registro y visualización de inventario. |
| **Gestión de Clientes** | Pendiente | En desarrollo. |
| **Préstamos** | Pendiente | En desarrollo. |

## Guía de Uso

### Módulo de Libros
Para registrar un nuevo libro en el sistema:

1. Navegue a la pestaña **"Libros"**.
2. Complete los campos obligatorios: **Título**, **Autor** e **ISBN**.
3. Presione el botón **"Registrar Libro"**.
4. Verifique la tabla inferior:
   - El libro aparecerá automáticamente en la lista.
   - El estado **"Disponible"** se mostrará en color verde.
   - Si intenta registrar un ISBN repetido, el sistema mostrará un mensaje de error.

## Instrucciones de Instalación

1. Instalar la librería necesaria:
   pip install flet