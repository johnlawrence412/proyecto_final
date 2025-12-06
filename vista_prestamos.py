# vista_prestamos.py
import flet as ft


def crear_vista_prestamos(page: ft.Page, lista_libros, lista_clientes):
    return ft.Column(
        controls=[
            ft.Text("Módulo de Préstamos (Temporal hasta que los companeros terminen esta parte)"),
        ],
        scroll="AUTO",
    )
