from collections import defaultdict
from src.Ejer10 import calcular_puntaje, generar_ranking

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