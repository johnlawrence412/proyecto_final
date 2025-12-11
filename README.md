# Sistema de Control de Biblioteca

Proyecto final desarrollado en Python utilizando el framework Flet para la gestión integral de una biblioteca. El sistema permite administrar el inventario de libros, registrar clientes y controlar préstamos de manera eficiente con una interfaz moderna y responsiva.

## Características Principales

- **Interfaz gráfica moderna** desarrollada con Flet
- **Gestión completa de inventario** de libros
- **Registro y administración de clientes**
- **Control de préstamos y devoluciones**
- **Validaciones en tiempo real**
- **Interfaz web responsiva** accesible desde el navegador

## Estado del Proyecto

| Módulo | Estado | Descripción |
| :--- | :--- | :--- |
| **Gestión de Libros** | ✅ Completado | Módulo funcional para registro y visualización de inventario. |
| **Gestión de Clientes** | ✅ Completado | Sistema completo de registro de clientes con validación de cédula. |
| **Préstamos** | ✅ Completado | Gestión de préstamos y devoluciones con seguimiento en tiempo real. |

## Guía de Uso

### 📚 Módulo de Libros (Gestión de Inventario)

Este módulo permite administrar el inventario completo de la biblioteca.

**Para registrar un nuevo libro:**

1. Navegue a la pestaña **"Libros"**.
2. Complete los campos obligatorios:
   - **Título**: Nombre del libro
   - **Autor**: Autor del libro
   - **ISBN**: Código único de identificación
3. Presione el botón **"Registrar Libro"**.
4. Verifique la tabla inferior:
   - El libro aparecerá automáticamente en la lista.
   - El estado **"Disponible"** se mostrará en color verde con icono ✓
   - El estado **"Prestado"** se mostrará en color rojo con icono ✗
   - Si intenta registrar un ISBN repetido, el sistema mostrará un mensaje de error.

**Funcionalidades:**
- ✅ Registro de libros con validación de ISBN único
- ✅ Visualización del estado en tiempo real (Disponible/Prestado)
- ✅ Tabla dinámica con información completa del inventario
- ✅ Indicadores visuales con colores e iconos

### 👥 Módulo de Clientes (Ingreso de Clientes)

Este módulo gestiona el registro de clientes autorizados para préstamos.

**Para registrar un nuevo cliente:**

1. Navegue a la pestaña **"Clientes"**.
2. Complete los campos obligatorios:
   - **Nombre**: Nombre del cliente
   - **Apellido**: Apellido del cliente
   - **Cédula**: Número de identificación (debe ser único)
3. Presione el botón **"Registrar Cliente"**.
4. El sistema validará que:
   - Todos los campos estén completos
   - La cédula no esté registrada previamente
5. El cliente aparecerá en la tabla de clientes registrados.

**Funcionalidades:**
- ✅ Registro de clientes con tres campos obligatorios
- ✅ Validación de cédula única (no permite duplicados)
- ✅ Mensajes de error específicos para cada validación
- ✅ Tabla con todos los clientes registrados
- ✅ Limpieza automática de campos tras registro exitoso

### 📖 Módulo de Préstamos (Operador Demetrio)

Este módulo controla los préstamos y devoluciones de libros.

**Para realizar un préstamo:**

1. Navegue a la pestaña **"Préstamos"**.
2. Seleccione un **libro disponible** del primer menú desplegable.
   - Solo aparecerán libros con estado "Disponible"
3. Seleccione un **cliente registrado** del segundo menú desplegable.
4. Presione el botón **"Realizar Préstamo"**.
5. El préstamo se registrará y el libro cambiará a estado "Prestado".

**Para realizar una devolución:**

1. Localice el libro prestado en la tabla **"Préstamos Activos"**.
2. Presione el botón **"Devolver"** en la fila correspondiente.
3. El libro volverá a estado "Disponible" automáticamente.

**Funcionalidades:**
- ✅ Listado dinámico de libros disponibles
- ✅ Asignación de libros a clientes registrados
- ✅ Registro de préstamos activos en tabla
- ✅ Sistema de devoluciones con un clic
- ✅ Actualización automática de estados
- ✅ Botón de recarga manual de datos

## Instrucciones de Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación Paso a Paso

1. **Clonar o descargar el proyecto**
   ```bash
   # Si está en un repositorio Git
   git clone <url-del-repositorio>
   cd proyecto_final
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   # En Windows
   python -m venv .venv
   .venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install flet
   ```

4. **Ejecutar la aplicación**
   ```bash
   flet run main.py
   ```

5. **Acceder al sistema**
   - La aplicación se abrirá automáticamente en su navegador web
   - Por defecto se ejecuta en: `http://localhost:8080`

### Solución de Problemas

**Si hay errores de importación:**
- Verifique que el entorno virtual esté activado
- Reinstale flet: `pip install --upgrade flet`

## Estructura del Proyecto

```
proyecto_final/
│
├── main.py                 # Punto de entrada de la aplicación
├── modelos.py             # Definición de clases (Libro, Cliente)
├── vista_libros.py        # Módulo de gestión de libros
├── vista_clientes.py      # Módulo de gestión de clientes
├── vista_prestamos.py     # Módulo de préstamos y devoluciones
└── README.md              # Documentación del proyecto
```

## Tecnologías Utilizadas

- **Python 3.13**: Lenguaje de programación principal
- **Flet**: Framework para interfaces gráficas multiplataforma
- **Arquitectura modular**: Separación de responsabilidades por módulos

## Autores
Proyecto Final - Programación 3
Demetrio Garcia
John Roa
Yoel Amat
Jonathan Vergara

## Licencia

Este proyecto fue desarrollado con fines educativos.