from collections import defaultdict

rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]

def calcular_puntaje(kills, assists, deaths):
    return (kills * 3) + (assists) - (1 if deaths else 0)

def rondas(rounds):
    estadisticas_jugador = defaultdict(lambda: {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0})
    
    for i, datos_de_ronda in enumerate(rounds, 1):
        puntajes_de_ronda = {}
        estadisticas_ronda = {} 
        
        for jugador, estadisticas in datos_de_ronda.items():
            kills, assists, deaths = estadisticas['kills'], estadisticas['assists'], estadisticas['deaths']
            puntaje = calcular_puntaje(kills, assists, deaths)
            
            estadisticas_ronda[jugador] = {'kills': kills, 'assists': assists, 'deaths': int(deaths), 'points': puntaje, 'mvp': estadisticas_jugador[jugador]['mvp']}
            puntajes_de_ronda[jugador] = puntaje
            
            estadisticas_jugador[jugador]['kills'] += kills
            estadisticas_jugador[jugador]['assists'] += assists
            estadisticas_jugador[jugador]['deaths'] += int(deaths)
            estadisticas_jugador[jugador]['points'] += puntaje

        mvp = max(puntajes_de_ronda, key=puntajes_de_ronda.get)
        estadisticas_jugador[mvp]['mvp'] += 1
        estadisticas_ronda[mvp]['mvp'] = estadisticas_jugador[mvp]['mvp']
        
        print(f"\nRanking Ronda {i}:")
        generar_ranking(estadisticas_ronda)
    
    print("\nRanking Final:")
    generar_ranking(estadisticas_jugador)

def generar_ranking(estadisticas_gral):
    jugadores_ordenados = sorted(estadisticas_gral.items(), key=lambda x: x[1]['points'], reverse=True)
    print("Jugador   Kills   Asistencias   Muertes   MVPs   Puntos")
    print("--------------------------------------------------------")
    for jugador, estadisticas in jugadores_ordenados:
        print(f"{jugador:<9} {estadisticas['kills']:<7} {estadisticas['assists']:<13} {estadisticas['deaths']:<9} {estadisticas['mvp']:<6} {estadisticas['points']:<5}")
    print("--------------------------------------------------------")

rondas(rounds)