# main.py

import flet as ft
from modelos import Libro, Cliente
from vista_libros import crear_vista_libros
from vista_clientes import crear_vista_clientes
from vista_prestamos import crear_vista_prestamos


def main(page: ft.Page):
    # Configuracion de la app
    page.title = "Sistema de Biblioteca - Proyecto Final"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "AUTO"

    #  Estado global
    # Estas listas se compartiran con todos los modulos
    lista_libros: list[Libro] = []
    lista_clientes: list[Cliente] = [
        Cliente("Juan", "Pérez", "8-978-3456"),
        Cliente("María", "González", "8-765-4321"),
        Cliente("Carlos", "Rodríguez", "1-122-3344"),
        Cliente("Ana", "Martínez", "5-566-7788"),
    ]

    #  Vistas y Pestañas
    vista_libros = crear_vista_libros(page, lista_libros)
    vista_clientes = crear_vista_clientes(page, lista_clientes)
    vista_prestamos = crear_vista_prestamos(page, lista_libros, lista_clientes)

    tab_libros = ft.Tab(
        text="Libros",
        content=vista_libros,
    )

    tab_clientes = ft.Tab(
        text="Clientes",
        content=vista_clientes,
    )

    tab_prestamos = ft.Tab(
        text="Prestamos",
        content=vista_prestamos,
    )

    def on_tab_change(e):
        # Refrescar la vista según la pestaña seleccionada
        selected_index = e.control.selected_index

        # Índice 0: Libros
        if selected_index == 0:
            if hasattr(vista_libros, 'on_visible') and vista_libros.on_visible:
                vista_libros.on_visible(None)

        # Índice 1: Clientes
        elif selected_index == 1:
            if hasattr(vista_clientes, 'on_visible') and vista_clientes.on_visible:
                vista_clientes.on_visible(None)

        # Índice 2: Préstamos
        elif selected_index == 2:
            if hasattr(vista_prestamos, 'on_visible') and vista_prestamos.on_visible:
                vista_prestamos.on_visible(None)

    tabs = ft.Tabs(
        selected_index=0,
        expand=True,
        tabs=[tab_libros, tab_clientes, tab_prestamos],
        on_change=on_tab_change,
    )

    # Agregar todo a la pagina
    page.add(tabs)


# Punto de entrada de Flet
if __name__ == "__main__":
    
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)