from copy import deepcopy

def breadth_first_search(tablero):
    registro = {
        'nodo'     : 0,
        'repetir'  : 0,
        'franja'   : 0,
        'explorado' : set([])
    }

    if tablero.finalizar():
        return registro, tablero

    cola = [tablero]
    registro['nodo'] += 1

    while True:

        if not cola:
            print registro
            raise Exception('No existe Solucion.')

        nodo = cola.pop(0)
        registro['explorado'].add(hash(nodo))
        registro['franja'] = len(cola)

        for direccion, cost in nodo.movimientos_disponibles():
            hijo = deepcopy(nodo).mover(direccion)
            registro['nodo'] += 1

            if hash(hijo) not in registro['explorado'] and hijo not in cola:
                if hijo.finalizar():
                    return registro, hijo
                cola.append(hijo)
            else:
                registro['repetir'] += 1