from PyQt5 import QtWidgets,uic
from load.load_ventana_ejercicio2 import VentanaCalculadora
from load.load_ventana_ejercicio1 import VentanaCalculadora1
from load.load_ventana_ejercicio3 import VentanaCalculadora3

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui",self)
        self.showMaximized()
        
        self.actionEjercicio_1.triggered.connect(self.ingresarEjercicio1)
        self.actionEjercicio_2.triggered.connect(self.ingresarEjercicio2)
        self.actionEjercicio_6.triggered.connect(self.ingresarEjercicio3)
        self.actionSalir.triggered.connect(self.salir)
        
    def salir(self):
        self.close()
        
    def ingresarEjercicio1(self):
       vc= VentanaCalculadora1()
       vc.exec()
        
    def ingresarEjercicio2(self):
       vc= VentanaCalculadora()
       vc.exec()
       
    def ingresarEjercicio3(self):
       vc= VentanaCalculadora3()
       vc.exec()
       
       
    