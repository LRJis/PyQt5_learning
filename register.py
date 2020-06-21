# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(713, 415)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(53, 50, 111, 21))
        self.label.setStyleSheet("font: 16pt \"Arial\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(210, 40, 401, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 101, 31))
        self.label_2.setStyleSheet("font: 16pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 120, 401, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 231, 41))
        self.pushButton.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setPlaceholderText('name:')
        self.textEdit.textChanged.connect(self.reset_buttons)
        self.textEdit_2.setPlaceholderText('password:')
        self.textEdit_2.textChanged.connect(self.reset_buttons)
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your name:"))
        self.label_2.setText(_translate("Dialog", "password:"))
        self.pushButton.setText(_translate("Dialog", "Register"))

    def check_filled(self):
        if self.textEdit.toPlainText() and self.textEdit_2.toPlainText():
            return True
        return False

    def reset_buttons(self):
        # print(self.check_filled())
        self.pushButton.setEnabled(self.check_filled())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

