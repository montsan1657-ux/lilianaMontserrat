from PyQt5 import QtWidgets, uic
from clases.ejercicio2 import Calculadora
from clases.ejercicio3 import CalculadoraInversa

class VentanaCalculadora3(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/encontrar_x.ui", self)
        self.show()
        
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        try:
            valor = float(self.edit_numero1.text())
            dof = int(self.edit_numero2.text())

            if valor < 1:
                calc = CalculadoraInversa(valor, dof)
                resultado = calc.encontrar_x()
                self.label_resultado.setText("x = " + str(resultado))
            else:
                calc = Calculadora(valor, dof)
                calc.integrar()
                self.label_resultado.setText("p = " + str(calc.resultado))

        except:
            self.label_resultado.setText("Error en datos")