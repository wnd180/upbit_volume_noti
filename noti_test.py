import pyupbit
import time
import requests

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def restart(coin,vol):
    noti_message = "---------------------------------\n\n"+"유의 코인 : "+ str(coin)+"\n\n" + "거래량 상승률 : " + str(vol)
    post_message(myToken,"volume_noti",noti_message)


myToken = "xoxb-3266901814165-3282486848545-NHe6MuLJPqvFp4Oaegm6QQee"

tickers = pyupbit.get_tickers()
time.sleep(0.1)

krw_tickers = []
volumeList = []
priceList = []

for i in tickers:
    if "KRW-" in i:
        krw_tickers.append(i)

for i in range(len(tickers)):
    volumeList.append(0)
    priceList.append(0)

while 1:
    print("okay")

    for i in range(len(krw_tickers)):
        df = pyupbit.get_ohlcv(krw_tickers[i], count=2,interval="minute1")
        time.sleep(0.05) 
        print(df)
        lastvolume = df.iloc[0]['volume']
        nowvolume = df.iloc[1]['volume']


        if lastvolume*5 < nowvolume:
            lastprice = df.iloc[0]['close']
            nowprice = df.iloc[1]['close']
            if lastprice<nowprice:
                volumeUp = nowvolume/lastvolume
                restart(krw_tickers[i],volumeUp)
