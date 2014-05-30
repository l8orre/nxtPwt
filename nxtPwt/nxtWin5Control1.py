# -*- coding: utf-8 -*-
"""
 Copyright (c) 2014 l8orre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

#import sys


from PyQt4 import QtGui, Qt, QtCore
from PyQt4.QtCore import QObject , pyqtSignal, pyqtSlot, SIGNAL
from PyQt4.QtCore import  QObject
#import numpy as np
from os import listdir as ls
#from PyQt4.Qt import QPixmap
import os
import time


import nxtPwt
#import requests, json
 
class nxtWin5Control(QObject):
    """ class nxtWin5Control(): here""" 
    def __init__(self, app): #, application
        super(QObject, self, ).__init__()
        import nxtPwt.ui_nxtWin5 as nxtWin5  # the QtCreator-generated Widget.py!!
        ui = nxtWin5.Ui_MainWindow() # Ui_MainWindow() is the autogenerated class in m2def.py
        self.ui_nxtWin5 = ui 
        self.app = app  # 
         
        # self.userDataContainer = self.app.nxtMain.userDataContainer
        self.server = ''
        self.account =''
        self.secretPhrase = ''
        #self.app.algo.ui_nxtWin = ui # make the ui_AlgoWin known to the Algo!!! this is N( at the algo when init'ing
        self.app.nxtWin5 = self # make this   WinControl1  known  
 
        
    def init(self): #, ui_AlgoWin):
        """ the AlgoWin """ 
        # maybe this gives trouble w/ MainWIn, self.app.algo = Algo1(self.app, ui)
        ### re - init hte algo here!!!
        
        ui = self.ui_nxtWin5
         


               




############################
############################        
############################
########## Window Maintenance

    
    def show(self):
        self.uiFrame = QtGui.QMainWindow()
        self.ui_nxtWin5.setupUi(self.uiFrame)
        self.init() #self.ui_AlgoWin)
        self.uiFrame.show()     


        
        
        
