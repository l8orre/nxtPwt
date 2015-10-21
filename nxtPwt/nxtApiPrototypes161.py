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
    """ python dict as container object for all NRS query prototypes. use these to compose queries
    38 tx types pooled on top."""

    def __init__(self):


        self.txTemplate = {
                                        "requestType" : "TEMPLATE" , \
                                        "secretPhrase" : "" ,\
                                        "publicKey" : "" ,\
                                        "feeNQT" : "100000000" ,\
                                        "deadline" : "" ,\
                                        "referencedTransactionFullHash" : "" ,\
                                        "broadcast" : "" ,\
                                        "message" : "" ,\
                                        "messageIsText" : "" ,\
                                        "messageIsPrunable" : "" ,\
                                        "messageToEncrypt" : "" ,\
                                        "messageToEncryptIsText" : "" ,\
                                        "encryptedMessageData" : "" ,\
                                        "encryptedMessageNonce" : "" ,\
                                        "encryptedMessageIsPrunable" : "" ,\
                                        "compressMessageToEncrypt" : "" ,\
                                        "messageToEncryptToSelf" : "" ,\
                                        "messageToEncryptToSelfIsText" : "" ,\
                                        "encryptToSelfMessageData" : "" ,\
                                        "encryptToSelfMessageNonce" : "" ,\
                                        "compressMessageToEncryptToSelf" : "" ,\
                                        "phased" : "" ,\
                                        "phasingFinishHeight" : "" ,\
                                        "phasingVotingModel" : "" ,\
                                        "phasingQuorum" : "" ,\
                                        "phasingMinBalance" : "" ,\
                                        "phasingHolding" : "" ,\
                                        "phasingMinBalanceModel" : "" ,\
                                        "phasingWhitelisted" : "" ,\
                                        "phasingWhitelisted" : "" ,\
                                        "phasingWhitelisted" : "" ,\
                                        "phasingLinkedFullHash" : "" ,\
                                        "phasingLinkedFullHash" : "" ,\
                                        "phasingLinkedFullHash" : "" ,\
                                        "phasingHashedSecret" : "" ,\
                                        "phasingHashedSecretAlgorithm" : "" ,\
                                        "recipientPublicKey" : "" ,\
            }

        self.txApproveTransaction = {
                                        "requestType" : "approveTransaction" , \
                                        "transactionFullHash" : "" , \
                                        "transactionFullHash" : "" , \
                                        "transactionFullHash" : "" , \
                                        "revealedSecret" : "" , \
                                        "revealedSecretIsText" : "" , \
                                        }
 

        self.txBuyAlias = {
                                        "requestType" : "buyAlias" , \
                                        "alias" : "" , \
                                        "aliasName" : "" , \
                                        "amountNQT" : "" , \
                                        }

        self.txCancelAskOrder= {
                                        "requestType" : "cancelAskOrder" , \
                                        "order" : "" ,\
                                         }

        self.txCancelBidOrder= {
                                        "requestType" : "cancelBidOrder" , \
                                        "order" : "",\
                                         }
        
        self.txCastVote ={                "requestType" : "castVote",\
                                        "poll" : "enterID" , \
                                        "vote00" : "enterVote" ,\
                                        "vote01" : "enterVote" ,\
                                        "vote02" : "enterVote" ,\
                                        }

        self.txCreatePoll ={            "requestType" : "createPoll", \
                                        "name" : "name" , \
                                        "description" : "description", \
                                        "option1" : "TODO:MAKE LIST1 ",\
                                        "option2" : "TODO:MAKE LIST2 ",\
                                        "option3" : "TODO:MAKE LIST3 ",\
                                        "minNumberOfOptions" : "",\
                                        "maxNumberOfOptions" : "",\
                                        "optionsAreBinary" : "true",\
                                         }

        self.txCurrencyBuy = {
                                        "requestType" : "currencyBuy" , \
                                        "currency" : "" , \
                                        "rateNQT" : "" , \
                                        "units" : "" , \
                                        }

        self.txCurrencyMint = {
                                        "requestType" : "currencyMint" , \
                                        "currency" : "" , \
                                        "nonce" : "" , \
                                        "units" : "" , \
                                        "counter" : "",\
                                        }

        self.txCurrencyReserveClaim = {
                                        "requestType" : "currencyReserveClaim" , \
                                        "currency" : "" , \
                                        "units" : "" , \
                                        }

        self.txCurrencyReserveIncrease = {
                                        "requestType" : "currencyReserveIncrease" , \
                                        "currency" : "" , \
                                        "amountPerUnitNQT" : "" , \
                                        }

        self.txCurrencySell = {
                                        "requestType" : "currencySell" , \
                                        "currency" : "" , \
                                        "rateNQT" : "" , \
                                        "units" : "" , \
                                        }

        self.txDeleteAlias = {
                                        "requestType" : "deleteAlias" , \
                                        "alias" : "" , \
                                        "aliasName" : "" , \
                                        "amountNQT" : "" , \
                                        }
                                        
        self.txDeleteCurrency = {
                                        "requestType" : "deleteCurrency" , \
                                        "currency" : "" , \
                                        }

        self.txDgsDelisting = {
                                        "requestType" : "dgsDelisting", \
                                        "goods" : "" , \
                                }

        self.txDgsDelivery = {
                                        "requestType" : "dgsDelivery", \
                                        "purchase" : "" , \
                                        "discountNQT" : "" , \
                                        "goodsData" : "" , \
                                        "goodsText" : "" , \
                                        "encryptedGoodsData" : "" , \
                                        "encryptedGoodsNonce" : "" , \
                                        }

        self.txDgsFeedback = {
                                        "requestType" : "dgsFeedback", \
                                        "purchase" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        }

        self.txDgsListing = {
                                        "requestType" : "dgsListing", \
                                        "name" : "" , \
                                        "description" : "" , \
                                        "tags" : "" , \
                                        "quantity" : "" , \
                                        "priceNQT" : "" , \
                                        }

        self.txDgsPriceChange = {
                                        "requestType" : "dgsPriceChange", \
                                        "goods" : "" , \
                                        "priceNQT" : "" , \
                                        }
        self.txDgsPurchase = {
                                        "requestType" : "dgsPurchase", \
                                        "goods" : "" , \
                                        "priceNQT" : "" , \
                                        "quantity" : "" , \
                                        "deliveryDeadlineTimestamp" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        }

        self.txDgsQuantityChange = {
                                        "requestType" : "dgsQuantityChange", \
                                        "goods" : "" , \
                                        "deltaQuantity" : "" , \
                                        }

        self.txDgsRefund = {
                                        "requestType" : "dgsRefund", \
                                        "purchase" : "" , \
                                        "refundNQT" : "" , \
                                        "note" : "" , \
                                        "encryptedNote" : "" , \
                                        "encryptedNoteNonce" : "" , \
                                        }

        self.txDividendPayment = {
                                        "requestType" : "dividendPayment" , \
                                        "asset" : "" , \
                                        "height" : "" , \
                                        "amountNQTPerQNT" : "" , \
                                        }

        self.txExtendTaggedData = {
                                        "requestType" : "extendTaggedData" ,  \
            "":" TODO CHEC TIS"
                                        }

        self.txIssueAsset= {
                                        "requestType" : "issueAsset" , \
                                        "name" : "ASSETNAME", \
                                        "description" : "DESCRIPTION", \
                                        "quantityQNT" : "QTY" ,\
                                        "decimals":"0",\
                                         }

        self.txIssueCurrency = {
                                        "requestType" : "issueCurrency" , \
                                        "name" : "" , \
                                        "code" : "" , \
                                        "description" : "" , \
                                        "type" : "" , \
                                        "initialSupply" : "" , \
                                        "reserveSupply" : "" , \
                                        "maxSupply" : "" , \
                                        "issuanceHeight" : "" , \
                                        "minReservePerUnitNQT" : "" , \
                                        "minDifficulty" : "" , \
                                        "maxDifficulty" : "" , \
                                        "ruleset" : "" , \
                                        "algorithm" : "" , \
                                        "decimals" : "" 
                                        }

        self.txLeaseBalance= {
                                        "requestType" : "leaseBalance" , \
                                        "recipient" : "" ,\
                                        "period" : "1440", \
                                         }

        self.txPlaceAskOrder= {
                                        "requestType" : "placeAskOrder" , \
                                        "asset" : "asset",\
                                        "quantityQNT" : "QTY",\
                                        "priceNQT" : "",\
                                         }
        
        self.txPlaceBidOrder= {
                                        "requestType" : "placeBidOrder" , \
                                        "asset" : "asset",\
                                        "quantityQNT" : "QTY",\
                                        "priceNQT" : "",\
                                         }

        self.txSellAlias = {
                                        "requestType" : "sellAlias", \
                                        "alias" : "" , \
                                        "aliasName" : "" , \
                                        "recipient" : "" , \
                                        "priceNQT" : "" , \
                                        }

        self.txSendMessage= {
                                        "requestType" : "sendMessage" ,\
                                        "recipient" : "RECIP_ACCOUNT" ,\
                                         }

        self.txSendMoney= {             "requestType" : "sendMoney" , \
                                        "amountNQT" : "",\
                                        "recipient" : "RECIPACCOUNT" , \
                                         }

        self.txSetAccountInfo= {
                                        "requestType" : "setAccountInfo" , \
                                        "name" : "name",\
                                        "description" : "description", \
                                         }

        self.txSetAlias = {
                                        "requestType" : "setAlias", \
                                        "aliasName" : "" , \
                                        "aliasURI" : "" , \
                                        }

        self.txTransferAsset= {
                                        "requestType" : "transferAsset" , \
                                        "recipient" : "" ,\
                                        "asset" : "ASSETID",\
                                        "quantityQNT" : "QTY" ,\
                                        }

        self.txTransferCurrency = {
                                        "requestType" : "transferCurrency" , \
                                        "recipient" : "" , \
                                        "currency" : "" , \
                                        "units" : "" 
                                        }

        self.txPublishExchangeOffer = {
                                        "requestType" : "publishExchangeOffer" , \
                                        "currency" : "" , \
                                        "buyRateNQT" : "" , \
                                        "sellRateNQT" : "" , \
                                        "totalBuyLimit" : "" , \
                                        "totalSellLimit" : "" , \
                                        "initialBuySupply" : "" , \
                                        "initialSellSupply" : "" , \
                                        "expirationHeight" : "" 
                                        }


        self.txUploadTaggedData = {
        "requestType" : "txUploadTaggedData" , \
        "":" TODO CHEC TIS"

        }

# TXs are on top despite the alphabetical ordering.
# much more concise.
#
#
#
#
#
#


        self.addPeer= {
                                        "requestType" : "addPeer" , \
                                        "peer" : "" ,\

                                 }

        self.blacklistPeer= {
                                        "requestType" : "blacklistPeer" , \
                                        "peer" : "" ,\

                                        }

        self.broadcastTransaction= {
                                        "requestType" : "broadcastTransaction" , \
                                        "transactionJSON" : "transactionJSON" ,\
                                        "transactionBytes" : "transactionBytes"
                                        }


        self.calculateFullHash = {
                                        "requestType" : "calculateFullHash", \
                                        "unsignedTransactionBytes" : "" , \
                                        "signatureHash" : ""
                                    }


        self.canDeleteCurrency = {
                                        "requestType" : "canDeleteCurrency" , \
                                        "account" : "" ,\
                                        "currency" : "" ,\
                                        "requireBlock" : "" ,\
                                        "requireLastBlock" : "" ,\
                                 }

        self.clearUnconfirmedTransactions = {
                                        "requestType" : "clearUnconfirmedTransactions"
                                        }


        self.decodeFileToken = {
                                        "requestType" : "decodeFileToken" , \
                                        "file" : "" ,\
                                        "token" : "" ,\

                                 }

        self.decodeHallmark = {
                                        "requestType" : "decodeHallmark" , \
                                        "hallmark" : "" ,\

                                 }
 
        self.decodeQRCode = {
                                        "requestType" : "decodeQRCode" , \
                                        "qrCodeBase64" : "" ,\
                                     }


        self.decodeToken = {
                                        "requestType" : "decodeToken" , \
                                        "website" : "" ,\
                                        "token" : "" ,\

                                 }


        self.decryptFrom = {
                                        "requestType" : "decryptFrom" , \
                                        "account" : "" ,\
                                        "data" : "" ,\
                                        "nonce" : "" , \
                                        "decryptedMessageIsText" : "" ,\
                                        "uncompressDecryptedMessage" : "" ,\
                                        "secretPhrase" : "" ,\
                                 }


        self.decodeHallmark= {
                                        "requestType" : "decodeHallmark" , \
                                        "hallmark" : "HEXSTRING"
                                        }
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

        self.downloadTaggedData = {
                                        "requestType" : "downloadTaggedData", \
                                        "transaction" : "" , \
                                        "requireBlock": "" ,\
                                        "requireLastBlock": "" ,\

                                        }

        self.dumpPeers = {
                                        "requestType" : "dumpPeers", \
                                        "version" : "" , \
                                        "weight": "" ,\
                                        "connect": "" ,\
                                        }

        self.encodeQRCode = {
                                        "requestType" : "encodeQRCode", \
                                        "qrCodeData" : "" , \
                                        "width": "" ,\
                                        "height": "" ,\
                                        }
    
        self.encryptTo = {
                                        "requestType" : "encryptTo", \
                                        "recipient" : "" , \
                                        "messageToEncrypt": "" ,\
                                        "messageToEncryptIsText": "" ,\
                                        "secretPhrase" : ""
                                        "compressMessageToEncrypt" : ""
                                        }

        self.eventRegister = {
                                        "requestType" : "eventRegister", \
                                        "event" : "" , \
                                        "event" : "" , \
                                        "event" : "" , \
                                        "add" : "" , \
                                        "remove": "" ,\
                                        "requireBlock": "" ,\
                                        "requireLastBlock" : "",\
                                        }

        self.eventWait = {
                                        "requestType" : "eventWait", \
                                        "timeout" : "" , \
                                        "requireBlock" : "" , \
                                        "requireLastBlock" : "" , \

                                        }

        self.fullHashToId = {
                                        "requestType" : "fullHashToId" ,  \
                                        "fullHash" : ""
                                        }

        self.fullReset = {
                                        "requestType" : "fullReset" ,  \
                                        }

        
        self.generateFileToken = {
                                        "requestType" : "generateFileToken" ,  \
                                        "file" : "", \
                                        "secretPhrase" : ""
                                        }
        self.generateToken = {
                                        "requestType" : "generateToken" ,  \
                                        "website" : "", \
                                        "secretPhrase" : ""
                                        }
        #
        self.getAccount = {
                                        "requestType" : "getAccount" , \
                                        "account" : "account", \
                                        "includeLessors" : "", \
                                        "includeAssets" : "", \
                                        "includeCurrencies" : "", \
                                        "includeEffectiveBalance" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }
        self.getAccountAssetCount = {
                                        "requestType" : "getAccountAssetCount", \
                                        "account" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "height": "" ,\
                                        }

        self.getAccountAssets = {
                                        "requestType" : "getAccountAssets", \
                                        "account" : "" , \
                                        "asset": "" ,\
                                        "height": ""
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
        self.getAccountBlockCount = {
                                        "requestType" : "getAccountBlockCount", \
                                        "account" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        #
        self.getAccountBlockIds= {
                                        "requestType" : "getAccountBlockIds" , \
                                        "account" : "ACCNUM",\
                                        "timestamp" : "0",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                       }

        self.getAccountBlocks= {
                                        "requestType" : "getAccountBlocks" , \
                                        "account" : "ACCNUM",\
                                        "timestamp" : "0",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "includeTransactions" : "true"
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }



        self.getAccountCurrencies = {
                                        "requestType" : "getAccountCurrencies" , \
                                        "account" : "" , \
                                        "currency" : "" , \
                                        "height" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getAccountCurrencyCount = {
                                        "requestType" : "getAccountCurrencyCount" , \
                                        "account" : "" , \
                                        "height" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        #
        self.getAccountCurrentAskOrderIds= {
                                        "requestType" : "getAccountCurrentAskOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getAccountCurrentAskOrders= {
                                        "requestType" : "getAccountCurrentAskOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }



        #
        self.getAccountCurrentBidOrderIds= {
                                        "requestType" : "getAccountCurrentBidOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAccountCurrentBidOrders= {
                                        "requestType" : "getAccountCurrentBidOrderIds" , \
                                        "asset" : "ASSETID",\
                                        "account" : "account",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAccountExchangeRequests = {
                                        "requestType" : "getAccountExchangeRequests" , \
                                        "account" : "" , \
                                        "currency" : "" , \
                                        "firstIndex" : "" , \
                                         "lastIndex" : "" ,\
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                         }


        #
        self.getAccountLessors = {
                                        "requestType" : "getAccountLessors" ,  \
                                        "account" : "account",   \
                                        "height" : "",\
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAccountPhasedTransactionCount = {
                                        "requestType" : "getAccountPhasedTransactionCount" ,  \
                                        "account" : "account", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAccountId = {
                                        "requestType" : "getAccountId" ,  \
                                        "secretPhrase" : "secretPhrase",   \
                                        "publicKey" : "publicKey"
                                        }


        self.getAccountPhasedTransactions = {
                                        "requestType" : "getAccountPhasedTransactions" ,  \
                                        "account" : "account", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
        
        self.getAccountPublicKey= {
                                        "requestType" : "getAccountPublicKey" , \
                                        "account" : "ACCNUM", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }



        self.getAccountTaggedData= {
                                        "requestType" : "getAccountTaggedData" , \
                                        "account" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "includeData" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 

        self.getAccountTransactionIds= {
                                        "requestType" : "getAccountTransactionIds" , \
                                        "account":       "ACCNUM", \
                                        "timestamp" : "0",\
                                        "type": "",\
                                        "subtype":"" ,\
                                        "firstIndex" : "" ,\
                                        "lastIndex":"",\
                                        "withMessage": "", \
                                        "numberOfConfirmations": "", \
                                        "withMessage" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAccountTransactions= {
                                        "requestType" : "getAccountTransactions" , \
                                        "account":       "ACCNUM", \
                                        "timestamp" : "0",\
                                        "type": "",\
                                        "subtype":"" ,\
                                        "firstIndex" : "" ,\
                                        "lastIndex":"",\
                                        "numberOfConfirmations": "", \
                                        "withMessage": "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAlias = {
                                        "requestType" : "getAlias" , \
                                        "alias" : "aliasId", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAliases = {
                                        "requestType" : "getAliases", \
                                        "timestamp" : "" , \
                                        "account" : "",\
                                        "firstIndex" : "",\
                                        "lastIndex" : ""
                                        }


        self.getAliasCount = {
                                        "requestType" : "getAliasCount" , \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
 

        self.getAliasesLike= {
                                        "requestType" : "getAliasesLike" , \
                                        "account" : "", \
                                        "aliasPrefix" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                       
                                        
                                        }
 
        self.getAllAssets = {
                                        "requestType" : "getAllAssets",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAllBroadcastedTransactions= {
                                        "requestType" : "" , \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\

                                        }


        self.getAllCurrencies = {
                                        "requestType" : "getAllCurrencies" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "includeCounts" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getAllExchanges = {
                                        "requestType" : "getAllExchanges" , \
                                        "timestamp" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "includeCurrencyInfo" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.getAllOpenAskOrders= {
                                        "requestType" : "getAllOpenAskOrders" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAllOpenBidOrders= {
                                        "requestType" : "getAllOpenBidOrders" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }


        self.getAllPrunableMessages= {
                                        "requestType" : "getAllPrunableMessages" , \
                                        "account" : "", \
                                        "timestamp" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAllTaggedData= {
                                        "requestType" : "getAllTaggedData" , \
                                        "account" : "", \
                                        "includeData" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

        self.getAllTrades= {
                                        "requestType" : "getAllTrades" , \
                                        "timestamp" : "0",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "includeAssetInfo" : "true", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                         }
        

        self.getAllWaitingTransactions= {
                                        "requestType" : "getAllWaitingTransactions" , \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }

        self.getAskOrder= {
                                        "requestType" : "getAskOrder" , \
                                        "order" : "ORDERID", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAskOrderIds= {
                                        "requestType" : "getAskOrderIds" , \
                                        "asset" : "assetId", \
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAskOrders = {
                                        "requestType" : "getAskOrders", \
                                        "asset" : "" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "showExpectedCancellations" : "" ,\
                }
        
        self.getAsset = {
                                        "requestType" : "getAsset" ,\
                                        "asset" : "ASSETID", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAssetAccounts = {
                                        "requestType" : "getAssetAccounts", \
                                        "asset" : "" , \
                                        "height" : "",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }


        #
        self.getAssetIds= {
                                        "requestType" : "getAssetIds",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                         }


        self.getAssetPhasedTransactions= {
                                        "requestType" : "getAssetPhasedTransactions" , \
                                        "account" : "", \
                                        "asset" : "", \
                                        "withoutWhitelist" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 
        self.getAssetTransfers= {
                                        "requestType" : "getAssetTransfers",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "",\
                                        "asset" : "" ,\
                                        "account" : "" ,\
                                        "includeAssetInfo" : "true", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                         }


        self.getAssets = {
                                        "requestType" : "getAssets" ,  \
                                        "assets" : "assets",\
                                        "assets" : "assets",\
                                        "assets" : "etc",\
                                        "includeCounts":"", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getAssetAccountCount = {
                                        "requestType" : "getAssetAccountCount" ,  \
                                        "asset" : "",\
                                        "height" : "" \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.getAssetsByIssuer = {
                                        "requestType" : "getAssetsByIssuer", \
                                        "account" : "" , \
                                        "account" : "" , \
                                        "account" : "",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }

        self.getBalance = {
                                        "requestType" : "getBalance", \
                                        "account" : "ACCNUM" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "includeEffectiveBalance" : ""
                                    }
        #
        self.getBidOrder= {
                                        "requestType" : "getBidOrder" , \
                                        "order" : "ORDERID", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
        #
        self.getBidOrderIds= {
                                        "requestType" : "getBidOrderIds" , \
                                        "asset" : "assetId",\
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getBidOrders = {
                                        "requestType" : "getBidOrders", \
                                        "asset" : "" , \
                                        "firstIndex" : "",\
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "showExpectedCancellations" : "" ,\
                                                }
        self.getBlock= {
                                        "requestType" : "getBlock" , \
                                        "block" : "",\
                                        "height": "",\
                                        "timestamp" : "" ,\
                                        "includeTransactions" : "true", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "includeExecutedPhased" : ""
                                        }



        self.getBlockId = {
                                        "requestType" : "getBlockId", \
                                        "height" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                            }

        self.getBlockchainStatus = {
                                        "requestType" : "getBlockchainStatus",
                                    }
       
        self.getBlockchainTransactions= {
                                        "requestType" : "getBlockchainTransactions" , \
                                        "firstIndex" : "",\
                                        "lastIndex": "",\
                                        "account" : "", \
                                        "numberOfConfirmations" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "timestamp" : "", \
                                        "type" : "", \
                                        "subtype" : "", \
                                        "withMessage" : "", \
                                        "phasedOnly" : "", \
                                        "nonPhasedOnly" : "", \
                                        "includeExpiredPrunable" : "", \
                                        "includePhasingResult" : "", \
                                        "executedOnly" : "", \
                                        }

        self.getBlocks= {
                                        "requestType" : "getBlocks" , \
                                        "firstIndex" : "",\
                                        "lastIndex": "",\
                                        "includeTransactions" : "true", \
                                        "requireLastBlock" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "includeExecutedPhased" : ""
                                        }

        self.getBuyOffers = {
                                        "requestType" : "getBuyOffers" , \
                                        "currency" : "" , \
                                        "account" : "" , \
                                        "availableOnly" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getChannelTaggedData= {
                                        "requestType" : "getChannelTaggedData" , \
                                        "account" : "", \
                                        "channel" : "", \
                                        "includeData ": "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
 
        self.getConstants= {
                                        "requestType" : "getConstants"
                                        }

        self.getCurrencies = {
                                        "requestType" : "getCurrencies" , \
                                        "currencies" : "" , \
                                        "currencies" : "" , \
                                        "currencies" : "" , \
                                         "includeCounts" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getCurrenciesByIssuer = {
                                        "requestType" : "getCurrenciesByIssuer" , \
                                        "account" : "" , \
                                        "account" : "" , \
                                        "account" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "includeCounts" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getCurrency = {
                                        "requestType" : "getCurrency" , \
                                        "currency" : "" , \
                                        "code" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getCurrencyAccountCount = {
                                        "requestType" : "getCurrencyAccountCount" , \
                                        "currency" : "" , \
                                        "height" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.getCurrencyAccounts = {
                                        "requestType" : "getCurrencyAccounts" , \
                                        "currency" : "" , \
                                        "height" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.getCurrencyFounders = {
                                        "requestType" : "getCurrencyFounders" , \
                                        "currency" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \

                                        }

        self.getCurrencyIds = {
                                        "requestType" : "getCurrencyIds" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : ""  , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getCurrencyPhasedTransactions= {
                                        "requestType" : "getCurrencyPhasedTransactions" , \
                                        "account" : "", \
                                        "currency" : "", \
                                        "withoutWhitelist" : "", \
                                        
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 
        self.getCurrencyTransfers = {
                                        "requestType" : "getCurrencyTransfers" , \
                                        "currency" : "" , \
                                        "account" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "timestamp" : "" , \
                                        "includeCurrencyInfo" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }
    
        self.getDGSExpiredPurchases= {
                                        "requestType" : "" , \
                                        "seller" : "", \
                                     
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

        self.getDGSGood = {
                                        "requestType" : "getDGSGood", \
                                        "goods" : "", \
                                        "includeCounts" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }

        self.getDGSGoods = {
                                        "requestType" : "getDGSGoods", \
                                        "seller" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "inStockOnly" : "",\
                                        "hideDelisted" : "" , \
                                        "includeCounts" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }

        self.getDGSGoodsCount = {
                                        "requestType" : "getDGSGoodsCount", \
                                        "seller" : "" , \
                                        "inStockOnly" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                }

        self.getDGSGoodsPurchases = {
                                        "requestType" : "getDGSGoodsPurchases", \
                                        "goods" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "withPublicFeedbacksOnly" : "",\
                                        "completed" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "buyer" : "", \

                }

        self.getDGSGoodsPurchaseCount = {
                                        "requestType" : "getDGSGoodsPurchaseCount", \
                                        "goods" : "" , \
                                        "withPublicFeedbacksOnly" : "" , \
                                         "completed" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }


        self.getDGSPendingPurchases = {
                                        "requestType" : "getDGSPendingPurchases", \
                                        "seller" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }
        self.getDGSPurchase = {
                                        "requestType" : "getDGSPurchase", \
                                        "purchase" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }

        self.getDGSPurchaseCount = {
                                        "requestType" : "getDGSPurchaseCount", \
                                        "seller" : "" , \
                                        "buyer" : "" , \
                                        "completed" : "",\
                                        "withPublicFeedbacksOnly" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }

        self.getDGSPurchases = {
                                        "requestType" : "getDGSPurchases", \
                                        "seller" : "" , \
                                        "buyer" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "completed" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }


        self.getDGSTags = {
                                        "requestType" : "getDGSTags", \
                                        "inStockOnly" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                }

        self.getDGSTagCount = {
                                        "requestType" : "getDGSTagCount", \
                                        "inStockOnly" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                            }
 
        self.getDGSTagsLike= {
                                        "requestType" : "getDGSTagsLike" , \
                                        "account" : "", \
                                        "tagPrefix" : "", \
                                        "inStockOnly" : "", \
                                        
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

##############################CHECK ALL!?!?! TODO

        self.getDataTagCount= {
                                        "requestType" : "getDataTagCount" , \
                                        "account" : "", \
                                        "getDataTags" : "", \
                                       
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

        self.getDataTagsLike= {
                                        "requestType" : "getDataTagsLike" , \
                                        "tagPrefix" : "", \
                                       
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getECBlock = {
                                        "requestType" : "getECBlock", \
                                        "timestamp" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                            }

        self.getExchanges = {
                                        "requestType" : "getExchanges" , \
                                        "currency" : "" , \
                                        "account" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                        "includeCurrencyInfo" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "timestamp" : ""
                                        }

        self.getExchangesByExchangeRequest = {
                                        "requestType" : "getExchangesByExchangeRequest" , \
                                        "transaction" : "" , \
                                        "includeCurrencyInfo" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }


        self.getExchangesByOffer = {
                                        "requestType" : "getExchangesByOffer" , \
                                        "offer" : "" , \
                                        "includeCurrencyInfo" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : ""  , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.getExpectedAskOrders= {
                                        "requestType" : "getExpectedAskOrders" , \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        "asset" : "" , \
                                        "sortByPrice" : ""  , \
                                        
                                        }


        self.getExpectedAssetTransfers= {
                                        "requestType" : "getExpectedAssetTransfers" , \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        "asset" : ""
                                        }
 
        self.getExpectedBidOrders= {
                                        "requestType" : "getExpectedBidOrders" , \
                                        "account" : "", \
                                        "asset" : "", \
                                        "sortByPrice" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }
 
        self.getExpectedBuyOffers= {
                                        "requestType" : "getExpectedBuyOffers" , \
                                        "account" : "", \
                                        "currency" : "", \
                                        "account" : "", \
                                        "sortByRate" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }

 
        self.getExpectedCurrencyTransfers= {
                                        "requestType" : "getExpectedCurrencyTransfers" , \
                                        "account" : "", \
                                        "currency" : "", \
                                        
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }
 

        self.getExpectedExchangeRequests= {
                                        "requestType" : "getExpectedExchangeRequests" , \
                                        "account" : "", \
                                        "currency" : "", \
                                        "includeCurrencyInfo" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }


        self.getExpectedOrderCancellations= {
                                        "requestType" : "getExpectedOrderCancellations" , \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }
 

        self.getExpectedSellOffers= {
                                        "requestType" : "getExpectedSellOffers" , \
                                        "account" : "", \
                                        "currency" : "", \
                                        "sortByRate" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }


        self.getExpectedTransactions= {
                                        "requestType" : "getExpectedTransactions" , \
                                        "account" : "", \
                                        "account" : "", \
                                        "account" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        }

        self.getForging= {
                                        "requestType" : "getForging" , \
                                        "secretPhrase" : "PASSPHRASE"   ,\
                                        "adminPassword" : ""   ,\
                                        }


        self.getGuaranteedBalance= {
                                        "requestType" : "getGuaranteedBalance", \
                                        "account" : "ACCNUM" ,\
                                        "numberOfConfirmations" : "CONFIRMATIONS" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                    }
 
        self.getInboundPeers= {
                                        "requestType" : "getInboundPeers" , \
                                        "includePeerInfo" : "", \
                                        
                                        }


        self.getLastExchanges= {
                                        "requestType" : "getLastExchanges" , \
                                        "account" : "", \
                                        "currencies" : "", \
                                        "currencies" : "", \
                                        "currencies" : "", \
                                         
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        
                                        }
 
        self.getLastTrades= {
                                        "requestType" : "getLastTrades" , \
                                        "account" : "", \
                                        "assets" : "", \
                                        "assets" : "", \
                                        "assets" : "", \
                                         
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }
 
        self.getLog= {
                                        "requestType" : "getLog" , \
                                        "count" : "", \
                                         
                                        
                                        }



        self.getMintingTarget = {
                                        "requestType" : "getMintingTarget" , \
                                        "currency" : "" , \
                                        "account" : "" , \
                                        "units" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.getMyInfo= {
                                        "requestType" : "getMyInfo"
                                       }

        self.getNextBlockGenerators = {
                                        "requestType" : "getNextBlockGenerators"
                                        }


        self.getOffer = {
                                        "requestType" : "getOffer" , \
                                        "offer" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }
 

        self.getOrderTrades= {
                                        "requestType" : "getOrderTrades" , \
                                         
                                        "askOrder" : "", \
                                        "bidOrder" : "", \
                                        "includeAssetInfo" : "", \
                                         
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }


        self.getPeer= {
                                        "requestType" : "getPeer" ,\
                                        "peer" : "PEERNAME"
                                        }
        #
        self.getPeers= {
                                        "requestType" : "getPeers",\
                                        "active" : "",\
                                        "state" : "",\
                                        "includePeerInfo" : ""
                                        }
 
        self.getPhasingPoll= {
                                        "requestType" : "getPhasingPoll" , \
                                        "transaction" : "", \
                                        "countVotes" : "", \
                                         
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        
                                        }

        self.getPhasingPollVote= {
                                        "requestType" : "getPhasingPollVote" , \
                                        "account" : "", \
                                        "transaction" : "", \
                                       
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        
                                        }


        self.getPhasingPollVotes= {
                                        "requestType" : "getPhasingPollVotes" , \
                                        "transaction" : "", \
                                        
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

        self.getPhasingPolls= {
                                        "requestType" : "getPhasingPolls" , \
                                        "account" : "", \
                                        "transaction" : "", \
                                        "transaction" : "", \
                                        "transaction" : "", \
                                        "countVotes" : "", \
                                         
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        
                                        }

        self.getPlugins= {
                                        "requestType" : "getPlugins" , \
                                        
                                        
                                        }


        self.getPoll ={                 "requestType" : "getPoll", \
                                        "poll" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

 
        self.getPollResult= {
                                        "requestType" : "getPollResult" , \
                                        "poll" : "", \
                                        "votingModel" : "", \
                                        "holding" : "", \
                                        "minBalance" : "", \
                                        "minBalanceModel" : "", \
                                         
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }


        self.getPollVote= {
                                        "requestType" : "getPollVote" , \
                                        "account" : "", \
                                        "poll" : "", \
                                        "includeWeights" : "", \
                                         
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }

        self.getPollVotes= {
                                        "requestType" : "getPollVotes" , \
                                        "poll" : "", \
                                        "includeWeights" : "", \
                                         
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 
        self.getPolls= {
                                        "requestType" : "getPolls" , \
                                        "account" : "", \
                                        "timestamp" : "", \
                                        "includeFinished" : "", \
                                        
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

        self.getPrunableMessage= {
                                        "requestType" : "getPrunableMessage" , \
                                        "transaction" : "", \
                                        "secretPhrase" : "", \
                                        
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }

        self.getPrunableMessage {
                                        "requestType" : "getPrunableMessage" , \
                                        "transaction" : "", \
                                        "secretPhrase" : "", \
                                        
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }

        self.getSellOffers= {
                                        "requestType" : "getSellOffers" , \
                                        "account" : "", \
                                        "currency" : "", \
                                        "availableOnly" : "", \
                                        
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }

                            
        self.getStackTraces= {
                                        "requestType" : "getStackTraces" , \
                                        "account" : "", \
                                        
                                        
                                        }


        self.getState= {
                                        "requestType" : "getState",\
                                        "includeCounts" : "true",\
                                        "adminPassword" : ""
                                        }
 

        self.getTaggedData= {
                                        "requestType" : "getTaggedData" , \
                                        "transaction" : "", \
                                        "includeData" : "", \
                                        
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }


        self.getTaggedDataExtendTransactions= {
                                        "requestType" : "getTaggedDataExtendTransactions" , \
                                        "transaction" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }

        self.getTime= {
                                        "requestType" : "getTime"
                                       }
        
        self.getTrades = {
                                        "requestType" : "getTrades" , \
                                        "asset" : "ASSETID" , \
                                        "firstIndex" : "" ,\
                                        "lastIndex": "",\
                                        "account" : "",\
                                        "includeAssetInfo" : "true", \
                                        "timestamp" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
        #43
        self.getTransaction= {
                                        "requestType" : "getTransaction" , \
                                        "transaction" : "transaction",\
                                        "fullHash": "fullHash", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "includePhasingResult" : ""
                                        }
        #44
        self.getTransactionBytes= {
                                        "requestType" : "getTransactionBytes" , \
                                        "transaction" : "transaction", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
        #45
        self.getUnconfirmedTransactionIds =  {
                                        "requestType" : "getUnconfirmedTransactionIds" , \
                                        "account":       "ACCNUM", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.getUnconfirmedTransactions = {
                                        "requestType" : "getUnconfirmedTransactions", \
                                        "account" : "" , \
                                        "account" : "" , \
                                        "account" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }
        

        self.getVoterPhasedTransactions= {
                                        "requestType" : "getVoterPhasedTransactions" , \
                                        "account" : "", \
                                        
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 

        self.hash= {
                                        "requestType" : "hash" , \
                                        "hashAlgorithm" : "", \
                                        "secret" : "", \
                                        "secretIsText" : "", \
                                       
                                        }


        self.hexConvert= {
                                        "requestType" : "hexConvert" , \
                                        "string" : "", \
                                    
                                        }

        self.longConvert = {
                                        "requestType" : "longConvert" ,  \
                                        "id" : " "
                                        }



        self.luceneReindex= {
                                        "requestType" : "luceneReindex" , \
                                         
                                        
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
                                        "transactionBytes" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }

        self.popOff = {
                                        "requestType" : "popOff", \
                                        "numBlocks" : "" , \
                                        "height" : ""
                }

        self.readMessage = {
                                        "requestType" : "readEncryptedNote", \
                                        "secretPhrase" : "" , \
                                        "transaction" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }

        self.rebroadcastUnconfirmedTransactions= {
                                        "requestType" : "rebroadcastUnconfirmedTransactions" , \
                                       
                                        
                                        }


        self.requeueUnconfirmedTransactions= {
                                        "requestType" : "requeueUnconfirmedTransactions" , \
                                     
                                        
                                        }


        self.rsConvert = {
                                        "requestType" : "rsConvert", \
                                        "account" : ""
                }

        self.scan = {
                                        "requestType" : "scan", \
                                        "numBlocks" : "" , \
                                        "height" : ""
                        }
 

        self.searchAccounts= {
                                        "requestType" : "searchAccounts" , \
                                        "query" : "", \
                                     
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }


        self.searchAssets = {
                                        "requestType" : "searchAssets", \
                                        "query":"", \
                                        "firstIndex":"", \
                                        "lastIndex" : "" , \
                                        "includeCounts" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                }


        self.searchCurrencies = {
                                        "requestType" : "searchCurrencies" , \
                                        "query" : "" , \
                                        "firstIndex" : "" , \
                                        "lastIndex" : "" , \
                                         "includeCounts" : "" , \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \

                                        }

        self.searchDGSGoods = {
                                        "requestType" : "searchDGSGoods", \
                                        "query":"", \
                                        "firstIndex":"", \
                                        "lastIndex" : "" , \
                                        "includeCounts" : "",\
                                        "seller" : "", \
                                        "inStockOnly" : "" , \
                                        "hideDelisted" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        "tag" : ""
                            }
 
        self.searchPolls {
                                        "requestType" : "searchPolls" , \
                                        "query" : "", \
                                        "includeFinished" : "", \
                                         
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 
        self.searchTaggedData= {
                                        "requestType" : "searchTaggedData" , \
                                        "account" : "", \
                                        "query" : "", \
                                        "tag" : "", \
                                        "channel" : "", \
                                        "includeData" : "", \
                                        "firstIndex" : "", \
                                        "lastIndex" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        
                                        }
 
        self.setLogging= {
                                        "requestType" : "setLogging" , \
                                        "account" : "", \
                                        "logLevel" : "", \
                                        "communicationEvent" : "", \
                                        "communicationEvent" : "", \
                                        "communicationEvent" : "", \
                                        
                                        }


 

        self.shutdown= {
                                        "requestType" : "shutdown" , \
                                        
                                        
                                        }
    

        self.signTransaction = {
                                        "requestType" : "signTransaction" ,  \
                                        "unsignedTransactionBytes" : "unsignedTransactionBytes" ,  \
                                        "unsignedTransactionJSON" : "",\
                                        "secretPhrase" : "PASSPHRASE",\
                                        "valdate": "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "", \
                                        }
 
        self.startForging = {
                                        "requestType" : "startForging" ,  \
                                        "secretPhrase" : "PASSPHRASE"
                                        }
        #
        self.stopForging = {
                                        "requestType" : "stopForging" ,  \
                                        "secretPhrase" : "",\
                                        "adminPassword" : ""
                                        }

        self.trimDerivedTables= {
                                        "requestType" : "trimDerivedTables" , \
                                      
                                        
                                        }
 

        self.verifyPrunableMessage= {
                                        "requestType" : "verifyPrunableMessage" , \
                                        "transaction" : "", \
                                        "message" : "", \
                                        "messageIsText" : "", \
                                        "messageToEncryptIsText" : "", \
                                        "encryptedMessageData" : "", \
                                        "encryptedMessageNonce" : "", \
                                        "compressMessageToEncrypt" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }
        # CHECECHER

        self.verifyTaggedData= {
                                        "requestType" : "verifyTaggedData" , \
                                        "file" : "", \
                                        "transaction" : "", \
                                        "name" : "", \
                                        "description" : "", \
                                        "tags" : "", \
                                        "type" : "", \
                                        "channel" : "", \
                                        "isText" : "", \
                                        "filename" : "", \
                                        "data" : "", \
                                        "requireBlock" : "", \
                                        "requireLastBlock" : "",\
                                        
                                        }





  ###########


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

