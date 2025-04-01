def calcular_puntaje(kills, assists, deaths):
    return (kills * 3) + (assists) - (1 if deaths else 0)

def generar_ranking(estadisticas_gral):
    jugadores_ordenados = sorted(estadisticas_gral.items(), key=lambda x: x[1]['points'], reverse=True)
    print("Jugador   Kills   Asistencias   Muertes   MVPs   Puntos")
    print("--------------------------------------------------------")
    for jugador, estadisticas in jugadores_ordenados:
        print(f"{jugador:<9} {estadisticas['kills']:<7} {estadisticas['assists']:<13} {estadisticas['deaths']:<9} {estadisticas['mvp']:<6} {estadisticas['points']:<5}")
    print("--------------------------------------------------------")
