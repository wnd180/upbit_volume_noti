import pyupbit
import time
import requests


def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel, "text": text},
    )


def start(coin, priceUp, close_price):
    noti_message = (
        "---------------------------------\n\n"
        + "유의 코인 : "
        + str(coin)
        + "\n\n"
        + "5분봉 가격 상승률 : "
        + str(priceUp)
        + "\n\n"
        + "현재가 : "
        + str(close_price)
    )
    post_message(myToken, "volume_noti", noti_message)


myToken = "your slack token here"

tickers = pyupbit.get_tickers()
time.sleep(0.1)

krw_tickers = [
    "KRW-ETH",
    "KRW-NEO",
    "KRW-MTL",
    "KRW-LTC",
    "KRW-XRP",
    "KRW-ETC",
    "KRW-OMG",
    "KRW-SNT",
    "KRW-WAVES",
    "KRW-XEM",
    "KRW-QTUM",
    "KRW-LSK",
    "KRW-STEEM",
    "KRW-XLM",
    "KRW-ARDR",
    "KRW-ARK",
    "KRW-STORJ",
    "KRW-GRS",
    "KRW-REP",
    "KRW-ADA",
    "KRW-SBD",
    "KRW-POWR",
    "KRW-BTG",
    "KRW-ICX",
    "KRW-EOS",
    "KRW-TRX",
    "KRW-SC",
    "KRW-ONT",
    "KRW-ZIL",
    "KRW-POLY",
    "KRW-ZRX",
    "KRW-LOOM",
    "KRW-BCH",
    "KRW-BAT",
    "KRW-IOST",
    "KRW-RFR",
    "KRW-CVC",
    "KRW-IQ",
    "KRW-IOTA",
    "KRW-MFT",
    "KRW-ONG",
    "KRW-GAS",
    "KRW-UPP",
    "KRW-ELF",
    "KRW-KNC",
    "KRW-BSV",
    "KRW-THETA",
    "KRW-QKC",
    "KRW-MOC",
    "KRW-ENJ",
    "KRW-TFUEL",
    "KRW-MANA",
    "KRW-ANKR",
    "KRW-AERGO",
    "KRW-ATOM",
    "KRW-TT",
    "KRW-CRE",
    "KRW-MBL",
    "KRW-WAXP",
    "KRW-HBAR",
    "KRW-MED",
    "KRW-MLK",
    "KRW-STPT",
    "KRW-ORBS",
    "KRW-VET",
    "KRW-CHZ",
    "KRW-STMX",
    "KRW-DKA",
    "KRW-HIVE",
    "KRW-KAVA",
    "KRW-AHT",
    "KRW-LINK",
    "KRW-XTZ",
    "KRW-BORA",
    "KRW-JST",
    "KRW-CRO",
    "KRW-TON",
    "KRW-SXP",
    "KRW-HUNT",
    "KRW-PLA",
    "KRW-DOT",
    "KRW-SRM",
    "KRW-MVL",
    "KRW-STRAX",
    "KRW-AQT",
    "KRW-GLM",
    "KRW-SSX",
    "KRW-META",
    "KRW-FCT2",
    "KRW-CBK",
    "KRW-SAND",
    "KRW-HUM",
    "KRW-DOGE",
    "KRW-STRK",
    "KRW-PUNDIX",
    "KRW-FLOW",
    "KRW-DAWN",
    "KRW-AXS",
    "KRW-STX",
    "KRW-XEC",
    "KRW-SOL",
    "KRW-MATIC",
    "KRW-NU",
    "KRW-AAVE",
    "KRW-1INCH",
    "KRW-ALGO",
    "KRW-NEAR",
    "KRW-WEMIX",
    "KRW-AVAX",
    "KRW-T",
    "KRW-CELO",
]

while 1:
    for i in range(len(krw_tickers)):
        try:
            df = pyupbit.get_ohlcv(krw_tickers[i], count=1, interval="minute5")
            time.sleep(0.1)

            open_price = df.iloc[0]["open"]
            close_price = df.iloc[0]["close"]
            priceUp = (close_price - open_price) / open_price * 100
            if priceUp > 2:
                start(krw_tickers[i], priceUp, close_price)
        except Exception as e:
            print(e)
