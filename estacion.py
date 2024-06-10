from datetime import timedelta


class Estacion:
    def __init__(self, id, nombre, capacidad, tiempo_procesamiento):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.tiempo_procesamiento = tiempo_procesamiento
        self.ocupacion = 0  # Representa el número de botellas procesadas

    def procesar_botellas(self, cantidad, fecha_inicio):
        if self.ocupacion + cantidad <= self.capacidad:
            self.ocupacion += cantidad
            tiempo_total = self.tiempo_procesamiento * cantidad
            fecha_fin = fecha_inicio + timedelta(seconds=tiempo_total)
            return True, cantidad, fecha_fin
        else:
            cantidad_procesada = self.capacidad - self.ocupacion
            self.ocupacion = self.capacidad
            tiempo_total = self.tiempo_procesamiento * cantidad_procesada
            fecha_fin = fecha_inicio + timedelta(seconds=tiempo_total)
            return False, cantidad_procesada, fecha_fin

    def desprocesar_botellas(self, cantidad):
        if self.ocupacion >= cantidad:
            self.ocupacion -= cantidad
            return True, self.tiempo_procesamiento * cantidad
        else:
            cantidad_desprocesada = self.ocupacion
            self.ocupacion = 0
            return False, self.tiempo_procesamiento * cantidad_desprocesada
