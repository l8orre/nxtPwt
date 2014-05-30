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

from PyQt4 import Qt, QtCore
#from PyQt4.QtCore import QTimer

#import time
from copy import copy

from nxtPwt.nxtApiSigs import nxtApi
from nxtPwt.nxtApiPrototypes import nxtQs

import time



# jsonrpc stuff
from requests import Request as Req
from requests import Response  as Resp
from requests import Session
import requests 


from werkzeug.wrappers import  Response ,Request
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher





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

 

class UC_Bridge1(nxtUseCaseMeta):
    """
        output of ./bitcoin-cli help:
        
            addmultisigaddress nrequired ["key",...] ( "account" )
            addnode "node" "add|remove|onetry"
            backupwallet "destination"
            createmultisig nrequired ["key",...]
            createrawtransaction [{"txid":"id","vout":n},...] {"address":amount,...}
            decoderawtransaction "hexstring"
            decodescript "hex"
            dumpprivkey "bitcoinaddress"
            dumpwallet "filename"
            getaccount "bitcoinaddress"
            getaccountaddress "account"
            getaddednodeinfo dns ( "node" )
            getaddressesbyaccount "account"
            getbalance ( "account" minconf )
            getbestblockhash
            getblock "hash" ( verbose )
            getblockcount
            getblockhash index
            getblocktemplate ( "jsonrequestobject" )
            getconnectioncount
            getdifficulty
            getgenerate
            gethashespersec
            getinfo
            getmininginfo
            getnettotals
            getnetworkhashps ( blocks height )
            getnewaddress ( "account" )
            getpeerinfo
            getrawchangeaddress
            getrawmempool ( verbose )
            getrawtransaction "txid" ( verbose )
            getreceivedbyaccount "account" ( minconf )
            getreceivedbyaddress "bitcoinaddress" ( minconf )
            gettransaction "txid"
            gettxout "txid" n ( includemempool )
            gettxoutsetinfo
            getunconfirmedbalance
            getwork ( "data" )
            help ( "command" )
            importprivkey "bitcoinprivkey" ( "label" rescan )
            importwallet "filename"
            keypoolrefill ( newsize )
            listaccounts ( minconf )
            listaddressgroupings
            listlockunspent
            listreceivedbyaccount ( minconf includeempty )
            listreceivedbyaddress ( minconf includeempty )
            listsinceblock ( "blockhash" target-confirmations )
            listtransactions ( "account" count from )
            listunspent ( minconf maxconf  ["address",...] )
            lockunspent unlock [{"txid":"txid","vout":n},...]
            move "fromaccount" "toaccount" amount ( minconf "comment" )
            ping
            sendfrom "fromaccount" "tobitcoinaddress" amount ( minconf "comment" "comment-to" )
            sendmany "fromaccount" {"address":amount,...} ( minconf "comment" )
            sendrawtransaction "hexstring" ( allowhighfees )
            sendtoaddress "bitcoinaddress" amount ( "comment" "comment-to" )
            setaccount "bitcoinaddress" "account"
            setgenerate generate ( genproclimit )
            settxfee amount
            signmessage "bitcoinaddress" "message"
            signrawtransaction "hexstring" ( [{"txid":"id","vout":n,"scriptPubKey":"hex","redeemScript":"hex"},...] ["privatekey1",...] sighashtype )
            stop
            submitblock "hexdata" ( "jsonparametersobject" )
            validateaddress "bitcoinaddress"
            verifychain ( checklevel numblocks )
            verifymessage "bitcoinaddress" "signature" "message"
            walletlock
            walletpassphrase "passphrase" timeout
            walletpassphrasechange "oldpassphrase" "newpassphrase"
            
            
tested examples for the BTC-NXT mappings implemented below, using two different curl syntax methods.

NXT:
curl param encoding 1
-----------------------
 
curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getinfo", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getbalance", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getconnectioncount", "params": {}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getreceivedbyaccount", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getreceivedbyaddress", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "gettransaction", "params": {"txid":"1448848043607985937"}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "sendfrom", "params": {"amount":0.00001, "fromaccount":"17oreosetc17oreosetc",  "tobitcoinaddress":"2865886802744497404",  "minconf":1,  "comment":"" , "comment-to":"" }, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "settxfee", "params": {}, "id": 12}' http://localhost:7879/jsonrpc

curl -i -X POST -d '{"jsonrpc": "2.0", "method": "validateaddress", "params": {"PASSPHRASE":"17oreosetc17oreosetc"}, "id": 12}' http://localhost:7879/jsonrpc

 


NXT:
curl param encoding 2
-----------------------

curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getinfo","params": {} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc

curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getbalance","params": {"account":"16159101027034403504"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc

curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getconnectioncount","params": {} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
 
curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getreceivedbyaccount","params":  {"account":"16159101027034403504"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc

curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getreceivedbyaddress","params":  {"account":"16159101027034403504"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
 
curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"gettransaction","params":  {"txid":"1448848043607985937"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
  
curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"sendfrom","params":  {"amount":0.00003, "fromaccount":"17oreosetc17oreosetc",  "tobitcoinaddress":"2865886802744497404",  "minconf":1,  "comment":"" , "comment-to":"" } }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc

curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"settxfee","params":  {} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
 
curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"validateaddress","params": {"PASSPHRASE":"17oreosetc17oreosetc"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
 
 
 
            """

    changeResident_Sig = pyqtSignal(object, object)

    def __init__(self, sessMan, host = 'localhost', port = '6876'  ):
        super(UC_Bridge1   , self   ).__init__(sessMan)
        #self.app = app # we need to know app
        self.sessMan = sessMan
        self.meta = {'caller':'Bridge1'}
        defPass17 = '0' # '17oreosetc17oreosetc'
        acctSecKey = defPass17
        print(host + port)
        self.mm = BridgeThread( host  , port   )
        # self start w/o BridgeCtrl mm.jsonServ_Slot()

#
# this might go into a models-like class 
##################################################################
 
 
 
class BridgeThread(QObject):
    
    # housekeeping ogf the threads may have to be taken care of
    def __init__(self, host, port):
        super(QObject, self).__init__( parent = None)
        self.qPool=QtCore.QThreadPool.globalInstance()
        self.qPool.setMaxThreadCount(2500) # robustness
        self.host = host
        self.port = port
        #self.qPool.activeThreadCount() this is how many we have running?!
    @pyqtSlot() # 61
    def jsonServ_Slot(self, ):
        self.json_Runner = JSON_Runner( self.host, self.port ) # json_Emitter, self to THIS !!!!!!
          
        self.qPool.start(self.json_Runner)
         
        
class JSON_Runner(QtCore.QRunnable):
    """- This is what needs to be put into the QThreadpool """
    nxtApi = nxtApi
    
    def __init__(self,   host = 'localhost', port = '6876' ): #emitter, 
        super(QtCore.QRunnable, self).__init__()
        global session # this must be global to be accessible from the dispatcher methods
        session = Session()
        headers = {'content-type': 'application/json'}
        #sessUrl = 'http://localhost:6876/nxt?' 
        sessUrl = 'http://' + host + ':' + port + '/nxt?' 
        global NxtReq
        NxtReq = Req( method='POST', url = sessUrl, params = {}, headers = headers        )
        #print("\n1111######" + str(self)  )
 
        # can't access self.NAMESPACE here !?!?!?!
############################
 # 2 generic Nxt APIs
    @dispatcher.add_method
    def getState(**kwargs):
        payload = { "requestType" : "getState" } 
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        #print(str(type(NxtResp)))
        Nxt2Btc = {}
        return NxtResp  

    @dispatcher.add_method
    def getTime( **kwargs):
        payload = { "requestType" : "getTime" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        #print(str(type(NxtResp))) # dct of cpurse
        Nxt2Btc = {}
        return NxtResp  

  
#######################
#
# Function Calls implemented below
# Numbers as per appeearance in listing of bitcoind help 
  
# 14 getbalance
# 21 getconnectioncount
# 25 getinfo 
# 33 getreceivedbyaccount
# 34 getreceivedbyaddress
# 35 gettransaction
# 52 sendfrom
# 58 settxfee
# 63 validateaddress


             

  
#######################
#######################
#######################
#######################
#######################
#######################


#######################
# 14 getbalance
  
    @dispatcher.add_method
    def getbalance( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
        1   getbalance
        
        2   [account] [minconf=1]	
        
        3   If [account] is not specified, returns the server's total available balance.
            If [account] is specified, returns the balance in the account.
        
        4   N	
        
        5   Y	
        
        6   return is a float 0.00000000

        7   http://localhost:7876/nxt?requestType=getBalance&account=ACCOUNT	

        8   {
            "unconfirmedBalanceNQT": UNCONFBALANCENQT,
            "effectiveBalanceNXT": EFFBALANCENXT,
            "balanceNQT": BALANCENQT
            }	

        9   here we use the account to pass in an NXT account number so you can enquire any account and dont need the secret phrase
            run this command for the specified nxt account return the BALANCENQT - <account> is required
        
        EXAMPLE:
                 
        curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getbalance", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc
        
        HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 81
        Server: Werkzeug/0.9.4 Python/3.4.0
        Date: Tue, 27 May 2014 13:10:34 GMT
        
        {"result": {"16159101027034403504": "4061839895698"}, "id": 12, "jsonrpc": "2.0"}azure@boxfish:~/workbench/nxtDev/BRIDGE$ 


        """
        ACCOUNT = kwargs["account"] #kwargs['account']
        payload = { "requestType" : "getBalance" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['account'] = ACCOUNT 
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        Nxt2Btc = {}
        Nxt2Btc =  {
                    ACCOUNT:NxtResp['balanceNQT']
                    }
        
        return Nxt2Btc  
 
 
#########################
# 21 getconnectioncount
   
    @dispatcher.add_method
    def getconnectioncount( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
        
        
        1    getconnectioncount		
        
        2
        
        3    Returns the number of connections to other nodes.	
        
        4   N	
        
        5   Y	
        
        6       returns int of number of connections	
        
        7       ? requestType=getState	
        
        8       {
        "numberOfPolls": NUMPOLLS,
        "numberOfVotes": NUMVOTES,
        "numberOfTrades": NUMTRADES,
        "lastBlock": "LASTBLOCKID",
        "numberOfAliases": NUMALIASES,
        "lastBlockchainFeeder": "FEEDERPEER",
        "numberOfBlocks": HEIGHT,
        "numberOfPeers": NUMPEERS
        "totalMemory": CURMEMORY,
        "freeMemory": FREEMEMORY,
        "maxMemory": MAXMEMORY,
        "numberOfTransactions": NUMTRANS,
        "numberOfUnlockedAccounts": NUMUSERS,
        "version": "VERSION",
        "numberOfOrders": NUMORDERS,
        "totalEffectiveBalanceNXT": EFFECTIVEBALANCE
        "time": TIME,
        "availableProcessors": NUMPROCESSORS,
        "numberOfAssets": NUMASSETS,
        "cumulativeDifficulty": "CUMEDIFF"
        "numberOfAccounts": NUMACCOUNTS
        }	
        
        9   return numberOfPeers
        
        """
        payload = { "requestType" : "getState" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        Nxt2Btc = {}
         
        Nxt2Btc =  {
                    'numberOfPeers':NxtResp['numberOfPeers']
                    }
        
        return Nxt2Btc  
 
  

#########################
# 25 getinfo 
    @dispatcher.add_method
    def getinfo( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
        
        1        getinfo
        
        2        None
        
        3        Returns an object containing various state info.
        
        4        N
        
        5        Y
        
        6        Returns JSON as follows
        
        {
        "version" : 80300,
        "protocolversion" : 70001,
        "walletversion" : 60000,
        "balance" : 0.00000000,
        "blocks" : 253584,
        "timeoffset" : -5,
        "connections" : 13,
        "proxy" : "",
        "difficulty" : 50810339.04827648,
        "testnet" : false,
        "keypoololdest" : 1373494595,
        "keypoolsize" : 101,
        "paytxfee" : 0.00000000,
        "errors" : ""
        }	
        
        7        ? requestType=getState	
        
        8        {
        "numberOfPolls": NUMPOLLS,
        "numberOfVotes": NUMVOTES,
        "numberOfTrades": NUMTRADES,
        "lastBlock": "LASTBLOCKID",
        "numberOfAliases": NUMALIASES,
        "lastBlockchainFeeder": "FEEDERPEER",
        "numberOfBlocks": HEIGHT,
        "numberOfPeers": NUMPEERS
        "totalMemory": CURMEMORY,
        "freeMemory": FREEMEMORY,
        "maxMemory": MAXMEMORY,
        "numberOfTransactions": NUMTRANS,
        "numberOfUnlockedAccounts": NUMUSERS,
        "version": "VERSION",
        "numberOfOrders": NUMORDERS,
        "totalEffectiveBalanceNXT": EFFECTIVEBALANCE
        "time": TIME,
        "availableProcessors": NUMPROCESSORS,
        "numberOfAssets": NUMASSETS,
        "cumulativeDifficulty": "CUMEDIFF"
        "numberOfAccounts": NUMACCOUNTS
        }	
        
        9        Returns JSON as follows
        
        {
        "version" : VERSION,
        "protocolversion" : VERSION,
        "walletversion" : VERSION,
        "balance" : 0.00000000,
        "blocks" : HEIGHT,
        "timeoffset" : 0,
        "connections" : NUMPEERS,
        "proxy" : "",
        "difficulty" : CUMEDIFF,
        "testnet" : false,
        "keypoololdest" : CURMEMORY,
        "keypoolsize" : FREEMEMORY,
        "paytxfee" : 0.00000000,
        "errors" : ""
        }
        
        EXAMPLES:
        
        curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getinfo","params":[]}' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc

        curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getinfo", "params": { "": "","":""}, "id": 7}' http://localhost:7879/jsonrpc

        """
        #print(str(kwargs))   
        payload = { "requestType" : "getState" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        #print(str(type(NxtResp))) # dct of cpurse
        VERSION = NxtResp['version']
        HEIGHT = NxtResp['numberOfBlocks']
        NUMPEERS = NxtResp['numberOfPeers']
        CUMEDIFF = NxtResp['cumulativeDifficulty']
        CURMEMORY = NxtResp['totalMemory']
        FREEMEMORY = NxtResp['freeMemory']
        FALSE = False
        Nxt2Btc = {}
        Nxt2Btc =  {
                    "version" : VERSION,
                    "protocolversion" : VERSION,
                    "walletversion" : VERSION,
                    "balance" : 0.00000000,
                    "blocks" : HEIGHT,
                    "timeoffset" : 0,
                    "connections" : NUMPEERS,
                    "proxy" : "",
                    "difficulty" : CUMEDIFF,
                    "testnet" :  FALSE,
                    "keypoololdest" : CURMEMORY,
                    "keypoolsize" : FREEMEMORY,
                    "paytxfee" : 0.00000000,
                    "errors" : ""
                    }
        
        return Nxt2Btc  


 
##################################################
 
# 33 getreceivedbyaccount
         
    @dispatcher.add_method
    def getreceivedbyaccount( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
                 
        1   getreceivedbyaccount	
        
        2   [account] [minconf=1]	
        
        3   Returns the total amount received by addresses with [account] in transactions with at least [minconf] confirmations. If [account] not provided return will include all transactions to all accounts. (version 0.3.24)
        
        4   N	
        
        5   Y	
        
        6   account=walletaccountnumber, minconf=10, returns float 0.00000000	
        
        7   http://localhost:7876/nxt?
        requestType=getBalance&
        account=ACCOUNT
        
        8	
        
        {
        "guaranteedBalanceNQT": "GUARANTEED_BALANCE",
        "balanceNQT": "BALANCENQT",
        "effectiveBalanceNXT": EFFBALANCENXT,
        "unconfirmedBalanceNQT": "UNCONFBALANCENQT",
        "forgedBalanceNQT": "FORGEDBAL"
        }	
        
        9   Pass in the nxt account number and return GUARANTEED_BALANCE as float


        EXAMPLES:
        
        curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getreceivedbyaccount","params":  {"account":"16159101027034403504"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc

        {"result": {"16159101027034403504": 4061839895698.0}, "id": "curltext", "jsonrpc": "2.0"}


        
        curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getreceivedbyaccount", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc
        
        {"result": {"16159101027034403504": 4061839895698.0}, "id": 12, "jsonrpc": "2.0"}



        """
        #print("getreceivedbyaccount" +str(kwargs))   
        ACCOUNT = kwargs["account"] #kwargs['account']
        payload = { "requestType" : "getBalance" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['account'] = ACCOUNT 
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        Nxt2Btc = {}
        Nxt2Btc =  {
                    ACCOUNT : float(NxtResp['balanceNQT'])
                    }
        
        return Nxt2Btc  
        
        
        
        
        
        
# 34 getreceivedbyaddress
 
    @dispatcher.add_method
    def getreceivedbyaddress( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
             
             
                     
        
        1   getreceivedbyaddress	
        
        2   <bitcoinaddress> [minconf=1]	
        
        3   Returns the amount received by <bitcoinaddress> in transactions with at least [minconf] confirmations. It correctly handles the case where someone has sent to the address in multiple transactions. Keep in mind that addresses are only ever used for receiving transactions. Works only for addresses in the local wallet, external addresses will always show 0.
        
        4   N
        
        5   Y	
        
        6   address=bitcoinaddress, minconf=10, returns float 0.00000000	
        
        7   http://localhost:7876/nxt?
        requestType=getAccountId&
        secretPhrase=PASSPHRASE
        Followed by
        http://localhost:7876/nxt?
        requestType=getBalance&
        account=ACCOUNT	
        
        8   Use bitcoinaddress as the secret phrase to return the NXT account ID
        
        {
        "GUARANTEED_BALANCE",
        "GUARANTEED_BALANCE",
        "BALANCENQT",
        "BALANCENQT",
        EFFBALANCENXT,
        EFFBALANCENXT,
        "unconfirmedBalanceNQT": "UNCONFBALANCENQT",
        "FORGEDBAL"
        "FORGEDBAL"
        }	
        
        9   In this model I have mapeed bitcoinaddress as the NXT secretphrase passed to the server return GUARANTEED_BALANCE as float
        
        
        
        EXAMPLES:
        
        
        curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"getreceivedbyaddress","params":  {"account":"16159101027034403504"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
        
        {"jsonrpc": "2.0", "id": "curltext", "result": {"16159101027034403504": 4061839895698.0}}


        
        curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getreceivedbyaddress", "params": {"account":"16159101027034403504","minconf":"1"}, "id": 12}' http://localhost:7879/jsonrpc
        
        {"jsonrpc": "2.0", "id": 12, "result": {"16159101027034403504": 4061839895698.0}}




        """
        #print("getreceivedbyaddress" +str(kwargs))   
        ACCOUNT = kwargs["account"] #kwargs['account']
        payload = { "requestType" : "getBalance" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['account'] = ACCOUNT 
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        Nxt2Btc = {}
        Nxt2Btc =  {
                    ACCOUNT : float(NxtResp['balanceNQT'])
                    }
        
        return Nxt2Btc  
        
        
        
        
      

# 35 gettransaction
  
        
        
    @dispatcher.add_method
    def gettransaction( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
                 
        1   gettransaction	
        
        2   <txid>	
        
        3   Returns an object about the given transaction containing:
        "amount" : total amount of the transaction
        "confirmations" : number of confirmations of the transaction
        "txid" : the transaction ID
        "time" : time associated with the transaction[1].
        "details" - An array of objects containing:
        "account"
        "address"
        "category"
        "amount"
        "fee"
        
        4   N
        
        5   Y
        
        6	{
        "amount" : 0.05000000,
        "confirmations" : 0,
        "txid" : "9ca8f969bd3ef5ec2a8685660fdbf7a8bd365524c2e1fc66c309acbae2c14ae3",
        "time" : 1392660908,
        "timereceived" : 1392660908,
        "details" : [
        {
        "account" : "",
        "address" : "1hvzSofGwT8cjb8JU7nBsCSfEVQX5u9CL",
        "category" : "receive",
        "amount" : 0.05000000
        }
        ]
        }
        
        7	http://localhost:7876/nxt?
        requestType=getTransaction&
        transaction=TRANSID<txid>	{
        
        8   "sender": "SENDERACCOUNT",
        "senderRS": "SENDERACCOUNTRS",
        "feeNQT": "FEE",
        "amountNQT": "AMOUNT",
        "timestamp": TIME,
        "referencedTransaction": REFTX,
        "confirmations": CONFIRMS,
        "subtype": SUBTYPE,
        "block": "BLOCKID",
        "senderPublicKey": "PUBKEY",
        "type": TYPE,
        "deadline": DEADLINE,
        "signature": "SIGNATURE",
        "recipient": "RECIPACCOUNT",
        "recipientRS": "RECIPACCOUNTRS",
        "fullHash": "FULLHASH", 
        "signatureHash": "SIGHASH", 
        "hash": "HASH", 
        "transaction": "TRANSID", 
        "attachment":
        {
        ATTACHMENT
        }
        }	
        
        9   Pass in a NXT tx id previously obtained and get information on the confirmation status of that.
        {
        "amount" : float(AMOUNT),
        "confirmations" : CONFIRMS,
        "txid" : TRANSID
        "time" : TIME,
        "timereceived" : TIME,
        "details" : [
        {
        "account" : “”,
        "address" : RECIPACCOUNT 
        "category" : "receive",
        "amount" : AMOUNT
        }
        ]
        }
         
        
        ./bitcoin-cli help gettransaction
        gettransaction "txid"
        
        Get detailed information about in-wallet transaction <txid>
        
        Arguments:
        1. "txid"    (string, required) The transaction id
        
        Result:
        {
          "amount" : x.xxx,        (numeric) The transaction amount in btc
          "confirmations" : n,     (numeric) The number of confirmations
          "blockhash" : "hash",  (string) The block hash
          "blockindex" : xx,       (numeric) The block index
          "blocktime" : ttt,       (numeric) The time in seconds since epoch (1 Jan 1970 GMT)
          "txid" : "transactionid",   (string) The transaction id, see also https://blockchain.info/tx/[transactionid]
          "time" : ttt,            (numeric) The transaction time in seconds since epoch (1 Jan 1970 GMT)
          "timereceived" : ttt,    (numeric) The time received in seconds since epoch (1 Jan 1970 GMT)
          "details" : [
            {
              "account" : "accountname",  (string) The account name involved in the transaction, can be "" for the default account.
              "address" : "bitcoinaddress",   (string) The bitcoin address involved in the transaction
              "category" : "send|receive",    (string) The category, either 'send' or 'receive'
              "amount" : x.xxx                  (numeric) The amount in btc
            }
            ,...
          ],
          "hex" : "data"         (string) Raw data for transaction
        }
        
        bExamples
        > bitcoin-cli gettransaction "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"
        > curl --user myusername --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": ["1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"] }' -H 'content-type: text/plain;' http://127.0.0.1:8332/



        
        BITCOIN TX REPLY:
        curl --user 'rpcNxtBitcoin:4JLstlAJ6gJyV1DHv2' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"gettransaction","params":["f0b20213346b14361795a9a387ac28078dc9a8a14fd9ced4f7b32eab9966820f"]}' -H 'content-type:text/plain;' http://127.0.0.1:8332
        {"result":{
        
        "amount":-0.00010000,
        "fee":-0.00010000,
        "confirmations":5521,
        "blockhash":"0000000000000000091ae589c034bc0466e2feca51dc018bb2c3303e8ab8648b",
        "blockindex":156,
        "blocktime":1398350348,
        "txid":"f0b20213346b14361795a9a387ac28078dc9a8a14fd9ced4f7b32eab9966820f",
        "walletconflicts":[],
        "time":1398349976,
        "timereceived":1398349976,
        "details":[
        		{"account":"",
                   "address":"19SCQ8fWR4sChAPwbfNACsv1s6CNspF6Yh",
                   "category":"send",
                   "amount":-0.00010000,
                   "fee":-0.00010000}
        
        ],
        "hex":"0100000001033e27a990fe6f3dba62493dcd59b16405dab0bcf2bdcf9b098b613dfb614790010000006b483045022100f61632e64c9b47a70445166bb5de5bae6d8d099ba96ac0d1219842ac2fdb6c0902204be319107f76dee45e5332a10202c6152da7c0391e91397c273d036b95c4d88d01210272518a71e864d296ca61efd5bd8be6061afa70248462c958b58f52afaff6b688ffffffff0250c30000000000001976a9147fa916934255d62febf440a3fad445e1d743d95a88ac10270000000000001976a9145c84ebab10bdf995178e972e5aac94c6b1c5405688ac00000000"},
        "error":null,
        "id":"curltext"
        }





         Nxt testNet TX: 1448848043607985937
              
        
        
        Nxt full getTransaction reply:
        
        {
            "fullHash": "110fc68c9e571b14bb05bcd7d64aea5ae342a4fa80f32deb85be4bdf285ef8d4",
            "confirmations": 29448,
            "signatureHash": "8169819b0f3f6e950db238ba5dab2c7080b5754c2630eb4d4b3ebdf8639e65d6",
            "transaction": "1448848043607985937",
            "amountNQT": "300000000",
            "block": "9383935361491353106",
            "recipientRS": "NXT-3P9W-VMQ3-9DRR-4EFKH",
            "type": 0,
            "feeNQT": "100000000",
            "recipient": "2865886802744497404",
            "sender": "16159101027034403504",
            "timestamp": 13323520,
            "height": 81053,
            "subtype": 0,
            "senderPublicKey": "f9cecd0a2d38afcb4a799ec7e7c718ce451053bd2a2924c15fbd5922aa915825",
            "deadline": 180,
            "blockTimestamp": 13323576,
            "senderRS": "NXT-L6PJ-SMZ2-5TDB-GA7J2",
            "signature": "b210c5b3e1fa28c9aa5c5fd05d2e6ca64869b191d3d4bc04369f06ffdcffc8044fce36f2825b155ba2be9eeef10a1644306609c965632e638598ee954684c86e"
        }
        
        
                
        EXAMPLES:
        
        curl -i -X POST -d '{"jsonrpc": "2.0", "method": "gettransaction", "params": {"txid":"1448848043607985937"}, "id": 12}' http://localhost:7879/jsonrpc
        
        {"result": {"amount": 300000000.0, "details": [{"amount": 300000000.0, "account": "16159101027034403504", "category": "receive", "address": "2865886802744497404"}], "time": 13323520, "timereceived": 13323520, "confirmations": 29471, "txid": "1448848043607985937"}, "jsonrpc": "2.0", "id": 12} 
        
        
        curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"gettransaction","params":  {"txid":"1448848043607985937"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
        
        {"result": {"amount": 300000000.0, "details": [{"amount": 300000000.0, "account": "16159101027034403504", "category": "receive", "address": "2865886802744497404"}], "time": 13323520, "timereceived": 13323520, "confirmations": 29473, "txid": "1448848043607985937"}, "jsonrpc": "2.0", "id": "curltext"}




        """
        TXid = kwargs["txid"] #kwargs['account']
        try:
            TX_hash = kwargs['hash']
        except:
            TX_hash = ''
        payload = { "requestType" : "getTransaction" }  
        
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['transaction'] = TXid
        NxtApi['hash'] = TX_hash 
        
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        
         
        CONFIRMS = NxtResp['confirmations']
        TRANSID = NxtResp['transaction']
        TIME = NxtResp['timestamp']
        SENDER = NxtResp['sender']
        RECIPIENT = NxtResp['recipient']
        
        AMOUNT = NxtResp['amountNQT']
        
        #print(str(NxtResp))
        Nxt2Btc = {}
        Nxt2Btc =  {
                "amount" : float(AMOUNT),
                "confirmations" : CONFIRMS,
                "txid" : TRANSID,
                "time" : TIME,
                "timereceived" : TIME,
                "details" : [
                            {
                            "account" : SENDER,
                            "address" : RECIPIENT,
                            "category" : "receive",
                            "amount" : float(AMOUNT)
                            }
                            ]
                            }
                    
        return Nxt2Btc  
 






# 52 sendfrom

        
    @dispatcher.add_method
    def sendfrom( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
 
            
            1   sendfrom	
            
            2   <fromaccount> <tobitcoinaddress> <amount> [minconf=1] [comment] [comment-to]	
            
            3   <amount> is a real and is rounded to 8 decimal places. Will send the given amount to the given address, ensuring the account has a valid balance using [minconf] confirmations. Returns the transaction ID if successful (not in JSON object).	
            
            4   Y	
            
            5   N	
            
            6   { “txid” : “<txid>” }	
            
            7   http://localhost:7876/nxt?
            requestType=sendMoney&
            secretPhrase=<fromaccount>&
            recipient=<tobitcoinaddress>& 
            amountNQT=<amount>& 
            feeNQT=(from set tx fee)& 
            deadline=(default 1440)	
            
            8   { 
            "transaction": "TRANSACTIONID" 
            }	
            
            9   Would have preferred a better bitcond call here as I swap the use of accont and address but I dont see any other option
            use the <fromaccount> to pass the secretphrase for the NXT account, <tobitcoinaddress> becomes the nxt account number, need to convert the float amount into NQT the fee should be defaulted to the minimum or set using set tx fee command, convert the json to pass back the transaction id

            
            EXAMPLES:
            
            curl -i -X POST -d '{"jsonrpc": "2.0", "method": "sendfrom", "params": {"amount":0.00001, "fromaccount":"SECRETPHRASE",  "tobitcoinaddress":"1234567890123456789",  "minconf":1,  "comment":"" , "comment-to":"" }, "id": 12}' http://localhost:7879/jsonrpc
            
            {"jsonrpc": "2.0", "id": 12, "result": {"txid": "948172143107956553"}
            
            
            
            
            curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"sendfrom","params":  {"amount":0.00003, "fromaccount":"SECRETPHRASE",  "tobitcoinaddress":"1234567890123456789",  "minconf":1,  "comment":"" , "comment-to":"" } }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
            {"jsonrpc": "2.0", "id": "curltext", "result": {"txid": "16837301710895534070"}}
            
            
            CORRECT INTERNAL NXT SERVER DICT:
            {'fullHash': 'ce2964c99d93d21688f9755a8bc0b6928f8d01306e5846c0ac9525665e24e42d', 'transaction': '1644539119841585614', 'unsignedTransactionBytes': '00004dfbf3000100f9cecd0a2d38afcb4a799ec7e7c718ce451053bd2a2924c15fbd5922aa915825fcd410ecdcacc527e80300000000000000e1f50500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 'signatureHash': '7e7829a740b5c2286eb698ad6dd3b90ce15d56c70b6343135cd548dbb3177aeb', 'transactionBytes': '00004dfbf3000100f9cecd0a2d38afcb4a799ec7e7c718ce451053bd2a2924c15fbd5922aa915825fcd410ecdcacc527e80300000000000000e1f505000000000000000000000000000000000000000000000000000000000000000000000000054cc9b39f8e5644a06976f92883876451b427890763c6f38746fd8fe27a85022e6bd35254e937fa321083835ed5034e7ca9fb7c3987627066408720077a434b', 'broadcasted': True}
            
            127.0.0.1 - - [28/May/2014 15:33:02] "POST /jsonrpc HTTP/1.1" 200 -

            """


 
        payload = { "requestType" : "sendMoney" }  

        amountNQT = int( float(kwargs['amount'] ) * 100000000)
        

        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['publicKey'] =  ""
        NxtApi['referencedTransaction'] =  ""
        NxtApi['secretPhrase'] =  kwargs['fromaccount']
        NxtApi['deadline'] =  kwargs['minconf']
        NxtApi['feeNQT'] =  "100000000"
        NxtApi['amountNQT'] = amountNQT
        NxtApi['recipient'] =  kwargs['tobitcoinaddress']
        
        
        
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp = response.json()
        
          
        TX_ID = NxtResp['transaction']
        
        print(str(NxtResp))
        Nxt2Btc = {}
        Nxt2Btc =  {
                
                "txid" : TX_ID,
                
                            }
                    
        return Nxt2Btc  
 
















 
 

  

# 58 settxfee
 
    @dispatcher.add_method
    def settxfee( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
         
         
         

1   settxfee	

2   <amount>	<amount> 

3   is a real and is rounded to the nearest 0.00000001	

4   N	

5   Y	

6   returns true	

7   no api	

8   n/a	

9   use to set the default tx fee in nxtcoind


        EXAMPLES:
        
        """
        print("settxfee"+str(kwargs))   
        payload = { "requestType" : "getState" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        #preppedReq = NxtReq.prepare()
        #response = session.send(preppedReq)
        #NxtResp = response.json()
        Nxt2Btc = {}
        Nxt2Btc =  {
                    "settxfee" : "n/a"
                    }
        
        return Nxt2Btc  



# 63 validateaddress

    @dispatcher.add_method
    def validateaddress( **kwargs):
        """ Mapping Commentary. See keys at [Nxt2Btc_Mapping_Comments] in docstring of def application()
         
                 
        1   validateaddress	
        
        2   <bitcoinaddress>	
        
        3   Return information about <bitcoinaddress>.	
        
        4   N	
        
        5   Y	
        
        6   {
            "isvalid" : true,
            "address" : "168La15SRLLaJBz6zUrxxyDQXU6cnzoHS2",
            "ismine" : false
            }
            
        7   http://localhost:7876/nxt?
            requestType=getAccountId& secretPhrase=PASSPHRASEhttp://local
            
            Follwed by 
            
            Host:7876/nxt?
            requestType=getAccountPublicKey&
            account=ACCOUNTNUM	
        
        8   {
            "publicKey": "PUBKEY"
            }	
            
        9   Convert as follows – isvalid=true if pubkey exists, ismine=true as secretphrase is known and address is passed back using secretphrease to be consistent
            {
            "isvalid" : IFPUBKEY(true),
            "address" : "PASSPHRASE",
            "ismine" : true
            }

          

        EXAMPLES:
        
        
        curl -i -X POST -d '{"jsonrpc": "2.0", "method": "validateaddress", "params": {"PASSPHRASE":"17oreosetc17oreosetc"}, "id": 12}' http://localhost:7879/jsonrpc
        
        {"jsonrpc": "2.0", "result": {"ismine": true, "address": "16159101027034403504", "isvalid": true}, "id": 12}azure@boxfish:~/workbench/nxtDev/BRIDGE$ ^C
        
        
        
        curl --user 'anyName:anyPW' --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"validateaddress","params": {"PASSPHRASE":"17oreosetc17oreosetc"} }' -H 'content-type:text/plain;' http://127.0.0.1:7879/jsonrpc
        
        {"jsonrpc": "2.0", "result": {"ismine": false, "address": "16159101027034403504", "isvalid": true}, "id": "curltext"}azure@boxfish:~/workbench/nxtDev/BRIDGE$  




        """
        print("validateaddress "+str(kwargs))   


        payload = { "requestType" : "getAccountId" } 
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['secretPhrase'] =  kwargs['PASSPHRASE'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp1 = response.json()
        #print(" NxtResp1 "+str(NxtResp1))   

        ACCOUNT = NxtResp1['accountId']

        
        payload = { "requestType" : "getForging" } 
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['secretPhrase'] =  kwargs['PASSPHRASE'] # here we translate BTC params to NXT params
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp2 = response.json()
        #print(str(NxtResp2))
#
#        self.getForging= {
#                                        "requestType" : "getForging" , \
#                                        "secretPhrase" : "PASSPHRASE"   ,\
#                                        }

        if "errorCode" in NxtResp2.keys():
            isForging = False
        elif "remaining" in NxtResp2.keys():
            isForging = True
  




        payload = { "requestType" : "getAccountPublicKey" } #getTime"   }
        NxtApi = {}
        NxtApi['requestType'] =  payload['requestType'] # here we translate BTC params to NXT params
        NxtApi['account'] =  ACCOUNT
        #ACCOUNT = kwargs["account"] #kwargs['account']
        NxtReq.params=NxtApi # same obj, only replace params
        preppedReq = NxtReq.prepare()
        response = session.send(preppedReq)
        NxtResp3 = response.json()
        
        #print(str(NxtResp3))

        if "errorCode" in NxtResp3.keys():
            isvalid = False
        elif "publicKey" in NxtResp3.keys():
            isvalid = True
            
            
        Nxt2Btc = {}
        Nxt2Btc =  {
                    "isvalid" : isvalid,
                    "address" : ACCOUNT,
                    "ismine" : isForging
                    }
        
        return Nxt2Btc  


 
 
 

    @Request.application
    def application(self, request ):
        """    Nxt2Btc_Mapping_Comments
             1 BitcoinD Command/RPC	
             2 Parameters	
             3 Description	
             4 Requires unlocked wallet? (v0.4.0+)	
             5 Supported in nxtcoind v1.0	
             6 BitcoinD return format	
             7 NXT API	
             8 NXT format	
             9 Implementation Rules How to map a NXT API return to a XXXCOIND API return
            """
         
        response = JSONRPCResponseManager.handle(request.get_data(cache=False, as_text=True), dispatcher)
        return    Response(response.json, mimetype='application/json') 

    def run(self,):
        run_simple('localhost', 7879, self.application,  )
 
         
#        print("\n++++++###+" + str(request.__dir__()) +"++++\n")
#        print("\n++++++###+" + str(dispatcher.__dir__()) +"++++\n")
#        print("\n++++++###items+" + str(dispatcher.items()) +"++++\n")
#        print("\n++++++###keys+" + str(dispatcher.keys()) +"++++\n")
#        