from copy import deepcopy

def depth_first_search(tablero):
    registro = {
        'nodo'      : 0,
        'repetir'   : 0,
        'franja'    : 0,
        'explorado' : set()
    }

    if tablero.finalizar():
        return registro, tablero

    cola = [tablero]

    while True:
        if not cola:
            print registro
            raise Exception('No existe Solucion.')

        nodo = cola.pop(0)
        registro['explorado'].add(hash(nodo))
        registro['franja'] = len(cola)

        if nodo.finalizar():
            return registro, nodo

        opciones = nodo.movimientos_disponibles()
        if not opciones:
            cola.pop(0)    
        else:
            for direccion, cost in opciones:
                registro['nodo'] += 1
                hijo = deepcopy(nodo).mover(direccion)

                if hash(hijo) not in registro['explorado'] and hijo not in cola:
                    cola.insert(0, hijo)
                else:
                    registro['repetir'] += 1