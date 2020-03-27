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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSalir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSalir.setGeometry(QtCore.QRect(470, 460, 75, 23))
        self.pushButtonSalir.setObjectName("pushButtonSalir")
        self.pushButtonObtemerResumen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonObtemerResumen.setGeometry(QtCore.QRect(380, 460, 81, 23))
        self.pushButtonObtemerResumen.setObjectName("pushButtonObtemerResumen")
        self.label_Texto = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto.setGeometry(QtCore.QRect(50, 90, 101, 16))
        self.label_Texto.setObjectName("label_Texto")
        self.label_Resumen = QtWidgets.QLabel(self.centralwidget)
        self.label_Resumen.setGeometry(QtCore.QRect(60, 260, 51, 16))
        self.label_Resumen.setObjectName("label_Resumen")
        self.textEdit_Entrada = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Entrada.setGeometry(QtCore.QRect(50, 110, 441, 131))
        self.textEdit_Entrada.setObjectName("textEdit_Entrada")
        self.textEdit_Salida = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida.setGeometry(QtCore.QRect(60, 280, 431, 131))
        self.textEdit_Salida.setObjectName("textEdit_Salida")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


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

    def imprime(self):
        text=self.textEdit_Entrada.toPlainText()
        table, res=self.r1.resumir(text)
        self.textEdit_Salida.setText(res)
        
        self.abrirDialogoAviso("Hola")

    def abrirDialogoAviso(self, texto):
        self.ventanaCam=QtWidgets.QDialog()
        self.uiCam=Ui_DialogAviso()
        self.uiCam.setupUi(self.ventanaCam,texto)
        self.ventanaCam.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
