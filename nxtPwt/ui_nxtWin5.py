# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nxtWin5_h900.ui'
#
# Created: Wed Jul  2 10:58:11 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1280, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 35, 531, 811))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit_NRSRaw1 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_NRSRaw1.setGeometry(QtCore.QRect(0, 20, 511, 791))
        self.textEdit_NRSRaw1.setReadOnly(True)
        self.textEdit_NRSRaw1.setObjectName(_fromUtf8("textEdit_NRSRaw1"))
        self.lcdNumber_time1 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_time1.setGeometry(QtCore.QRect(1030, 10, 241, 51))
        self.lcdNumber_time1.setObjectName(_fromUtf8("lcdNumber_time1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu = QtGui.QAction(MainWindow)
        self.actionMenu.setObjectName(_fromUtf8("actionMenu"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NxtPowerTools Network Explorer", None))
        self.groupBox.setTitle(_translate("MainWindow", "nxt server display", None))
        self.actionMenu.setText(_translate("MainWindow", "menu", None))

