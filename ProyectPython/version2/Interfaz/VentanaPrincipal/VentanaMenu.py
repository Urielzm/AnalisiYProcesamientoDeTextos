# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from Dialogos.DialogoAviso.DialogoAvisos import Ui_DialogAviso
from VentanaPrincipal import Ui_MainWindow
from Backend.Resumen import Resumen


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 248)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 214, 243, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_resumir_texto = QtWidgets.QPushButton(Form)
        self.pushButton_resumir_texto.setGeometry(QtCore.QRect(120, 120, 101, 31))
        self.pushButton_resumir_texto.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 214, 243, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_resumir_texto.setObjectName("pushButton_resumir_texto")
        self.pushButton_texto_url = QtWidgets.QPushButton(Form)
        self.pushButton_texto_url.setGeometry(QtCore.QRect(120, 160, 101, 31))
        self.pushButton_texto_url.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 214, 243, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_texto_url.setObjectName("pushButton_texto_url")
        self.pushButton_salir = QtWidgets.QPushButton(Form)
        self.pushButton_salir.setGeometry(QtCore.QRect(120, 200, 101, 31))
        self.pushButton_salir.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 214, 243, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.label_escudo_fi = QtWidgets.QLabel(Form)
        self.label_escudo_fi.setGeometry(QtCore.QRect(270, 10, 81, 91))
        self.label_escudo_fi.setStyleSheet("border-image: url(:/escudofi/Imagenes/InterfazPrincipal/escudo_fi_color.png);")
        self.label_escudo_fi.setText("")
        self.label_escudo_fi.setObjectName("label_escudo_fi")
        self.label_escudo_unam = QtWidgets.QLabel(Form)
        self.label_escudo_unam.setGeometry(QtCore.QRect(0, 10, 91, 91))
        self.label_escudo_unam.setStyleSheet("image: url(:/escudoUnam/Imagenes/ImagenesSesion/unam.png);")
        self.label_escudo_unam.setText("")
        self.label_escudo_unam.setObjectName("label_escudo_unam")

        self.pushButton_resumir_texto.clicked.connect(self.abrirVentanaPrincipal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def abrirVentanaPrincipal(self):
        self.ventana0=QtWidgets.QMainWindow()
        #self.ui0=Ui_FormVentanaPrincipal()
        self.ui0=Ui_MainWindow()
        self.ui0.setupUi(self.ventana0)
        self.ventana0.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_resumir_texto.setText(_translate("Form", "Resumir texto"))
        self.pushButton_texto_url.setText(_translate("Form", "Texto URL"))
        self.pushButton_salir.setText(_translate("Form", "Salir"))

import Logos.LogoVentanaInicio.LogoEscudoFi_rc
import Logos.LogoVentanaInicio.LogoEscudoUNAM_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
