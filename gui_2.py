# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dex2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName(_fromUtf8("Home"))
        Home.resize(564, 374)
        Home.setStyleSheet(_fromUtf8("background-color:  rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(Home)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ViewM = QtGui.QPushButton(self.centralwidget)
        self.ViewM.setGeometry(QtCore.QRect(10, 30, 549, 71))
        self.ViewM.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);"))
        self.ViewM.setObjectName(_fromUtf8("ViewM"))
        self.CreateM = QtGui.QPushButton(self.centralwidget)
        self.CreateM.setGeometry(QtCore.QRect(10, 110, 549, 71))
        self.CreateM.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
""))
        self.CreateM.setObjectName(_fromUtf8("CreateM"))
        self.ViewT = QtGui.QPushButton(self.centralwidget)
        self.ViewT.setGeometry(QtCore.QRect(10, 190, 549, 71))
        self.ViewT.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
""))
        self.ViewT.setObjectName(_fromUtf8("ViewT"))
        self.ViewS = QtGui.QPushButton(self.centralwidget)
        self.ViewS.setGeometry(QtCore.QRect(10, 270, 549, 71))
        self.ViewS.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);\n"
""))
        self.ViewS.setObjectName(_fromUtf8("ViewS"))
        Home.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Home)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(_translate("Home", "main", None))
        self.ViewM.setText(_translate("Home", "View Meeting", None))
        self.CreateM.setText(_translate("Home", "View Schedule", None))
        self.ViewT.setText(_translate("Home", "View Today\'s Meetings", None))
        self.ViewS.setText(_translate("Home", "Create Meeting", None))

import sys
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Home = QtGui.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())

def run():
#    app = QtGui.QApplication(sys.argv)
    Home = QtGui.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
#    sys.exit(app.exec_())