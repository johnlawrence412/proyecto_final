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
    lista_clientes: list[Cliente] = []

    #  Vistas y Pestañas
    tab_libros = ft.Tab(
        text="Libros",
        content=crear_vista_libros(page, lista_libros),
    )

    tab_clientes = ft.Tab(
        text="Clientes",
        content=crear_vista_clientes(page, lista_clientes),
    )

    tab_prestamos = ft.Tab(
        text="Prestamos",
        content=crear_vista_prestamos(page, lista_libros, lista_clientes),
    )

    tabs = ft.Tabs(
        selected_index=0,
        expand=True,
        tabs=[tab_libros, tab_clientes, tab_prestamos],
    )

    # Agregar todo a la pagina
    page.add(tabs)


# Punto de entrada de Flet
if __name__ == "__main__":
    
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)