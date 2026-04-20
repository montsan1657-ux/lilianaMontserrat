from clases.ejercicio1 import Ejercicio1
from PyQt5 import QtWidgets, uic

class VentanaCalculadora1(QtWidgets.QDialog):
    def _init_(self):
        super()._init_()
        uic.loadUi("gui/ventana_ejercicios.ui", self)  # ⚠️ ajusta ruta si cambia

        # 🔥 conectar botón
        self.btnCalcular.clicked.connect(self.ejecutar_ejercicio)

        self.show()

    def ejecutar_ejercicio(self):
        try:
            # 📥 Entradas
            x = list(map(float, self.inputX.text().split(",")))
            y = list(map(float, self.inputY.text().split(",")))
            xk = float(self.inputXk.text())

            if len(x) != len(y):
                raise ValueError("Datos inválidos")

            # 📊 Cálculo
            ejercicio = Ejercicio1()
            ejercicio.cargar_datos(x, y)

            b0, b1, r, yk = ejercicio.calcular(xk)

            # 📤 Salidas
            self.lblB0.setText(f"b0: {b0:.4f}")
            self.lblB1.setText(f"b1: {b1:.4f}")
            self.lblR.setText(f"r: {r:.4f}")
            self.lblYk.setText(f"Predicción: {yk:.4f}")

        except:
            self.lblB0.setText("b0: error")
            self.lblB1.setText("b1: error")
            self.lblR.setText("r: error")
            self.lblYk.setText("Predicción: error")