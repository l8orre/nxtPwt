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

from PyQt4.QtCore import   QObject , pyqtSignal, pyqtSlot, SIGNAL
from copy import copy
from PyQt4 import   QtGui
from PyQt4 import Qt,  QtCore
import os

#import logging as lg


class nxtApi(Qt.QObject):
    """ class to check state and emit signals when changes have occurred-
            currently implementing ..

enter new calls:
1 here for documentation
2 add signal here:  broadcastTransaction_Sig =  pyqtSignal(dict,dict)  #1
3 add decorator here
4 add prototype

# these calls updated up tp 1.4.12



    addPeer_Sig =  pyqtSignal(dict,dict)

    blacklistPeer_Sig =  pyqtSignal(dict,dict)

broadcastTransaction
buyAlias
calculateFullHash
cancelAskOrder
cancelBidOrder
    cancelDeleteCurrency_Sig =  pyqtSignal(dict,dict)

castVote
createPoll
    currencyBuy_Sig =  pyqtSignal(dict,dict)

    currencyMint_Sig =  pyqtSignal(dict,dict)

    currencyReserveClaim_Sig =  pyqtSignal(dict,dict)

    currencyReserveIncrease_Sig =  pyqtSignal(dict,dict)

    currencySell_Sig =  pyqtSignal(dict,dict)

decodeHallmark
decodeToken

    deleteAlias_Sig =  pyqtSignal(dict,dict)

decryptFrom
    deleteCurrency_Sig =  pyqtSignal(dict,dict)

dgsDelisting
dgsDelivery
dgsFeedback
dgsListing
dgsPriceChange
dgsPurchase
dgsQuantityChange
dgsRefund
    dividendPayment_Sig =  pyqtSignal(dict,dict)

encryptTo
generateToken
getAccount

getAccountAssets *NEW 1


getAccountAssetCount *NEW 2


getAccountBlockCount  *NEW 3

getAccountBlockIds
    getAccountCurrencies_Sig =  pyqtSignal(dict,dict)

    getAccountCurrencyCount_Sig =  pyqtSignal(dict,dict)

    getAccountExchangeRequests_Sig =  pyqtSignal(dict,dict)
getAccountCurrentAskOrderIds
getAccountCurrentBidOrderIds
getAccountId
getAccountPublicKey
getAccountTransactionIds
getAlias
getAliases

getAliasCount,  *NEW 4


getAllAssets
    getAllCurrencies_Sig =  pyqtSignal(dict,dict)

    getAllExchanges_Sig =  pyqtSignal(dict,dict)

getAllOpenOrders
getAllTrades
getAskOrder
getAskOrderIds
getAskOrders
getAsset
getAssetIds
getAssets


getAssetAccountCount

getAssetsByIssuer
getBalance
getBidOrder
getBidOrderIds
getBidOrders
getBlock
getBlockId
getBlockchainStatus
    getBuyOffers_Sig

getConstants

    getCurrencies_Sig =  pyqtSignal(dict,dict)

    getCurrenciesByIssuer_Sig =  pyqtSignal(dict,dict)

    getCurrency_Sig =  pyqtSignal(dict,dict)

    getCurrencyAccountCount_Sig =  pyqtSignal(dict,dict)

    getCurrencyAccounts_Sig =  pyqtSignal(dict,dict)

    getCurrencyFounders_Sig =  pyqtSignal(dict,dict)

    getCurrencyIds_Sig =  pyqtSignal(dict,dict)

    getCurrencyTransfers_Sig =  pyqtSignal(dict,dict)

getDGSGood


getDGSGoods


getDGSGoodsCount,

getDGSGoodsPurchase

getDGSGoodsPurchaseCount,

getDGSPurchaseCount

getDGSTags


    getDGSTagCount_Sig =  pyqtSignal(dict,dict)

getECBlock
    getExchanges_Sig =  pyqtSignal(dict,dict)

    getExchangesByExchangeRequest_Sig =  pyqtSignal(dict,dict)

    getExchangesByOffer_Sig =  pyqtSignal(dict,dict)

getForging
getGuaranteedBalance
    getMintingTarget_Sig =  pyqtSignal(dict,dict)

getMyInfo
getNextBlockGenerators
getPeer
getPeers
    getOffer_Sig =  pyqtSignal(dict,dict)

getPoll
getPollIds
    getSellOffers_Sig =  pyqtSignal(dict,dict)

getState
getTime
getTrades
getTransaction
getTransactionBytes
getUnconfirmedTransactionIds
getUnconfirmedTransactions
issueAsset
    issueCurrency_Sig =  pyqtSignal(dict,dict)

leaseBalance
markHost
parseTransaction
placeAskOrder
placeBidOrder
    publishExchangeOffer_Sig =  pyqtSignal(dict,dict)

readEncryptedNote
rsConvert

searchAssets


    searchCurrencies_Sig =  pyqtSignal(dict,dict)

searchDGSGoods
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

    transferCurrency_Sig =  pyqtSignal(dict,dict)

            catchAll <-------
            """

    # these are the receiver slots from nxtBroker



    addPeer_Sig =  pyqtSignal(dict,dict)

    blacklistPeer_Sig =  pyqtSignal(dict,dict)

    deleteAlias_Sig =  pyqtSignal(dict,dict)

    dividendPayment_Sig =  pyqtSignal(dict,dict)

    getDGSTagCount_Sig =  pyqtSignal(dict,dict)

    cancelDeleteCurrency_Sig =  pyqtSignal(dict,dict)

    currencyBuy_Sig =  pyqtSignal(dict,dict)

    currencyMint_Sig =  pyqtSignal(dict,dict)

    currencyReserveClaim_Sig =  pyqtSignal(dict,dict)

    currencyReserveIncrease_Sig =  pyqtSignal(dict,dict)

    currencySell_Sig =  pyqtSignal(dict,dict)

    deleteCurrency_Sig =  pyqtSignal(dict,dict)

    getAccountCurrencies_Sig =  pyqtSignal(dict,dict)

    getAccountCurrencyCount_Sig =  pyqtSignal(dict,dict)

    getAccountExchangeRequests_Sig =  pyqtSignal(dict,dict)

    getAllCurrencies_Sig =  pyqtSignal(dict,dict)

    getAllExchanges_Sig =  pyqtSignal(dict,dict)

    getBuyOffers_Sig =  pyqtSignal(dict,dict)

    getCurrencies_Sig =  pyqtSignal(dict,dict)

    getCurrenciesByIssuer_Sig =  pyqtSignal(dict,dict)

    getCurrency_Sig =  pyqtSignal(dict,dict)

    getCurrencyAccountCount_Sig =  pyqtSignal(dict,dict)

    getCurrencyAccounts_Sig =  pyqtSignal(dict,dict)

    getCurrencyFounders_Sig =  pyqtSignal(dict,dict)

    getCurrencyIds_Sig =  pyqtSignal(dict,dict)

    getCurrencyTransfers_Sig =  pyqtSignal(dict,dict)

    getExchanges_Sig =  pyqtSignal(dict,dict)

    getExchangesByExchangeRequest_Sig =  pyqtSignal(dict,dict)

    getExchangesByOffer_Sig =  pyqtSignal(dict,dict)

    getMintingTarget_Sig =  pyqtSignal(dict,dict)

    getOffer_Sig =  pyqtSignal(dict,dict)

    getSellOffers_Sig =  pyqtSignal(dict,dict)

    issueCurrency_Sig =  pyqtSignal(dict,dict)

    publishExchangeOffer_Sig =  pyqtSignal(dict,dict)

    searchCurrencies_Sig =  pyqtSignal(dict,dict)

    transferCurrency_Sig =  pyqtSignal(dict,dict)

    deleteAlias_Sig =  pyqtSignal(dict,dict)

    dividendPayment_Sig =  pyqtSignal(dict,dict)

    getDGSTagCount_Sig =  pyqtSignal(dict,dict)

    broadcastTransaction_Sig =  pyqtSignal(dict,dict)

    buyAlias_Sig =  pyqtSignal(dict,dict)

    calculateFullHash_Sig =  pyqtSignal(dict,dict)

    cancelAskOrder_Sig =  pyqtSignal(dict,dict)

    cancelBidOrder_Sig =  pyqtSignal(dict,dict)

    castVote_Sig =  pyqtSignal(dict,dict)

    clearUnconfirmedTransactions_Sig =  pyqtSignal(dict,dict) # DEBUG API!!!

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

    fullReset_Sig =  pyqtSignal(dict,dict)  #20 # DEBUG API!!!

    getAccount_Sig =  pyqtSignal(dict,dict)

    getAccountAssets_Sig =  pyqtSignal(dict,dict)  #20 *NEW

    getAccountAssetCount_Sig =  pyqtSignal(dict,dict)  #20 # DEBUG API!!! *NEW

    getAccountBlockCount =  pyqtSignal(dict,dict) #*NEW

    getAccountBlockIds_Sig =  pyqtSignal(dict,dict  )

    getAccountBlocks_Sig =  pyqtSignal(dict,dict  ) # nxt130

    getAccountCurrentAskOrderIds_Sig =  pyqtSignal(dict,dict)

    getAccountCurrentAskOrders_Sig =  pyqtSignal(dict,dict)

    getAccountCurrentBidOrderIds_Sig =  pyqtSignal(dict,dict)

    getAccountLessors_Sig =  pyqtSignal(dict,dict)

    getAccountCurrentBidOrders_Sig =  pyqtSignal(dict,dict)

    getAccountId_Sig =  pyqtSignal(dict,dict)

    getAccountPublicKey_Sig =  pyqtSignal(dict,dict)

    getAccountTransactionIds_Sig =  pyqtSignal(dict,dict)

    getAccountTransactions_Sig =  pyqtSignal(dict,dict)

    getAlias_Sig  =  pyqtSignal(dict,dict)

    getAliases_Sig  =  pyqtSignal(dict,dict)

    getAliasCount_Sig  =  pyqtSignal(dict,dict) # *NEW

    getAllAssets_Sig =  pyqtSignal(dict,dict)  # 30

    getAllOpenAskOrders_Sig =  pyqtSignal(dict,dict)

    getAllOpenBidOrders_Sig =  pyqtSignal(dict,dict)

    getAllTrades_Sig =  pyqtSignal(dict,dict)

    getAskOrder_Sig =  pyqtSignal(dict,dict)

    getAskOrderIds_Sig =  pyqtSignal(dict,dict)

    getAskOrders_Sig =  pyqtSignal(dict,dict)

    getAsset_Sig  =  pyqtSignal(dict,dict)

    getAssetAccounts_Sig  =  pyqtSignal(dict,dict)

    getAssetIds_Sig =  pyqtSignal(dict,dict)

    getAssetTransfers_Sig =  pyqtSignal(dict,dict)

    getAssets_Sig  =  pyqtSignal(dict,dict)

    getAssetAccountCount_Sig  =  pyqtSignal(dict,dict)#  *NEW

    getAssetsByIssuer_Sig  =  pyqtSignal(dict,dict)

    getBalance_Sig =  pyqtSignal(dict, dict)  # 40

    getBidOrder_Sig =  pyqtSignal(dict,dict)

    getBidOrderIds_Sig =  pyqtSignal(dict,dict)

    getBidOrders_Sig =  pyqtSignal(dict,dict)

    getBlock_Sig =  pyqtSignal(dict,dict)

    getBlocks_Sig =  pyqtSignal(dict,dict)

    getBlockId_Sig =  pyqtSignal(dict,dict)

    getBlockchainStatus_Sig =  pyqtSignal(dict,dict)

    getConstants_Sig =  pyqtSignal(dict,dict)

    getDGSGood_Sig =  pyqtSignal(dict,dict)

    getDGSGoods_Sig =  pyqtSignal(dict,dict)

    getDGSGoodsCount_Sig =  pyqtSignal(dict,dict) # NEW

    getDGSGoodsPurchases_Sig =  pyqtSignal(dict,dict) # NEW

    getDGSGoodsPurchaseCount_Sig =  pyqtSignal(dict,dict) # NEW

    getDGSPendingPurchases_Sig =  pyqtSignal(dict,dict) # 50

    getDGSPurchase_Sig =  pyqtSignal(dict,dict)

    getDGSPurchaseCount_Sig =  pyqtSignal(dict,dict)#  *NEW

    getDGSPurchases_Sig =  pyqtSignal(dict,dict)

    getDGSTags_Sig =  pyqtSignal(dict,dict) # *NEW

    getECBlock_Sig =  pyqtSignal(dict,dict)

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

    getTX_Sig =  pyqtSignal(dict,dict)

    getTransactionBytes_Sig =  pyqtSignal(dict,dict)

    getUnconfirmedTransactionIds_Sig =  pyqtSignal(dict,dict)

    getUnconfirmedTransactions_Sig =  pyqtSignal(dict,dict)

    issueAsset_Sig =  pyqtSignal(dict,dict)

    leaseBalance_Sig =  pyqtSignal(dict,dict)

    longConvert_Sig =  pyqtSignal(dict,dict)

    markHost_Sig =  pyqtSignal(dict,dict)  # 70

    parseTransaction_Sig =  pyqtSignal(dict,dict)

    placeAskOrder_Sig =  pyqtSignal(dict,dict)

    placeBidOrdere_Sig =  pyqtSignal(dict,dict)

    popOff_Sig =  pyqtSignal(dict,dict)

    readMessage_Sig =  pyqtSignal(dict,dict)

    rsConvert_Sig =  pyqtSignal(dict,dict)

    searchAssets_Sig =  pyqtSignal(dict,dict) # NEW

    searchDGSGoods_Sig =  pyqtSignal(dict,dict) # NEW

    scan_Sig =  pyqtSignal(dict,dict)

    sellAlias_Sig =  pyqtSignal(dict,dict)

    sendMessage_Sig =  pyqtSignal(dict,dict)

    sendMoney_Sig =  pyqtSignal(dict,dict)

    setAccountInfo_Sig =  pyqtSignal(dict,dict)    #80

    setAlias_Sig =  pyqtSignal(dict,dict)

    signTransaction_Sig =  pyqtSignal(dict,dict)

    startForging_Sig =  pyqtSignal(dict,dict)

    stopForging_Sig =  pyqtSignal(dict,dict)

    transferAsset_Sig=  pyqtSignal(dict,dict) #85

    catchAll_Sig =  pyqtSignal(dict, dict)



    # this signal is for maintenace access to the raw url string
    queryURL_Sig = pyqtSignal(object, ) # it is emtitted before starting the QThread.

    connectChanged_Slot = pyqtSlot(object) # create a new session/request object

    ################################################################


    def __init__(self, sessMan,   logger1=None ):

        super(nxtApi, self).__init__()

        self.sessMan = sessMan
        self.session = Session()
        #

        self.apiLogger = logger1


        self.session.verify = True #
        #self.session.cert = "./mycert.pkcs12"

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

    def initSignals(self, NXXconn):

        QObject.connect(self.sessMan, SIGNAL("NRSconnCHANGED_Sig(PyQt_PyObject)"), self.connectChanged_Slot) # sessMan: seesion management!
        self.sessUrl = NXXconn.comp['url']
        self.makeConnection()

            #
    def makeConnection(self):

        self.conn['url'] = self.sessUrl
        self.connectChanged_Slot()   # now make one!

        #
    ###############################################
    #
    # this is for creating a new connection object when the server changes
    #
    @pyqtSlot() #   UC29 maps here
    def connectChanged_Slot(self, ):
        # THIS WON'T work in the present from!!
        del self.session

        self.session = Session()
        self.session.verify = False # True #
        #        auth = requests.auth.HTTPBasicAuth('','') # 'rpcuser',  'xcppw1234')
        headers = {'content-type': 'application/json'}

        self.req = Request( method='POST', url = self.sessUrl, params = {}, headers = headers,       )

        self.conn['changed'] = 'test1'
        meta =  {'newConn':self.sessUrl} # not really needed, but must comply with format of Sig
        self.catchAll_Sig.emit(self.conn, meta) #

        #self.apiLogger.info('nxtApi init - : %s ', str(self) )
        #self.apiLogger.info('nxtApi init - : %s ', str(self.__dict__) )
        #self.apiLogger.info('nxtApi init - : %s ', str(self.req.url) )
        #self.replyFetcher = ReplyFetcher( replyEmitter,    )   # replace this with the below
        #self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger   )


    ########################################################
    #
    # regular api calls
        #


#
#
# ################
#
#     @pyqtSlot()
#     def broadcastTransaction_Slot(self,apiReq, meta = {}):
#         """- """
#         self.req.params=apiReq # same obj, only replace params
#         preppedReq = self.req.prepare()
#         self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
#         meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
#         replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
#         self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
#         QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.broadcastTransaction_Sig)
#         self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def addPeer_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.addPeer_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def blacklistPeer_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.blacklistPeer_Sig)
        self.qPool.start(self.replyFetcher)




    @pyqtSlot()
    def broadcastTransaction_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.cancelBidOrder_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def cancelDeleteCurrency_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.cancelDeleteCurrency_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 49
    def castVote_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.castVote_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 49 # DEBUG API!!!
    def clearUnconfirmedTransactions_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.clearUnconfirmedTransactions_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()#50
    def createPoll_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.createPoll_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def currencyBuy_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.currencyBuy_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def currencyMint_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.currencyMint_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def currencyReserveClaim_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.currencyReserveClaim_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def currencyReserveIncrease_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.currencyReserveIncrease_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def currencySell_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.currencySell_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 15
    def decodeHallmark_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.decodeToken_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def deleteAlias_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.deleteAlias_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def deleteCurrency_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.deleteCurrency_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 31
    def decryptFrom_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dgsRefund_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def dividendPayment_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.dividendPayment_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def encryptTo_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.encryptTo_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 31
    def fullReset_Slot(self,apiReq, meta = {}): # DEBUG API !!!
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.fullReset_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 46
    def generateToken_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccount_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() #
    def getAccountAssets_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountAssets_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() #
    def getAccountAssetCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountAssetCount_Sig)
        self.qPool.start(self.replyFetcher)
    @pyqtSlot() #
    def getAccountBlockCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountBlockCount_Sig)
        self.qPool.start(self.replyFetcher)








    @pyqtSlot() # 2
    def getAccountBlockIds_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountBlockIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # nxt130
    def getAccountBlocks_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountBlocks_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def getAccountCurrencies_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrencies_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getAccountCurrencyCount_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrencyCount_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getAccountExchangeRequests_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountExchangeRequests_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 40
    def getAccountCurrentAskOrderIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrentAskOrderIds_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 40
    def getAccountCurrentAskOrders_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrentAskOrders_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 39
    def getAccountCurrentBidOrderIds_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrentBidOrderIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 39
    def getAccountCurrentBidOrders_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountCurrentBidOrders_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 1
    def getAccountLessors_Slot(self, apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountLessors_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 1
    def getAccountId_Slot(self, apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAccountTransactionIds_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 23
    def getAccountTransactions_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAlias_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getAllCurrencies_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllCurrencies_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getAllExchanges_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllExchanges_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getAliases_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAliases_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() #
    def getAliasCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAliasCount_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 60
    def getAllAssets_Slot(self,apiReq, meta = {}):
        """ - """
        #self.apiLogger.info('nxtApi init - : %s ', str(self) )
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllAssets_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() #52
    def getAllOpenAskOrders_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllOpenAskOrders_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() #52
    def getAllOpenBidOrders_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAllOpenBidOrders_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 55
    def getAllTrades_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAsset_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 35
    def getAssetAccounts_Slot(self, apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetAccounts_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 36
    def getAssetIds_Slot(self,apiReq, meta = {}):
        """ connect this slot directly to QTimer signal! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetIds_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 36
    def getAssetTransfers_Slot(self,apiReq, meta = {}):
        """ connect this slot directly to QTimer signal! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetTransfers_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 61
    def getAssets_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssets_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getAssetAccountCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getAssetAccountCount_Sig)
        self.qPool.start(self.replyFetcher)




    @pyqtSlot() # 31
    def getAssetsByIssuer_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBlock_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 10
    def getBlocks_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBlocks_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 31
    def getBlockId_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBlockchainStatus_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getBuyOffers_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getBuyOffers_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 7
    def getConstants_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getConstants_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getCurrencies_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrencies_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrenciesByIssuer_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrenciesByIssuer_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrency_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrency_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrencyAccountCount_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrencyAccountCount_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrencyAccounts_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrencyAccounts_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrencyFounders_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrencyFounders_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrencyIds_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrencyIds_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getCurrencyTransfers_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getCurrencyTransfers_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 31
    def getDGSGood_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSGoods_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getDGSGoodsCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSGoodsCount_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def getDGSGoodsPurchases_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSGoodsPurchases_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def getDGSGoodsPurchaseCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSGoodsPurchaseCount_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSPendingPurchases_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSPurchase_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def getDGSPurchaseCount_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSPurchaseCount_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 31
    def getDGSPurchases_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSPurchases_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def getDGSTagCount_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSTagCount_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getDGSTags_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getDGSTags_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot() # 54
    def getECBlock_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getECBlock_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getExchanges_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getExchanges_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getExchangesByExchangeRequest_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getExchangesByExchangeRequest_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getExchangesByOffer_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getExchangesByOffer_Sig)
        self.qPool.start(self.replyFetcher)




    @pyqtSlot() # 54
    def getForging_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getGuaranteedBalance_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getMintingTarget_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getMintingTarget_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 8
    def getMyInfo_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getNextBlockGenerators_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def getOffer_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getOffer_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 11
    def getPeer_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getPollIds_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def getSellOffers_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getSellOffers_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 9
    def getState_Slot(self,  apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getTransaction_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 26 this is a doubling. this getTX is supposed to be called by TXs that are put on a timer to self.Poll.
    def getTX_Slot(self,apiReq, meta = {}): # this may collide with the getTransaction calls that are made by other funcs that are not sef.Poll timers.
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.getTX_Sig)
        #QObject.connect(self.replyFetcher.emitter, SIGNAL("CancelTEST(PyQt_PyObject, PyQt_PyObject)"),self.cancelAskTESTSPEZIAL_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 41
    def getTransactionBytes_Slot(self,apiReq, meta = {}):
        """ -! """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.issueAsset_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot()
    def issueCurrency_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.issueCurrency_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 57
    def leaseBalance_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.leaseBalance_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 57
    def longConvert_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.longConvert_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 14
    def markHost_Slot(self,apiReq, meta = {}):
        """ -"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.placeBidOrder_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 34
    def popOff_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.popOff_Sig)
        self.qPool.start(self.replyFetcher)



    @pyqtSlot()
    def publishExchangeOffer_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.publishExchangeOffer_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 31
    def readMessage_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.rsConvert_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def searchAssets_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.searchAssets_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def searchCurrencies_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.searchCurrencies_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 42 ################################### NEW
    def searchDGSGoods_Slot(self, apiReq , meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.searchDGSGoods_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 34
    def scan_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.scan_Sig)
        self.qPool.start(self.replyFetcher)


    @pyqtSlot() # 31
    def sellAlias_Slot(self,apiReq, meta = {}):
        """-"""
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.sellAlias_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 18
    def sendMessage_Slot(self,apiReq, meta = {}):
        """ - """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
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
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.stopForging_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot() # 85
    def transferAsset_Slot(self,apiReq, meta = {}):
        """   """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.transferAsset_Sig)
        self.qPool.start(self.replyFetcher)

    @pyqtSlot()
    def transferCurrency_Slot(self,apiReq, meta = {}):
        """- """
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger )
        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.transferCurrency_Sig)
        self.qPool.start(self.replyFetcher)




    ###########
    ###########
    ###########

    @pyqtSlot() # 86
    def catchAll_Slot( self,apiReq, meta = {}): # this catches everything that is thrown at it, but returns as unspecific!
        """ - """
        self.apiLogger.debug('nxtApi init - : %s ', str(apiReq) )
        self.req.params=apiReq # same obj, only replace params
        preppedReq = self.req.prepare()
        self.queryURL_Sig.emit(preppedReq.url) # this is the raw request text. it goes back from here to the api access.
        meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
        replyEmitter = ReplyEmitter( self.session, preppedReq  , meta )
        self.replyFetcher = ReplyFetcher( replyEmitter, self.apiLogger   )

        QObject.connect(self.replyFetcher.emitter, SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject)"),self.catchAll_Sig)
        self.qPool.start(self.replyFetcher)

        # this is instantiation WITHOUT a logger- keep here to be able to re-switch!
        #self.replyFetcher = ReplyFetcher( replyEmitte r, self.apiLogger )
        #self.replyFetcher = ReplyFetcher( replyEmitte r, self.apiLogger )

###################################################################
#
# threading requests

class ReplyEmitter(QObject):
    """ - this is needed in QRunnable, because QRunnable is NOT able to emit signals. But this is. """

    NRSREPLY = pyqtSignal(object  ,object) #  object1 is the request, object2 can carry meta data for use case logic

    CancelTEST  = pyqtSignal(object  ,object)


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

    def __init__(self, emitter, apiLogger ):

        super(QtCore.QRunnable, self).__init__()
        self.emitter = emitter
        self.apiLogger = apiLogger

    def run(self,):

        try:
            #self.apiLogger.debug('nxtApi except - : %s - %s ',  str(self.emitter.preppedReq.url), str(inst)  )
            #print("sleep WITH DELAY- now! " +str(time.time())+ " - " +  self.emitter.metaThread['queryNum'])
            time.sleep(0.1 * self.emitter.metaThread['qqLen']) # THIS IS TO PROTECT THE SERVER FROM dropping fast requests
        except:
            pass # no QueryQueueLength -> just go ahead time.sleep(0.001) #pass
        try:
            resp = self.emitter.session.send(self.emitter.preppedReq)
        except Exception as inst:
            self.apiLogger.debug('nxtApi except - : %s - %s ',  str(self.emitter.preppedReq.url), str(inst)  )
            resp={'apiError': str(inst)}
        try:
            resp=resp.json()
        except Exception as inst:
            self.apiLogger.debug('nxtApi except - : %s - %s ',  str(self.emitter.preppedReq.url), str(inst)  )
        #
        # # YES, they are always ALL double!
        # #self.apiLogger.info('--------> nxtApiSigs: nxtApi returns resp - meta  %s \n %s \n %s  \n %s \n',  str(resp), str(self.emitter.metaThread), str(time.time()), str(self)      )
        # #
        # # #self.apiLogger.info('--------> nxtApiSigs: AM I DOUBLE FOR ALL ?? %s \n %s %s',  str(self.emitter), str(time.time()), str(self)      )
        # try: # this can beused to look for SPECIFIC API CALLS- KEEP THIS HERE!! USEFUL! this is very good for debugging!!
        # #     if True: # --------> nxtApiSigs: nxtApi returns resp - meta   {'errorCode': 5, 'errorDescription': 'Unknown account'} uc32_ID
        #     #if (self.emitter.metaThread['TXcreator'] ==  'cancelAskOrder' or  self.emitter.metaThread['TXcreator'] ==  'placeAskOrder'):
        #     if ('TXcreator' in self.emitter.metaThread.keys()): # ==  'cancelAskOrder' or  self.emitter.metaThread['TXcreator'] ==  'placeAskOrder'):
        #
        #         if self.emitter.metaThread['TXcreator'] == 'cancelAskOrder':
        #             #self.emitter.emit(SIGNAL("CancelTEST(PyQt_PyObject, PyQt_PyObject )"), resp, self.emitter.metaThread )
        #
        #
        #
        #             self.apiLogger.info('--------> nxtApiSigs: nxtApi returns CancelTESTCancelTEST resp - meta \n %s \n %s \n %s  \n %s \n',  str(resp), str(self.emitter.metaThread), str(time.time()), str(self)      )
        # #             #self.apiLogger.info('--------> nxtApiSigs: self.emitter.preppedReq.url: %s  \n',  str(self.emitter.preppedReq.url)  )
        # except: #  THIS IS VERY USEFUL KEEP THIS!!     <nxtPwt.nxtApiSigs.ReplyFetcher object at 0x7fe68026d048>  this is the very exact same OBJECT that emitstwice
        #
        #     pass

        #self.apiLogger.info('nxtApi returns resp - meta   %s   %s \n',  str(resp), str(self.emitter.metaThread)  )



        self.emitter.emit(SIGNAL("NRSREPLY(PyQt_PyObject, PyQt_PyObject )"), resp, self.emitter.metaThread )
        #self.apiLogger.info('--------> nxtApiSigs: apiReq: %s  \n',  str( apiReq)  )
        # self.apiLogger.info('--------> nxtApi.req.__dict__: %s  \n',  str(self.req.__dict__)  )
        # self.apiLogger.info('--------> nxtApi.req.url: %s  \n',  str(self.req.url)  )
        # self.apiLogger.info('--------> nxtApiSigs: self.emitter.preppedReq.url: %s  \n',  str(preppedReq.url)  )

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