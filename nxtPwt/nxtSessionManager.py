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
 

from PyQt4.QtCore import   QObject , pyqtSignal, pyqtSlot

#from PyQt4.QtGui import QSortFilterProxyModel

#import FR

import nxtPwt.nxtUseCases as nxtUseCases

import nxtPwt.nxtUC_Bridge as nxtUC_Bridge
import logging as lg

import nxtPwt.nxtModels as nxtMods
from nxtPwt.nxtApiSigs import nxtApi

import os
# Here we can do some control on whether or not to do testing 
#import nxtPwt.nxtTestCases as nxtTestCases


class nxtSessionManager(QObject):
    """ 
    
session management. 

container and brokering services for the useCases. 

connection management.

  
  """

    changeConn_Sig = pyqtSignal( object )

    # these signlas MUST be thrown by the sessMan, because the connects can only be done to singletons,
    # not to bork

    # the TX signals are thrown by the sessMan
    TX_status_Sig = pyqtSignal(object, object) # second must have some meta
    #
    TX_sendMoney_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_issueAsset_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_placeAskOrder_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_placeBidOrder_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_cancelAskOrder_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_cancelBidOrder_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_transferAsset_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_setAccountInfo_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_lease_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    #
    TX_sendMSG_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_assAlias_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_vote_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    TX_poll_Sig = pyqtSignal(object, object) # each TX throws its nw recepit wignal
    #



    #TX_receipt_Sig
    # sessMan throws all these Signals with the different objects in them!
    # these Signals can only be connected when the identity is known



    def __init__(self, app, args ):# app, self.lastSess
        """
        sessMan can do things himself.
        But most of the things are done in the UC instances which are clollected here.
        So this is a container object for useCases and models

       """
        super(nxtSessionManager, self).__init__()
        self.app = app
        self.app.sessMan = self #
        
        runAs = args['runAs']


        self.apiLoggerNXT = lg.getLogger('apiLogger')
        self.apiLoggerNXT.setLevel(lg.INFO) # INFO DEBUG
        aLhandler = lg.StreamHandler()
        aLhandler.setLevel(lg.INFO)      # INFO DEBUG
        after = lg.Formatter('\n%(asctime)s - %(message)s')
        aLhandler.setFormatter(after)
        self.apiLoggerNXT.addHandler(aLhandler)


        self.nxtApi = nxtApi(self, self.apiLoggerNXT) # make the apiSigs instance here!

        self.activeNRS = nxtMods.NRSconn(self)

        self.nxtApi.initSignals(self.activeNRS) # leapFrog init: account and NRSconn must be made before connecting their Sigs on nxtApi

        #self.nxtApi.initSignals() # leapFrog init: account and NRSconn must be made before connecting their Sigs on nxtApi




        self.logShort = True
        self.logLong = False

        self.logFshort = open('nxtPwt_logS.txt', 'a')
        self.logFlong = open('nxtPwt_logL.txt', 'a')

        # # UCs:

        if runAs == 'B':
            host = 'localhost'
            port = '6876'
            #port = '7876'

            self.uc_bridge = nxtUC_Bridge.UC_Bridge1(self,host  , port )
            
        elif runAs == 'W':
            #self.uc_bridge = nxtUC_Bridge.UC_Bridge1(self, )
            
            self.uc1_pollNRS = nxtUseCases.UC1_pollNRS(self,  ) #
            self.uc2_accHndlr = nxtUseCases.UC2_accountHandler(self,   ) #
            self.uc3_TX_monitor = nxtUseCases.UC3_TX_monitor(self)
            self.uc4_sendMoney = nxtUseCases.UC4_sendMoney(self,  )#
            #todo self.uc4_setName = nxtUseCases.UC4_setName(self,  )#
    
            self.uc29_changeConn = nxtUseCases.UC29_changeConn(self,  ) #
            
            self.uc51_blkch_trav =  nxtUseCases.UC51_BlockchainTraversal(self,  ) #
            self.uc30 = nxtUseCases.nxtUC_apiAccess(self,   ) #
            self.uc30.initSignals()
    #
    # getAssetsByName is gone       self.uc5_AE = nxtUseCases.UC5_AE(self,  )#
            self.uc6_AO = nxtUseCases.UC6_AO(self,  )#
            self.uc7_ATX = nxtUseCases.UC7_ATX(self,  )#
            self.uc8_Trades = nxtUseCases.UC8_Trades(self,  )#

 
 
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
      
        
        
   
        
if __name__ == "__main__":
    import sys
    sys.path += [os.path.dirname(os.path.dirname(os.path.realpath(__file__))) ]
    argv = sys.argv
    app = QtGui.QApplication(sys.argv) # creation of the app object
    standAloneTest = "needs to be defined here"
    done = app.exec_()
    sys.exit(done)
 
 
 
  
  
  
  
  
  
  
   