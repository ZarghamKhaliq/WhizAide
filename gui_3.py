# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewmeetings.ui'
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

class Ui_ViewMeetings(object):
    def setupUi(self, ViewMeetings):
        ViewMeetings.setObjectName(_fromUtf8("ViewMeetings"))
        ViewMeetings.resize(588, 457)
        ViewMeetings.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(ViewMeetings)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(25, 81, 541, 351))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 111, 20))
        self.label.setObjectName(_fromUtf8("label"))
        ViewMeetings.setCentralWidget(self.centralwidget)

        self.retranslateUi(ViewMeetings)
        QtCore.QMetaObject.connectSlotsByName(ViewMeetings)

    def retranslateUi(self, ViewMeetings):
        ViewMeetings.setWindowTitle(_translate("ViewMeetings", "View Meetings", None))
        self.label.setText(_translate("ViewMeetings", "Meetings:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ViewMeetings = QtGui.QMainWindow()
    ui = Ui_ViewMeetings()
    ui.setupUi(ViewMeetings)
    ViewMeetings.show()
    sys.exit(app.exec_())

