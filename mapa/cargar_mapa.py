PARED    = set(['#'])
JUGADOR  = set(['@', '+'])
OBJETIVO = set(['.', '+', '*'])
CAJA     = set(['$','*'])

from tablero import Tablero

def Cargar_Mapa(map_str):
    tablero_nuevo = Tablero()
    
    map_lineas = map_str.split('\n')
    tablero_nuevo.num_lineas = int(len(map_lineas[0].strip()))

    for y, linea in enumerate(map_lineas[0:]):
        linea = linea.replace('\n', '')
        if linea:
            for x, char in enumerate(linea):
                pos = (x, y)

                if char in PARED:
                    tablero_nuevo.add_pared(pos)
                if char in OBJETIVO:
                    tablero_nuevo.add_objetivo(pos)
                if char in CAJA:
                    tablero_nuevo.add_caja(pos)
                if char in JUGADOR:
                    tablero_nuevo.add_jugador(pos)

    return tablero_nuevo
