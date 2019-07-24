from copy import deepcopy

def iterative_deepening_search(tablero):
    registro = {
        'nodo'      : 0,
        'repetir'   : 0,
        'franja'    : 0,
        'explorado' : set()
    }

    if tablero.finalizar():
        return registro, tablero

    cola = [tablero]

    nivel = 0
    revision = 1
    while nivel <= revision:
        if not cola:
            print registro
            raise Exception('No existe Solucion.')

        nodo = cola.pop(0)
        registro['explorado'].add(hash(nodo))
        registro['franja'] = len(cola)

        if nodo.finalizar():
            return registro, nodo
        else:
            nivel += 1

        opciones = nodo.movimientos_disponibles()
        if not opciones:
            cola.pop(0)    
        else:
            for direccion, cost in opciones:
                registro['nodo'] += 1
                hijo = deepcopy(nodo).mover(direccion)

                if hash(hijo) not in registro['explorado'] and hijo not in cola:
                    cola.insert(0, hijo)
                    revision += 1
                else:
                    registro['repetir'] += 1