# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nxtWin1_h900.ui'
#
# Created: Mon May 26 12:24:43 2014
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
        MainWindow.resize(1280, 880)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 880))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 880))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget_querySel = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_querySel.setGeometry(QtCore.QRect(5, -5, 1181, 871))
        self.tabWidget_querySel.setObjectName(_fromUtf8("tabWidget_querySel"))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.pb_typeSort = QtGui.QPushButton(self.tab_4)
        self.pb_typeSort.setGeometry(QtCore.QRect(1090, 800, 71, 31))
        self.pb_typeSort.setObjectName(_fromUtf8("pb_typeSort"))
        self.textEdit_relNotes = QtGui.QTextEdit(self.tab_4)
        self.textEdit_relNotes.setGeometry(QtCore.QRect(30, 20, 1031, 811))
        self.textEdit_relNotes.setObjectName(_fromUtf8("textEdit_relNotes"))
        self.tabWidget_querySel.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget_querySel.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.groupBox = QtGui.QGroupBox(self.tab_6)
        self.groupBox.setGeometry(QtCore.QRect(170, 25, 521, 821))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit1 = QtGui.QTextEdit(self.groupBox)
        self.textEdit1.setGeometry(QtCore.QRect(50, 20, 441, 801))
        self.textEdit1.setReadOnly(True)
        self.textEdit1.setObjectName(_fromUtf8("textEdit1"))
        self.tabWidget_querySel.addTab(self.tab_6, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu = QtGui.QAction(MainWindow)
        self.actionMenu.setObjectName(_fromUtf8("actionMenu"))

        self.retranslateUi(MainWindow)
        self.tabWidget_querySel.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NxtPowerTools Account Explorer", None))
        self.pb_typeSort.setText(_translate("MainWindow", "type", None))
        self.tabWidget_querySel.setTabText(self.tabWidget_querySel.indexOf(self.tab_4), _translate("MainWindow", "coming soon", None))
        self.tabWidget_querySel.setTabText(self.tabWidget_querySel.indexOf(self.tab_5), _translate("MainWindow", "AccountTXs", None))
        self.groupBox.setTitle(_translate("MainWindow", "nxt Messages", None))
        self.tabWidget_querySel.setTabText(self.tabWidget_querySel.indexOf(self.tab_6), _translate("MainWindow", "Messaging", None))
        self.actionMenu.setText(_translate("MainWindow", "nxTrading", None))

