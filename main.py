from load.load_ventana_calculo import VentanaCalculadora
from PyQt5 import QtWidgets
import sys

def main():
    app=QtWidgets.QApplication(sys.argv)
    ventana= VentanaCalculadora()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    