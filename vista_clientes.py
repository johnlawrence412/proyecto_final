# vista_clientes.py
import flet as ft


def crear_vista_clientes(page: ft.Page, lista_clientes):
    return ft.Column(
        controls=[
            ft.Text("Módulo de Clientes (Temporal hasta que los companeros terminen esta parte)"),
        ],
        scroll="AUTO",
    )
