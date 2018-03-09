# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import test

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

import gui_2

class Ui_MainWindow(object):

    def SignUpBtnPressed(self):
        test.SignUpBtnCall(self.email.toPlainText(), self.password.toPlainText())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Whiz Aide"))
	#self.setWindowIcon(QtGui.QIcon('insertpicture')
        MainWindow.resize(766, 502)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.SignUpbutton = QtGui.QPushButton(self.centralwidget)
        self.SignUpbutton.setGeometry(QtCore.QRect(180, 380, 391, 51))
        self.SignUpbutton.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: white;\n"
""))
        self.SignUpbutton.setObjectName(_fromUtf8("SignUpbutton"))
        self.SignUpbutton.clicked.connect(self.SignUpBtnPressed)

        self.password = QtGui.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(180, 330, 391, 31))
        self.password.setObjectName(_fromUtf8("password"))
        self.email = QtGui.QTextEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(180, 290, 391, 31))
        self.email.setObjectName(_fromUtf8("email"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(187, 100, 391, 101))
        self.label.setStyleSheet(_fromUtf8("font: 60pt \"STIXVariants\";"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.SignUpbutton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Click to signup</p></body></html>", None))
        self.SignUpbutton.setText(_translate("MainWindow", "SignUP", None))
        self.label.setText(_translate("MainWindow", "Whiz Aide", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow()
#    ui.MainWindow_1 = MainWindow
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())



