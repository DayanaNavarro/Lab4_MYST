
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

#--- Visualizaciones por exchange y moneda

import ccxt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import collections
import functions as fn


cryptos=['BTC/USDT','BTC/USDC','ETH/USDT']
seconds=20
limite=20
exchanges=[ccxt.bitmart(),ccxt.bitforex(),ccxt.bibox()]

def visualization(data,crypto):
    d1=data[data['exchange']==str(exchanges[0])]
    d2=data[data['exchange']==str(exchanges[1])]
    d3=data[data['exchange']==str(exchanges[2])]
    fig = go.Figure(layout=dict(title=dict(text=crypto+" Mid Price")))
    fig.add_trace(go.Scatter(x=d1['timeStamp'], y=d1['mid_price'],
                        mode='lines',name=str(exchanges[0])+' '+crypto+': MidPrice',line=dict(color='skyblue')))
    fig.add_trace(go.Scatter(x=d2['timeStamp'], y=d2['mid_price'],
                        mode='lines',name=str(exchanges[1])+' '+crypto+': MidPrice',line=dict(color='lightsalmon')))
    fig.add_trace(go.Scatter(x=d3['timeStamp'], y=d3['mid_price'],
                        mode='lines',name=str(exchanges[2])+' '+crypto+': MidPrice',line=dict(color='lawngreen')))
    fig.update_xaxes(
            title_text = "TimeStamp",
            title_standoff = 25)

    fig.update_yaxes(
            title_text = "MidPrice",
            title_standoff = 25)
    return fig.show()