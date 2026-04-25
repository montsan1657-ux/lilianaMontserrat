import math
from clases.ejercicio2 import Calculadora

class CalculadoraInversa(Calculadora):
    def __init__(self, p, dof):
        super().__init__(0, dof)
        self.p = p

    def encontrar_x(self):
        x = 1.0
        d = 0.5
        error_permitido = 0.00001

        error_anterior = 0

        while True:
            self.x = x
            self.integrar()

            p_calculado = self.resultado
            error = self.p - p_calculado

            if abs(error) < error_permitido:
                return x

            if error > 0:
                x += d
            else:
                x -= d

            if error_anterior != 0:
                if (error > 0 and error_anterior < 0) or (error < 0 and error_anterior > 0):
                    d = d / 2

            error_anterior = error