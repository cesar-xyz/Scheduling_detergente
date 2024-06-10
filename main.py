from estacion import Estacion
from demanda import Demanda
from planificador import Planificador

def main():
    # Creación de estaciones
    lavado = Estacion(1, "Lavado", 180, 7)
    llenado = Estacion(2, "Llenado", 180, 5)
    sellado = Estacion(3, "Sellado", 180, 2)
    etiquetado = Estacion(4, "Etiquetado", 180, 3)
    empaquetado = Estacion(5, "Empaquetado", 180, 3)

    # Creación del planificador
    planificador = Planificador()
    planificador.agregar_estacion(lavado)
    planificador.agregar_estacion(llenado)
    planificador.agregar_estacion(sellado)
    planificador.agregar_estacion(etiquetado)
    planificador.agregar_estacion(empaquetado)

    # Ejemplo de demanda
    demanda1 = Demanda("Detergente 1", 100, "2024-05-27 08:00:00")
    demanda2 = Demanda("Detergente 2", 2, "2024-05-27 08:30:00")
    demanda3 = Demanda("Detergente 3", 3, "2024-06-27 09:00:00")
    demanda4 = Demanda("Detergente 4", 4, "2024-08-27 09:30:00")

    # Programación manual
    programado, cantidad_programada, fecha_fin = planificador.programar_manual(demanda1, 1)
    if programado:
        tiempo_total = fecha_fin - demanda1.fecha_inicio
        print(f"\nProgramación manual exitosa: {cantidad_programada} se tardo {tiempo_total} en terminar.")
    else:
        print(f"\nProgramación manual fallida para la demanda de {demanda1.cantidad} botellas.")

    # Desprogramación manual
    desprogramado, cantidad_desprogramada, tiempo_total = planificador.desprogramar_manual(demanda1, 1)
    if desprogramado:
        print(f"Desprogramación manual exitosa: {cantidad_desprogramada} botellas. \n")
    else:
        print(f"Desprogramación manual fallida para la demanda de {demanda1.cantidad} botellas.\n")

    # Programación automática
    lista_demandas = [demanda1, demanda2, demanda3, demanda4]
    secuencia_produccion = planificador.programar_automatico(lista_demandas)
    print("Resultados de la programación automática:")
    print("=========================================")
    for produccion in secuencia_produccion:
        print(f"Producto: {produccion['Producto']}")
        print(f"Estación: {produccion['Estacion']}")
        print(f"FechaHoraInicio: {produccion['FechaHoraInicio']}")
        print(f"FechaHoraFin: {produccion['FechaHoraFin']}")
        print(f"CantidadProgramada: {produccion['CantidadProgramada']} {produccion['UnidadVentas']}")
        print()
if __name__ == "__main__":
    main()
