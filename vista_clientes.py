import flet as ft
from modelos import Cliente


def crear_vista_clientes(page: ft.Page, lista_clientes: list[Cliente]):

    # --- 1. CONFIGURACIÓN DE UI (ENTRADAS) ---
    nombre_input = ft.TextField(
        label="Nombre",
        width=300,
        hint_text="Ej. Juan",
        border_radius=10
    )
    apellido_input = ft.TextField(
        label="Apellido",
        width=300,
        hint_text="Ej. Pérez",
        border_radius=10
    )
    cedula_input = ft.TextField(
        label="Cédula",
        width=300,
        hint_text="Ej. 8-978-1234",
        border_radius=10
    )

    mensaje = ft.Text("", size=14, weight="bold")

    # --- 2. TABLA DE DATOS ---
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre", weight="bold")),
            ft.DataColumn(ft.Text("Apellido", weight="bold")),
            ft.DataColumn(ft.Text("Cédula", weight="bold")),
        ],
        rows=[],
        border=ft.border.all(1, "grey"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, "grey"),
        heading_row_color="grey200",
        heading_row_height=60,
        data_row_min_height=50,
    )

    def refrescar_tabla():
        """Actualiza la tabla con todos los clientes registrados."""
        tabla.rows = []

        for cliente in lista_clientes:
            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(cliente.nombre)),
                    ft.DataCell(ft.Text(cliente.apellido)),
                    ft.DataCell(
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(name="badge", color="blue", size=16),
                                ft.Text(cliente.cedula, color="blue", weight="bold")
                            ], spacing=5),
                            bgcolor="blue50",
                            padding=5,
                            border_radius=5
                        )
                    ),
                ]
            )
            tabla.rows.append(fila)

        page.update()

    # --- 3. LÓGICA DE REGISTRO ---
    def registrar_cliente(e):

        mensaje.value = ""

        # Paso 1: Obtener datos ingresados
        nombre = nombre_input.value.strip()
        apellido = apellido_input.value.strip()
        cedula = cedula_input.value.strip()

        # Validación: Campos obligatorios (los 3 campos son requeridos)
        if not nombre:
            mensaje.value = "⚠️ Error: El nombre es obligatorio."
            mensaje.color = "red"
            page.update()
            return

        if not apellido:
            mensaje.value = "⚠️ Error: El apellido es obligatorio."
            mensaje.color = "red"
            page.update()
            return

        if not cedula:
            mensaje.value = "⛔ Error: Cedula Obligatoria"
            mensaje.color = "red"
            page.update()
            return

        # Paso 2 y 3: Validar si la cédula ya existe
        for cliente in lista_clientes:
            if cliente.cedula == cedula:
                mensaje.value = "⛔ Error: Cedula Obligatoria"
                mensaje.color = "red"
                page.update()
                return

        # Paso 4: Crear Cliente
        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, cedula=cedula)

        # Paso 5: Agregar a lista de Clientes
        lista_clientes.append(nuevo_cliente)
        refrescar_tabla()

        # Paso 6: Limpiar Campos de texto
        nombre_input.value = ""
        apellido_input.value = ""
        cedula_input.value = ""

        mensaje.value = "✅ Cliente registrado con éxito."
        mensaje.color = "green"
        page.update()

    # Botón de registro
    boton_registrar = ft.ElevatedButton(
        text="Registrar Cliente",
        icon="person_add",
        bgcolor="green",
        color="white",
        on_click=registrar_cliente,
        height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    # --- 4. DISEÑO ---
    vista = ft.Column(
        controls=[
            ft.Container(
                content=ft.Column([
                    ft.Text("Ingreso de Clientes", size=24, weight="bold", color="green"),
                    ft.Text("Ingresa los datos del nuevo cliente a continuación:", size=16, color="grey"),
                    ft.Divider(),
                    ft.Row([nombre_input, apellido_input], wrap=True),
                    ft.Row([cedula_input], wrap=True),
                    ft.Container(height=10),
                    ft.Row(
                        [boton_registrar, mensaje],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                ]),
                padding=25,
                margin=ft.margin.only(top=20),
                bgcolor="green50",
                border_radius=15,
                border=ft.border.all(1, "green100")
            ),

            ft.Divider(height=30, thickness=1),

            ft.Text("Lista de Clientes Registrados", size=20, weight="bold"),
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

    refrescar_tabla()

    return vista
