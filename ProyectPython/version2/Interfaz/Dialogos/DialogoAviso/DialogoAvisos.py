# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoAvisos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogAviso(object):
    def setupUi(self, DialogAviso, texto):
        DialogAviso.setObjectName("DialogAviso")
        DialogAviso.resize(537, 191)
        self.buttonBoxAceptar = QtWidgets.QDialogButtonBox(DialogAviso)
        self.buttonBoxAceptar.setGeometry(QtCore.QRect(150, 140, 341, 32))
        self.buttonBoxAceptar.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxAceptar.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxAceptar.setCenterButtons(True)
        self.buttonBoxAceptar.setObjectName("buttonBoxAceptar")
        self.label = QtWidgets.QLabel(DialogAviso)
        self.label.setGeometry(QtCore.QRect(160, 10, 321, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogAviso)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 131, 111))
        self.label_2.setStyleSheet("border-image: url(:/LogoAdmiracion/Admi.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DialogAviso,texto)
        self.buttonBoxAceptar.accepted.connect(DialogAviso.accept)
        self.buttonBoxAceptar.rejected.connect(DialogAviso.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAviso)

    def retranslateUi(self, DialogAviso,texto):
        _translate = QtCore.QCoreApplication.translate
        DialogAviso.setWindowTitle(_translate("DialogAviso", "Dialog"))
        self.label.setText(_translate("DialogAviso", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">¡ "+str(texto)+" !</span></p></body></html>"))

import Logos.LogoDialogoAvisoModulo.LoagoAdmiracion_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAviso = QtWidgets.QDialog()
    ui = Ui_DialogAviso()
    ui.setupUi(DialogAviso)
    DialogAviso.show()
    sys.exit(app.exec_())

