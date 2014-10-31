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

#


class nxtQs(object):
    """ python dict as container object for all NRS query prototypes. use these to compose queries """

    def __init__(self):

        #1
        self.broadcastTransaction= {
                                        "requestType" : "broadcastTransaction" , \
                                        "transactionJSON" : "transactionJSON" ,\
                                        "transactionBytes" : "transactionBytes"
                                        }

        #"priceNQT" : "" , \ buyAlias does not have a price any more ?!?!?!

        self.buyAlias = {
                                        "requestType" : "buyAlias" , \
                                        "alias" : "" , \
                                        "aliasName" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "",\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": ""
                                        }


        self.calculateFullHash = {
                                        "requestType" : "calculateFullHash", \
                                        "unsignedTransactionBytes" : "" , \
                                        "signatureHash" : ""
        }

        self.cancelAskOrder= {
                                        "requestType" : "cancelAskOrder" , \
                                        "secretPhrase" : "PASSPHRASE" ,\
                                        "order" : "ORDERID" ,\
                                        "deadline" : "DEADLINE",\
                                        "publicKey":"",\
                                        "feeNQT" : "100000000" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": ""
                                         }
        #4
        self.cancelBidOrder= {
                                        "requestType" : "cancelBidOrder" , \
                                        "secretPhrase" : "PASSPHRASE",\
                                        "order" : "ORDERID",\
                                        "deadline" : "DEADLINE" ,\
                                        "publicKey":"",\
                                        "feeNQT" : "100000000" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": ""
                                         }
        #5
        self.castVote ={                "requestType" : "castVote",\
                                        "publicKey":"",\
                                        "secretPhrase" : "PASSPHRASE"   ,\
                                        "poll" : "enterID" , \
                                        "deadline" : "DEADLINE",\
                                        "vote1" : "enterVote" ,\
                                        "vote2" : "enterVote" ,\
                                        "vote3" : "enterVote" ,\
                                        "feeNQT" : "100000000", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": ""
                                        }

         # DEBUG API!!!
        self.clearUnconfirmedTransactions = {
                                        "requestType" : "clearUnconfirmedTransactions"
                                        }


        #6
        self.createPoll ={              "requestType" : "createPoll", \
                                        "publicKey":"",\
                                        "name" : "name" , \
                                        "description" : "description", \
                                        "option1" : "TODO:MAKE LIST1 ",\
                                        "option2" : "TODO:MAKE LIST2 ",\
                                        "option3" : "TODO:MAKE LIST3 ",\
                                        "minNumberOfOptions" : "",\
                                        "maxNumberOfOptions" : "",\
                                        "deadline" : "deadline",\
                                        "feeNQT" : "100000000",\
                                        "secretPhrase" : "secretPhrase"   ,\
                                        "optionsAreBinary" : "true",\
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": ""
                                         }
        #7
        self.decodeHallmark= {
                                        "requestType" : "decodeHallmark" , \
                                        "hallmark" : "HEXSTRING"
                                        }
        #8
        self.decodeToken= {
                                        "requestType" : "decodeToken" , \
                                        "website" :"WEBSITE" ,\
                                        "token" : "AUTHSTRING"
                                        }

        self.decryptFrom = {
                                        "requestType" : "decryptFrom", \
                                        "account" : "" , \
                                        "data" : "" , \
                                        "nonce" : "" , \
                                        "secretPhrase" : "",\
                                        "decryptedMessageIsText": ""
                                         }

        self.dgsDelisting = {
                                        "requestType" : "dgsDelisting", \
                                        "goods" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\

                }

        self.dgsDelivery = {
                                        "requestType" : "dgsDelivery", \
                                        "purchase" : "" , \
                                        "discountNQT" : "" , \
                                        "goodsData" : "" , \
                                        "goodsText" : "" , \
                                        "encryptedGoodsData" : "" , \
                                        "encryptedGoodsNonce" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                }

        self.dgsFeedback = {
                                        "requestType" : "dgsFeedback", \
                                        "purchase" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                }

        self.dgsListing = {
                                        "requestType" : "dgsListing", \
                                        "name" : "" , \
                                        "description" : "" , \
                                        "tags" : "" , \
                                        "quantity" : "" , \
                                        "priceNQT" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\

                }
        self.dgsPriceChange = {
                                        "requestType" : "dgsPriceChange", \
                                        "goods" : "" , \
                                        "priceNQT" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                }
        self.dgsPurchase = {
                                        "requestType" : "dgsPurchase", \
                                        "goods" : "" , \
                                        "priceNQT" : "" , \
                                        "quantity" : "" , \
                                        "deliveryDeadlineTimestamp" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                }

        self.dgsQuantityChange = {
                                        "requestType" : "dgsQuantityChange", \
                                        "goods" : "" , \
                                        "deltaQuantity" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                }

        self.dgsRefund = {
                                        "requestType" : "dgsRefund", \
                                        "purchase" : "" , \
                                        "refundNQT" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                        }
        self.encryptTo = {
                                        "requestType" : "encryptTo", \
                                        "recipient" : "" , \
                                        "messageToEncrypt": "" ,\
                                        "messageToEncryptIsText": "" ,\
                                        "secretPhrase" : ""
                                        }


        #9 # DEBUG API!!!
        self.fullReset = {
                                        "requestType" : "fullReset" ,  \
                                        }

        #9
        self.generateToken = {
                                        "requestType" : "generateToken" ,  \
                                        "website" : "WEBSITE", \
                                        "secretPhrase" : "PASSPHRASE"
                                        }
        #10
        self.getAccount = {
                                        "requestType" : "getAccount" , \
                                        "account" : "account"
                                        }
        #11
        self.getAccountBlockIds= {
                                        "requestType" : "getAccountBlockIds" , \
                                        "account" : "ACCNUM",\
                                        "timestamp" : "0",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }

        self.getAccountBlocks= {
                                        "requestType" : "getAccountBlocks" , \
                                        "account" : "ACCNUM",\
                                        "timestamp" : "0",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "includeTransactions" : "true"
                                        }


        #12
        self.getAccountCurrentAskOrderIds= {
                                        "requestType" : "getAccountCurrentAskOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }


        self.getAccountCurrentAskOrders= {
                                        "requestType" : "getAccountCurrentAskOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }



        #13
        self.getAccountCurrentBidOrderIds= {
                                        "requestType" : "getAccountCurrentBidOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }

        self.getAccountCurrentBidOrders= {
                                        "requestType" : "getAccountCurrentBidOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }

        #14
        self.getAccountLessors = {
                                        "requestType" : "getAccountLessors" ,  \
                                        "account" : "account",   \
                                        "height" : ""
                                        }


        #14
        self.getAccountId = {
                                        "requestType" : "getAccountId" ,  \
                                        "secretPhrase" : "secretPhrase",   \
                                        "publicKey" : "publicKey"
                                        }
        #15
        self.getAccountPublicKey= {
                                        "requestType" : "getAccountPublicKey" , \
                                        "account" : "ACCNUM"
                                        }

# HERE CHANGE

        #16
        self.getAccountTransactionIds= {
                                        "requestType" : "getAccountTransactionIds" , \
                                        "account":       "ACCNUM", \
                                        "timestamp" : "0",\
                                        "type": "",\
                                        "subtype":"" ,\
                                        "firstIndex" : "" ,\
                                        "lastIndex":"",\
                                        "numberOfConfirmations": ""
                                        }


        #16
        self.getAccountTransactions= {
                                        "requestType" : "getAccountTransactions" , \
                                        "account":       "ACCNUM", \
                                        "timestamp" : "0",\
                                        "type": "",\
                                        "subtype":"" ,\
                                        "firstIndex" : "" ,\
                                        "lastIndex":"",\
                                        "numberOfConfirmations": ""
                                        }
# HERE CHANGE
        #17
        self.getAlias = {
                                        "requestType" : "getAlias" , \
                                        "alias" : "aliasId"
                                        }

        self.getAliases = {
                                        "requestType" : "getAliases", \
                                        "timestamp" : "" , \
                                        "account" : "",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }
        #56
        self.getAllAssets = {
                                        "requestType" : "getAllAssets",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }
        #21
        self.getAllOpenAskOrders= {
                                        "requestType" : "getAllOpenAskOrders" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }

        self.getAllOpenBidOrders= {
                                        "requestType" : "getAllOpenBidOrders" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }


        #22
        self.getAllTrades= {
                                        "requestType" : "getAllTrades" , \
                                        "timestamp" : "0",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "includeAssetInfo" : "true"
                                         }
        #23
        self.getAskOrder= {
                                        "requestType" : "getAskOrder" , \
                                        "order" : "ORDERID"
                                        }
        #24
        self.getAskOrderIds= {
                                        "requestType" : "getAskOrderIds" , \
                                        "asset" : "assetId", \
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }

        self.getAskOrders = {
                                        "requestType" : "getAskOrders", \
                                        "asset" : "" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                }
        #25
        self.getAsset = {
                                        "requestType" : "getAsset" ,\
                                        "asset" : "ASSETID"
                                        }



        self.getAssetAccounts = {
                                        "requestType" : "getAssetAccounts", \
                                        "asset" : "" , \
                                        "height" : "",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                }


        #26
        self.getAssetIds= {
                                        "requestType" : "getAssetIds",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                         }


        self.getAssetTransfers= {
                                        "requestType" : "getAssetTransfers",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "asset" : "" ,\
                                        "account" : "" ,\
                                        "includeAssetInfo" : "true"
                                         }


        #57
        self.getAssets = {
                                        "requestType" : "getAssets" ,  \
                                        "assets" : "assets",\
                                        "assets" : "assets",\
                                        "assets" : "etc"
                                        }

        self.getAssetsByIssuer = {
                                        "requestType" : "getAssetsByIssuer", \
                                        "account" : "" , \
                                        "account" : "" , \
                                        "account" : "",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                }
         #28


        self.getBalance = {
                                        "requestType" : "getBalance", \
                                        "account" : "ACCNUM" \
                                    }
        #29
        self.getBidOrder= {
                                        "requestType" : "getBidOrder" , \
                                        "order" : "ORDERID"
                                        }
        #30
        self.getBidOrderIds= {
                                        "requestType" : "getBidOrderIds" , \
                                        "asset" : "assetId",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }

        self.getBidOrders = {
                                        "requestType" : "getBidOrders", \
                                        "asset" : "" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                                }
        self.getBlock= {
                                        "requestType" : "getBlock" , \
                                        "block" : "",\
                                        "height": "",\
                                        "timestamp" : "" ,\
                                        "includeTransactions" : "true"
                                        }


        self.getBlocks= {
                                        "requestType" : "getBlocks" , \
                                        "firstIndex" : "",\
                                        "lastIndex": "",\
                                        "includeTransactions" : "true"
                                        }


        self.getBlockId = {
                                        "requestType" : "getBlockId", \
                                        "height" : ""
                            }

        self.getBlockchainStatus = {
                                        "requestType" : "getBlockchainStatus",
                                    }
        #32
        self.getConstants= {
                                        "requestType" : "getConstants"
                                        }


        self.getDGSGood = {
                                        "requestType" : "getDGSGood", \
                                        "goods" : ""
                }
        self.getDGSGoods = {
                                        "requestType" : "getDGSGoods", \
                                        "seller" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "inStockOnly" : ""
                }
        self.getDGSPendingPurchases = {
                                        "requestType" : "getDGSPendingPurchases", \
                                        "seller" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : ""
                }
        self.getDGSPurchase = {
                                        "requestType" : "getDGSPurchase", \
                                        "purchase" : ""
                }

        self.getDGSPurchases = {
                                        "requestType" : "getDGSPurchases", \
                                        "seller" : "" , \
                                        "buyer" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "completed" : ""
                }


        self.getECBlock = {
                                "requestType" : "getECBlock", \
                                "timestamp" : ""
                            }



        #33
        self.getForging= {
                                        "requestType" : "getForging" , \
                                        "secretPhrase" : "PASSPHRASE"   ,\
                                        }

        #34
        self.getGuaranteedBalance= {
                                        "requestType" : "getGuaranteedBalance", \
                                        "account" : "ACCNUM" ,\
                                        "numberOfConfirmations" : "CONFIRMATIONS"
                                    }
        #35
        self.getMyInfo= {
                                        "requestType" : "getMyInfo"
                                       }

        self.getNextBlockGenerators = {
                                        "requestType" : "getNextBlockGenerators"
                                        }
        #36
        self.getPeer= {
                                        "requestType" : "getPeer" ,\
                                        "peer" : "PEERNAME"
                                        }
        #37
        self.getPeers= {
                                        "requestType" : "getPeers",\
                                        "active" : "",\
                                        "state" : ""
                                        }


        # HERE CHANGE





        #38
        self.getPoll ={                 "requestType" : "getPoll", \
                                        "poll" : ""
                                        }
        #39
        self.getPollIds ={              "requestType" : "getPollIds"

                                        }
        #40
        self.getState= {
                                        "requestType" : "getState",\
                                        "includeCounts" : "true"
                                        }
        #41
        self.getTime= {
                                        "requestType" : "getTime"
                                       }
        #42
        self.getTrades = {
                                        "requestType" : "getTrades" , \
                                        "asset" : "ASSETID" , \
                                        "firstIndex" : "" ,\
                                        "lastIndex": "",\
                                        "account" : "",\
                                        "includeAssetInfo" : "true"
                                        }
        #43
        self.getTransaction= {
                                        "requestType" : "getTransaction" , \
                                        "transaction" : "transaction",\
                                        "fullHash": "fullHash"
                                        }
        #44
        self.getTransactionBytes= {
                                        "requestType" : "getTransactionBytes" , \
                                        "transaction" : "transaction"
                                        }
        #45
        self.getUnconfirmedTransactionIds =  {
                                        "requestType" : "getUnconfirmedTransactionIds" , \
                                        "account":       "ACCNUM", \
                                        }

        self.getUnconfirmedTransactions = {
                                        "requestType" : "getUnconfirmedTransactions", \
                                        "account" : "" , \

                }
        #46
        self.issueAsset= {
                                        "requestType" : "issueAsset" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET" ,\
                                        "name" : "ASSETNAME", \
                                        "description" : "DESCRIPTION", \
                                        "quantityQNT" : "QTY" ,\
                                        "deadline" : "DEADLINE",\
                                        "decimals":"0",\
                                        "feeNQT" : "100000000", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         }

        #47
        self.leaseBalance= {
                                        "requestType" : "leaseBalance" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "0", \
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000" ,\
                                        "recipient" : "" ,\
                                        "period" : "1440", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         }

        #50
        self.longConvert = {
                                        "requestType" : "longConvert" ,  \
                                        "id" : " "
                                        }


        #49
        self.markHost= {
                                        "requestType" : "markHost" , \
                                        "secretPhrase" : "MY_SECRET" ,\
                                        "host" : "MY_HOST",\
                                        "weight" : "WEIGHT" ,\
                                        "date" :"CURRENT_DATE"
                                        }

        #50
        self.parseTransaction = {
                                        "requestType" : "parseTransaction" ,  \
                                        "transactionJSON" : "transactionJSON" ,\
                                        "transactionBytes" : ""
                                        }

        #51
        self.placeAskOrder= {
                                        "requestType" : "placeAskOrder" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET",\
                                        "asset" : "asset",\
                                        "quantityQNT" : "QTY",\
                                        "priceNQT" : "",\
                                        "deadline" : "180" ,\
                                        "feeNQT" : "100000000", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         }
        #52
        self.placeBidOrder= {
                                        "requestType" : "placeBidOrder" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET",\
                                        "asset" : "asset",\
                                        "quantityQNT" : "QTY",\
                                        "priceNQT" : "",\
                                        "deadline" : "180" ,\
                                        "feeNQT" : "100000000", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         }


        # DEBUG API !!!
        self.popOff = {
                                        "requestType" : "popOff", \
                                        "numBlocks" : "" , \
                                        "height" : ""
                }



        self.readMessage = {
                                        "requestType" : "readEncryptedNote", \
                                        "secretPhrase" : "" , \
                                        "transaction" : ""
                }


        self.rsConvert = {
                                        "requestType" : "rsConvert", \
                                        "account" : ""
                }


        # DEBUG API !!!
        self.scan = {
                                        "requestType" : "scan", \
                                        "numBlocks" : "" , \
                                        "height" : ""
                }


        self.sellAlias = {
                                        "requestType" : "sellAlias", \
                                        "alias" : "" , \
                                        "aliasName" : "" , \
                                        "recipient" : "" , \
                                        "priceNQT" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                }

        #53
        self.sendMessage= {
                                        "requestType" : "sendMessage" ,\
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET",\
                                        "recipient" : "RECIP_ACCOUNT" ,\
                                        "message" : "HEX_STRING" ,\
                                        "deadline" : "DEADLINE" ,\
                                        "feeNQT" : "100000000", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         }
        #54
        self.sendMoney= {               "requestType" : "sendMoney" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET" ,\
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000",\
                                        "amountNQT" : "",\
                                        "recipient" : "RECIPACCOUNT" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         }



        #55
        self.setAccountInfo= {
                                        "requestType" : "setAccountInfo" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "0", \
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000" ,\
                                        "name" : "name",\
                                        "description" : "description", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                         } #"recipient" : "" ,\ ???



        self.setAlias = {
                                        "requestType" : "setAlias", \
                                        "aliasName" : "" , \
                                        "aliasURI" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "", \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                        }
        #56
        self.signTransaction = {
                                        "requestType" : "signTransaction" ,  \
                                        "unsignedTransactionBytes" : "unsignedTransactionBytes" ,  \
                                        "unsignedTransactionJSON" : "",\
                                        "secretPhrase" : "PASSPHRASE"
                                        }
        #57
        self.startForging = {
                                        "requestType" : "startForging" ,  \
                                        "secretPhrase" : "PASSPHRASE"
                                        }
        #58
        self.stopForging = {
                                        "requestType" : "stopForging" ,  \
                                        "secretPhrase" : "PASSPHRASE"
                                        }



# HERE CHANGE
#
#
#         #58
        self.transferAsset= {
                                        "requestType" : "transferAsset" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET", \
                                        "recipient" : "" ,\
                                        "asset" : "ASSETID",\
                                        "quantityQNT" : "QTY" ,\
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" ,\
                                        "message": "" , \
                                        "messageIsText": "" , \
                                        "messageToEncrypt": "" , \
                                        "messageToEncryptIsText": "" , \
                                        "encryptedMessageData":	 "" , \
                                        "encryptedMessageNonce": "" , \
                                        "messageToEncryptToSelf": "" , \
                                        "messageToEncryptToSelfIsText":	 "" , \
                                        "encryptToSelfMessageData": "" , \
                                        "encryptToSelfMessageNonce": "" , \
                                        "recipientPublicKey": "" ,\
                                        }



#
#Is there a definition of the bytes in a transaction? I am trying to figure out which ones are AM and which ones are not.
#I thought maybe doing a getTransaction call would return what type of transaction it is, but it doesnt seem to.
#
#Where can we get a reference on decoding the bytes of a getTransactionBytes API call?  And is there anyway to get the bytes for an entire block?  Id really like to learn more about the bits/bytes of NXT, can someone point me in the right direction as far as decoding the blockchain?
#
# #
#Error Codes
#
#    1 - Incorrect request
#    2 - Blockchain not up to date
#    3 - Parameter not specified
#    4 - Incorrect parameter
#    5 - Unknown object (block, transaction, etc.)
#        In the case of accounts, this error means that no transaction has ever been sent to or from the account. This likely means the account is "unclaimed"/unused.
#    6 - Not enough funds
#

