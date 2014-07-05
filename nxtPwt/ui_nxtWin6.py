# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nxtWin6_h900.ui'
#
# Created: Sat Jul  5 16:58:40 2014
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
        MainWindow.setMaximumSize(QtCore.QSize(1280, 900))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget_Req = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_Req.setGeometry(QtCore.QRect(0, 0, 1251, 881))
        self.tabWidget_Req.setObjectName(_fromUtf8("tabWidget_Req"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit_testReport = QtGui.QTextEdit(self.tab)
        self.textEdit_testReport.setGeometry(QtCore.QRect(410, 30, 601, 801))
        self.textEdit_testReport.setReadOnly(True)
        self.textEdit_testReport.setObjectName(_fromUtf8("textEdit_testReport"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1050, 140, 160, 128))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pb_test2Prep = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_test2Prep.setObjectName(_fromUtf8("pb_test2Prep"))
        self.gridLayout.addWidget(self.pb_test2Prep, 2, 0, 1, 1)
        self.pb_test1Prep = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_test1Prep.setObjectName(_fromUtf8("pb_test1Prep"))
        self.gridLayout.addWidget(self.pb_test1Prep, 0, 0, 1, 1)
        self.pb_test1Start = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_test1Start.setObjectName(_fromUtf8("pb_test1Start"))
        self.gridLayout.addWidget(self.pb_test1Start, 1, 0, 1, 1)
        self.pb_test2Start = QtGui.QPushButton(self.gridLayoutWidget)
        self.pb_test2Start.setObjectName(_fromUtf8("pb_test2Start"))
        self.gridLayout.addWidget(self.pb_test2Start, 3, 0, 1, 1)
        self.textEdit_testComment = QtGui.QTextEdit(self.tab)
        self.textEdit_testComment.setGeometry(QtCore.QRect(0, 30, 401, 801))
        self.textEdit_testComment.setReadOnly(True)
        self.textEdit_testComment.setObjectName(_fromUtf8("textEdit_testComment"))
        self.pb_clearComments = QtGui.QPushButton(self.tab)
        self.pb_clearComments.setGeometry(QtCore.QRect(1100, 10, 131, 41))
        self.pb_clearComments.setObjectName(_fromUtf8("pb_clearComments"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(410, 0, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pb_clearReplies = QtGui.QPushButton(self.tab)
        self.pb_clearReplies.setGeometry(QtCore.QRect(1100, 60, 131, 41))
        self.pb_clearReplies.setObjectName(_fromUtf8("pb_clearReplies"))
        self.tabWidget_Req.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 691, 801))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget_Req.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.treeWidget = QtGui.QTreeWidget(self.tab_3)
        self.treeWidget.setGeometry(QtCore.QRect(10, 0, 681, 801))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.tabWidget_Req.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionMenu = QtGui.QAction(MainWindow)
        self.actionMenu.setObjectName(_fromUtf8("actionMenu"))

        self.retranslateUi(MainWindow)
        self.tabWidget_Req.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "NxtPowerTools ShopKeeper", None))
        self.pb_test2Prep.setText(_translate("MainWindow", "test2Prep", None))
        self.pb_test1Prep.setText(_translate("MainWindow", "test1Prep", None))
        self.pb_test1Start.setText(_translate("MainWindow", "test1Start", None))
        self.pb_test2Start.setText(_translate("MainWindow", "test2Start", None))
        self.pb_clearComments.setText(_translate("MainWindow", "clear Comments", None))
        self.label.setText(_translate("MainWindow", "textEdit_testComment", None))
        self.label_2.setText(_translate("MainWindow", "NRS Replies: textEdit_testReport", None))
        self.pb_clearReplies.setText(_translate("MainWindow", "clear Replies", None))
        self.tabWidget_Req.setTabText(self.tabWidget_Req.indexOf(self.tab), _translate("MainWindow", "TextView", None))
        self.tabWidget_Req.setTabText(self.tabWidget_Req.indexOf(self.tab_2), _translate("MainWindow", "TableView", None))
        self.tabWidget_Req.setTabText(self.tabWidget_Req.indexOf(self.tab_3), _translate("MainWindow", "TreeView", None))
        self.actionMenu.setText(_translate("MainWindow", "menu", None))

