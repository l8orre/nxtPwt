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

from requests import Request, Session
import time

import json
import requests  # can be dropped when seesion is ready,
from PyQt4.QtCore import   QObject , pyqtSignal, pyqtSlot, SIGNAL
from copy import copy
from PyQt4 import   QtGui
from PyQt4 import Qt,  QtCore
 

#from requests.auth import HTTPBasicAuth

  

class nxtApi(Qt.QObject):
    """ class to check state and emit signals when changes have occurred-   
            currently implementing ..

             broadcastTransaction
buyAlias
calculateFullHash
cancelAskOrder
cancelBidOrder
castVote
createPoll
decodeHallmark
decodeToken
decryptFrom
dgsDelisting
dgsDelivery
dgsFeedback
dgsListing
dgsPriceChange
dgsPurchase
dgsQuantityChange
dgsRefund
encryptTo
generateToken
getAccount
getAccountBlockIds
getAccountCurrentAskOrderIds
getAccountCurrentBidOrderIds
getAccountId
getAccountPublicKey
getAccountTransactionIds
getAlias
getAliases
getAllAssets
getAllOpenOrders
getAllTrades
getAskOrder
getAskOrderIds
getAskOrders
getAsset
getAssetIds
getAssets
getAssetsByIssuer
getBalance
getBidOrder
getBidOrderIds
getBidOrders
getBlock
getBlockId
getBlockchainStatus
getConstants
getDGSGood
getDGSGoods
getDGSPendingPurchases
getDGSPurchase
getDGSPurchases
getForging
getGuaranteedBalance
getMyInfo
getNextBlockGenerators
getPeer
getPeers
getPoll
getPollIds
getState
getTime
getTrades
getTransaction
getTransactionBytes
getUnconfirmedTransactionIds
getUnconfirmedTransactions
issueAsset
leaseBalance
markHost
parseTransaction
placeAskOrder
placeBidOrder
readEncryptedNote
rsConvert
sellAlias
sendEncryptedNote
sendMessage
sendMoney
setAccountInfo
setAlias
signTransaction
startForging
stopForging
transferAsset

            catchAll <-------#59
            """
                
    # these are the receiver slots from nxtBroker

    broadcastTransaction_Sig =  pyqtSignal(dict,dict)  #1

    buyAlias_Sig =  pyqtSignal(dict,dict)

    calculateFullHash_Sig =  pyqtSignal(dict,dict)

    cancelAskOrder_Sig =  pyqtSignal(dict,dict)

    cancelBidOrder_Sig =  pyqtSignal(dict,dict)

    castVote_Sig =  pyqtSignal(dict,dict)

    createPoll_Sig =  pyqtSignal(dict,dict)

    decodeHallmark_Sig =  pyqtSignal(dict,dict)

    decodeToken_Sig =  pyqtSignal(dict,dict)

    decryptFrom_Sig =  pyqtSignal(dict,dict) #10

    dgsDelisting_Sig =  pyqtSignal(dict,dict)

    dgsDelivery_Sig =  pyqtSignal(dict,dict)

    dgsFeedback_Sig =  pyqtSignal(dict,dict)

    dgsListing_Sig =  pyqtSignal(dict,dict)

    dgsPriceChange_Sig =  pyqtSignal(dict,dict)

    dgsPurchase_Sig =  pyqtSignal(dict,dict)

    dgsQuantityChange_Sig =  pyqtSignal(dict,dict)

    dgsRefund_Sig =  pyqtSignal(dict,dict)

    encryptTo_Sig =  pyqtSignal(dict,dict)

    generateToken_Sig =  pyqtSignal(dict,dict)  #20

    getAccount_Sig =  pyqtSignal(dict,dict)

    getAccountBlockIds_Sig =  pyqtSignal(dict,dict  )

    getAccountCurrentAskOrderIds_Sig =  pyqtSignal(dict,dict)

    getAccountCurrentBidOrderIds_Sig =  pyqtSignal(dict,dict)

    getAccountId_Sig =  pyqtSignal(dict,dict)

    getAccountPublicKey_Sig =  pyqtSignal(dict,dict)

    getAccountTransactionIds_Sig =  pyqtSignal(dict,dict)

    getAlias_Sig  =  pyqtSignal(dict,dict)

    getAliases_Sig  =  pyqtSignal(dict,dict)

    getAllAssets_Sig =  pyqtSignal(dict,dict)  # 30

    getAllOpenOrders_Sig =  pyqtSignal(dict,dict)

    getAllTrades_Sig =  pyqtSignal(dict,dict)

    getAskOrder_Sig =  pyqtSignal(dict,dict)

    getAskOrderIds_Sig =  pyqtSignal(dict,dict)

    getAskOrders_Sig =  pyqtSignal(dict,dict)

    getAsset_Sig  =  pyqtSignal(dict,dict)

    getAssetIds_Sig =  pyqtSignal(dict,dict)

    getAssets_Sig  =  pyqtSignal(dict,dict)

    getAssetsByIssuer_Sig  =  pyqtSignal(dict,dict)

    getBalance_Sig =  pyqtSignal(dict, dict)  # 40

    getBidOrder_Sig =  pyqtSignal(dict,dict)

    getBidOrderIds_Sig =  pyqtSignal(dict,dict)

    getBidOrders_Sig =  pyqtSignal(dict,dict)

    getBlock_Sig =  pyqtSignal(dict,dict)

    getBlockId_Sig =  pyqtSignal(dict,dict)

    getBlockchainStatus_Sig =  pyqtSignal(dict,dict)

    getConstants_Sig =  pyqtSignal(dict,dict)

    getDGSGood_Sig =  pyqtSignal(dict,dict)

    getDGSGoods_Sig =  pyqtSignal(dict,dict)

    getDGSPendingPurchases_Sig =  pyqtSignal(dict,dict) # 50

    getDGSPurchase_Sig =  pyqtSignal(dict,dict)

    getDGSPurchases_Sig =  pyqtSignal(dict,dict)

    getForging_Sig =  pyqtSignal(dict,dict)

    getGuaranteedBalance_Sig =  pyqtSignal(dict,dict)

    getMyInfo_Sig =  pyqtSignal(dict,dict)

    getNextBlockGenerators_Sig =  pyqtSignal(dict,dict)

    getPeer_Sig =  pyqtSignal(dict,dict)
    
    getPeers_Sig =  pyqtSignal(dict,dict)

    getPoll_Sig =  pyqtSignal(dict,dict)

    getPollIds_Sig =  pyqtSignal(dict,dict)  # 60

    getState_Sig =  pyqtSignal(dict,dict)

    getTime_Sig =  pyqtSignal(dict,dict)

    getTrades_Sig =  pyqtSignal(dict,dict)

    getTransaction_Sig =  pyqtSignal(dict,dict)

    getTransactionBytes_Sig =  pyqtSignal(dict,dict)

    getUnconfirmedTransactionIds_Sig =  pyqtSignal(dict,dict)

    getUnconfirmedTransactions_Sig =  pyqtSignal(dict,dict)

    issueAsset_Sig =  pyqtSignal(dict,dict)

    leaseBalance_Sig =  pyqtSignal(dict,dict)

    markHost_Sig =  pyqtSignal(dict,dict)  # 70

    parseTransaction_Sig =  pyqtSignal(dict,dict)

    readEncryptedNote_Sig =  pyqtSignal(dict,dict)

    rsConvert_Sig =  pyqtSignal(dict,dict)

    sellAlias_Sig =  pyqtSignal(dict,dict)

    sendEncryptedNote_Sig =  pyqtSignal(dict,dict)

    sendMessage_Sig =  pyqtSignal(dict,dict)

    sendMoney_Sig =  pyqtSignal(dict,dict)

    setAccountInfo_Sig =  pyqtSignal(dict,dict)

    setAlias_Sig =  pyqtSignal(dict,dict)

    signTransaction_Sig =  pyqtSignal(dict,dict)    #80

    startForging_Sig =  pyqtSignal(dict,dict)

    stopForging_Sig =  pyqtSignal(dict,dict)

    transferAsset_Sig=  pyqtSignal(dict,dict) #83

    catchAll_Sig =  pyqtSignal(dict, dict)



    # this signal is for maintenace access to the raw url string     
    queryURL_Sig = pyqtSignal(object, ) # it is emtitted before starting the QThread.

    connectChanged_Slot = pyqtSlot(object) # create a new session/request object

    ################################################################

    
    def __init__(self, sessMan ): #app
        
        super(nxtApi, self).__init__()
         
        self.sessMan = sessMan
        self.session = Session()
        
        self.session.verify = True #  False
        #self.session.cert = "./mycert.pkcs12"  #  
        
        self.conn={}

        #***************************        
        #self.lock = Qt.QReadWriteLock()
        #self.qLock = Qt.QMutex()
        #
        # MAYBE WITH LOCKS; WE WILL SEE!!!
        #**************
        self.qPool=QtCore.QThreadPool.globalInstance()
        self.qPool.setMaxThreadCount(2500) # robustness
        #self.qPool.activeThreadCount() this is how many we have running?!

    def initSignals(self):
        QObject.connect(self.sessMan, SIGNAL("NRSconnCHANGED_Sig(PyQt_PyObject)"), self.connectChanged_Slot) # sessMan: seesion management!
        self.makeConnection()

            #
    def makeConnection(self):
        #print(str(self.sessMan.activeNRS.comp['url']))
        sessUrl =  self.sessMan.activeNRS.comp['url']
        print(sessUrl)
        self.conn['url'] = sessUrl
        self.connectChanged_Slot(sessUrl) # now make one!
        #
    ###############################################
    #
    # this is for creating a new connection object when the server changes
    # 
    @pyqtSlot() #   UC29 maps here
    def connectChanged_Slot(self, newConn): # newConn ): # just fetch it directly from the sessMan data. no passing around. newConn):

        del self.session

        self.session = Session()
        self.session.verify = False # True #
        
        sessUrl =  self.sessMan.activeNRS.comp['url']
        #print("sessUrl -  "+ str(sessUrl))
        
        #        auth = requests.auth.HTTPBasicAuth('','') # 'rpcuser',  'xcppw1234')
        headers = {'content-type': 'application/json'}
        # self.req = Request( method='GET', url = sessUrl, params = {})
        #self.conn['url'] = sessUrl
        self.req = Request( method='POST', url = sessUrl, params = {}, headers = headers,       )
        
        self.conn['changed'] = 'test1'
        meta =  {'newConn':sessUrl} # not really needed, but must comply with format of Sig
        self.catchAll_Sig.emit(self.conn, meta) #  

        #self.session = requests.session()
        #        self.session.mount('http://', requests.adapters.HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize))
        #        self.session.mount('https://', requests.adapters.HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize))
        #
        # ToDo : https & POST
        # THIS COMMENT MAY EXPLAIN HOW TO USE HTTPS AND POST!!!

        #
        #I've figured out the issue to my problem. I am sending the self.user_agent to the remote host when I connect via the proxy for the first time, which interferes with the SSL Handshake.
        #
        #To solve this, I put an initial self.request.recv() in the def setup(self) function before I call ssl.wrap_socket on the socket.
        #
        #Traceback (most recent call last):
        #  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 319, in send
        #    timeout=timeout
        #  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 575, in urlopen
        #    raise SSLError(e)
        #urllib3.exceptions.SSLError: EOF occurred in violation of protocol (_ssl.c:548)


    ########################################################
    #
    # regular api calls
        #
        #
        #
        #




    @pyqtSlot() # 24
    def broadcastTransaction_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.broadcastTransaction_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def buyAlias_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.buyAlias_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def calculateFullHash_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.calculateFullHash_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def cancelAskOrder_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.cancelAskOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 32
    def cancelBidOrder_Slot(self,apiReq, meta = {}): ##
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.cancelBidOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 49
    def castVote_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.castVote_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()#50
    def createPoll_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.createPoll_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 15
    def decodeHallmark_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.decodeHallmark_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 17
    def decodeToken_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.decodeToken_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def decryptFrom_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.decryptFrom_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsDelisting_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsDelisting_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsDelivery_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsDelivery_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsFeedback_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsFeedback_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsListing_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsListing_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsPriceChange_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsPriceChange_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsPurchase_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsPurchase_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsQuantityChange_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsQuantityChange_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def dgsRefund_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsRefund_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def encryptTo_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.encryptTo_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 46
    def generateToken_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.generateToken_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 42
    def getAccount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccount_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 2
    def getAccountBlockIds_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountBlockIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 39
    def getAccountCurrentBidOrderIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrentBidOrderIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 40
    def getAccountCurrentAskOrderIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrentAskOrderIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 1
    def getAccountId_Slot(self, apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountId_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 4 
    def getAccountPublicKey_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountPublicKey_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 23
    def getAccountTransactionIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountTransactionIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() #51
    def getAlias_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAlias_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getAliases_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAliases_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 60
    def getAllAssets_Slot(self,apiReq, meta = {}):
        """ - """
        print(str(self))
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllAssets_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() #52
    def getAllOpenOrders_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllOpenOrders_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 55
    def getAllTrades_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllTrades_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 27
    def getAskOrder_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAskOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 28
    def getAskOrderIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAskOrderIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getAskOrders_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAskOrders_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 35
    def getAsset_Slot(self, apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAsset_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 36
    def getAssetIds_Slot(self,apiReq, meta = {}):
        """ connect this slot directly to QTimer signal! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 61
    def getAssets_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssets_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getAssetsByIssuer_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetsByIssuer_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 3  <<<<<<<<<<<<<<--------------------
    def getBalance_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBalance_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 29
    def getBidOrder_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBidOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 30
    def getBidOrderIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBidOrderIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getBidOrders_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBidOrders_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 10
    def getBlock_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBlock_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 31
    def getBlockId_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBlockId_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getBlockchainStatus_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBlockchainStatus_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 7
    def getConstants_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getConstants_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSGood_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSGood_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSGoods_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSGoods_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSPendingPurchases_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSPendingPurchases_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSPurchase_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSPurchase_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSPurchases_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSPurchases_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 54
    def getForging_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getForging_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 5
    def getGuaranteedBalance_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getGuaranteedBalance_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 8
    def getMyInfo_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getMyInfo_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getNextBlockGenerators_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getNextBlockGenerators_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 11
    def getPeer_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getPeer_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 12
    def getPeers_Slot(self, apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getPeers_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 48
    def getPoll_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getPoll_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 47
    def getPollIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getPollIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 9
    def getState_Slot(self,  apiReq, meta = {}):
        """ - """
        ##################################
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getState_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 13 
    def getTime_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getTime_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 43
    def getTrades_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getTrades_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 26
    def getTransaction_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getTransaction_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 41
    def getTransactionBytes_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getTransactionBytes_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 25
    def getUnconfirmedTransactionIds_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getUnconfirmedTransactionIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getUnconfirmedTransactions_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getUnconfirmedTransactions_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 37
    def issueAsset_Slot(self, apiReq, meta = {}): #is directly hit from the UseCase with the full dict
        """   """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.issueAsset_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 57
    def leaseBalance_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.leaseBalance_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 14 
    def markHost_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.markHost_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 58
    def parseTransaction_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.parseTransaction_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 33
    def placeAskOrder_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.placeAskOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 34
    def placeBidOrder_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.placeBidOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def readEncryptedNote_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.readEncryptedNote_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def rsConvert_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.rsConvert_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def sellAlias_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.sellAlias_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def sendEncryptedNote_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.sendEncryptedNote_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 18
    def sendMessage_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.sendMessage_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 16
    def sendMoney_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.sendMoney_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 56
    def setAccountInfo_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.setAccountInfo_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def setAlias_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.setAlias_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 59
    def signTransaction_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.signTransaction_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 44
    def startForging_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.startForging_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 45
    def stopForging_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.stopForging_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 38
    def transferAsset_Slot(self,apiReq, meta = {}):
        """   """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.transferAsset_Sig)
        self.qPool.start(self.replyFetcher)



    ###########
    ###########
    ###########
    
    @pyqtSlot() # 62
    def catchAll_Slot( self,apiReq, meta = {}): # this catches everything that is thrown at it, but returns as unspecific!
        """ - """
        #print("CATCHALL")        
        #print(str(self)) # <nxtBridge.nxtApiSigs.nxtApi object at 0x7fc1ee7ad168>

        #print(str(apiReq))
        
        self.req.params=apiReq # same obj, only replace params
        #print(str(apiReq))
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.catchAll_Sig)
        self.qPool.start(self.replyFetcher)


###################################################################
#
# threading requests

class ReplyEmitter(QObject):
    """ - this is needed in QRunnable, because QRunnable is NOT able to emit signals. But this is. """    

    NRSREPLY = pyqtSignal(object  ,object) #  object1 is the request, object2 can carry meta data for use case logic 

    def __init__(self, session, preppedReq , meta  = {}): # meta is organizational meta data that client can use
        super(QObject, self, ).__init__()
        self.preppedReq = preppedReq 
        self.session = session
        metaThread = copy(meta)
        # NOTE: This MUST be done, otherwise the 'meta' object will only be ONE meta object (from the last query)
        # that is referenced for EVERY query and the metaData of the earlier queries will be destroyed!!!!!!!!        
        del meta
        self.metaThread = metaThread
         
class ReplyFetcher(QtCore.QRunnable):
    """- This is what needs to be put into the QThreadpool """
    
    def __init__(self, emitter,  ):
        super(QtCore.QRunnable, self).__init__()
        self.emitter = emitter

    def run(self,):

        try:
                        #print("sleep WITH DELAY- now! " +str(time.time())+ " - " +  self.emitter.metaThread['queryNum'])
            time.sleep(0.1 * self.emitter.metaThread['qqLen']) # THIS IS TO PROTECT THE SERVER FROM dropping fast requests
                         # AND CAN ALSO BE USED FOR LOAD TESTING  #print("wake - now! "+str(time.time()))

        except:
            pass # no QueryQueueLength -> just go ahead time.sleep(0.001) #pass

        try:
            resp = self.emitter.session.send(self.emitter.preppedReq)

        except Exception as inst:
            print(str(self.emitter.preppedReq.url) + " sent")
            print(str(inst))
            resp={'apiError': str(inst)}
            print("please get loggers for this!\n\n\n\n")

        try:
            resp=resp.json()
        except:
            respSTR = str(resp)
            print(respSTR)
        #self.emitter.meta['timestamp2']=str(time.time())      
        print("\n\n##api returns: " + str(resp) + " -\n " + str(self.emitter.metaThread)) # CAN BE USEFULEFOR DEBUGGING
        self.emitter.emit(SIGNAL( "NRSREPLY(PyQt_PyObject, PyQt_PyObject )" ), resp, self.emitter.metaThread )  
############################################################## 
 





    
if __name__ == "__main__":
    import sys
    sys.path += [ os.path.dirname(os.path.dirname(os.path.realpath(__file__))) ]
    argv = sys.argv
    app = QtGui.QApplication(sys.argv) # creation of the app object
    # here is the earliest we could plug any backend classes into app
    nxtQueryTest = nxtQuery({},app)    
    #main = MainApplication(app)
    #main.openMainWindow()
    nxtQueryTest.stateChanged.connect( Test )
    nxtQueryTest.emitter()
    done = app.exec_()
    sys.exit(done)
 
 
 
 
 
 
  