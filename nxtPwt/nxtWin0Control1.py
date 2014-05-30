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

from PyQt4 import  Qt , QtGui,  QtCore
#from PyQt4.QtGui import  QMainWindow
from PyQt4.QtCore import  SIGNAL , QObject, pyqtSignal, pyqtSlot

# timer:
import os
import time

from requests import Request # as Request
from requests import Response  as Resp
from requests import   Session

import requests


#from werkzeug.wrappers import Request, Response
#from werkzeug.serving import run_simple


#from jsonrpc import JSONRPCResponseManager, dispatcher

from nxtPwt.nxtApiSigs import nxtApi


# obs: this apparently ccreates the werkzeug server right here when loading the app!
# 
###################################################################
#
# threading requests
#
#class JSON_Emitter(QObject):
#    """ - this is needed in QRunnable, because QRunnable is NOT able to emit signals. But this is. """    
#
#    JSONREPL = pyqtSignal(object  ,object) #  object1 is the request, object2 can carry meta data for use case logic 
#
#    def __init__(self,     meta  = {}): # meta is organizational meta data that client can use
#        super(QObject, self, ).__init__()
#        #self.jsonReq = jsonReq 
#         
#        #metaThread = copy(meta)
#        # NOTE: This MUST be done, otherwise the 'meta' object will only be ONE meta object (from the last query)
#        # that is referenced for EVERY query and the metaData of the earlier queries will be destroyed!!!!!!!!        
#        #del meta
#        #self.metaThread = metaThread
#
#         
#         
#         
#class JSON_Runner(QtCore.QRunnable):
#    """- This is what needs to be put into the QThreadpool """
#    nxtApi = nxtApi
#    
#    def __init__(self, emitter,  ):
#        super(QtCore.QRunnable, self).__init__()
#        self.emitter = emitter
#
#        #self.apiCalls = nxtQs()
#        #self.nxtApi = nxtApi
#        self.session = Session()
#        sessUrl =  'http://localhost:6876/nxt?' #self.sessMan.activeNRS.comp['url']
#        #print("sessUrl -  "+ str(sessUrl))
#        
#        #        auth = requests.auth.HTTPBasicAuth('','') # 'rpcuser',  'xcppw1234')
#        headers = {'content-type': 'application/json'}
#        # self.req = Request( method='GET', url = sessUrl, params = {})
#        #self.conn['url'] = sessUrl
#        #self.req = Request( method='POST', url = sessUrl, params = {}, headers = headers,       )
#        
#        #QObject.connect( self.nxtApi, SIGNAL("catchAll_Sig(PyQt_PyObject, PyQt_PyObject)"), self.testFun ) # all of them
#        
## check if this goes to class
## 
##        ##############
##    @dispatcher.add_method
##    def getState(**kwargs):
##
##        payload = { "requestType" : "getState"   }
##        # can do this fancy with the session object also
##        response = requests.post('http://localhost:6876/nxt?', params=payload)
##        
##        rawRes=response.json()
##        
##        return rawRes #kwargs["p1"] + kwargs["p2"]
##
##    @dispatcher.add_method
##    def getTime(**kwargs):
##        payload = { "requestType" : "getTime"   }
##        
##        response = requests.post('http://localhost:6876/nxt?', params=payload)
##        rawRes=response.json()
##        return rawRes #kwargs["p1"] + kwargs["p2"]
##
##    
##    @Request.application
##    def application(self, request ):
##        
##        response = JSONRPCResponseManager.handle(request.get_data(cache=False, as_text=True), dispatcher)
##        RR = Response(response.json, mimetype='application/json')
##        
##        return    RR           #finalRes #Response(jsonRes, mimetype='application/json')
#    # this sends this well-bahved reply to curl:
#    #azure@boxfish:~/workbench/nxtDev/BRIDGE$ curl -i -X POST -d '{"jsonrpc": "2.0", "method": "getTime", "params": { "par1": "val1","p2":"v2"}, "id": 12}' http://localhost:4000/jsonrpc
#    #HTTP/1.0 200 OK
#    #Content-Type: application/json
#    #Content-Length: 58
#    #Server: Werkzeug/0.9.4 Python/3.4.0
#    #Date: Mon, 26 May 2014 09:15:27 GMT
#    #
#    #{"jsonrpc": "2.0", "result": {"time": 15801327}, "id": 12}azure@boxfish:~/workbench/nxtDev/BRIDGE$ 
#    #
#
#    def run(self,):
#        
#        run_simple('localhost', 7878, self.application,  )
#
# 
# 
# 
# 
#
#class BridgeThread(QObject):
#
#    JSON_Sig  =  pyqtSignal(dict,dict)  #6
#    
#    
#    def __init__(self):
#        super(QObject, self).__init__( parent = None)
#        print("1")
#        self.qPool=QtCore.QThreadPool.globalInstance()
#        self.qPool.setMaxThreadCount(25) # robustness
#        #self.qPool.activeThreadCount() this is how many we have running?!
#    @pyqtSlot() # 61
#    def jsonServ_Slot(self, ):
#        """ - """
#        
#        #meta['qqLen'] = self.qPool.activeThreadCount() # this line is  for timing the delay in the # QThread to wait for the proper delay time
#
#        json_Emitter = JSON_Emitter()
#        self.json_Runner = JSON_Runner( json_Emitter, )
#
#        QObject.connect(self.json_Runner.emitter, SIGNAL("JSONRPL(PyQt_PyObject, PyQt_PyObject)"),self.JSON_Sig)
#        
#        self.qPool.start(self.json_Runner)
#
#
#
#
#





class nxtWin0Control(QObject):
    """ Main Window -- This init creates the entire structure of the app-object with the api and business logic utility classes
    
    0 connect buttons to open more windows  (main only)    
    1 INCOMING signals from UseCaseLogic - distribute to local widgets for display
    2 OUTGOING local signals from User input that are distributed via local callbacks to                  sessionManager
    3 register and activate useCases - widgets activated by user input send the activation signals to the UseCases
    4 developer access
    5 Activate useCase controllers - QTimer to local callbacks that then activate useCaseLogic
    6 Layout and visual appearance properties of the local widgets on this win
 


        """
    # usage:
    #self.emit( SIGNAL( "UC2activate(int)"), 42 )    # can  pass args!
    #self.app.emit(SIGNAL( "mySig(PyQt_PyObject)" ), myType )

    UC29changeConn_Sig = pyqtSignal(  object)
    UCTEST_activate = pyqtSignal( object)


    def __init__(self, app ):
        super(QObject, self, ).__init__()
        import nxtPwt.ui_nxtWin0 as MainWindow # the QtCreator-generated Widget.py!!
        # Reminder of namespaces
        # <nxtMainControl3.nxtMainControl instance at 0x26b0e18> this is nxtMainControl instance
        # HERE, THIS IS APP: <__main__.MainApplication instance at 0x1e15248> THE SAME AS IN THE CALLING MAIN
        #        
        ui = MainWindow.Ui_MainWindow() # Ui_MainWindow() is the autogenerated class in m2def.py
        self.ui_nxtWin0 = ui 
        self.app = app # we have full access to the QAppliucatoin object!
        print(str(self.app))
        self.localTimer1 = QtCore.QTimer() #  local TIMER
        self.localTime1 = 2000

        self.timerStrobe = QtCore.QTimer() #  local TIMER
        self.timeStrobe = 2000

        self.app.nxtWin0 = self # make this   WinControl1  known  in the app namespace.  When this Win throws sigs, they can be recvd anywhere where this isknown.

        #self.app.sessMan.uc29_changeConn.initWin0(self.app.nxtWin0, ui)
        self.state = app.sessMan.activeNRS.state # just to have the name shortewr
        self.block = app.sessMan.activeNRS.block # just to have the name shortewr
        self.account = app.sessMan.uc2_accHndlr.accRes   # just to have the name shortewr
        self.sessMan = app.sessMan
        self.NRSconn = app.sessMan.activeNRS

        # be able to receive Signals from UC1
        self.uc1 = self.app.sessMan.uc1_pollNRS
         
        
    def init(self):  
        """ Here all signals must be connected """  
        ui =  self.ui_nxtWin0 #self.ui_MainWin # only to save writing - maybe redundant
        #
        # devTest
        QtCore.QObject.connect(ui.pushButton_TESTBUTTON , SIGNAL("clicked()"), self.donateButton_CB )
        QObject.connect(self.timerStrobe, SIGNAL("timeout()"),  self.confLED1_strobe4)
        #
        #########################################
        ##########################################        
        # Connect Signals to Slots and Callbacks
        #########################################
        ##########################################        
        ###############################################################
        # 
        # 0 connect buttons to open more windows  (main only)        
        QtCore.QObject.connect(ui.pushButton_nxtWin1 , SIGNAL("clicked()"), self.openWin1 )
        QtCore.QObject.connect(ui.pushButton_nxtWin2 , SIGNAL("clicked()"), self.openWin2 )
        QtCore.QObject.connect(ui.pushButton_nxtWin2 , SIGNAL("clicked()"), self.openWin3 )
        QtCore.QObject.connect(ui.pushButton_nxtWin4 , SIGNAL("clicked()"), self.openWin4 )
        QtCore.QObject.connect(ui.pushButton_nxtWin5 , SIGNAL("clicked()"), self.openWin5 )
        QtCore.QObject.connect(ui.pushButton_nxtWin6 , SIGNAL("clicked()"), self.openWin6 )
        QtCore.QObject.connect(ui.pushButton_nxtWin7 , SIGNAL("clicked()"), self.openWin7 )
        #
        ##############################################################

        # testing ctrls for bridge
        QtCore.QObject.connect(ui.pb_test1 , SIGNAL("clicked()"), self.pb_test1_Clk )
        QtCore.QObject.connect(ui.pb_test2 , SIGNAL("clicked()"), self.pb_test2_Clk )
        QtCore.QObject.connect(ui.pb_test3 , SIGNAL("clicked()"), self.pb_test3_Clk )
        QtCore.QObject.connect(ui.pb_clearTextEditMSG , SIGNAL("clicked()"), self.pb_clearTextEditMSG_Clk )
        QtCore.QObject.connect(ui.pb_clearResponse_2 , SIGNAL("clicked()"), self.pb_clearResponse_2_Clk )
        
        QtCore.QObject.connect(ui.lineEdit_T1 ,    SIGNAL("returnPressed()"), self.lineEdit_T1_Clk)
        QtCore.QObject.connect(ui.lineEdit_T2 ,    SIGNAL("returnPressed()"), self.lineEdit_T2_Clk )
		 



        QObject.connect(self.state, SIGNAL("stateUpdate_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC1_displayNodeStateCB)
        QObject.connect(self.block, SIGNAL("blockUpdate_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC1_displayBlockCB)
        QObject.connect(self.account, SIGNAL("getAccountUpdate_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC2_getAccountUpdateCB )
        QObject.connect(self.NRSconn, SIGNAL("connErr_Sig(PyQt_PyObject, PyQt_PyObject)"), self.NRSconnErrCB )


        # TX monitoring:
        # for TX DOWNstream creation, we'll have a connect to where the receipt shall go
        QObject.connect(self.sessMan, SIGNAL("TX_sendMoney_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC4_TX_sendMoney_CB )
        QObject.connect(self.sessMan, SIGNAL("TX_setAccountInfo_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC2_TX_AccountInfo_CB )
        QObject.connect(self.sessMan, SIGNAL("TX_leaseBalance_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC2_TX_LeaseBalance_CB )






        # these are UPstream, i.e. appear in the Blockchain from elsewhere
        # this sig is generic for ALL TXs appearing on the blockchain
        QObject.connect(self.sessMan, SIGNAL("TX_status_Sig(PyQt_PyObject, PyQt_PyObject)"),self.UC3_TX_statusCB)

        # todo: change this to recv SIG from uc3, not from block itself!
        QObject.connect(self.block, SIGNAL("newTXs_Sig(PyQt_PyObject, PyQt_PyObject)"), self.UC3_TX_fromBlockchain_CB)

        # USER INPUTS:
        QtCore.QObject.connect(ui.gb_poll0,    SIGNAL("clicked()"), self.UC1_toggle) #
        QtCore.QObject.connect(ui.lineEdit_pollTimer0 ,    SIGNAL("returnPressed()"), self.UC1_mod)



        QtCore.QObject.connect(ui.cb_acctName , SIGNAL("clicked()"), self.UC2_setName1_Clk) # get extra confirmation button

        QtCore.QObject.connect(ui.lineEdit_passPhr, SIGNAL("returnPressed()"), self.UC2_newPassPhr_Init)
        QtCore.QObject.connect(ui.lineEdit_nxtServer, SIGNAL("returnPressed()"), self.UC1_newConn_Init)
        QtCore.QObject.connect(ui.pb_sendMoney , SIGNAL("clicked()"), self.UC4_sendMoney_Clk) # get extra confirmation button
 
        #QtCore.QObject.connect(ui.pb_startForging , SIGNAL("clicked()"), self.UC2_startForge_Clk) # get extra confirmation button
        #QtCore.QObject.connect(ui.pb_stopForging , SIGNAL("clicked()"), self.UC2_stopForge_Clk) # get extra confirmation button

        QtCore.QObject.connect(ui.gb_ForgeCtrl , SIGNAL("clicked()"), self.UC2_ForgeCtrl_Clk) # get extra confirmation button
        QtCore.QObject.connect(ui.pb_lease , SIGNAL("clicked()"), self.UC2_leaseBalance_Clk) # get extra confirmation button
 

        # sendMoney:
        QtCore.QObject.connect(ui.lineEdit_amount, SIGNAL("returnPressed()"), self.lineEdit_amount_CB)
        QtCore.QObject.connect(ui.lineEdit_amountNQT, SIGNAL("returnPressed()"), self.lineEdit_amount_CB)
        QtCore.QObject.connect(ui.lineEdit_fee, SIGNAL("returnPressed()"), self.lineEdit_fee_CB)
        QtCore.QObject.connect(ui.lineEdit_deadline, SIGNAL("returnPressed()"), self.lineEdit_deadline_CB)
        QtCore.QObject.connect(ui.lineEdit_recipient, SIGNAL("returnPressed()"), self.lineEdit_recipient_CB)

        # widget control
        QtCore.QObject.connect(ui.pb_clearText_2 , SIGNAL("clicked()"), self.clear_newTXs_CB) # get extra confirmation button


        ##################################################
        #  
        # 6 Layout and visual appearance properties of the local widgets on this win
        # local settings
        #
        ##############
        # init widgets        
        #blue = "#0000ff"
        #style_str = "QWidget {background-color: %s}"
        #ui.lcdNumber_time.setStyleSheet(style_str % blue)
        #ui.lcdNumber_time.setDigitCount(8)        #
        #ui.lcdNumber_time.setSegmentStyle(2)

        ui.lcdNumber_accBal.setDigitCount(9)        #
        ui.lcdNumber_accBal.setSegmentStyle(2)

        ui.lcdNumber_accBalNQT.setDigitCount(8)        #
        ui.lcdNumber_accBalNQT.setSegmentStyle(2)

        ui.lcdNumber_accBalUnconf.setDigitCount(9)        #
        ui.lcdNumber_accBalUnconf.setSegmentStyle(2)

        ui.lcdNumber_accBalUnconfNQT.setDigitCount(9)        #
        ui.lcdNumber_accBalUnconfNQT.setSegmentStyle(2)

        ui.lcdNumber_accBalEff.setDigitCount(9)        #
        ui.lcdNumber_accBalEff.setSegmentStyle(2)

        #
        self.blinkerCols = [Qt.Qt.darkYellow, Qt.Qt.magenta]
        self.strobeCols = [Qt.Qt.cyan, Qt.Qt.green]

        ui.kled_poll0.setColor(Qt.Qt.darkBlue)
        ui.kled_poll0.setColor(Qt.Qt.darkBlue)

        ui.kled_conf1.setColor(Qt.Qt.darkBlue)
        ui.gb_poll0.setChecked(True)
        # 
        ################################################
        #
        # init data entry widgets at startup. also display messages etc.
        #
        ################################################
        #        

        ui.lineEdit_nxtServer.setText(self.app.sessMan.activeNRS.comp['serverAddr'] )
        ui.lineEdit_pollTimer0.setText( str(self.app.sessMan.activeNRS.state.time1    )) # unused - self.app.sessMan.uc1_PollAcc.pollTime1 ))
        ui.lineEdit_account0.setText(self.app.sessMan.uc2_accHndlr.accRes.data['account'] )
        ui.lineEdit_passPhr.setText(self.app.sessMan.uc2_accHndlr.accRes.data['secretPhrase']  )
        ui.lineEdit_recipient.setText("2865886802744497404") # '0'
        ui.lineEdit_fee.setText("0")
        ui.lineEdit_deadline.setText("180" )
        ui.lineEdit_fee.setText('1'  )
        ui.lineEdit_feeNQT.setText('00000000'  )
        ui.lineEdit_amount.setText('0')
        ui.lineEdit_amountNQT.setText('00000000' )

        ui.tw_newTXs.setAlternatingRowColors(True)

        # disclaimer for alpha version

        #ui.lineEdit_TXid.setTextColor(Qt.Qt.darkGreen)

        ui.textEdit_response.setTextColor(Qt.Qt.red)
        ui.textEdit_response.setFontPointSize(14)
        ui.gb_ForgeCtrl.setChecked(False)
        #ui.lineEdit_amount.setColor(Qt.Qt.darkGreen)
        #ui.lineEdit_amount.setFontPointSize(12)

        # the 'leaseBalance func can be intergated into the regular GUI later
        ui.lineEdit_leaseRec.setText('0')
        ui.lineEdit_leasePer.setText('0')
        ui.lineEdit_leaseDeadline.setText('180')


        ui.lineEdit_logF.setText('nxtPwt_logL.txt')
        QtCore.QObject.connect(ui.gb_files,    SIGNAL("clicked()"), self.logF_toggle_Clk) #



        ##########################################################
        # MAINTENANCE ACCESS: just go directly to nxtWin6
        #self.app.openWin7()
        #self.app.openWin3()
        #self.app.openWin2()
        
        ui.textEdit_response.append("this is a beta version. \nplease read the release notes on Win1.")
 
 
    ####################################
    #
    # init is finished        
        #################################
        #################################
        #################################
        
        
        
    def pb_test1_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.append("start sever")
        
        mm = BridgeThread()
        mm.jsonServ_Slot()
    
        #run_simple('localhost', 4000, self.application, processes = 20 )#threaded=True )
        
        ui.textEdit_response_2.append("server startedtest1")

    def pb_test2_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.append("test1")
        ui.textEdit_response_2.append("test1")
        
    def pb_test3_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.append("test1")
        ui.textEdit_response_2.append("test1")
         
    def pb_clearTextEditMSG_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.clear()
      
    def pb_clearResponse_2_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response_2.clear()
 
    def lineEdit_T1_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.append("test1")
        ui.textEdit_response_2.append("test1")
        
    def lineEdit_T2_Clk(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.append("test1")
        ui.textEdit_response_2.append("test1")
         
 










###############

    def UC3_TX_fromBlockchain_CB(self, newTXs,  meta):
        ui = self.ui_nxtWin0
        for TX in newTXs:
            #ui.textEdit_newTXs.append("newTX: " + str(TX.cont['transaction']) +"\n" )
            ui.textEdit_newTXs.append("newTX_ID: " + str(meta) +"\n" )
            ui.textEdit_newTXs.append("newTX_ID: " + str(TX) +"\n" + str(meta) )

        ui.textEdit_newTXs.append("\n~~~~~~~~~~~~~~~~~~~\n")

        #for newTX in newTXs:
            #print(str(newTX) + " in win0!")

    def NRSconnErrCB(self, errReply, meta):
        ui = self.ui_nxtWin0
        ui.kled_connActive.setColor(Qt.Qt.red)

    def UC3_TX_statusCB(self, TX_cont, meta): # status update for polled TXs
        ui = self.ui_nxtWin0
        ui.textEdit_newTXs.append( "\n###############\n\n" + str(time.asctime()) )
        try:
            if TX_cont['confirmations'] > 6:
                self.confLED1_strobe1()
        except:
            pass #self.confLED1_notOK(200)
        ui.textEdit_newTXs.append("TX id: " + TX_cont['transaction'])
        try:
            ui.textEdit_newTXs.append("TX confs: " + str(TX_cont['confirmations']) )
        except:
            ui.textEdit_newTXs.append("TX poll - TX not in BC yet" )
            #print(" self.sessMan.uc2_accHndlr.residAcc.TXs: " + str(self.sessMan.uc2_accHndlr.residAcc.TXs))
    # this is where we receive filtered TXs from blockchain filter to display selectively etc


    def clear_newTXs_CB(self):
        ui = self.ui_nxtWin0
        ui.textEdit_newTXs.clear()

    def UC1_displayNodeStateCB(self, nodeState, meta):
        #receive from uc1
        ui = self.ui_nxtWin0

        ui.kled_poll0.setColor(self.blinkerCols[0]) # activity indicator
        self.blinkerCols.reverse()
        try:
            ui.kled_connActive.setColor(Qt.Qt.green)
            self.ui_nxtWin0.label_state_timeD.setNum( nodeState['time'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfBlocksD.setNum( nodeState['numberOfBlocks'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfTransactionsD.setNum( nodeState['numberOfTransactions'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfOrdersD.setNum( nodeState['numberOfOrders'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfAssetsD.setNum( nodeState['numberOfAssets'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfAccountsD.setNum(nodeState['numberOfAccounts'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfAliasesD.setNum(nodeState['numberOfAliases'] ) ################## ok
            self.ui_nxtWin0.label_state_totalEffectiveBalanceD.setNum( nodeState['totalEffectiveBalanceNXT'] ) ################## ok
            self.ui_nxtWin0.label_state_availableProcessorsD.setNum( nodeState['availableProcessors'] ) ################## ok
            self.ui_nxtWin0.label_state_totalMemoryD.setNum(nodeState['totalMemory'] ) ################## ok
            self.ui_nxtWin0.label_state_freeMemoryD.setNum(nodeState['freeMemory'] ) ################## ok
            self.ui_nxtWin0.label_state_maxMemoryD.setNum(nodeState['maxMemory'] ) ################## ok
            self.ui_nxtWin0.label_state_numberOfPeersD.setNum(nodeState['numberOfPeers'] ) ################## ok
            self.ui_nxtWin0.label_state_lastBlockchainFeederD.setText(nodeState['lastBlockchainFeeder'] ) ################## ok
            self.ui_nxtWin0.label_state_lastBlockD.setText(nodeState['lastBlock'] ) ################## ok
            self.ui_nxtWin0.label_state_cumulDiffD.setText( nodeState['cumulativeDifficulty'] ) ################## ok
            self.ui_nxtWin0.label_state_versionD.setText( nodeState['version'] ) ################## ok
            self.ui_nxtWin0.label_state_numUnlAccsD.setNum(nodeState['numberOfUnlockedAccounts'] ) ################## ok
            self.ui_nxtWin0.label_state_numPollsD.setNum(nodeState['numberOfPolls'] ) ################## ok
            self.ui_nxtWin0.label_state_numVotesD.setNum(nodeState['numberOfVotes'] ) ################## ok
            self.ui_nxtWin0.label_state_numTradesD.setNum(nodeState['numberOfTrades'] ) ################## ok

            self.ui_nxtWin0.label_block_addressD.setText( nodeState['lastBlock'] ) #  'lastBlock': '18032658041779838502'
        except:
            ui.kled_connActive.setColor(Qt.Qt.red)
            #cou=1
            # for key in nodeState:
            #     print(str(cou) + " - " + key +" - " +  str(nodeState[key]))
            #     cou+=1
        example = """
                1 - numberOfOrders - 0 - <class 'int'>
                2 - cumulativeDifficulty - 2309742228091435 - <class 'str'>
                3 - numberOfAliases - 61321 - <class 'int'>
                4 - version - 0.9.8e - <class 'str'>
                5 - numberOfUnlockedAccounts - 0 - <class 'int'>
                6 - totalMemory - 651165696 - <class 'int'>
                7 - numberOfAccounts - 25103 - <class 'int'>
                8 - numberOfTrades - 0 - <class 'int'>
                9 - numberOfBlocks - 75536 - <class 'int'>
                10 - numberOfAssets - 0 - <class 'int'>
                11 - numberOfVotes - 0 - <class 'int'>
                12 - numberOfTransactions - 132265 - <class 'int'>
                13 - numberOfPolls - 0 - <class 'int'>
                14 - maxMemory - 954728448 - <class 'int'>
                15 - lastBlockchainFeeder - 209.126.73.158 - <class 'str'>
                16 - freeMemory - 76531408 - <class 'int'>
                17 - time - 12781663 - <class 'int'>
                18 - numberOfPeers - 25 - <class 'int'>
                19 - totalEffectiveBalanceNXT - 941066422 - <class 'int'>
                20 - lastBlock - 7353381867603648155 - <class 'str'>
                21 - availableProcessors - 4 - <class 'int'>
                """

    def UC1_displayBlockCB(self, block, meta):
        ui = self.ui_nxtWin0
        try:
            self.ui_nxtWin0.label_block_generationSignatureD.setText( block['generationSignature'] )
            #
            self.ui_nxtWin0.plainTextEdit_blockSigD.clear()
            self.ui_nxtWin0.plainTextEdit_TXsD.clear()
            self.ui_nxtWin0.plainTextEdit_blockSigD.appendPlainText( block['blockSignature'] )
            self.ui_nxtWin0.plainTextEdit_TXsD.appendPlainText( str(block['transactions'] ))
            #
            self.ui_nxtWin0.label_block_previousBlockHashD.setText( block['previousBlockHash'] )
            self.ui_nxtWin0.label_block_totalFeeNQTD.setText( block['totalFeeNQT'] )
            self.ui_nxtWin0.label_block_totalAmountNQTD.setText( block['totalAmountNQT'] )
            self.ui_nxtWin0.label_block_numberOfTransactionsD.setNum( block['numberOfTransactions'] )
            self.ui_nxtWin0.label_block_heightD.setNum( block['height'] )
            self.ui_nxtWin0.label_block_generatorD.setText( block['generator'] )
            self.ui_nxtWin0.label_block_timeD.setNum( block['timestamp'] )
            #
            try:
                self.ui_nxtWin0.label_block_nextBlockD.setText( block['nextBlock'] )

            except Exception as inst:
                self.ui_nxtWin0.label_block_nextBlockD.setText( 'this is the last block' )
                #print("no nextBlock?" + str(inst))
            self.ui_nxtWin0.label_block_prevBlockD.setText( block['previousBlock'] )
            #
            self.ui_nxtWin0.label_block_payloadLengthD.setNum( block['payloadLength'] )
            self.ui_nxtWin0.label_block_paylHashD.setText( block['payloadHash'] )
            self.ui_nxtWin0.label_block_baseTargetD.setText( block['baseTarget'] )
            self.ui_nxtWin0.label_block_versionD.setNum( block['version'] )
        except:
            ui.kled_connActive.setColor(Qt.Qt.red)

        example =  """
            1 - numberOfTransactions - 0 - <class 'int'>
            2 - height - 75522 - <class 'int'>
            3 - generationSignature - 5b5fae93379c3558173ef796ca77be7d73f50fa34b2364adbb6d1e24f0b238e1 - <class 'str'>
            4 - totalAmountNQT - 0 - <class 'str'>
            5 - totalFeeNQT - 0 - <class 'str'>
            6 - version - 2 - <class 'int'>
            7 - previousBlockHash - 23a22c3bd924885f12a0c56d23d086210c6deab27c5926893913b8f25f501aa9 - <class 'str'>
            8 - previousBlock - 6883792545855087139 - <class 'str'>
            9 - timestamp - 12780571 - <class 'int'>
            10 - transactions - [] - <class 'list'>
            11 - generator - 4747512364439223888 - <class 'str'>
            12 - payloadLength - 0 - <class 'int'>
            13 - payloadHash - e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 - <class 'str'>
            14 - baseTarget - 2134001905 - <class 'str'>
            15 - blockSignature - 02633870047e7ed7cb810ab4e042a29b24abf21599e51d3b7b18d127cbe7e001f4706dfd36e35f
            """


    def UC2_getAccountUpdateCB(self, reply, meta):
        ui = self.ui_nxtWin0
        self.account = meta['activeAccount']
        Nqt=self.account.balance.Nqt
        Nxt=self.account.balance.Nxt
        NqtU=self.account.balanceU.Nqt
        NxtU=self.account.balanceU.Nxt
        NxtEff=self.account.balanceEff
        ui.lcdNumber_accBal.display(Nxt)       #
        ui.lcdNumber_accBalNQT.display(Nqt)       #
        ui.lcdNumber_accBalUnconf.display(NxtU)   #
        ui.lcdNumber_accBalUnconfNQT.display(NqtU)
        ui.lcdNumber_accBalEff.display(NxtEff)
        ui.lineEdit_publicKey.setText(self.account.publicKey)

        if self.account.name != 'unknown':
            ui.lineEdit_account0Name.setText(self.account.name)
            ui.lineEdit_acctDescr.setText(self.account.description)
            ui.kled_acctName.setColor(Qt.Qt.green)
        else:
            ui.lineEdit_account0Name.setText(self.account.name)
            ui.lineEdit_acctDescr.setText(self.account.description)
            ui.kled_acctName.setColor(Qt.Qt.red)

        if self.account.publicKey == 'account has no pubKey':
            ui.kled_acctExists.setColor(Qt.Qt.green)
            ui.kled_acctUnlocked.setColor(Qt.Qt.red)
            try:

                Nqt=self.account.balance.Nqt
                Nxt=self.account.balance.Nxt
                NqtU=self.account.balanceU.Nqt
                NxtU=self.account.balanceU.Nxt
                NxtEff=self.account.balanceEff
                ui.lcdNumber_accBal.display(Nxt)       #
                ui.lcdNumber_accBalNQT.display(Nqt)       #
                ui.lcdNumber_accBalUnconf.display(NxtU)   #
                ui.lcdNumber_accBalUnconfNQT.display(NqtU)
                ui.lcdNumber_accBalEff.display(NxtEff)
                ui.lineEdit_publicKey.setText(self.account.publicKey)
            except:
                print("no amount in account")

        else:
            ui.kled_acctExists.setColor(Qt.Qt.green)
            ui.kled_acctUnlocked.setColor(Qt.Qt.green)

        ui.lineEdit_account0.setText(self.account.data['account'] )




        ui.lineEdit_remaining.setText(self.account.forgeRem)
        ui.lineEdit_ForgeDeadline.setText(self.account.forgeDeadline)



    def UC2_ForgeCtrl_Clk(self):
        ui = self.ui_nxtWin0
        if ui.gb_ForgeCtrl.isChecked():
            #print("F ON")
            self.sessMan.uc2_accHndlr.startForge()

        else:
            #print("F OFF")
            self.sessMan.uc2_accHndlr.stopForge()
            




    def UC2_newPassPhr_Init(self):
        ui = self.ui_nxtWin0
        newPW = ui.lineEdit_passPhr.text()
        self.sessMan.uc2_accHndlr.changeResidAccount(newPW)
        self.confLED1_ma()



    def logF_toggle_Clk(self):
        ui = self.ui_nxtWin0
        if ui.gb_files.isChecked():
            self.sessMan.logShort = True
            print(str(self.sessMan.logShort))
        else:
            self.sessMan.logShort = False
            print(str(self.sessMan.logShort))



    #########################
    #
    # UseCase1 - timer, get basicData, getState, get latestBlock
    #
    def UC1_toggle(self):
        ui = self.ui_nxtWin0
        if ui.gb_poll0.isChecked():

            meta={'caller':'uc1_single'}
            self.state.poll1Single( meta  )
            ui.kled_poll0.setColor(self.blinkerCols[0]) # activity indicator
            self.state.timer1.start( self.state.time1 )

        else:
            ui.kled_poll0.setColor(Qt.Qt.darkBlue)
            ui.kled_connActive.setColor(Qt.Qt.darkBlue)
            self.state.timer1.stop( )


    def UC1_mod(self,):
        ui = self.ui_nxtWin0
        #print("MOD" +ui.lineEdit_pollTimer0.text())
        self.state.timer1.stop()
        self.state.time1 = int(ui.lineEdit_pollTimer0.text())
        self.state.timer1.start( self.state.time1 )


    def UC1_newConn_Init(self):
        ui = self.ui_nxtWin0
        newUrl=ui.lineEdit_nxtServer.text()
        newUrl = newUrl.split('/')
        newComp = {}
        if newUrl[0] == 'http:':
            newComp['protocoll'] = 'http://' #
            print(newUrl)
        elif newUrl[0]=='https:':
            print(newUrl)
            newComp['protocoll'] = 'https://' #
        newHostLong = newUrl[2].split(':')
        newHost=newHostLong[0]
        newPort=newHostLong[1]
        newUrl = newComp['protocoll'] + newHost + ':' + newPort + "/nxt?"
        self.sessMan.uc29_changeConn.changeConn(newUrl)




    #########################
    #
    #
    # UseCase4 SEND

    def UC4_sendMoney_Clk(self): # send money or set name

        ui = self.ui_nxtWin0

        if ui.cb_acctName.isChecked():
            self.UC2_setName2_Clk() #divert!


        else:
            TXparms={}
            if (ui.lineEdit_amount.text()  == '0') and (  ui.lineEdit_amountNQT.text() == '00000000' ):
                #ui.textEdit_response.append("no amount set!\n" )
                ui.lineEdit_amount.setText("no Amount!")
                self.confLED1_notOK()
                return None

            if ( len(ui.lineEdit_amount.text())   > 9) or (  len(ui.lineEdit_amountNQT.text()) > 8 ):
                ui.lineEdit_amount.setText("Amount too long?!")
                self.confLED1_notOK()
                return None


            if ui.lineEdit_recipient.text() == '0':
                #ui.textEdit_response.append("no recipient specified!\n" )
                ui.lineEdit_recipient.setText("no recipient!")
                self.confLED1_notOK()
                return None

            if ui.lineEdit_fee.text() == '0':
                #ui.textEdit_response.append("no fee specified!\n" )
                ui.lineEdit_fee.setText("no Fee!")
                self.confLED1_notOK()
                return None

            if ui.lineEdit_deadline.text() == '0':
                #ui.textEdit_response.append("no deadline specified!\n" )
                ui.lineEdit_deadline.setText("no deadline!")
                self.confLED1_notOK()
                return None

            else:
                amountNQT =ui.lineEdit_amountNQT.text()
                amountNQT = (8 - len(amountNQT)) * '0' + amountNQT # zero padding!
                amountNXT = ui.lineEdit_amount.text()
                self.amountTOT = amountNXT + amountNQT
                TXparms['amountNQT'] = self.amountTOT
                TXparms['recipient'] = ui.lineEdit_recipient.text()
                feeNQT =ui.lineEdit_feeNQT.text()
                feeNXT=ui.lineEdit_fee.text()
                TXparms['feeNQT'] = feeNXT + feeNQT
                TXparms['deadline'] =ui.lineEdit_deadline.text()
                self.confLED1_cy()

                self.sessMan.uc4_sendMoney.sendMoney(TXparms)
                # prep UC4:


    # RECEIVE REPLY
    def UC4_TX_sendMoney_CB(self, TX, meta):
        ui = self.ui_nxtWin0
        for key in TX.crypt1:
            ui.textEdit_newTXs.append("sendMoney " + key + " -" + str(TX.crypt1[key]) +"\n" )
        ui.textEdit_newTXs.append(  str(time.asctime() + "\n###############\n"))
        TX_ID = TX.crypt1['transaction']
        ui.lineEdit_TXid.setText(TX_ID )
        ui.lineEdit_recipient.setText("0")
        #self.sessMan.logFshort.write(TX_ID + " - sendMoney - " + str(time.asctime()) +  "\n")
        #self.sessMan.logFlong.write(TX_ID +  str(time.asctime()) + "\n")

        self.confLED1_OK()

        # this is where we receive a send money TX! from sessMan


    def UC2_TX_AccountInfo_CB(self, TX, meta):
        ui = self.ui_nxtWin0
        for key in TX.crypt1:
            ui.textEdit_newTXs.append("setName " + key + " -" + str(TX.crypt1[key]) +"\n" )
        ui.textEdit_newTXs.append(  str(time.asctime() + "\n###############\n"))
        TX_ID = TX.crypt1['transaction']
        ui.lineEdit_TXid.setText(TX_ID )
        ui.lineEdit_recipient.setText("0")
        self.confLED1_OK()



    def UC2_TX_LeaseBalance_CB(self,TX, meta):
        ui = self.ui_nxtWin0
        TX_ID = TX.crypt1['transaction']
        ui.lineEdit_TXid.setText(TX_ID )
        print("w0 - UC2_TX_LeaseBalance_CB - " + str(TX))
        self.confLED1_OK()



    def UC2_leaseBalance_Clk(self):
        ui = self.ui_nxtWin0

        TXparms={}
        TXparms['recipient'] = ui.lineEdit_leaseRec.text()
        TXparms['period'] = ui.lineEdit_leasePer.text()

        feeNXT=ui.lineEdit_fee.text()
        feeNQT =ui.lineEdit_feeNQT.text()

        TXparms['feeNQT'] = feeNXT + feeNQT
        TXparms['deadline'] =ui.lineEdit_leaseDeadline.text()

        self.confLED1_cy()
        self.sessMan.uc2_accHndlr.leaseBalance( TXparms )

#
#
# ToDo: setAccountINfo is UC2 not UC4 !!!!!!!!!!!!!!!!!!! later
#
    def UC2_setName2_Clk(self):
        ui = self.ui_nxtWin0
        self.confLED1_cy()
        ui.pb_sendMoney.setText("send Money")
        ui.cb_acctName.setCheckState(False)
        ui.kled_acctName.setColor(Qt.Qt.green)
        TXparms={}
        TXparms['name'] = ui.lineEdit_account0Name.text()
        TXparms['description'] = ui.lineEdit_acctDescr.text()

        feeNXT=ui.lineEdit_fee.text()
        feeNQT =ui.lineEdit_feeNQT.text()

        TXparms['feeNQT'] = feeNXT + feeNQT
        TXparms['deadline'] =ui.lineEdit_deadline.text()

        for k in TXparms:
            print(k + TXparms[k])

        self.sessMan.uc2_accHndlr.setAccountInfo( TXparms )

    def UC2_setName1_Clk(self):
        ui = self.ui_nxtWin0
        if not ui.cb_acctName.isChecked(): # was on , is off nOW
            ui.pb_sendMoney.setText("send Money")

            self.account.poll1Start({'caller':'win0 restarted by cb setName off'} )
            ui.kled_acctName.setColor(Qt.Qt.green)
            return None # LEAVE HERE!


        elif ui.cb_acctName.isChecked():
            self.account.poll1Stop() #{'caller':'win0 stopped by cb setName off'}

            ui.kled_acctName.setColor(Qt.Qt.red)
            ui.pb_sendMoney.setText("set Name")

        # setIcon(). If t


        if ui.lineEdit_account0Name.text() == '':
            ui.lineEdit_account0Name.setText("no Name specified!")
            self.confLED1_notOK()
            return None

        if ui.lineEdit_acctDescr.text() == '':
            ui.lineEdit_acctDescr.setText("no Description specified!")
            self.confLED1_notOK()
            return None
        # can add mor checks like fee deadline etc






 ##############
 ##############
 ##############
 ##############




    def lineEdit_recipient_CB(self):
        ui =  self.ui_nxtWin0
        self.recipient = ui.lineEdit_recipient.text()
        self.confLED1_cy()
        
    def lineEdit_amount_CB(self):
        ui =  self.ui_nxtWin0
        self.amountNQT =ui.lineEdit_amountNQT.text()
        self.amountNQT = (8 - len(self.amountNQT)) * '0' + self.amountNQT # zero padding!
        self.amountNXT=ui.lineEdit_amount.text()
        self.amountTOT = self.amountNXT + self.amountNQT
        self.confLED1_cy()
        
    def lineEdit_fee_CB(self):
        ui =  self.ui_nxtWin0
        self.feeNQT = ui.lineEdit_fee.text()
        self.confLED1_cy()
        
    def lineEdit_deadline_CB(self):
        ui =  self.ui_nxtWin0
        self.deadline = ui.lineEdit_deadline.text()
        self.confLED1_cy()

    def confLED1_strobe1(self):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(Qt.Qt.cyan)
        self.strobeC=0
        self.timerStrobe.start(100)

    def confLED1_strobe4(self):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(self.strobeCols[0])
        self.strobeCols.reverse()
        self.strobeC += 1
        if self.strobeC > 25:
            self.strobeC = 0
            self.timerStrobe.stop()
            self.confLED1_OK()

    def confLED1_OK(self, fTime = 1000):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(Qt.Qt.green)
        self.localTimer1.singleShot(fTime,self.confLED1_off)

    def confLED1_cy(self):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(Qt.Qt.cyan)
        self.localTimer1.singleShot(500,self.confLED1_off)
      
    def confLED1_ma(self):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(Qt.Qt.magenta)
        self.localTimer1.singleShot(1000,self.confLED1_off)
    
    def confLED1_notOK(self, fTime = 1000):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(Qt.Qt.red)
        self.localTimer1.singleShot(fTime,self.confLED1_off)
    
    def confLED1_off(self):
        ui = self.ui_nxtWin0
        ui.kled_conf1.setColor(Qt.Qt.darkBlue)
        
    def clearText(self):
        ui = self.ui_nxtWin0
        ui.textEdit_response.clear()
        disclaimer2 = "Thank You. \n\n Enter passphrase above and hit <return>"
        ui.textEdit_response.append( disclaimer2)
        
          
    #
          #
          # There are EIGHT user-input lineEdits on this window
          #
          # There 15 user-pressable PBs on theis window
    ############################################
    # local data entry widgets send newly entered data to nxtSessionBroker. callbacks:
    ############
         #        
    def lineEdit_nxtServerCB(self):
        ui = self.ui_nxtWin0  
        self.server = ui.lineEdit_nxtServer.text()   
        self.app.sessMan.activeNRS.comp['serverP'] = ui.lineEdit_nxtServer.text()
        self.app.sessMan.activeNRS.comp['url'] = self.app.sessMan.activeNRS.comp['serverP'] + "/nxt?"  
        self.emit( SIGNAL( "UC29changeConn_Sig(PyQt_PyObject)"), str(self.app.sessMan.activeNRS.comp['serverP']))# str(self.app.sessMan.activeNRS.comp['serverP']) )    # 
        self.confLED1_cy()
        # NEW SESSION OBJECT! 
        # now make new req object
        # make kled blink for 500ms!

         
          
    def donateButton_CB(self):
        ui =  self.ui_nxtWin0
        self.confLED1_strobe1()
        ui.lineEdit_recipient.setText( '1674414626317090683')
        ui.lineEdit_fee.setText('1')
        ui.lineEdit_deadline.setText('180')
        ui.lineEdit_amount.setText('APPRECIATED!')
        #self.confLED1_cy()
        
        
        
############################
############################        
############################
########## Window Maintenance

    def show(self):
        self.uiFrame = QtGui.QMainWindow()
        self.ui_nxtWin0.setupUi(self.uiFrame)
        self.init()
        self.uiFrame.show()

    def openWin1(self):
        """ openWin1  """
        self.app.openWin1( ) #
    
    def openWin2(self):
        """ openWin2  """
        self.app.openWin2( ) #
        
    def openWin3(self):
        """ openWin3  """
        self.app.openWin3( ) #
    
    def openWin4(self):
        """ openWin4  """
        self.app.openWin4( ) #

    def openWin5(self):
        """ openWin5  """
        self.app.openWin5( ) #

    def openWin6(self):
        """ openWin6  """
        self.app.openWin6(  ) #

    def openWin7(self):
        """ openWin7  """
        self.app.openWin7(  ) #





