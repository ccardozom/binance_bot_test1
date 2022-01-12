#import os
#from binance.spot import Spot
#from binance.client import Client
#from binance.enums import *
#from binance.stream import BinanceSocketManager
#from binance.exceptions import BinanceAPIException, BinanceOrderException
#import pandas as pd
#from datetime import timedelta, datetime
#import math
from binance.client import Client
import config

cliente = Client(config.API_KEY, config.API_SECRET_KEY)
#cliente = Spot(config.API_KEY, config.API_SECRET_KEY)

info = cliente.get_account_snapshot(type='FUTURES')

sim = info['simbol']
for i in sim:
    if i['symbol' == 'ADAUSDT']:
        print('ADAUSDT')

#print(cliente.ticker_price("ADAUSDT"))
#print(cliente.klines("ADAUSDT", "4h"))
