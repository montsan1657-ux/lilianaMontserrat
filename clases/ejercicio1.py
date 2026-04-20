from psp.psp1 import RegresionLineal

class Ejercicio1:
    def _init_(self):
        self.x = []
        self.y = []

    def cargar_datos(self, x, y):
        self.x = x
        self.y = y

    def calcular(self, xk):
        modelo = RegresionLineal(self.x, self.y)

        b1 = modelo.calcular_b1()
        b0 = modelo.calcular_b0(b1)
        r = modelo.correlacion()
        yk = modelo.prediccion(xk, b0, b1)

        return b0, b1, r, yk