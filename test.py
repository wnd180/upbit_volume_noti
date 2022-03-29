import pyupbit
import time

tickers = pyupbit.get_tickers()
time.sleep(0.1)

df = pyupbit.get_ohlcv('KRW-BTC',count =1 ,interval="minute1")
print(df.iloc[0]['open'])