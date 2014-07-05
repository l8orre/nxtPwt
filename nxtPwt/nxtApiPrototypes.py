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



class nxtQs(object):
    """ python dict as container object for all NRS query prototypes. use these to compose queries """

    def __init__(self):

        #1
        self.broadcastTransaction= {
                                        "requestType" : "broadcastTransaction" , \
                                        "transactionBytes" : "transactionBytes"
                                        }

        self.buyAlias = {
                                        "requestType" : "buyAlias" , \
                                        "alias" : "" , \
                                        "aliasName" : "" , \
                                        "priceNQT" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : ""
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
                                        "referencedTransaction" : "",\
                                        "feeNQT" : "100000000"
                                         }
        #4
        self.cancelBidOrder= {
                                        "requestType" : "cancelBidOrder" , \
                                        "secretPhrase" : "PASSPHRASE",\
                                        "order" : "ORDERID",\
                                        "deadline" : "DEADLINE" ,\
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "feeNQT" : "100000000"
                                         }
        #5
        self.castVote ={                "requestType" : "castVote",\
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "secretPhrase" : "PASSPHRASE"   ,\
                                        "poll" : "enterID" , \
                                        "deadline" : "DEADLINE",\
                                        "vote1" : "enterVote" ,\
                                        "vote2" : "enterVote" ,\
                                        "vote3" : "enterVote" ,\
                                        "feeNQT" : "100000000"
                                        }
        #6
        self.createPoll ={              "requestType" : "createPoll", \
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "name" : "name" , \
                                        "description" : "description", \
                                        "option1" : "TODO:MAKE LIST ",\
                                        "minNumberOfOptions" : "",\
                                        "maxNumberOfOptions" : "",\
                                        "deadline" : "deadline",\
                                        "feeNQT" : "100000000",\
                                        "secretPhrase" : "secretPhrase"   ,\
                                        "optionsAreBinary" : "true"
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
                                        "secretPhrase" : ""
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
                                        "broadcast" : "" ,
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
                                        }
        self.encryptTo = {
                                        "requestType" : "encryptTo", \
                                        "recipient" : "" , \
                                        "note" : "" , \
                                        "secretPhrase" : ""
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
                                        "timestamp" : "0"
                                        }
        #12
        self.getAccountCurrentAskOrderIds= {
                                        "requestType" : "getAccountCurrentAskOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account"
                                        }
        #13
        self.getAccountCurrentBidOrderIds= {
                                        "requestType" : "getAccountCurrentBidOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account"
                                        }
        #14
        self.getAccountId = {
                                        "requestType" : "getAccountId" ,  \
                                        "secretPhrase" : "secretPhrase"   \
                                        }
        #15
        self.getAccountPublicKey= {
                                        "requestType" : "getAccountPublicKey" , \
                                        "account" : "ACCNUM"
                                        }
        #16
        self.getAccountTransactionIds= {
                                        "requestType" : "getAccountTransactionIds" , \
                                        "account":       "ACCNUM", \
                                        "timestamp" : "0",\
                                        "type": "",\
                                        "subtype":""
                                        }
        #17
        self.getAlias = {
                                        "requestType" : "getAlias" , \
                                        "alias" : "aliasId"
                                        }

        self.getAliases = {
                                        "requestType" : "getAliases", \
                                        "timestamp" : "" , \
                                        "account" : ""
                                        }
        #56
        self.getAllAssets = {
                                        "requestType" : "getAllAssets"
                                        }
        #21
        self.getAllOpenOrders= {
                                        "requestType" : "getAllOpenOrders" , \

                                        }
        #22
        self.getAllTrades= {
                                        "requestType" : "getAllTrades" , \
                                        "timestamp" : "0"
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
                                        "limit":""
                                        }

        self.getAskOrders = {
                                        "requestType" : "getAskOrders", \
                                        "asset" : "" , \
                                        "limit" : ""
                }
        #25
        self.getAsset = {
                                        "requestType" : "getAsset" ,\
                                        "asset" : "ASSETID"
                                        }
        #26
        self.getAssetIds= {
                                        "requestType" : "getAssetIds"
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
                                        "account" : ""
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
                                        "limit":""
                                        }

        self.getBidOrders = {
                                        "requestType" : "getBidOrders", \
                                        "asset" : "" , \
                                        "limit" : ""
                                                }
        self.getBlock= {
                                        "requestType" : "getBlock" , \
                                        "block" : "BLOCKADDRESS"
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
                                        "requestType" : "getPeers"
                                        }
        #38
        self.getPoll ={                 "requestType" : "getPoll", \
                                        "poll" : ""
                                        }
        #39
        self.getPollIds ={              "requestType" : "getPollIds"

                                        }
        #40
        self.getState= {
                                        "requestType" : "getState"
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
                                        "lastIndex": ""
                                        }
        #43
        self.getTransaction= {
                                        "requestType" : "getTransaction" , \
                                        "transaction" : "transaction",\
                                        "hash": "hash"
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
                                        "referencedTransaction" : "",\
                                        "secretPhrase" : "SECRET" ,\
                                        "name" : "ASSETNAME", \
                                        "description" : "DESCRIPTION", \
                                        "quantityQNT" : "QTY" ,\
                                        "deadline" : "DEADLINE",\
                                        "decimals":"0",\
                                        "feeNQT" : "100000000"
                                         }

        #47
        self.leaseBalance= {
                                        "requestType" : "leaseBalance" , \
                                        "referencedTransaction" : "",\
                                        "publicKey":"",\
                                        "secretPhrase" : "0", \
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000" ,\
                                        "recipient" : "" ,\
                                        "period" : "1440"
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
                                        "transactionBytes" : ""
                                        }

        #51
        self.placeAskOrder= {
                                        "requestType" : "placeAskOrder" , \
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "secretPhrase" : "SECRET",\
                                        "asset" : "asset",\
                                        "quantityQNT" : "QTY",\
                                        "priceNQT" : "",\
                                        "deadline" : "180" ,\
                                        "feeNQT" : "100000000"
                                         }
        #52
        self.placeBidOrder= {
                                        "requestType" : "placeBidOrder" , \
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "secretPhrase" : "SECRET",\
                                        "asset" : "asset",\
                                        "quantityQNT" : "QTY",\
                                        "priceNQT" : "",\
                                        "deadline" : "180" ,\
                                        "feeNQT" : "100000000"
                                         }

        self.readEncryptedNote = {
                                        "requestType" : "readEncryptedNote", \
                                        "secretPhrase" : "" , \
                                        "transaction" : ""
                }
        self.rsConvert = {
                                        "requestType" : "rsConvert", \
                                        "account" : ""
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
                                        "broadcast" : "" , \
                }
        self.sendEncryptedNote = {
                                        "requestType" : "sendEncryptedNote", \
                                        "recipient" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        "secretPhrase" : "" , \
                                        "publicKey" : "" , \
                                        "feeNQT" : "100000000" , \
                                        "deadline" : "" , \
                                        "referencedTransactionFullHash" : "" , \
                                        "broadcast" : "" , \
                }
        #53
        self.sendMessage= {
                                        "requestType" : "sendMessage" ,\
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "secretPhrase" : "SECRET",\
                                        "recipient" : "RECIP_ACCOUNT" ,\
                                        "message" : "HEX_STRING" ,\
                                        "deadline" : "DEADLINE" ,\
                                        "feeNQT" : "100000000"
                                         }
        #54
        self.sendMoney= {               "requestType" : "sendMoney" , \
                                        "publicKey":"",\
                                        "referencedTransaction" : "",\
                                        "secretPhrase" : "SECRET" ,\
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000",\
                                        "amountNQT" : "",\
                                        "recipient" : "RECIPACCOUNT" ,\
                                         }



        #55
        self.setAccountInfo= {
                                        "requestType" : "setAccountInfo" , \
                                        "referencedTransaction" : "",\
                                        "publicKey":"",\
                                        "secretPhrase" : "0", \
                                        "deadline" : "DEADLINE",\
                                        "feeNQT" : "100000000" ,\
                                        "name" : "name",\
                                        "description" : "description"
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
                                        "broadcast" : ""
                                        }
        #56
        self.signTransaction = {
                                        "requestType" : "signTransaction" ,  \
                                        "unsignedTransactionBytes" : "unsignedTransactionBytes" ,  \

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
        #58
        self.transferAsset= {
                                        "requestType" : "transferAsset" , \
                                        "publicKey":"",\
                                        "secretPhrase" : "SECRET", \
                                        "recipient" : "" ,\
                                        "asset" : "ASSETID",\
                                        "quantityQNT" : "QTY" ,\
                                        "deadline" : "DEADLINE",\
                                        "comment" :"TX comment",\
                                        "referencedTransaction" : "",\
                                        "feeNQT" : "100000000"
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

