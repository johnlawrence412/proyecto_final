# vista_libros.py

import flet as ft
from modelos import Libro

def crear_vista_libros(page: ft.Page, lista_libros: list[Libro]):
    
    # Usamos hints para guiar al usuario
    titulo_input = ft.TextField(label="Título", width=300, hint_text="Ej. El Principito", border_radius=10)
    autor_input = ft.TextField(label="Autor", width=300, hint_text="Ej. Antoine de Saint-Exupéry", border_radius=10)
    isbn_input = ft.TextField(label="ISBN", width=200, hint_text="Ej. 978-3-16-148410-0", border_radius=10)

    # Mensaje para feedback (error o éxito)
    mensaje = ft.Text("", size=14, weight="bold")

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Título", weight="bold")),
            ft.DataColumn(ft.Text("Autor", weight="bold")),
            ft.DataColumn(ft.Text("ISBN", weight="bold")),
            ft.DataColumn(ft.Text("Estado", weight="bold")), # Aquí aplicaremos el color
        ],
        rows=[],
        border=ft.border.all(1, ft.colors.OUTLINE),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, ft.colors.OUTLINE),
        heading_row_color=ft.colors.SURFACE_VARIANT,
        heading_row_height=60,
        data_row_min_height=50,
    )

    def refrescar_tabla():
        """Recorre la lista global y reconstruye las filas de la tabla."""
        tabla.rows = [] # Limpiamos filas anteriores para no duplicar
        
        for libro in lista_libros:
            # --- LOGICA VISUAL DE ESTADO (REQUISITO EXAMEN) ---
            # Si está disponible -> Verde con Check
            # Si está prestado -> Rojo con X
            if libro.estado == "Disponible":
                color_texto = ft.colors.GREEN
                icono = ft.icons.CHECK_CIRCLE_OUTLINE
                bg_color = ft.colors.GREEN_50
            else:
                color_texto = ft.colors.RED
                icono = ft.icons.HIGHLIGHT_OFF
                bg_color = ft.colors.RED_50

            # Creamos la fila
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(libro.titulo)),
                    ft.DataCell(ft.Text(libro.autor)),
                    ft.DataCell(ft.Text(libro.isbn)),
                    # Celda de Estado Personalizada
                    ft.DataCell(
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(icono, color=color_texto, size=16),
                                ft.Text(libro.estado, color=color_texto, weight="bold")
                            ], spacing=5),
                            bgcolor=bg_color,
                            padding=5,
                            border_radius=5
                        )
                    ),
                ]
            )
            tabla.rows.append(fila)
        
        page.update()

    def registrar_libro(e):
        mensaje.value = ""
        
        # Obtener valores limpios
        t = titulo_input.value.strip()
        a = autor_input.value.strip()
        i = isbn_input.value.strip()

        # Validación: ¿Faltan datos?
        if not t or not a or not i:
            mensaje.value = "⚠️ Error: Faltan datos obligatorios."
            mensaje.color = ft.colors.ERROR
            page.update()
            return

        # Validación: ¿ISBN ya existe?
        for libro in lista_libros:
            if libro.isbn == i:
                mensaje.value = f"⛔ Error: El ISBN '{i}' ya está registrado."
                mensaje.color = ft.colors.ERROR
                page.update()
                return

        # Crear Libro (El modelo pone 'Disponible' por defecto)
        nuevo_libro = Libro(titulo=t, autor=a, isbn=i)

        # Agregar a la lista compartida
        lista_libros.append(nuevo_libro)

        # Actualizar tabla y limpiar formulario
        refrescar_tabla()
        
        titulo_input.value = ""
        autor_input.value = ""
        isbn_input.value = ""
        
        mensaje.value = "✅ Libro registrado con éxito."
        mensaje.color = ft.colors.GREEN
        page.update()

    # Botón con estilo
    boton_registrar = ft.ElevatedButton(
        text="Registrar Libro",
        icon=ft.icons.ADD,
        bgcolor=ft.colors.PRIMARY,
        color=ft.colors.ON_PRIMARY,
        on_click=registrar_libro,
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    vista = ft.Column(
        controls=[
            # Sección de Formulario (Tarjeta bonita)
            ft.Container(
                content=ft.Column([
                    ft.Text("Gestión de Inventario", size=24, weight="bold", color=ft.colors.PRIMARY),
                    ft.Text("Ingresa los datos del nuevo libro a continuación:", size=16, color=ft.colors.SECONDARY),
                    ft.Divider(),
                    ft.Row([titulo_input, autor_input], wrap=True),
                    ft.Row([isbn_input], wrap=True),
                    ft.Container(height=10), # Espacio
                    ft.Row([boton_registrar, mensaje], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ]),
                padding=25,
                bgcolor=ft.colors.SURFACE_VARIANT.with_opacity(0.3), # Fondo suave
                border_radius=15,
                border=ft.border.all(1, ft.colors.OUTLINE_VARIANT)
            ),
            
            ft.Divider(height=30, thickness=1),
            
            # Sección de Tabla
            ft.Text("Inventario Actual", size=20, weight="bold"),
            ft.Container(
                content=tabla, 
                padding=10, 
                border_radius=10,
                # Si la lista es muy larga, permite scroll horizontal en la tabla
            ),
        ],
        scroll="AUTO", # Scroll general de la página
        expand=True,
        spacing=20
    )

    # Carga inicial (por si ya hay datos en memoria)
    refrescar_tabla()

    return vista