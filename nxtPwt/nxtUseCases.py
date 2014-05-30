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

 
from PyQt4.QtCore import   QObject , pyqtSignal, pyqtSlot, SIGNAL

from PyQt4 import Qt
#from PyQt4.QtCore import QTimer

#import time
#from copy import copy


from nxtPwt.nxtApiPrototypes import nxtQs

import nxtPwt.nxtModels as nxtMods
import numpy as np

from PyQt4.QtGui import QSortFilterProxyModel



class nxtUseCaseMeta(QObject):
    """ This is an abstract meta class that has elemtary sigs and methods defined.
    All use case classes inherit from this, so they know all the signals for emission
    The useCaseClass is tho ONLY one that talks to the api.    

     """
    
    apiCalls = nxtQs() # static! dict of prototypes to be filled with vals for apiReq
    blinkerCols = [Qt.Qt.darkYellow, Qt.Qt.magenta]
   
   
    
    def __init__(self,  sessMan  ): # 
        """ just call the super init here: QObject.
       """        
        super(nxtUseCaseMeta, self).__init__()
        self.nxtApi = sessMan.nxtApi  # there is only ONE apiSigs instance, and that is in the sessMan.


    
class nxtUC_apiAccess(nxtUseCaseMeta): # this is old style. leave as it is for now - legacy API access
    """ 
    old style - useful legacy
  connect the buttons on Win7 to the reqPrepareCBs on win7, then have that prepared apiReq sent here to the api,
  connect the replies ALL to one catcher that hands them back to win7.
    """
   
    def __init__(self, sessMan,   ):
        super(nxtUC_apiAccess   , self   ).__init__(sessMan)
        self.apiCalls = nxtQs()
        #self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {}
        
    def initWin7(self, nxtWin7, ui7 ):
        """ - these are the activators FROM the widgets""" 
        self.nxtWin7 = nxtWin7
        self.ui7 = ui7
        QObject.connect(self.nxtWin7, SIGNAL("UC30_apiAcc(PyQt_PyObject)"),  self.execUC30_CB) # catch the activator from app.
  
    def initSignals(self,):    
        """   returning FROM the api   """
         # same CB here to return to the widget.
        QObject.connect( self.nxtApi, SIGNAL("catchAll_Sig(PyQt_PyObject, PyQt_PyObject)"), self.catchAll_fromApiSlot ) # all of them
        QObject.connect( self.nxtApi, SIGNAL("queryURL_Sig(PyQt_PyObject)"), self.catchQ ) # all of them
          
    def execUC30_CB(self, apiReq): # hit the apiBroker with these two requests: self.nxtApi,
        self.nxtApi.catchAll_Slot( apiReq, self.meta)


    @pyqtSlot( ) #  
    def catchQ(self, query): #queryURL_Sig
        try:
            self.ui7.lineEdit1_nxtFullQ.setText(query)
        except Exception as inst:
            pass #print(str(inst) + "-? seems no probelm! ---")

    @pyqtSlot( ) # catch reply from api and do s.t. with it
    def catchAll_fromApiSlot(self, reply, meta):
        #print("caught reply back from api: " + str(reply))
        try:
            for key in reply:
                self.ui7.textEdit_NRSRaw1.append( str(key) + " - " + str(reply[key]))
            #for key in reply:
            #    print( str(key) + " - " + str(reply[key]) + " - " + str(type(reply[key])))

        except Exception as inst:
            pass #print(str(inst))
            #print("nxtWin7 not active")


class UC1_pollNRS(nxtUseCaseMeta):
    """ ___ use case architecture update  """

    def __init__(self, sessMan,   ):
        super(UC1_pollNRS   , self   ).__init__(sessMan)

        #self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'uc1'}

        # activate Timers on nxtModels
        self.sessMan.activeNRS.poll1Start(self.meta)
        self.sessMan.activeNRS.state.poll1Start(self.meta)
        #self.sessMan.account.poll1Start(self.meta)


class UC2_accountHandler(nxtUseCaseMeta):

    changeResident_Sig = pyqtSignal(object, object)

    def __init__(self, sessMan, ):
        super(UC2_accountHandler   , self   ).__init__(sessMan)


        #self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'uc2'}

        self.allAccs = nxtMods.Accounts(sessMan)

        # persistence later
        defPass14 = '14oreosetc14oreosetc'
        defPass15 = '15oreosetc15oreosetc'
        defPass16 = '16oreosetc16oreosetc'
        defPass17 = '17oreosetc17oreosetc'

        acctSecKey = defPass17

        self.accRes = nxtMods.Account(self, sessMan, acctSecKey,  )
        self.accRes.getAccountId(self.meta )

        self.accFOC = self.accRes.data['account']

        self.accSLT =  nxtMods.Account(self, sessMan, '0',)
        self.accOIss =  nxtMods.Account(self, sessMan, '0',)

        self.pollaccRes()

# acct handler needs own methods!


    def changeResidAccount(self, acctSecKey):
        # move resident to list
        # make new one. check if new is in list already, else totally new<

        self.allAccs.accountsDi[self.accRes.data['account']] = self.accRes

        # create new account instance
        self.accRes = nxtMods.Account(self, self.sessMan, acctSecKey,   )
        self.accRes.getAccountId( self.meta )
        # announce new accRes
        self.meta['caller'] = ['uc2_accRes']
        self.emit( SIGNAL( "changeResident_Sig(PyQt_PyObject, PyQt_PyObject)"), self.accRes, self.meta)
        #print(str(self.allAccs.accountsDi))
        self.pollaccRes()

    # this starts polling the resident account
    def pollaccRes(self):
        self.accRes.poll1Start(self.meta)
    # here we can poll any account we want
    def pollAccStop(self):
        self.accRes.poll1Stop(self.meta)

    def startForge(self):
        self.accRes.startForging()

    def stopForge(self):
        self.accRes.stopForging()


    def getAccount(self):
        pass

    # TX creation API calls done by this UC

    def setAccountInfo(self, TXparms):
        self.TX = nxtMods.SetAccountInfo(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta)
        self.TX.setAccountInfo() #make TX instance, rest is autonomous

    def leaseBalance(self, TXparms):
        self.TX = nxtMods.LeaseBalance(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta)
        self.TX.leaseBalance() #make TX instance, rest is autonomous
    #################
    def assignAlias(self):
        pass

    #############################
    # retro TXs:  get activity from past
    def getAliases(self):
        pass
    def MSGs(self): # including Polls
        pass
    def getNxtXfers(self):
        pass



class UC29_changeConn(nxtUseCaseMeta):
    """
    UC29 does not communicate with api
    """

    def __init__(self, sessMan,  ):
        super(UC29_changeConn   , self   ).__init__(sessMan)
        self.apiCalls = nxtQs()
        #self.app = app # we need to know app
        self.sessMan = sessMan


    def changeConn(self, newConn):

        #self.sessMan.uc29_newConn.newUrl(newUrl)
        del self.sessMan.activeNRS

        print(str(newConn))
        self.sessMan.activeNRS = nxtMods.NRSconn(self, newConn)

        self.nxtApi.initSignals()






class UC3_TX_monitor(nxtUseCaseMeta):

    """- """

    newAsset_Sig = pyqtSignal(object, object)
    newMXfer_Sig = pyqtSignal(object, object)
    newAskOrder_Sig = pyqtSignal(object, object)
    newBidOrder_Sig = pyqtSignal(object, object)
    newTrade_Sig = pyqtSignal(object, object)
    newBidOrderCancel_Sig = pyqtSignal(object, object)
    newAskOrderCancel_Sig = pyqtSignal(object, object)
    newMSG_Sig = pyqtSignal(object, object)
    newAlias_Sig = pyqtSignal(object, object)
    newLease_Sig = pyqtSignal(object, object)
    newAcctInfo_Sig = pyqtSignal(object, object)
    newPoll_Sig = pyqtSignal(object, object)
    newVote_Sig = pyqtSignal(object, object)


    def __init__(self, sessMan,  ):
        super(UC3_TX_monitor   , self   ).__init__(sessMan)
        self.apiCalls = nxtQs()
        #self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'UC_TXchecker'}
        print(str(self.sessMan.activeNRS.block))
        self.TXs = {}
        self.init_Sigs()

    def init_Sigs(self):
        QObject.connect(self.sessMan.activeNRS.block, SIGNAL("newTXs_Sig(PyQt_PyObject, PyQt_PyObject)"),  self.newTXs_CB)
        QObject.connect(self.sessMan.nxtApi, SIGNAL("getTransaction_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getTransaction_fromApi)


    def newTXs_CB(self, newTXs_inBlock, meta):
        print("NEW TXS!\n")
        for TX in newTXs_inBlock:
            self.TXs[TX] = nxtMods.TX(self.sessMan, TX )
            print( str(TX) + str(meta))

    def getTransaction_fromApi(self, TX, meta): # TX is a dict returned from the API! NOT the TX INSTANCE ITSELF!
        print("getTransaction_fromApi in uc3: " + str(TX) + " --- " + str(meta) + "\n")
        # in principle this works, it is only a bit bit ugly.
        # has been tested, these appear once in the new block!
        if 'caller' in meta.keys():

            if meta['caller'] == 'fromBlockCH':
                pass
                #print("TX fromBlockCH,   TX detect")
                #for m in meta:
                #    print(str(m) + " - " + str(meta[m]) )
                #for k in TX:
                #    print(str(k) + " - " + str(TX[k]) )
            elif  meta['caller'] == 'toBlockCH':
                print("TX toBlockCH, not a TX detect")
        #    print("\n################" )
        #print("\n+++++++++++++++++++++++++" )


    # later - for detailed TX monitoring eg new asset emission
    def newAsset(self):
        self.emit( SIGNAL( "newAsset_Sig(PyQt_PyObject, PyQt_PyObject)"), self.cont, self.meta )







class UC4_sendMoney(nxtUseCaseMeta):
    """ UC classes do the TX handling- TX is an object itself """

    def __init__(self, sessMan,   ):
        super(UC4_sendMoney   , self   ).__init__(sessMan)
        #self.apiCalls = nxtQs()
        # self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'uc4_sendMoney'}

    # TX creation API calls done by this UC
    # these functions are called to create TX instances
    def sendMoney(self, TXparms):
        self.TX = nxtMods.SendMoney(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.sendMoney() #make TX instance, rest is autonomous
        # todo: check : the TX instance may be overwritten when new TXs are sent too fast
        # for the first TX to return before the next TX is sent -
        # self.TX_Li1.append(copy(TX))  # these can be extended to collector classes
        # this may be overwritten before it has been recevied back again?


    #  obs
    # def setAccountInfo(self, TXparms):
    #     self.TX = nxtMods.SetAccountInfo(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta)
    #     self.TX.setAccountInfo() #make TX instance, rest is autonomous
    #








class UC5_AE(nxtUseCaseMeta):

    """ api comm. can be handled by the UC OR by the model - try this: hanlde here by model _"""
    # more specific Sigs are throen by the UCs themselves
    uc5_getAllAssets_Sig = pyqtSignal(object, object)
    uc5_getAssets_Sig = pyqtSignal(object, object)
    uc5_getAsset_Sig = pyqtSignal(object, object)
    uc5_getAssetIds_Sig = pyqtSignal(object, object)
    uc5_getAssetsByName_Sig = pyqtSignal(object, object)

    uc5_getAccountResid_Sig = pyqtSignal(object, object)
    uc5_getAccountSlated_Sig = pyqtSignal(object, object)

    uc5_focusAsset_Sig = pyqtSignal(object, object) # emit by AE_assets to send assetId to Orderbook!


    def __init__(self, sessMan,):
        super(UC5_AE   , self   ).__init__(sessMan)
        self.sessMan = sessMan
        self.meta={'caller':'uc5'}
        self.nxtApi = self.sessMan.nxtApi
        # these are just for collection and overview of what happens here.
        self.apiReq_getAsset = self.apiCalls.getAsset
        self.apiReq_getAllAssets = self.apiCalls.getAllAssets
        self.apiReq_getAssetIds = self.apiCalls.getAssetIds
        self.apiReq_getAssets = self.apiCalls.getAssets
        self.apiReq_getAssetsByName = self.apiCalls.getAssetsByName
        #
        self.apiReq_getAccount = self.apiCalls.getAccount
        #
        self.assets = nxtMods.Assets(sessMan)
        self.uc5_allAssets_proxy = QSortFilterProxyModel(self)
        self.uc5_allAssets_proxy.setSourceModel(self.assets.allAssetsQtM)
        #
        self.uc5_accAssets_proxy = QSortFilterProxyModel(self)
        self.uc5_accAssets_proxy.setSourceModel(self.assets.accAssetsQtM)


        self.orders= nxtMods.Orders(sessMan)
        self.uc5_askO_single_proxy = QSortFilterProxyModel(self)
        self.uc5_askO_single_proxy.setSourceModel(self.orders.ordersAsk_QtM)

        self.uc5_bidO_single_proxy = QSortFilterProxyModel(self)
        self.uc5_bidO_single_proxy.setSourceModel(self.orders.ordersBid_QtM)

        self.uc5_assetShortList = nxtMods.SimpleListQMod(sessMan, 10, 'noHeader')

        self.uc5_acctShortList = nxtMods.SimpleListQMod(sessMan, 10, 'noHeader')





        QObject.connect(self.nxtApi, SIGNAL("getAllAssets_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getAllAssets_fromApi)
        QObject.connect(self.nxtApi, SIGNAL("getAccount_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getAccount_fromApi)


    # request to api and return of result
    def getAllAssets(self): # toApi
        self.assets.allAssetsQtM.clear()
        self.nxtApi.getAllAssets_Slot( self.apiReq_getAllAssets , self.meta)

    def getAllAssets_fromApi(self, reply, meta):
        self.assets.enterAllAssetsTable(reply, meta)

    def getAccount(self, accountToFetch, caller):
        self.meta['usedFor'] = 'getAccountAssets'
        self.meta['whichAcc'] = caller
        self.assets.accAssetsQtM.clear()
        self.apiReq_getAccount['account'] = accountToFetch
        self.nxtApi.getAccount_Slot( self.apiReq_getAccount , self.meta)

    def getAccount_fromApi(self, reply, meta):
        if meta['caller']=='uc5':
            self.assets.enterAccAssetsTable(reply, meta) # <--- DIRECTLY INTO THE MODEL HERE!
            if meta['whichAcc'] == 'accRes':
                self.emit( SIGNAL( "uc5_getAccountResid_Sig(PyQt_PyObject, PyQt_PyObject)"), reply, meta)
            elif meta['whichAcc'] == 'accSLT':
                self.emit( SIGNAL( "uc5_getAccountSlated_Sig(PyQt_PyObject, PyQt_PyObject)"), reply, meta)



class UC6_AO(nxtUseCaseMeta):

    def __init__(self, sessMan,):
        super(UC6_AO   , self   ).__init__(sessMan)
        self.sessMan = sessMan
        self.meta={'caller':'uc6'}
        self.nxtApi = self.sessMan.nxtApi

        self.apiReq_getAskOrderIds = self.apiCalls.getAskOrderIds
        self.apiReq_getBidOrderIds = self.apiCalls.getBidOrderIds

        self.apiReq_getAskOrder = self.apiCalls.getAskOrder
        self.apiReq_getBidOrder = self.apiCalls.getBidOrder

        self.orders= nxtMods.Orders(sessMan)
        self.uc6_askO_single_proxy = QSortFilterProxyModel(self)
        self.uc6_askO_single_proxy.setSourceModel(self.orders.ordersAsk_QtM)

        self.uc6_bidO_single_proxy = QSortFilterProxyModel(self)
        self.uc6_bidO_single_proxy.setSourceModel(self.orders.ordersBid_QtM)

        QObject.connect(self.nxtApi, SIGNAL("getAskOrderIds_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getAskOrderIds_fromApi)
        QObject.connect(self.nxtApi, SIGNAL("getBidOrderIds_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getBidOrderIds_fromApi)

        QObject.connect(self.nxtApi, SIGNAL("getAskOrder_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getAskOrder_fromApi)
        QObject.connect(self.nxtApi, SIGNAL("getBidOrder_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getBidOrder_fromApi)


    def getOrders(self, assetID):
        self.assetID = assetID
        self.meta['usedFor'] = 'getOrderIds'
        self.apiReq_getBidOrderIds['asset'] = self.assetID
        self.nxtApi.getBidOrderIds_Slot( self.apiReq_getBidOrderIds , self.meta)
        self.apiReq_getAskOrderIds['asset'] = self.assetID
        self.nxtApi.getAskOrderIds_Slot( self.apiReq_getAskOrderIds , self.meta)

    def getAskOrder(self,askO):
        self.meta['usedFor'] = 'getAskOrder'
        self.apiReq_getAskOrder['order'] = askO
        self.nxtApi.getAskOrder_Slot( self.apiReq_getAskOrder , self.meta)
    def getBidOrder(self, bidO):
        self.meta['usedFor'] = 'getBidOrder'
        self.apiReq_getBidOrder['order'] = bidO
        self.nxtApi.getBidOrder_Slot( self.apiReq_getBidOrder , self.meta)

    def getAskOrder_fromApi(self, reply, meta):
        # print("UCl459")
        self.orders.getAskOrder_uc6(reply, meta)

    def getBidOrder_fromApi(self, reply, meta):
        self.orders.getBidOrder_uc6(reply, meta) # <--- DIRECTLY INTO THE MODEL HERE!

    def getAskOrderIds_fromApi(self, reply, meta):
        askOrderIds=reply['askOrderIds']
        self.orders.ordersAsk_QtM.clear()
        for askO in askOrderIds:
            self.getAskOrder(askO)

    def getBidOrderIds_fromApi(self, reply, meta):
        bidOrderIds=reply['bidOrderIds']
        self.orders.ordersBid_QtM.clear()
        for bidO in bidOrderIds:
            self.getBidOrder(bidO)

    def getAllOpenOrders(self):
        pass




class UC7_ATX(nxtUseCaseMeta):

    def __init__(self, sessMan,):
        super(UC7_ATX   , self   ).__init__(sessMan)
        self.sessMan = sessMan
        self.meta={'caller':'uc7'}
        self.nxtApi = self.sessMan.nxtApi
        # todo: check : the TX instance may be overwritten when new TXs are sent too fast

    # AE TX creation
    # these functions are called to create TX instances

    # this is s.t. the resident account does
    def issueAsset(self, TXparms):
        self.TX = nxtMods.IssueAsset(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.issueAsset()
    def transferAsset(self, TXparms):
        self.TX = nxtMods.TransferAsset(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.transferAsset()

    def placeAskOrder(self, TXparms):
        self.TX = nxtMods.PlaceAskOrder(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.placeAskOrder() #make TX instance, rest is autonomous
    def placeBidOrder(self, TXparms):
        self.TX = nxtMods.PlaceBidOrder(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.placeBidOrder()
    def cancelAskOrder(self, TXparms):
        self.TX = nxtMods.CancelAskOrder(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.cancelAskOrder()
    def cancelBidOrder(self, TXparms):
        #print("cancel bid")
        self.TX = nxtMods.CancelBidOrder(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.cancelBidOrder()

    def sendMessage(self,TXparms):
        #print("cancel bid")
        self.TX = nxtMods.CancelBidOrder(self.sessMan, TX_ID=None, TXparms=TXparms, meta = self.meta )
        self.TX.cancelBidOrder() # etc





class UC8_Trades(nxtUseCaseMeta):



    def __init__(self, sessMan,):
        super(UC8_Trades   , self   ).__init__(sessMan)
        #self.apiCalls = nxtQs()
        self.sessMan = sessMan
        self.meta = {'caller':'UC8_Trades'}


        self.nxtApi = self.sessMan.nxtApi

        self.apiReq_getTrades = self.apiCalls.getTrades
        self.apiReq_getAllTrades = self.apiCalls.getAllTrades

        QObject.connect(self.nxtApi, SIGNAL("getTrades_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getTrades_fromApi)
        QObject.connect(self.nxtApi, SIGNAL("getAllTrades_Sig(PyQt_PyObject, PyQt_PyObject)"), self.getAllTrades_fromApi)


        self.trades = nxtMods.Trades(sessMan)

        self.uc8_allTrades_proxy = QSortFilterProxyModel(self)
        self.uc8_allTrades_proxy.setSourceModel(self.trades.tradesQtM)


    def getTrades(self, selAssetId, firstIndex, lastIndex):
        self.meta['usedFor'] = 'getTrades'
        #print("getTrades_fromApi: "  +  str(selAssetId) +" - " +  firstIndex + " - " + lastIndex)
        self.apiReq_getTrades['asset'] = selAssetId # )
        self.apiReq_getTrades['lastIndex'] = '' # lastIndex
        self.apiReq_getTrades['firstIndex'] = '' # firstIndex
        self.nxtApi.getTrades_Slot( self.apiReq_getTrades , self.meta)

    def getAllTrades_fromApi(self, reply, meta):
        #print("getTrades_fromApi ---- ")# +str(reply) + " - " + str(meta))
        pass

    def getTrades_fromApi(self, reply, meta):
        #print("getTrades_fromApi - " +str(reply) + " - " + str(meta))
        self.trades.enterTrades( reply, meta)









class UC9_MSGer_handler(nxtUseCaseMeta):

    def __init__(self, sessMan,  app,):
        super(UC9_MSG_handler   , self   ).__init__(sessMan)
        self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'UC9_MSG_handler'}

    # these functions are called to create TX instances
    def sendMessage(self):
        pass
    def createPoll(self):
        pass
    def castVote(self):
        pass


class UC_BlockchainTraversal(nxtUseCaseMeta):

    """- """

    def __init__(self, sessMan,  app):
        super(UC_BlockchainTraversal   , self   ).__init__(sessMan)
        self.apiCalls = nxtQs()
        self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'UC_BlockhainTraversal'}


class UC_shopKeeper(nxtUseCaseMeta):



    def __init__(self, sessMan,  app):
        super(UC_shopKeeper   , self   ).__init__(sessMan)
        self.apiCalls = nxtQs()
        self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'ucShopKeeper'}








#######################################################################
##############  
############## THIS IS A TEMPLATE FOR MAKING NEW USE CASES KEEP THIS HERE! 
##############                OLD TEMPLATE
#######################################################################

   
  
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
 
   
   
        
if __name__ == "__main__":
    import sys
    sys.path += [ os.path.dirname(os.path.dirname(os.path.realpath(__file__))) ]
    argv = sys.argv
    app = QtGui.QApplication(sys.argv) # creation of the app object
    done = app.exec_()
    sys.exit(done)
 
 
 
# 
## subclass QApplication and slap on whatever you want:
#class XCPApplication(QApplication):
#        """
#    A basic subclass of the QApplication object that provides us with some app-wide state
#    """
#    def __init__(self, *args, **kwargs):
#        super(XCPApplication, self).__init__(*args, **kwargs)
#        self.wallet = Wallet()
#        self.xcp_client = XCPAsyncAppClient()
#        self.btc_client = BTCAsyncAppClient()
#        self.LAST_BLOCK = None
#
#    def examine_local_wallet(self, after):
#        def cb(res):
#            self.wallet.update_addresses(res)
#            after()
#        self.btc_client.get_wallet_addresses(cb)
#
#    def fetch_initial_data(self, update_wallet_callback_func):
#        pass
#        
#   old docstring
# 1.) in WinCtrl.py
#
#     - register activator signal to be emitted from WinCtrl as:
#         UC_test1_activate = pyqtSignal(object)
#
#     - in WinCTrl __init__(), register sessMan:uc instance as:
#         self.app.sessMan.ucTest1.initWin6(self.app.nxtWin6, ui)
#
#     - connect activator widget in win to activator CB on Win as:
#         QtCore.QObject.connect(ui.pb_test1Start , SIGNAL("clicked()"), self.UC_test1_activateCB )
#
#     - in activator callback prepare signal and emit as:
#
#         def UC_test2_activateCB(self,):
#             do_something_Flash_a_LED_or_so()
#             self.emit( SIGNAL( "UC_test2_activate(PyQt_PyObject)"),  {'uc':'test2'} )    #
#
# 2.) in nxtSessionManager.py
#
#     - instantiate UC as:
#
#         self.ucTest1 = nxtUseCases.nxtUCTest1(self, self.app ) #
#         self.ucTest1.initSignals()
#
# 3.) in nxtUseCase.py
#
#     - construct UC class as per this example
#     - do what the use case is supposed to do



