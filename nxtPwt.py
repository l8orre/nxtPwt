#!/usr/bin/python3
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

import sys
import os
from PyQt4 import QtGui
 
#import nxtPwt
from nxtPwt.nxtSessionManager import nxtSessionManager

#import argparse
#import configparser


from nxtPwt import nxtBridgeCtrl

from nxtPwt import nxtWin0Control1, \
                nxtWin1Control1, \
                nxtWin2Control1, \
                nxtWin3Control1, \
                nxtWin4Control1, \
                nxtWin5Control1, \
                nxtWin6Control1, \
                nxtWin7Control1


class MainApplication:
    """  Win """
    
    def __init__(self, app, args): # = None):
        self.app = app
        
        self.args = args
        #runAs = self.args['runAs']
        
        #here we can reboot other sessions
        self.sessMan = nxtSessionManager(app, args ) # self = app        

        #self.startBridge()

    #
    # # these are controllers
    # def startBridge(self):
    #     """ This means that PowerTools can also be run WITHOUT windows!   """
    #     self.nxtBridge1Ctrl = nxtBridgeCtrl.Bridge1Ctrl(self) # bridge is what the WinCtrl would be
    #     self.nxtBridge1Ctrl.activate()

    def openMainWindow(self):
        # reminder of namespaces: keep here.
        # NB: what goes as 'self' into self.nxtMain = nxtMainControl    3.nxtMainControl(self)
        # IS THE APP OBJECT INSTANCE!!!
        # AS SUCH, it also knows the app object: self.app = <PyQt4.QtGui.QApplication object at 0x1f81cc8>
        # this is self here: the __main__.APP: print self # <__main__.MainApplication instance at 0x1e15248>
        self.nxtWin0 = nxtWin0Control1.nxtWin0Control(self) # self is the 'app' instance!!!!
        self.nxtWin0.show()

    def openWin1(self): 
        #import nxtWin1Control1
        self.nxtWin1 =  nxtWin1Control1.nxtWin1Control(self)
        self.nxtWin1.show()
          
    def openWin2(self):
        #import nxtWin2Control1
        self.nxtWin2 =  nxtWin2Control1.nxtWin2Control(self)
        self.nxtWin2.show()
    # now we can hook up as many windows as we want, using this pattern!
          
    def openWin3(self): 
        #import nxtWin3Control1
        self.nxtWin3 =  nxtWin3Control1.nxtWin3Control(self)
        self.nxtWin3.show()
          
    def openWin4(self): 
        #import nxtWin4Control1
        self.nxtWin4 =  nxtWin4Control1.nxtWin4Control(self)
        self.nxtWin4.show()
           
    def openWin5(self): 
        #import nxtWin5Control1
        self.nxtWin5 =  nxtWin5Control1.nxtWin5Control(self)
        self.nxtWin5.show()
           
    def openWin6(self): 
        #import nxtWin6Control1
        self.nxtWin6 =  nxtWin6Control1.nxtWin6Control(self)
        self.nxtWin6.show()
       
    def openWin7(self): 
        #import nxtWin7Control1
        self.nxtWin7 =  nxtWin7Control1.nxtWin7Control(self)
        self.nxtWin7.show()
                          
 


def main(argv):
    
    sys.path += [ os.path.dirname(os.path.dirname(os.path.realpath(__file__))) ]
    argv = sys.argv

 
    
    print(str(argv))
    # todo : arg parse

    if len(argv) <2:
        argv.append('W')
    runAs = argv[1]

    args={}
    args['runAs'] = runAs
    app = QtGui.QApplication(sys.argv) # creation of the app object
    main = MainApplication(app, args )
    main.openMainWindow( )
    done = app.exec_()

    # if runAs== 'W':
    #     main.openMainWindow( )
    #     done = app.exec_()
    #
    # elif runAs == 'B':
    #     main.startBridge( )
    #     done = app.exec_()
    #
    # print(done )

    sys.exit(done)



        
if __name__ == "__main__":
    #import sys

    main(sys.argv)
    







