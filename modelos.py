# modelos.py


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, estado: str = "Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado    # Disponible o Prestado
        self.cliente = None     # (Cliente o None)


class Cliente:
    def __init__(self, nombre: str, apellido: str, cedula: str):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
