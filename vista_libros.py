import flet as ft
from modelos import Libro

def crear_vista_libros(page: ft.Page, lista_libros: list[Libro]):
    
    # --- 1. CONFIGURACIÓN DE UI (ENTRADAS) ---
    titulo_input = ft.TextField(label="Título", width=300, hint_text="Ej. El Principito", border_radius=10)
    autor_input = ft.TextField(label="Autor", width=300, hint_text="Ej. Antoine de Saint-Exupéry", border_radius=10)
    isbn_input = ft.TextField(label="ISBN", width=200, hint_text="Ej. 978-3-16-148410-0", border_radius=10)

    # Mensaje para feedback (error o éxito)
    mensaje = ft.Text("", size=14, weight="bold")

    # --- 2. TABLA DE DATOS CON ESTILO ---
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Título", weight="bold")),
            ft.DataColumn(ft.Text("Autor", weight="bold")),
            ft.DataColumn(ft.Text("ISBN", weight="bold")),
            ft.DataColumn(ft.Text("Estado", weight="bold")), 
        ],
        rows=[],
        # CAMBIO: Usamos "grey" en lugar de ft.colors.OUTLINE para evitar errores
        border=ft.border.all(1, "grey"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, "grey"),
        heading_row_color="grey200", # Color gris claro de fondo para encabezados
        heading_row_height=60,
        data_row_min_height=50,
    )

    def refrescar_tabla():
        """Recorre la lista global y reconstruye las filas de la tabla."""
        tabla.rows = [] 
        
        for libro in lista_libros:
            # --- LOGICA VISUAL DE ESTADO ---
            # CAMBIO: Usamos strings ("green", "red") para máxima compatibilidad
            if libro.estado == "Disponible":
                color_texto = "green"
                icono = ft.icons.CHECK_CIRCLE_OUTLINE
                bg_color = "green50" # Un verde muy clarito
            else:
                color_texto = "red"
                icono = ft.icons.HIGHLIGHT_OFF
                bg_color = "red50" # Un rojo muy clarito

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

    # --- 3. LÓGICA DE REGISTRO ---
    def registrar_libro(e):
        mensaje.value = ""
        
        t = titulo_input.value.strip()
        a = autor_input.value.strip()
        i = isbn_input.value.strip()

        # Validación: ¿Faltan datos?
        if not t or not a or not i:
            mensaje.value = "⚠️ Error: Faltan datos obligatorios."
            mensaje.color = "red"
            page.update()
            return

        # Validación: ¿ISBN ya existe?
        for libro in lista_libros:
            if libro.isbn == i:
                mensaje.value = f"⛔ Error: El ISBN '{i}' ya está registrado."
                mensaje.color = "red"
                page.update()
                return

        # Crear Libro
        nuevo_libro = Libro(titulo=t, autor=a, isbn=i)

        # Agregar a la lista compartida
        lista_libros.append(nuevo_libro)

        # Actualizar tabla y limpiar formulario
        refrescar_tabla()
        
        titulo_input.value = ""
        autor_input.value = ""
        isbn_input.value = ""
        
        mensaje.value = "✅ Libro registrado con éxito."
        mensaje.color = "green"
        page.update()

    # Botón con estilo
    boton_registrar = ft.ElevatedButton(
        text="Registrar Libro",
        icon=ft.icons.ADD,
        bgcolor="blue", # Color azul estándar
        color="white",
        on_click=registrar_libro,
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    # --- 4. DISEÑO DE LA VISTA (LAYOUT) ---
    vista = ft.Column(
        controls=[
            # Sección de Formulario
            ft.Container(
                content=ft.Column([
                    ft.Text("Gestión de Inventario", size=24, weight="bold", color="blue"),
                    ft.Text("Ingresa los datos del nuevo libro a continuación:", size=16, color="grey"),
                    ft.Divider(),
                    ft.Row([titulo_input, autor_input], wrap=True),
                    ft.Row([isbn_input], wrap=True),
                    ft.Container(height=10), 
                    ft.Row([boton_registrar, mensaje], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ]),
                padding=25,
                bgcolor="blue50", # Fondo azul muy suave
                border_radius=15,
                border=ft.border.all(1, "blue100")
            ),
            
            ft.Divider(height=30, thickness=1),
            
            # Sección de Tabla
            ft.Text("Inventario Actual", size=20, weight="bold"),
            ft.Container(
                content=tabla, 
                padding=10, 
                border_radius=10,
            ),
        ],
        scroll="AUTO",
        expand=True,
        spacing=20
    )

    # Carga inicial
    refrescar_tabla()

    return vista