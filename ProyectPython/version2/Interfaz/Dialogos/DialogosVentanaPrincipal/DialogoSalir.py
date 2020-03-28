# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoSalir.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog, parent=None):#Para regresar a la clase que lo llama
        self.parent=parent#Para regresar a la clase que lo llama
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 116)
        self.buttonBoxAceptarCancelar = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxAceptarCancelar.setGeometry(QtCore.QRect(10, 70, 341, 32))
        self.buttonBoxAceptarCancelar.setMouseTracking(False)
        self.buttonBoxAceptarCancelar.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxAceptarCancelar.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBoxAceptarCancelar.setCenterButtons(True)
        self.buttonBoxAceptarCancelar.setObjectName("buttonBoxAceptarCancelar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 10, 181, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBoxAceptarCancelar.accepted.connect(Dialog.accept)
        self.buttonBoxAceptarCancelar.accepted.connect(self.accept)
        self.buttonBoxAceptarCancelar.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p>tyytyt</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">¿Seguro desa Salir?</span></p></body></html>"))

    def accept(self):
        self.parent.limpiaMesas()
        self.parent.cerrarVentana()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

