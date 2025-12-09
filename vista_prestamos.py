import flet as ft
from modelos import Libro, Cliente

def crear_vista_prestamos(page: ft.Page, lista_libros: list[Libro], lista_clientes: list[Cliente]):
    
    # --- 1. ELEMENTOS DE UI (Dropdowns y Botón) ---
    dd_libros = ft.Dropdown(
        label="Seleccionar Libro Disponible",
        width=400,
        hint_text="Elige un libro...",
        border_radius=10,
    )

    dd_clientes = ft.Dropdown(
        label="Seleccionar Cliente",
        width=400,
        hint_text="Elige un cliente...",
        border_radius=10,
    )

    mensaje = ft.Text("", size=14, weight="bold")

    # --- 2. TABLA DE PRÉSTAMOS ACTIVOS ---
    tabla_prestamos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Libro Prestado", weight="bold")),
            ft.DataColumn(ft.Text("Cliente", weight="bold")),
            ft.DataColumn(ft.Text("Cédula", weight="bold")),
            ft.DataColumn(ft.Text("Acción", weight="bold")), 
        ],
        rows=[],
        border=ft.border.all(1, "grey"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, "grey"),
        heading_row_color="grey200",
    )

    # --- 3. LÓGICA DE ACTUALIZACIÓN ---
    
    def actualizar_dropdowns():
        """Recarga las listas desplegables con datos actuales."""
        dd_libros.options.clear()
        dd_clientes.options.clear()

        # Llenar Dropdown Libros (Filtrado por estado 'Disponible')
        for libro in lista_libros:
            if libro.estado == "Disponible":
                texto_opcion = f"{libro.titulo} - {libro.autor}"
                dd_libros.options.append(ft.dropdown.Option(key=libro.isbn, text=texto_opcion))

        # Llenar Dropdown Clientes (Todos los registrados)
        for cliente in lista_clientes:
            texto_opcion = f"{cliente.nombre} {cliente.apellido}"
            dd_clientes.options.append(ft.dropdown.Option(key=cliente.cedula, text=texto_opcion))
        
        # Validación de UI: Solo actualizar si los controles ya están montados en la página
        if dd_libros.page: 
            dd_libros.update()
        if dd_clientes.page:
            dd_clientes.update()

    def devolver_libro(isbn_libro):
        """Restablece el estado del libro a Disponible y elimina la asignación de cliente."""
        for libro in lista_libros:
            if libro.isbn == isbn_libro:
                libro.estado = "Disponible"
                libro.cliente = None 
                break
        
        mensaje.value = "✅ Libro devuelto correctamente."
        mensaje.color = "green"
        mensaje.update()
        refrescar_pantalla()

    def refrescar_tabla():
        """Reconstruye la tabla visual mostrando solo los libros con estado 'Prestado'."""
        tabla_prestamos.rows = []
        
        for libro in lista_libros:
            if libro.estado == "Prestado" and libro.cliente is not None:
                fila = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(libro.titulo)),
                        ft.DataCell(ft.Text(f"{libro.cliente.nombre} {libro.cliente.apellido}")),
                        ft.DataCell(ft.Text(libro.cliente.cedula)),
                        ft.DataCell(
                            ft.ElevatedButton(
                                "Devolver",
                                icon="keyboard_return",
                                icon_color="white",
                                bgcolor="red400",
                                color="white",
                                height=30,
                                # Uso de lambda para capturar el ISBN específico de la fila
                                on_click=lambda e, isbn=libro.isbn: devolver_libro(isbn)
                            )
                        ),
                    ]
                )
                tabla_prestamos.rows.append(fila)
        
        # Validación de UI para la tabla
        if tabla_prestamos.page:
            tabla_prestamos.update()

    def refrescar_pantalla():
        """Actualiza tanto los dropdowns como la tabla de datos."""
        actualizar_dropdowns()
        refrescar_tabla()

    # --- 4. LÓGICA DE NEGOCIO (Realizar Préstamo) ---
    
    def realizar_prestamo(e):
        isbn_sel = dd_libros.value
        cedula_sel = dd_clientes.value

        # Validación de entrada
        if not isbn_sel or not cedula_sel:
            mensaje.value = "⚠️ Debes seleccionar un libro y un cliente."
            mensaje.color = "red"
            mensaje.update()
            return

        # Búsqueda de objetos
        libro_encontrado = None
        for l in lista_libros:
            if l.isbn == isbn_sel:
                libro_encontrado = l
                break
        
        cliente_encontrado = None
        for c in lista_clientes:
            if c.cedula == cedula_sel:
                cliente_encontrado = c
                break
        
        # Ejecución del préstamo
        if libro_encontrado and cliente_encontrado:
            libro_encontrado.estado = "Prestado"
            libro_encontrado.cliente = cliente_encontrado
            
            mensaje.value = f"✅ Préstamo exitoso: '{libro_encontrado.titulo}' entregado a {cliente_encontrado.nombre}."
            mensaje.color = "green"
            
            # Limpiar selección tras éxito
            dd_libros.value = None
            dd_clientes.value = None
            
            refrescar_pantalla()
            page.update()

    boton_prestar = ft.ElevatedButton(
        text="Realizar Préstamo",
        icon="handshake", 
        bgcolor="blue",
        color="white",
        height=50,
        width=200,
        on_click=realizar_prestamo
    )

    boton_actualizar_datos = ft.IconButton(
        icon="refresh",
        tooltip="Actualizar listas manualmente",
        on_click=lambda e: refrescar_pantalla()
    )

    # --- 5. ESTRUCTURA FINAL DE LA VISTA ---
    
    # Carga inicial de datos en memoria (sin renderizar aún)
    refrescar_pantalla()

    vista = ft.Column(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Gestión de Préstamos", size=24, weight="bold", color="blue"),
                        boton_actualizar_datos
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    
                    ft.Text("Selecciona un libro disponible y asígnalo a un cliente.", size=16, color="grey"),
                    ft.Divider(),
                    
                    ft.Row([dd_libros, dd_clientes], wrap=True),
                    ft.Container(height=10),
                    ft.Row([boton_prestar, mensaje], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ]),
                padding=25,
                bgcolor="blue50",
                border_radius=15,
                border=ft.border.all(1, "blue100")
            ),

            ft.Divider(height=30, thickness=1),

            ft.Text("Préstamos Activos", size=20, weight="bold"),
            ft.Container(
                content=tabla_prestamos,
                padding=10,
                border_radius=10,
            ),
        ],
        scroll="AUTO",
        expand=True,
        spacing=20
    )

    return vista