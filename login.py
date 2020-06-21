# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtWidgets
from register import *
from PyQt5.QtWidgets import *
all_users = {
    'lrj': '12345',
    'zzm': '1234',
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 685)
        self.register_window = QDialog()
        d = Ui_Dialog()
        d.setupUi(self.register_window)
        self.dialog = d
        self.dialog.pushButton.clicked.connect(self.create_new_user)
        self.window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(73, 150, 131, 41))
        self.label.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 150, 581, 41))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 255, 111, 31))
        self.label_2.setStyleSheet("font: 16pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 260, 581, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 380, 111, 31))
        self.pushButton.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 380, 101, 31))
        self.pushButton_2.setStyleSheet("font: 16pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menufile.addAction(self.actionexit)
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText('Name:')
        self.textEdit.textChanged.connect(self.reset_buttons)
        self.textEdit_2.setPlaceholderText('password:')
        self.textEdit_2.textChanged.connect(self.reset_buttons)
        self.label.setText(_translate("MainWindow", "Your name:"))
        self.label_2.setText(_translate("MainWindow", "paasword:"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.pushButton_2.clicked.connect(self.show_register_window)
        # self.pushButton_2.setEnabled(False)
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionabout.setText(_translate("MainWindow", "about"))

    def check_filled(self):
        if self.textEdit.toPlainText() and self.textEdit_2.toPlainText():
            return True
        return False

    def reset_buttons(self):
        # print(self.check_filled())
        self.pushButton.setEnabled(self.check_filled())

    def login(self):
        user = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()
        if all_users[user] == password:
            QMessageBox.information(self.window, 'Information', 'Login!')
        else:
            QMessageBox.critical(self.window, 'Wrong', 'Not right!')

    def show_register_window(self):
        self.register_window.show()

    def create_new_user(self):
        new_name = self.dialog.textEdit.toPlainText()
        new_password = self.dialog.textEdit_2.toPlainText()
        all_users[new_name] = new_password
        self.register_window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

