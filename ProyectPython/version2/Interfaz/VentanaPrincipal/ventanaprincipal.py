# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from Dialogos.DialogoAviso.DialogoAvisos import Ui_DialogAviso
from Backend.Resumen import Resumen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(102, 255, 245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSalir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSalir.setGeometry(QtCore.QRect(620, 530, 75, 23))
        self.pushButtonSalir.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.pushButtonObtemerResumen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonObtemerResumen.setGeometry(QtCore.QRect(520, 530, 81, 23))
        self.pushButtonObtemerResumen.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.pushButtonObtemerResumen.setObjectName("pushButtonObtemerResumen")
        self.label_Texto = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto.setGeometry(QtCore.QRect(200, 30, 101, 16))
        self.label_Texto.setObjectName("label_Texto")
        self.label_Resumen = QtWidgets.QLabel(self.centralwidget)
        self.label_Resumen.setGeometry(QtCore.QRect(200, 350, 51, 16))
        self.label_Resumen.setObjectName("label_Resumen")
        self.textEdit_Entrada = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Entrada.setGeometry(QtCore.QRect(200, 50, 441, 131))
        self.textEdit_Entrada.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Entrada.setObjectName("textEdit_Entrada")
        self.textEdit_Salida = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida.setGeometry(QtCore.QRect(200, 380, 441, 131))
        self.textEdit_Salida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida.setReadOnly(False)
        self.textEdit_Salida.setObjectName("textEdit_Salida")
        self.textEdit_Salida_sentencais = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_sentencais.setGeometry(QtCore.QRect(200, 210, 441, 131))
        self.textEdit_Salida_sentencais.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_sentencais.setReadOnly(False)
        self.textEdit_Salida_sentencais.setObjectName("textEdit_Salida_sentencais")
        self.label_Texto_Tabla_fr = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto_Tabla_fr.setGeometry(QtCore.QRect(200, 190, 101, 16))
        self.label_Texto_Tabla_fr.setObjectName("label_Texto_Tabla_fr")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(330, -10, 201, 51))
        self.label_titulo.setObjectName("label_titulo")
        self.label_escudo_unam = QtWidgets.QLabel(self.centralwidget)
        self.label_escudo_unam.setGeometry(QtCore.QRect(10, 10, 131, 171))
        self.label_escudo_unam.setStyleSheet("border-image: url(:/escudoUnam/Imagenes/ImagenesSesion/unam.png);")
        self.label_escudo_unam.setText("")
        self.label_escudo_unam.setObjectName("label_escudo_unam")
        self.label_escudo_fi = QtWidgets.QLabel(self.centralwidget)
        self.label_escudo_fi.setGeometry(QtCore.QRect(660, 0, 131, 171))
        self.label_escudo_fi.setStyleSheet("border-image: url(:/escudofi/Imagenes/InterfazPrincipal/escudo_fi_color.png);")
        self.label_escudo_fi.setText("")
        self.label_escudo_fi.setObjectName("label_escudo_fi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.pushButtonObtemerResumen.clicked.connect(self.imprime)
        self.r1=Resumen()

        self.retranslateUi(MainWindow)
        self.pushButtonSalir.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSalir.setText(_translate("MainWindow", "Salir"))
        self.pushButtonObtemerResumen.setText(_translate("MainWindow", "Resumir texto"))
        self.label_Texto.setText(_translate("MainWindow", "Introduce el texto:"))
        self.label_Resumen.setText(_translate("MainWindow", "Resumen:"))
        self.label_Texto_Tabla_fr.setText(_translate("MainWindow", "Tabla de frecuencias"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#c8371a;\">Resumen</span></p></body></html>"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))

    def imprime(self):
        text=self.textEdit_Entrada.toPlainText()
        res, table=self.r1.resumir(text)
        self.textEdit_Salida.setText(res)
        self.textEdit_Salida_sentencais.setText(str(table))        
        self.abrirDialogoAviso("Hola")

    def abrirDialogoAviso(self, texto):
        self.ventanaCam=QtWidgets.QDialog()
        self.uiCam=Ui_DialogAviso()
        self.uiCam.setupUi(self.ventanaCam,texto)
        self.ventanaCam.show()

import Logos.LogoVentanaInicio.LogoEscudoFi_rc
import Logos.LogoVentanaInicio.LogoEscudoUNAM_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
