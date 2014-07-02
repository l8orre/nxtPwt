# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nxtWin4_h900.ui'
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
        MainWindow.setMaximumSize(QtCore.QSize(1280, 900))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget_MainDetail = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_MainDetail.setGeometry(QtCore.QRect(0, 0, 986, 896))
        self.tabWidget_MainDetail.setObjectName(_fromUtf8("tabWidget_MainDetail"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.textEdit_response = QtGui.QTextEdit(self.tab_6)
        self.textEdit_response.setGeometry(QtCore.QRect(10, 175, 926, 286))
        self.textEdit_response.setObjectName(_fromUtf8("textEdit_response"))
        self.pb_clearTextEditMSG = QtGui.QPushButton(self.tab_6)
        self.pb_clearTextEditMSG.setGeometry(QtCore.QRect(650, 150, 71, 21))
        self.pb_clearTextEditMSG.setObjectName(_fromUtf8("pb_clearTextEditMSG"))
        self.pb_test1 = QtGui.QPushButton(self.tab_6)
        self.pb_test1.setGeometry(QtCore.QRect(25, 10, 116, 46))
        self.pb_test1.setObjectName(_fromUtf8("pb_test1"))
        self.pb_test2 = QtGui.QPushButton(self.tab_6)
        self.pb_test2.setGeometry(QtCore.QRect(710, 10, 106, 41))
        self.pb_test2.setObjectName(_fromUtf8("pb_test2"))
        self.pb_test3 = QtGui.QPushButton(self.tab_6)
        self.pb_test3.setGeometry(QtCore.QRect(845, 10, 106, 41))
        self.pb_test3.setObjectName(_fromUtf8("pb_test3"))
        self.lineEdit_T1 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_T1.setGeometry(QtCore.QRect(685, 65, 266, 27))
        self.lineEdit_T1.setObjectName(_fromUtf8("lineEdit_T1"))
        self.label_1 = QtGui.QLabel(self.tab_6)
        self.label_1.setGeometry(QtCore.QRect(595, 70, 86, 17))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.lineEdit_T2 = QtGui.QLineEdit(self.tab_6)
        self.lineEdit_T2.setGeometry(QtCore.QRect(685, 100, 266, 27))
        self.lineEdit_T2.setObjectName(_fromUtf8("lineEdit_T2"))
        self.label_2 = QtGui.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(595, 105, 86, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_response_2 = QtGui.QTextEdit(self.tab_6)
        self.textEdit_response_2.setGeometry(QtCore.QRect(10, 495, 931, 336))
        self.textEdit_response_2.setObjectName(_fromUtf8("textEdit_response_2"))
        self.pb_clearResponse_2 = QtGui.QPushButton(self.tab_6)
        self.pb_clearResponse_2.setGeometry(QtCore.QRect(645, 465, 76, 21))
        self.pb_clearResponse_2.setObjectName(_fromUtf8("pb_clearResponse_2"))
        self.tabWidget_MainDetail.addTab(self.tab_6, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu = QtGui.QAction(MainWindow)
        self.actionMenu.setObjectName(_fromUtf8("actionMenu"))

        self.retranslateUi(MainWindow)
        self.tabWidget_MainDetail.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NxtPowerTools DGS", None))
        self.pb_clearTextEditMSG.setText(_translate("MainWindow", "clear", None))
        self.pb_test1.setText(_translate("MainWindow", "jsonrpc server\n"
"start", None))
        self.pb_test2.setText(_translate("MainWindow", "t2", None))
        self.pb_test3.setText(_translate("MainWindow", "t3", None))
        self.label_1.setText(_translate("MainWindow", "L1", None))
        self.label_2.setText(_translate("MainWindow", "L2", None))
        self.pb_clearResponse_2.setText(_translate("MainWindow", "clear", None))
        self.tabWidget_MainDetail.setTabText(self.tabWidget_MainDetail.indexOf(self.tab_6), _translate("MainWindow", "BTC-NXT Bridge", None))
        self.actionMenu.setText(_translate("MainWindow", "nxTrading", None))

