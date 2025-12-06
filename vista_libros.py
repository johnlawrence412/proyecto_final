# vista_libros.py

import flet as ft
from modelos import Libro


def crear_vista_libros(page: ft.Page, lista_libros: list[Libro]):
    #  Entradas de datos (Ingresar: Titulo, Autor, ISBN) 
    titulo_input = ft.TextField(label="Título", width=300)
    autor_input = ft.TextField(label="Autor", width=300)
    isbn_input = ft.TextField(label="ISBN", width=200)

    # Mensaje para mostrar errores o confirmaciones
    mensaje = ft.Text("", size=12)

    #  Tabla para mostrar tabla actualizada 
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Autor")),
            ft.DataColumn(ft.Text("ISBN")),
            ft.DataColumn(ft.Text("Estado")),
        ],
        rows=[],
    )

    def refrescar_tabla():
        """Actualizar la tabla con la lista actual de libros."""
        tabla.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(libro.titulo)),
                    ft.DataCell(ft.Text(libro.autor)),
                    ft.DataCell(ft.Text(libro.isbn)),
                    ft.DataCell(ft.Text(libro.estado)),
                ]
            )
            for libro in lista_libros
        ]

    
    def registrar_libro(e):
        # Limpiar mensaje 
        mensaje.value = ""
        mensaje.color = "red"

        titulo = titulo_input.value.strip()
        autor = autor_input.value.strip()
        isbn = isbn_input.value.strip()

        # 1) Faltan datos? - Error "Hizo falta un dato"
        if not titulo or not autor or not isbn:
            mensaje.value = 'Error: "Hizo falta un dato"'
            page.update()
            return

        # 2) El ISBN ya existe? - Error "Duplicado"
        for libro in lista_libros:
            if libro.isbn == isbn:
                mensaje.value = 'Error: "Duplicado" (el ISBN ya existe)'
                page.update()
                return

        # 3) Crear "Libro" (estado = Disponible por defecto)
        nuevo_libro = Libro(titulo=titulo, autor=autor, isbn=isbn)

        # 4) Agregar a la lista de libros
        lista_libros.append(nuevo_libro)

        # 5) Mostrar tabla actualizada
        refrescar_tabla()

        # Limpiar campos de texto
        titulo_input.value = ""
        autor_input.value = ""
        isbn_input.value = ""

        # Mensaje de éxito
        mensaje.value = "Libro registrado correctamente."
        mensaje.color = "green"

        page.update()

    boton_registrar = ft.ElevatedButton(
        text="Registrar libro",
        on_click=registrar_libro,
    )

    vista = ft.Column(
        controls=[
            ft.Text("Ingreso de Libros", size=20, weight="bold"),
            ft.Row(controls=[titulo_input, autor_input, isbn_input]),
            boton_registrar,
            mensaje,
            ft.Divider(),
            ft.Text("Lista de libros", size=16, weight="bold"),
            tabla,
        ],
        scroll="AUTO",
    )

    # Por si ya hay libros cargados
    refrescar_tabla()

    return vista
