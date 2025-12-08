import flet as ft
from modelos import Libro, Cliente


def crear_vista_prestamos(page: ft.Page, lista_libros: list[Libro], lista_clientes: list[Cliente]):
    # Entradas
    libro_dropdown = ft.Dropdown(label="Seleccionar Libro", width=500)
    cliente_dropdown = ft.Dropdown(label="Seleccionar Cliente", width=400)
    mensaje = ft.Text("", size=14, weight="bold")

    # Tabla de libros (vista resumida similar a la de libros)
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Título", weight="bold")),
            ft.DataColumn(ft.Text("Autor", weight="bold")),
            ft.DataColumn(ft.Text("ISBN", weight="bold")),
            ft.DataColumn(ft.Text("Estado", weight="bold")),
            ft.DataColumn(ft.Text("Cliente (si aplica)", weight="bold")),
        ],
        rows=[],
        border=ft.border.all(1, "grey"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, "grey"),
        heading_row_color="grey200",
        heading_row_height=50,
        data_row_min_height=40,
    )

    def refrescar_dropdowns():
        libro_dropdown.options = []
        for libro in lista_libros:
            texto = f"{libro.titulo} — {libro.autor} ({libro.isbn}) [{libro.estado}]"
            libro_dropdown.options.append(ft.dropdown.Option(key=libro.isbn, text=texto))
        cliente_dropdown.options = []
        for c in lista_clientes:
            texto = f"{c.nombre} {c.apellido} — {c.cedula}"
            cliente_dropdown.options.append(ft.dropdown.Option(key=c.cedula, text=texto))

    def refrescar_tabla():
        tabla.rows = []
        for libro in lista_libros:
            cliente_text = "-"
            if getattr(libro, "cliente", None):
                cl = libro.cliente
                # si se guardó solo la cédula, intentar buscar objeto cliente
                if isinstance(cl, Cliente):
                    cliente_text = f"{cl.nombre} {cl.apellido} ({cl.cedula})"
                else:
                    # buscar en lista_clientes por cedula
                    encontrado = next((x for x in lista_clientes if x.cedula == cl), None)
                    if encontrado:
                        cliente_text = f"{encontrado.nombre} {encontrado.apellido} ({encontrado.cedula})"
                    else:
                        cliente_text = str(cl)

            # Color según el estado
            color_estado = "green" if libro.estado == "Disponible" else "red"

            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(libro.titulo)),
                    ft.DataCell(ft.Text(libro.autor)),
                    ft.DataCell(ft.Text(libro.isbn)),
                    ft.DataCell(ft.Text(libro.estado, weight="bold", color=color_estado)),
                    ft.DataCell(ft.Text(cliente_text)),
                ]
            )
            tabla.rows.append(fila)

    def prestar_libro(e):
        mensaje.value = ""
        isbn_sel = libro_dropdown.value
        ced_sel = cliente_dropdown.value

        if not isbn_sel or not ced_sel:
            mensaje.value = "⚠️ Selecciona un libro y un cliente antes de prestar."
            mensaje.color = "red"
            page.update()
            return

        libro = next((l for l in lista_libros if l.isbn == isbn_sel), None)
        cliente = next((c for c in lista_clientes if c.cedula == ced_sel), None)

        if libro is None:
            mensaje.value = "⚠️ Libro no encontrado."
            mensaje.color = "red"
            page.update()
            return
        if cliente is None:
            mensaje.value = "⚠️ Cliente no encontrado."
            mensaje.color = "red"
            page.update()
            return

        # Verificar disponibilidad según tu diagrama
        if libro.estado != "Disponible":
            mensaje.value = f"⛔ Error: El libro '{libro.titulo}' ya está prestado."
            mensaje.color = "red"
            page.update()
            return

        # Marcar como prestado y vincular cliente
        libro.estado = "Prestado"
        libro.cliente = cliente  # guardamos el objeto Cliente
        mensaje.value = f"✅ Libro '{libro.titulo}' prestado a {cliente.nombre} {cliente.apellido}."
        mensaje.color = "green"

        # Limpiar selecciones
        libro_dropdown.value = None
        cliente_dropdown.value = None

        # Refrescar toda la vista
        refrescar_dropdowns()
        refrescar_tabla()
        page.update()

    boton_prestar = ft.ElevatedButton(
        text="Prestar Libro",
        icon="east",  # icono representativo
        on_click=prestar_libro,
        bgcolor="blue",
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        height=45,
    )

    # Layout
    vista = ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Módulo de Préstamos", size=22, weight="bold", color="blue"),
                        ft.Text("Seleccione un libro y un cliente para registrar un préstamo.", color="grey"),
                        ft.Divider(),
                        ft.Row([libro_dropdown, cliente_dropdown], wrap=True, alignment=ft.MainAxisAlignment.START),
                        ft.Container(height=8),
                        ft.Row([boton_prestar, mensaje], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    ]
                ),
                padding=20,
                bgcolor="blue50",
                border_radius=12,
                border=ft.border.all(1, "blue100"),
            ),
            ft.Divider(height=20),
            ft.Text("Inventario (estado actual)", size=18, weight="bold"),
            ft.Container(content=tabla, padding=8, border_radius=8),
        ],
        scroll="AUTO",
        expand=True,
        spacing=16,
    )

    # Función para refrescar toda la vista
    def refrescar_vista():
        refrescar_dropdowns()
        refrescar_tabla()
        page.update()

    # Inicializar vistas
    refrescar_vista()

    # Exponer función de refresco para llamar cuando se cambie de pestaña
    vista.on_visible = lambda _: refrescar_vista()

    return vista