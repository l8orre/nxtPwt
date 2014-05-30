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


# import pyqtgraph as pg  


# from PyQt4.QtCore import SIGNAL there is s.t. wrong w/ the import here!

from PyQt4 import  Qt ,  QtCore # QtGui,
#from PyQt4.QtGui import  QMainWindow
from PyQt4.QtCore import  SIGNAL , QObject, pyqtSignal, pyqtSlot

# timer:
import os
import time
  
   


from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher


from nxtPwt.nxtApiPrototypes import nxtQs 
#from nxtPwt.nxtApiSigs import nxtApi


 
class Bridge1Ctrl(QObject):
    """ Bridge Control - container and controller for useCase logic
        """
    
    UC29changeConn_Sig = pyqtSignal(  object)
    UCTEST_activate = pyqtSignal( object)

    def __init__(self, app ):
        super(QObject, self, ).__init__()
        
        self.app = app
        self.app.nxtBridge1 = self # make this   WinControl1  known  in the app namespace.  When this Win throws sigs, they can be recvd anywhere where this isknown.
        self.timer1 = Qt.QTimer()
        self.time1 = 10000
#        self.nxtApi = app.sessMan.nxtApi  # there is only ONE apiSigs instance, and that is in the sessMan.
#        self.apiCalls = nxtQs()
#            
    def init(self):  
        """ Here all signals must be connected """  
        pass
        #QObject.connect(self.timer1, SIGNAL("timeout()"),  self.timer1_CB)
        
    def timer1_CB(self):
        pass #print("t1 CB!")
 
###########################
  
############################
############################        
############################
########## Window Maintenance

    def activate(self):
        self.init()
        self.app.sessMan.uc_bridge.mm.jsonServ_Slot()
        
        
    def quitApp(self):
        print("QUITTING - not!?!?!")
        self.app.app.flush()
        self.app.app.emit(SIGNAL("aboutToQuit()") )
        
        self.app.app.exit(0)
        
        

 


 