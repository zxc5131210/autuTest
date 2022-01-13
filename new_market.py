import requests
import json
import numpy as np
import time
from random import choice
from jsonpath import jsonpath

# define time
btse_nonce = str(round(time.time()))
fromTime = int(btse_nonce)-9000
fromTime = str(fromTime)

# define user status
Coin = "ADA"
Type = '-USD'
base_url = "https://spot.oa.btse.io"
Token = "USER_TOKEN_LOGIN_8677065f187e98d8beacdc700e49f6ef_a6610a23627a4c029c507f1e69d6c5dd"
SendtoUser = "xitayo9939"
Sendtoemail = "xitayo9939@upsdom.com"

headers = {
    'token': Token,
    'Content-Type': 'application/json',
    'x-xsrf-token': '28dfbae9-1bcf-4550-bc7c-12a28b09ce9f',
    'cookie': 'XSRF-TOKEN=28dfbae9-1bcf-4550-bc7c-12a28b09ce9f'
}


# Get price to setting
'''
url=base_url+'/api/tradingView/history?symbol='+Coin+Type+'-0&resolution=15&from='+fromTime+'&to='+btse_nonce+'&countback=2'
payload={}
response = requests.request("GET", url, headers=headers, data=payload)
j_result = json.loads(response.text)
orderbook_pirce=j_result['o'][0]
orderbook_pirce= float(orderbook_pirce)
'''

# Market Setting
quote_Currency = ["USDC", "USDT", "USDP", "BTC", "ETH"]
# Limit
Limit_Price_Buy = 99999
Limit_Price_Sell = 99999
# MARKET_Buy
MARKET_Price = 10
# MARKET_SELL
MARKET_Size = 1
# OCO_BUY
OCO_Price = 0.01
OCO_Stop = 99999
OCO_Limit = 1
OCO_Size = 1
# OCO_SELL
OCO_PriceS = 99999
OCO_StopS = 0.01
OCO_LimitS = 1
OCO_SizeS = 1
# INDEX_BUY
INDEX_Price = 0.01
INDEX_Size = 1
Percentage = 10
Stealth = 100
# INDEX_SELL
INDEX_PriceS = 0.6
INDEX_SizeS = 1
PercentageS = 10
StealthS = 100

'''
#Market Setting
quote_Currency=["USDC","USDT","USDP","BTC","ETH"]
##Limit
Limit_Price_Buy=round(orderbook_pirce-(orderbook_pirce*0.1),2)
Limit_Price_Sell=round(orderbook_pirce+(orderbook_pirce*0.1),2)
##MARKET_Buy
MARKET_Price=10
##MARKET_SELL
MARKET_Size=1
##OCO_BUY 
OCO_Price=round(orderbook_pirce-(orderbook_pirce*0.1),2)
OCO_Stop=99999
OCO_Limit=1
OCO_Size=1
##OCO_SELL 
OCO_PriceS=99999
OCO_StopS=round(orderbook_pirce-(orderbook_pirce*0.1),2)
OCO_LimitS=orderbook_pirce
OCO_SizeS=1
##INDEX_BUY
INDEX_Price=int(orderbook_pirce)
INDEX_Size=1
Percentage=10
Stealth=100
##INDEX_SELL
INDEX_PriceS=int(orderbook_pirce)
INDEX_SizeS=1
PercentageS=10
StealthS=100
'''

# Testcoin_setting
Fiat = ["USD", "CNY", "JPY", "EUR", "GBP", "HKD",
        "SGD", "MYR", "THB", "AUD", "AED", "CAD", "CHF"]
Crypto = ["ETH", "BTC", "LTC", "XMR", "BTSE", "XRP", "LEO", "TRX", "UNI", "CRV", "COMP", "ATOM", "DOT", "BAND", "UMA", "WXMR", "FLY", "LINK", "WOO", "HT", "AAVE", "1INCH", "SUSHI", "ADA",
          "YFI", "BNT", "FIL", "MBM", "BAL", "MATIC", "FTT", "MKR", "BNB", "DOGE", "DODO", "AXS", "AVAX", "GRT", "ENJ", "CHZ", "BAT", "BADGER", "DYDX", "QRDO", "DOG", "FTM", "OMG", "CELR",
          "MANA", "CVX"]
Stablecoin = ["USDT", "TUSD", "USDC", "XAUT", "DAI", "WAED", "WAUD", "WCAD", "WCHF", "WEUR",
              "WGBP", "WHKD", "WINR", "WJPY", "WMYR", "WSGD", "WUSD", "BUSD", "XSGD", "USDP", "UST"]

TestList = ['USD', 'ETH', 'USDT']
OTClist = ['ETH', 'USDT']
'''
TestList1=choice(Fiat)
TestList.append(TestList1)
TestList1=choice(Crypto)
TestList.append(TestList1)
OTClist.append(TestList1)
TestList1=choice(Stablecoin)
TestList.append(TestList1)
OTClist.append(TestList1)

print("TestList",TestList)
print("OTClist",OTClist)
'''
'''
##Deposit
endpoints="/api/spot/api/v3.2/user/wallet/address?currency="+Coin
url=base_url+endpoints
payload = json.dumps({
})

response = requests.request("GET", url, headers=headers, data=payload)
print("Deposit:",response.text)

##Withdraw
endpoints='/api/spot/api/v3.2/user/wallet/withdraw'
url=base_url+endpoints

payload = json.dumps({
    	"currency": Coin+Blockchain ,
    	"address": withdraw_address,
    	"amount": "100"
    	})

response = requests.request("POST", url, headers=headers, data=payload)
print("Withdraw:",response.text)
'''
# Convert


def Convert():
    print('** Convert **')
    endpoints = '/api/capital/wallet/operation'
    url = base_url+endpoints

    ConvertTime = []
    for i in range(3):
        payload = json.dumps({
            "operation": "CONVERT",
            "fromWallet": [
                {
                    "wallet": "SPOT@",
                    "asset": Coin,
                    "amount": 1
                }
            ],
            "toAsset": TestList[i]
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        print("Convert", Coin, " to ", TestList[i], ":", j_result['msg'])
        time.sleep(1)

    for i in range(3):
        payload = json.dumps({
            "operation": "CONVERT",
            "fromWallet": [
                {
                    "wallet": "SPOT@",
                    "asset": TestList[i],
                    "amount": 0.1
                }
            ],
            "toAsset": Coin
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        print("Convert", TestList[i], " to ", Coin, ":", j_result['msg'])
        time.sleep(1)


# Sendto
def Sendto():
    endpoints = '/api/spot/api/v3.2/user/wallet/transfer'
    url = base_url+endpoints

    payload = json.dumps({
        "amount": "1.0",
        "asset":  Coin,
        "toUser": SendtoUser,
        "toUserMail": Sendtoemail
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    print("Sendto:", j_result)


# OTC
def OTC():
    for i in range(3):
        endpoints = '/api/otc/api/v1/quote'
        url = base_url+endpoints
        payload = json.dumps({
            "orderSizeInBaseCurrency": "1",
            "orderAmountInOrderCurrency": 0,
            "side": "buy",
            "baseCurrency": Coin,
            "orderCurrency": TestList[i],
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        if('quoteId' in j_result):
            if(j_result['status'] == 30001):
                url = base_url+"/api/otc/api/v1/accept/"+j_result['quoteId']
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                j_result = json.loads(response.text)
                if(j_result['status'] == 30007):
                    print("OTC-BUY:", Coin, " to ", TestList[i], ":Success")
                else:
                    print("OTC-BUY:", Coin, " to ",
                          TestList[i], ":Fail", " ", j_result['memo'])
            elif (j_result['quoteId'] == 'None'):
                print("OTC-BUY:", Coin, " to ",
                      TestList[i], ":Fail", " ", j_result['memo'])
        else:
            print("OTC-BUY:", Coin, " to ",
                  TestList[i], ":Fail", " ", j_result['msg'])

    for i in range(2):
        endpoints = '/api/otc/api/v1/quote'
        url = base_url+endpoints
        payload = json.dumps({
            "orderSizeInBaseCurrency": "1",
            "orderAmountInOrderCurrency": 0,
            "side": "BUY",
            "baseCurrency": OTClist[i],
            "orderCurrency": Coin,
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        if('quoteId' in j_result):
            if(j_result['status'] == 30001):
                url = base_url+"/api/otc/api/v1/accept/"+j_result['quoteId']
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                j_result = json.loads(response.text)
                if(j_result['status'] == 30007):
                    print("OTC-BUY:", OTClist[i], " to ", Coin, ":Success")
                else:
                    print("OTC-BUY:", OTClist[i], " to ",
                          Coin, ":Fail", " ", j_result['memo'])
            elif (j_result['quoteId'] == 'None'):
                print("OTC-BUY:", OTClist[i], " to ",
                      Coin, ":Fail", " ", j_result['memo'])
        else:
            print("OTC-BUY:", OTClist[i], " to ",
                  Coin, ":Fail", " ", j_result['msg'])

    for i in range(3):
        endpoints = '/api/otc/api/v1/quote'
        url = base_url+endpoints
        payload = json.dumps({
            "orderSizeInBaseCurrency": "1",
            "orderAmountInOrderCurrency": 0,
            "side": "SELL",
            "baseCurrency": Coin,
            "orderCurrency": TestList[i],
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        if('quoteId' in j_result):
            if(j_result['status'] == 30001):
                url = base_url+"/api/otc/api/v1/accept/"+j_result['quoteId']
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                j_result = json.loads(response.text)
                if(j_result['status'] == 30007):
                    print("OTC-SELL:", Coin, " to ", TestList[i], ":Success")
                else:
                    print("OTC-SELL:", Coin, " to ",
                          TestList[i], ":Fail", " ", j_result['memo'])
            elif (j_result['quoteId'] == 'None'):
                print("OTC-SELL:", Coin, " to ",
                      TestList[i], ":Fail", " ", j_result['memo'])
        else:
            print("OTC-SELL:", Coin, " to ",
                  TestList[i], ":Fail", " ", j_result['msg'])

    for i in range(2):
        endpoints = '/api/otc/api/v1/quote'
        url = base_url+endpoints
        payload = json.dumps({
            "orderSizeInBaseCurrency": "1",
            "orderAmountInOrderCurrency": 0,
            "side": "SELL",
            "baseCurrency": OTClist[i],
            "orderCurrency": Coin,
        })

        response = requests.request("POST", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        if('quoteId' in j_result):
            if(j_result['status'] == 30001):
                url = base_url+"/api/otc/api/v1/accept/"+j_result['quoteId']
                response = requests.request(
                    "POST", url, headers=headers, data=payload)
                j_result = json.loads(response.text)
                if(j_result['status'] == 30007):
                    print("OTC-SELL:", TestList[i], " to ", Coin, ":Success")
                else:
                    print("OTC-SELL:", TestList[i], " to ",
                          Coin, ":Fail", " ", j_result['memo'])
            elif (j_result['quoteId'] == 'None'):
                print("OTC-SELL:", TestList[i], " to ",
                      Coin, ":Fail", " ", j_result['memo'])
        else:
            print("OTC-SELL:", TestList[i], " to ",
                  Coin, ":Fail", " ", j_result['msg'])

# Market min-max price


def GetMarket():
    Support_Currencys = np.array(quote_Currency)
    print("*** Market ***")
    for i in range(Support_Currencys.size):
        endpoints = "/api/inquire/exchangeInfo?symbol=" + \
            Coin+"-"+quote_Currency[i]
        url = base_url+endpoints
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        j_result = json.loads(response.text)
        code = (j_result.get('code'))
        if code == 1:
            minValidPrice = jsonpath(j_result, "$..minValidPrice")
            minPriceIncrement = jsonpath(j_result, "$..minPriceIncrement")
            minOrderSize = jsonpath(j_result, "$..minOrderSize")
            maxOrderSize = jsonpath(j_result, "$..maxOrderSize")
            minSizeIncrement = jsonpath(j_result, "$..minSizeIncrement")
            print("MARKETquote_", quote_Currency[i], ":", "minValidPrice:", minValidPrice, "minPriceIncrement:", minPriceIncrement,
                "minOrderSize:", minOrderSize, "maxOrderSize:", maxOrderSize, "minSizeIncrement", minSizeIncrement)
            print("")


# Limit
def Market():
    endpoints = '/api/spot/api/v3.1/order'
    url = base_url+endpoints

# Limit-Buy
    print("** Limit **")
    payload = json.dumps({
        "type": "LIMIT",
        "txType": "LIMIT",
        "symbol": Coin+Type,
        "price": Limit_Price_Buy,
        "size": "1",
        "stopPrice": "",
        "triggerPrice": "",
        "time_in_force": "GTC",
        "postOnly": False,
        "side": "BUY",
        "clOrderID": "_cisxew1640062068796"
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 2 or status == 4 or status == 5):
        print("Limit-Buy:Success")
        print("")
    else:
        print("Limit-Buy:Fail")
        print(response.text)

# Limit-Sell
    payload = json.dumps({
        "type": "LIMIT",
        "txType": "LIMIT",
        "symbol": Coin+Type,
        "price": Limit_Price_Sell,
        "size": "1",
        "stopPrice": "",
        "triggerPrice": "",
        "side": "SELL",
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 2 or status == 4 or status == 5):
        print("Limit-Sell:Success")
        print("")
    else:
        print("Limit-Sell:Fail")
        print(response.text)

# MARKET-BUY
    print("** Market **")
    payload = json.dumps({
        "side": "BUY",
        "type": "MARKET",
        "txType": "LIMIT",
        "symbol": Coin+Type,
        "price": MARKET_Price,
        "clOrderID": "_iixdgjo1640071772347"
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 4 or status == 5):
        print("Market-Buy:Success")
        print("")
    else:
        print("Market-Buy:Fail")
        print(response.text)

# MARKET-SELL
    payload = json.dumps({
        "side": "SELL",
        "type": "MARKET",
        "txType": "LIMIT",
        "symbol": Coin+Type,
        "size": MARKET_Size,
        "clOrderID": "_iixdgjo1640071772347"
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 4 or status == 5):
        print("Market-Sell:Success")
        print("")
    else:
        print("Market-Sell:Fail")
        print(response.text)

#OCO-BUY  (triggerPrice=Stop,StopPrice=Limit)
    print("** OCO **")
    payload = json.dumps({
        "side": "BUY",
        "type": "OCO",
        "txType": "LIMIT",
        "symbol": Coin+Type,
        "price": OCO_Price,
        "size": OCO_Size,
        "stopPrice": OCO_Limit,
        "triggerPrice": OCO_Stop,
        "time_in_force": "GTC",
        "postOnly": False,
        "clOrderID": "_dfvc1640072490498"
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 2 or status == 4 or status == 5):
        print("OCO-Buy:Success")
        print("")
    else:
        print("OCO-Buy:Fail")
        print(response.text)

# OCO-SELL
    payload = json.dumps({
        "side": "SELL",
        "type": "OCO",
        "txType": "LIMIT",
        "symbol": Coin+Type,
        "price": OCO_PriceS,
        "size": OCO_SizeS,
        "stopPrice": OCO_LimitS,
        "triggerPrice": OCO_StopS,
        "time_in_force": "GTC",
        "postOnly": False,
        "clOrderID": "_czkvpu1639981365510"
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 2 or status == 4 or status == 5):
        print("OCO-Sell:Success")
        print("")
    else:
        print("OCO-Sell:Fail")
        print(response.text)

# INDEX-buy
    print("** Index **")
    endpoints = '/api/spot/api/v3.1/order/peg'
    payload = json.dumps({
        "type": "PEG",
        "symbol": Coin+Type,
        "price": INDEX_Price,
        "size": INDEX_Size,
        "stealth": Stealth,
        "deviation": Percentage,
        "side": "BUY",
        "clOrderID": "_tiylf1639981502067"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 2 or status == 4 or status == 5):
        print("Index-Buy:Success")
        print("")
    else:
        print("Index-Buy:Fail")
        print(response.text)

# INDEX-SELL
    payload = json.dumps({
        "type": "PEG",
        "symbol": Coin+Type,
        "price": INDEX_PriceS,
        "size": INDEX_SizeS,
        "stealth": StealthS,
        "deviation": PercentageS,
        "side": "SELL",
        "clOrderID": "_tiylf1639981502067"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    status = j_result[0]['status']
    if(status == 2 or status == 4 or status == 5):
        print("Index-Sell:Success")
        print("")
    else:
        print("Index-Sell:Fail")
        print(response.text)

# History_spot
def History():
    print("** Spot History **")
    btse_nonce = str(round(time.time()*1000))
    fromTime = int(btse_nonce)-172799000
    fromTime = str(fromTime)
    payload = {}
    endpoints = '/api/histories/spotWallet?fromTimestamp='+fromTime + \
    '&toTimestamp='+btse_nonce+'&currency='+Coin+'&currentPage=1&pageSize=10'
    url = base_url+endpoints
    response = requests.request("GET", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    data = (j_result.get('data'))
    print(j_result)

# History_trade
    print("** Trade History **")
    btse_nonce = str(round(time.time()*1000))
    fromTime = int(btse_nonce)-172799000
    fromTime = str(fromTime)
    payload = {}
    endpoints = '/api/histories/spotTrades?fromTimestamp='+fromTime + \
    '&toTimestamp='+btse_nonce+'&currency='+Coin+'&currentPage=1&pageSize=10'
    url = base_url+endpoints
    response = requests.request("GET", url, headers=headers, data=payload)
    j_result = json.loads(response.text)
    data = (j_result.get('data'))
    print(j_result)


def main():
    Convert()
    Sendto()
    OTC()
    GetMarket()
    Market()
    History()

main()
