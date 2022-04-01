import pyupbit
import time

df = pyupbit.get_ohlcv('KRW-CVC',count =3 ,interval="minute1")
print(df)