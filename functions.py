
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import ccxt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import collections
import time


cryptos=['BTC/USDT','BTC/USDC','ETH/USDT']
limite=20
exchanges=[ccxt.bitmart(),ccxt.bitforex(),ccxt.bibox()]



#------- Consumir datos de CCXT

def order_book(crypto,exchanges):
    limite=20
    ob1,ob2,ob3=[],[],[]
    delay = 60 # seconds
    now=60
    sec=now-60
    while sec<now:
        ob1+=collections.ChainMap(exchanges[0].fetch_order_book(crypto,limit=limite)).maps
        ob2+=collections.ChainMap(exchanges[1].fetch_order_book(crypto,limit=limite)).maps
        ob3+=collections.ChainMap(exchanges[2].fetch_order_book(crypto,limit=limite)).maps
        time.sleep (delay)
        sec+=1
    return ob1,ob2,ob3


#-------- Fechas

def times(exchanges,data):
    
    times=[]

    for i in range(len(exchanges)):
        for j in range(len(data[0])):
            times.append(data[i][j]['datetime'])
    return times


#------ Descarga de close price

def close_prices(exchanges,symbol,data,n):
    time=times(exchanges,data)[60*n]
    startDate=exchanges[n].parse8601(time)
    ohlcv = exchanges[n].fetch_ohlcv(symbol, timeframe='1m', since=startDate,limit=60)
    closes = [x[4] for x in ohlcv]
    dates = [exchanges[n].iso8601 (x[0]) for x in ohlcv]
    return closes,dates

#--------Visualización de la Microestructura


def verifavance2(data,limite,seconds,exchanges):
    exchange,times=[],[]
    ask_vol,bid_vol=[],[]
    ask_voll,bid_voll=[],[]
    mid,spread=[],[]
    ask,bid=[],[]
    c=0
    df=pd.DataFrame(columns=['exchange','timeStamp','level','ask_volume','bid_volume','total_volume','mid_price','vwap'])
    for i in range(len(exchanges)):
        exchange.append([str(exchanges[i])]*seconds)
        for j in range(seconds):
            times.append(data[i][j]['datetime'])
            mid.append((data[i][j]['bids'][0][0]+data[i][j]['asks'][0][0])/2)
            for m in range(limite):
                ask_vol.append(data[i][j]['asks'][m][1])
                bid_vol.append(data[i][j]['bids'][m][1])
                ask.append(data[i][j]['asks'][m][0])
                bid.append(data[i][j]['bids'][m][0])
            ask_voll.append(sum(ask_vol[c:c+limite]))
            bid_voll.append(sum(bid_vol[c:c+limite]))
            spread.append(np.mean(ask[c:c+limite])-np.mean(bid[c:c+limite]))
            c+=limite
    exchange=[exchange for exchanges in exchange for exchange in exchanges]
    df['exchange']=exchange
    df['timeStamp']=times
    df['level']=limite
    df['ask_volume']=ask_voll
    df['bid_volume']=bid_voll
    df['total_volume']=df['ask_volume']+df['bid_volume']
    df['mid_price']=mid
    df['vwap']=sum(spread*df['total_volume'])/df['total_volume']
    return df, spread

#------ MODELO DE ROLL

def verifavance3(spread, pricem1,pricem2,pricem3):
    df=pd.DataFrame(columns=['timestamp','Close','Spread','Effective Spread'])
    df['timestamp']=pricem1[1]+pricem2[1]+pricem3[1]
    df['Close']=pricem1[0]+pricem2[0]+pricem3[0]
    df['Spread']=spread
    for i in range(len(df)-5):
        df.loc[i+5,'Effective Spread']=2*np.sqrt(np.abs(np.cov(np.diff(df.loc[0:i+5,'Close']))))
    return df



