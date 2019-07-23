class Posicion:
    def __init__(self, cord_x, cord_y):
        self.x = cord_x
        self.y = cord_y

    def __add__(self, pos_2):
        return Posicion(self.x + pos_2.x, self.y + pos_2.y)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, pos_2):
        return self.x == pos_2.x and self.y == pos_2.y

    def __ne__(self, pos_2):
        return self.x != pos_2.x or self.y != pos_2.y

    def __hash__(self):
        return hash((self.x, self.y))

    def mult(self,cons):
        if not isinstance(cons, int):
            raise Exception('La constante no es un Entero')
        if not (not self.x) ^ (not self.y):
            raise Exception('Ninguna de las coordenadas de posicion == 0')
        return Posicion(self.x*cons, self.y*cons)

    def dist(self, pos_2):
        return abs(self.x - pos_2.x)+ abs(self.y - pos_2.y)