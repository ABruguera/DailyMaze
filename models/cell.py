class Cell:
    def __init__(self, muro_derecha = True, muro_izquierda = True, muro_arriba = True, muro_abajo = True):
        self.muro_derecha = muro_derecha
        self.muro_izquierda = muro_izquierda
        self.muro_arriba = muro_arriba
        self.muro_abajo = muro_abajo
        self.visited = False
        self.is_entrance = False
        self.is_exit = False
