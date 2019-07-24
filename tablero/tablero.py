from posicion import Posicion

DIRECCION = {
    'U' : Posicion(0,-1),
    'D' : Posicion(0, 1),
    'R' : Posicion(1, 0),
    'L' : Posicion(-1,0)
}

class Tablero(object):

    def __init__(self):
        self.num_lineas  = 0
        self.paredes     = set()
        self.objetivos   = set()
        self.cajas       = set()
        self.jugador     = None
        self.movimientos = []

    def mover(self, direccion):
        pos1 = self.jugador + DIRECCION[direccion]
        pos2 = self.jugador + DIRECCION[direccion].mult(2)

        if pos1 in self.cajas:
            self.cajas.remove(pos1)
            self.cajas.add(pos2)

        self.jugador = pos1
        self.movimientos.append(direccion)

        return self

    def finalizar(self):
        if not self.objetivos.difference(self.cajas):
            return True
        return False

    def movimientos_disponibles(self):
        movimientos_teoricos = ['U', 'R', 'D', 'L']
        posibles_movimientos = []

        for direccion in movimientos_teoricos:
            nueva_pos   = self.jugador + DIRECCION[direccion]
            proxima_pos = self.jugador + DIRECCION[direccion].mult(2)

            if nueva_pos in self.paredes:
                continue
            elif nueva_pos in self.cajas:
                if proxima_pos in self.paredes.union(self.cajas):
                    continue
                posibles_movimientos.append((direccion, 2))
            else:
                posibles_movimientos.append((direccion, 1))

        return posibles_movimientos

    def add_jugador(self, (x, y)):
        self.jugador = Posicion(x,y)

    def add_caja(self, (x, y)):
        self.cajas.add(Posicion(x,y))

    def add_objetivo(self, (x, y)):
        self.objetivos.add(Posicion(x,y))

    def add_pared(self, (x, y)):
        self.paredes.add(Posicion(x,y))

    def __hash__(self):
        return hash((
            hash(frozenset(self.cajas)),
            hash(self.jugador)
        ))

    def __str__(self):
        str_tablero = []
        for y in range(self.num_lineas):
            str_tablero.append([' ']*20)

        for pared in self.paredes:
            str_tablero[pared.y][pared.x] = '#'

        for caja in self.cajas.difference(self.objetivos):
            str_tablero[caja.y][caja.x] = '$'

        for caja in self.objetivos.union(self.cajas):
            str_tablero[caja.y][caja.x] = '*'

        for objetivo in self.objetivos.difference(self.cajas):
            str_tablero[objetivo.y][objetivo.x] = '.'

        if self.jugador in self.objetivos:
            str_tablero[self.jugador.y][self.jugador.x] = '@'
        else:
            str_tablero[self.jugador.y][self.jugador.x] = '+'

        return '\n'.join([''.join(linea) for linea in str_tablero])
