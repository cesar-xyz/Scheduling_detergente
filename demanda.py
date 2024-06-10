from datetime import datetime


class Demanda:
    def __init__(self, producto, cantidad, fecha_inicio):
        self.producto = producto
        self.cantidad = cantidad
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")
