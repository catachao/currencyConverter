import sys
import os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic

class Dialogo (QMainWindow):
    # Tipo de cambio 20240619
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoGBP = 0.79

    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\..\vista\CurrencyConvert2.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta,self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion( self ):
        convertido=0.0
        inicial=0.0

        inicial=float(self.leImporte.text())
        convertido=inicial

        if self.rbDeEUR.isChecked():
            convertido=inicial/self.USDtoEUR
        elif self.rbDePEN.isChecked():
            convertido = inicial / self.USDtoPEN
        elif self.rbDeGBP.isChecked():
            convertido = inicial / self.USDtoGBP

        if self.rbAEUR.isChecked():
            convertido=inicial*self.USDtoEUR
        elif self.rbAPEN.isChecked():
            convertido = inicial * self.USDtoPEN
        elif self.rbDeGBP.isChecked():
            convertido = inicial / self.USDtoGBP


        self.lblCambio.setText(f"{convertido:.2f}")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec_()