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
            
            getAccountId 1
            getAccountBlockIds
            getBalance
            getAccountPublicKey
            getGuaranteedBalance
            getAliasId 
            getConstants
            getMyInfo
            getState
            getBlock
            getPeer
            getPeers
            getTime
            markHost
            decodeHallmark
            sendMoney
            decodeToken
            sendMessage
            getAliasIds
            getAliasURI
            listAccountAliases
            assignAlias
            getAccountTransactionIds
            broadcastTransaction
            getUnconfirmedTransactionIds
            getTransaction
            getAskOrder
            getAskOrderIds
            getBidOrder
            getBidOrderIds
            cancelAskOrder
            cancelBidOrder
            placeAskOrder
            placeBidOrder
            getAsset 
            getAssetIds
            issueAsset
            transferAsset
            getAccountCurrentBidOrderIds
            getAccountCurrentAskOrderIds
            getTransactionBytes
            getAccount
            getTrades 43 
            startForging
            stopForging
            generateToken
            getPollIds
            getPoll
            castVote
            createPoll
            getAlias
            getAllOpenOrders
            getAssetsByName
            getForging
            getAllTrades
            setAccountInfo
            leaseBalance   <- 57
            parseTransaction 58
            catchAll <-------#59
            """
                
    # these are the receiver slots from nxtBroker
    getAccountId_Sig =  pyqtSignal(dict,dict)  #1
    
    getAccountBlockIds_Sig =  pyqtSignal(dict,dict  )  #2
    
    getBalance_Sig =  pyqtSignal(dict, dict)  #3 #  
    
    getAccountPublicKey_Sig =  pyqtSignal(dict,dict)  #4
    
    getGuaranteedBalance_Sig =  pyqtSignal(dict,dict)  #5
    
    getAliasId_Sig  =  pyqtSignal(dict,dict)  #6
    
    getConstants_Sig =  pyqtSignal(dict,dict)  #7
    
    getMyInfo_Sig =  pyqtSignal(dict,dict)  #8
    
    getState_Sig =  pyqtSignal(dict,dict)  #9 PyQt_PyObject
    
    getBlock_Sig =  pyqtSignal(dict,dict)  #10
    
    getPeer_Sig =  pyqtSignal(dict,dict)  #11
    
    getPeers_Sig =  pyqtSignal(dict,dict)  #12
    
    getTime_Sig =  pyqtSignal(dict,dict)  #13
    
    markHost_Sig =  pyqtSignal(dict,dict)  #14
    
    decodeHallmark_Sig =  pyqtSignal(dict,dict)  #15
    
    sendMoney_Sig =  pyqtSignal(dict,dict)  #16
    
    decodeToken_Sig =  pyqtSignal(dict,dict)  #17
    
    sendMessage_Sig =  pyqtSignal(dict,dict)  #18
    
    getAliasIds_Sig =  pyqtSignal(dict,dict)  #19
    
    getAliasURI_Sig =  pyqtSignal(dict,dict)  #20
    
    listAccountAliases_Sig =  pyqtSignal(dict,dict)  #21
    
    assignAlias_Sig =  pyqtSignal(dict,dict)  #22
    
    getAccountTransactionIds_Sig =  pyqtSignal(dict,dict)  #23
    
    broadcastTransaction_Sig =  pyqtSignal(dict,dict)  #24
    
    getUnconfirmedTransactionIds_Sig =  pyqtSignal(dict,dict)  #25
    
    getTransaction_Sig =  pyqtSignal(dict,dict)  #26
    
    getAskOrder_Sig =  pyqtSignal(dict,dict)  #27
    
    getAskOrderIds_Sig =  pyqtSignal(dict,dict)  #28
    
    getBidOrder_Sig =  pyqtSignal(dict,dict)  #29
    
    getBidOrderIds_Sig =  pyqtSignal(dict,dict)  #30
    
    cancelAskOrder_Sig =  pyqtSignal(dict,dict)  #31
    
    cancelBidOrder_Sig =  pyqtSignal(dict,dict)  #32
    
    placeAskOrder_Sig =  pyqtSignal(dict,dict)  #33
    
    placeBidOrder_Sig =  pyqtSignal(dict,dict)  #34
    
    getAsset_Sig  =  pyqtSignal(dict,dict)  #35
    
    getAssetIds_Sig =  pyqtSignal(dict,dict)  #36
    
    issueAsset_Sig =  pyqtSignal(dict,dict)  #37
    
    transferAsset_Sig=  pyqtSignal(dict,dict)  #38
    
    getAccountCurrentBidOrderIds_Sig =  pyqtSignal(dict,dict)  #39
    
    getAccountCurrentAskOrderIds_Sig =  pyqtSignal(dict,dict)  #40
    
    getTransactionBytes_Sig =  pyqtSignal(dict,dict)  #41
     
    getAccount_Sig =  pyqtSignal(dict,dict)  #42
    
    getTrades_Sig =  pyqtSignal(dict,dict)  #43
    
    startForging_Sig =  pyqtSignal(dict,dict)  #44
    
    stopForging_Sig =  pyqtSignal(dict,dict)  #45
    
    generateToken_Sig =  pyqtSignal(dict,dict)  #46
    
    getPollIds_Sig =  pyqtSignal(dict,dict)  #47
    
    getPoll_Sig =  pyqtSignal(dict,dict)  #48
    
    castVote_Sig =  pyqtSignal(dict,dict)  #49

    createPoll_Sig =  pyqtSignal(dict,dict)  #50

    getAlias_Sig =  pyqtSignal(dict,dict)  #51

    getAllOpenOrders_Sig =  pyqtSignal(dict,dict)  #52

    getAssetsByName_Sig =  pyqtSignal(dict,dict)  #53

    getForging_Sig =  pyqtSignal(dict,dict)  #54

    getAllTrades_Sig =  pyqtSignal(dict,dict)  #55

    setAccountInfo_Sig =  pyqtSignal(dict,dict)  #56

    leaseBalance_Sig =  pyqtSignal(dict,dict)  #57

    signTransaction_Sig =  pyqtSignal(dict,dict)  #58

    getAllAssets_Sig =  pyqtSignal(dict,dict)  #59

    getAssets_Sig =  pyqtSignal(dict,dict)  #60

    
    catchAll_Sig =  pyqtSignal(dict, dict)  #61





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
         
    @pyqtSlot() # 6 
    def getAliasId_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAliasId_Sig)
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
          
          
    @pyqtSlot() # 9 999999999999999999999999999999999999999999999999999
    def getState_Slot(self,  apiReq, meta = {}):
        """ - """
        #print('"HHHHHHHHHH"HHHHHHHHHHHHHHHHHHHHHH')
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getState_Sig)
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
        #print(str(type(self)))

        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getPeers_Sig)
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
         
    @pyqtSlot() # 19 
    def getAliasIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAliasIds_Sig)
        self.qPool.start(self.replyFetcher)
         
    @pyqtSlot() # 20 
    def getAliasURI_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAliasURI_Sig)
        self.qPool.start(self.replyFetcher)
         
    @pyqtSlot() # 21 
    def listAccountAliases_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.listAccountAliases_Sig)
        self.qPool.start(self.replyFetcher)
         
    @pyqtSlot() # 22
    def assignAlias_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.assignAlias_Sig)
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
          
    ## new 040614

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


    @pyqtSlot() # 53
    def getAssetsByName_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.

        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time

        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetsByName_Sig)
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

################




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
 
     
#
#    @pyqtSlot() # 62
#    def catchAll_Slot(self, apiReq, meta = {}): # this catches everything that is thrown at it, but returns as unspecific!
#        """ - """
#         
#        self.req.params=apiReq # same obj, only replace params
#         
#        preppedReq = self.req.prepare()
#        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
#
#        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
#
#        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
#        self.replyFetcher = ReplyFetcher( replyEmitter, )
#        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.catchAll_Sig)
#        self.qPool.start(self.replyFetcher)
# 

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
 
 
 
 
 
 
  