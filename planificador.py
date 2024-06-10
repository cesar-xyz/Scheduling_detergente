from datetime import timedelta


class Planificador:
    def __init__(self):
        self.estaciones = []

    def agregar_estacion(self, estacion):
        self.estaciones.append(estacion)

    def programar_manual(self, demanda, estacion_id):
        estacion = next((e for e in self.estaciones if e.id == estacion_id), None)
        if estacion:
            programado, cantidad_programada, fecha_fin = estacion.procesar_botellas(demanda.cantidad,
                                                                                    demanda.fecha_inicio)
            return programado, cantidad_programada, fecha_fin
        return False, 0, None

    def desprogramar_manual(self, demanda, estacion_id):
        estacion = next((e for e in self.estaciones if e.id == estacion_id), None)
        if estacion:
            desprogramado, tiempo_total = estacion.desprocesar_botellas(demanda.cantidad)
            return desprogramado, demanda.cantidad, tiempo_total
        return False, 0, 0

    def programar_automatico(self, lista_demandas):
        secuencia_produccion = []
        for demanda in lista_demandas:
            fecha_inicio = demanda.fecha_inicio
            for estacion in self.estaciones:
                programado, cantidad_programada, fecha_fin = estacion.procesar_botellas(demanda.cantidad, fecha_inicio)
                secuencia_produccion.append({
                    'Producto': demanda.producto,
                    'Estacion': estacion.nombre,
                    'FechaHoraInicio': fecha_inicio,
                    'FechaHoraFin': fecha_fin,
                    'CantidadProgramada': cantidad_programada,
                    'UnidadVentas': 'botellas'
                })
                fecha_inicio = fecha_fin  # La siguiente estación comienza cuando la anterior termina
        return secuencia_produccion
