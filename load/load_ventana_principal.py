from PyQt5 import QtWidgets,uic
from load.load_ventana_calculo import VentanaCalculadora

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("simpson/menu_principal.ui",self)
        self.showMaximized()
        
        self.actionEjercicio_1.triggered.connect(self.ingresarEjercicio1)
        self.actionEjercicio_2.triggered.connect(self.ingresarEjercicio2)
        self.actionSalir.triggered.connect(self.salir)
        
    def salir(self):
        self.close()
        
    def ingresarEjercicio1(self):
       vc= VentanaCalculadora()
       vc.exec()
        
    def ingresarEjercicio2(self):
       vc= VentanaCalculadora()
       vc.exec()