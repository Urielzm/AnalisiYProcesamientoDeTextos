# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
<<<<<<< HEAD
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
=======
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


>>>>>>> 7f9042e9f86e872e5749f8dd61c7fabb15d0e3e6
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")
from Dialogos.DialogoAviso.DialogoAvisos import Ui_DialogAviso
from Backend.Resumen import Resumen

<<<<<<< HEAD
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        MainWindow.setMinimumSize(QtCore.QSize(801, 600))
        MainWindow.setMaximumSize(QtCore.QSize(801, 600))
        MainWindow.setStyleSheet("background-color: rgb(102, 255, 245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Salir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Salir.setGeometry(QtCore.QRect(710, 530, 75, 23))
        self.pushButton_Salir.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.pushButton_Salir.setObjectName("pushButton_Salir")
        self.pushButton_Obtemer_Resumen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Obtemer_Resumen.setGeometry(QtCore.QRect(700, 490, 81, 23))
        self.pushButton_Obtemer_Resumen.setStyleSheet("background-color: rgb(154, 154, 154);")
        self.pushButton_Obtemer_Resumen.setObjectName("pushButton_Obtemer_Resumen")
        self.label_TextoIntroduce_Texto = QtWidgets.QLabel(self.centralwidget)
        self.label_TextoIntroduce_Texto.setGeometry(QtCore.QRect(170, 50, 221, 16))
        self.label_TextoIntroduce_Texto.setObjectName("label_TextoIntroduce_Texto")
        self.label_Resumen_Obtenido = QtWidgets.QLabel(self.centralwidget)
        self.label_Resumen_Obtenido.setGeometry(QtCore.QRect(170, 385, 241, 31))
        self.label_Resumen_Obtenido.setObjectName("label_Resumen_Obtenido")
        self.textEdit_Entrada_de_texto = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Entrada_de_texto.setGeometry(QtCore.QRect(170, 70, 441, 131))
        self.textEdit_Entrada_de_texto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Entrada_de_texto.setObjectName("textEdit_Entrada_de_texto")
        self.textEdit_Salida_Resumen_Obtenido = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_Resumen_Obtenido.setGeometry(QtCore.QRect(170, 420, 441, 151))
        self.textEdit_Salida_Resumen_Obtenido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_Resumen_Obtenido.setReadOnly(False)
        self.textEdit_Salida_Resumen_Obtenido.setObjectName("textEdit_Salida_Resumen_Obtenido")
        self.textEdit_Salida_Tabla_Frecuencias = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_Tabla_Frecuencias.setGeometry(QtCore.QRect(70, 250, 311, 131))
        self.textEdit_Salida_Tabla_Frecuencias.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_Tabla_Frecuencias.setReadOnly(False)
        self.textEdit_Salida_Tabla_Frecuencias.setObjectName("textEdit_Salida_Tabla_Frecuencias")
        self.label_Texto_Tabla_fr = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto_Tabla_fr.setGeometry(QtCore.QRect(70, 210, 241, 31))
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
        self.textEdit_Salida_Organizacion_Valorizacion = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Salida_Organizacion_Valorizacion.setGeometry(QtCore.QRect(420, 250, 311, 131))
        self.textEdit_Salida_Organizacion_Valorizacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_Salida_Organizacion_Valorizacion.setReadOnly(False)
        self.textEdit_Salida_Organizacion_Valorizacion.setObjectName("textEdit_Salida_Organizacion_Valorizacion")
        self.label_Texto_Org_Y_Valorizacion = QtWidgets.QLabel(self.centralwidget)
        self.label_Texto_Org_Y_Valorizacion.setGeometry(QtCore.QRect(420, 215, 301, 31))
        self.label_Texto_Org_Y_Valorizacion.setObjectName("label_Texto_Org_Y_Valorizacion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
=======

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
>>>>>>> 7f9042e9f86e872e5749f8dd61c7fabb15d0e3e6
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
<<<<<<< HEAD
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_Salir.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_Obtemer_Resumen.clicked.connect(self.imprime)
        self.r1=Resumen()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Salir.setText(_translate("MainWindow", "Salir"))
        self.pushButton_Obtemer_Resumen.setText(_translate("MainWindow", "Resumir texto"))
        self.label_TextoIntroduce_Texto.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Introduce el texto a resumir:</span></p></body></html>"))
        self.label_Resumen_Obtenido.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Resumen obtenido:</span></p></body></html>"))
        self.label_Texto_Tabla_fr.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Tabla de frecuencias</span></p></body></html>"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#c8371a;\">Resumen</span></p></body></html>"))
        self.label_Texto_Org_Y_Valorizacion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">Oraciones y Valorización</span></p></body></html>"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
    
    def imprime(self):
        text=self.textEdit_Entrada_de_texto.toPlainText()
        tabla_frecuencias=self.r1.tablaFrecuencias(text)
        oracionesYValorizacion=self.r1.oracionesYvalorizacion(tabla_frecuencias, text)
        tabla_frec_string=self.convertirAString(tabla_frecuencias)
        oracionesYvalorizacion_string=self.convertirAString(oracionesYValorizacion)
        #print(string)
        res =self.r1.resumir(text, oracionesYValorizacion)
        self.textEdit_Salida_Resumen_Obtenido.setText(str(res))
        self.textEdit_Salida_Tabla_Frecuencias.setText(str(tabla_frec_string))
        self.textEdit_Salida_Organizacion_Valorizacion.setText(str(oracionesYvalorizacion_string))        
        self.abrirDialogoAviso("Hola")

    def convertirAString(self, diccionario):
        string=""
        for key in diccionario:
            string+=str(key)+":"+"\t"+str(diccionario[key])+"\n"
        return string


=======


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

>>>>>>> 7f9042e9f86e872e5749f8dd61c7fabb15d0e3e6
    def abrirDialogoAviso(self, texto):
        self.ventanaCam=QtWidgets.QDialog()
        self.uiCam=Ui_DialogAviso()
        self.uiCam.setupUi(self.ventanaCam,texto)
        self.ventanaCam.show()

<<<<<<< HEAD
import Logos.LogoVentanaInicio.LogoEscudoFi_rc
import Logos.LogoVentanaInicio.LogoEscudoUNAM_rc

=======
>>>>>>> 7f9042e9f86e872e5749f8dd61c7fabb15d0e3e6

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())