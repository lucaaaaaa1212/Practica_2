def calcular_puntaje(kills, assists, deaths):
    return (kills * 3) + (assists) - (1 if deaths else 0)

def generar_ranking(estadisticas_gral):
    # la funcion sorted se utiliza para ordenar una secuencia
    # .items() convierte mi diccionario en una lista de tuplas, separando (juador,estadistica)
    # key sera el criterio de ordenacion, donde x es una tupla y x[1]['points'] referenciara a las estadisticas/puntos
    # reverse hace que se ordenen de mayor a menor
    jugadores_ordenados = sorted(estadisticas_gral.items(), key=lambda x: x[1]['points'], reverse=True)
    print("Jugador   Kills   Asistencias   Muertes   MVPs   Puntos")
    print("--------------------------------------------------------")
    # no aplico items en este jugadores_ordenados porque ya estoy trabajando con valores desmpaquetados
    for jugador, estadisticas in jugadores_ordenados:
        print(f"{jugador:<9} {estadisticas['kills']:<7} {estadisticas['assists']:<13} {estadisticas['deaths']:<9} {estadisticas['mvp']:<6} {estadisticas['points']:<5}")
    print("--------------------------------------------------------")
