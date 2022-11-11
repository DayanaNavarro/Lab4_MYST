
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

#--- Visualizaciones por exchange y moneda del MID

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


def visualizationMID(data,crypto):
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


#--- Visualizaciones por exchange y moneda del VWAP


def visualizationVWAP(data,crypto):
    d1=data[data['exchange']==str(exchanges[0])]
    d2=data[data['exchange']==str(exchanges[1])]
    d3=data[data['exchange']==str(exchanges[2])]
    fig = go.Figure(layout=dict(title=dict(text=crypto+" VWAP")))
    fig.add_trace(go.Scatter(x=d1['timeStamp'], y=d1['vwap'],
                        mode='lines',name=str(exchanges[0])+' '+crypto+': Vwap',line=dict(color='skyblue')))
    fig.add_trace(go.Scatter(x=d2['timeStamp'], y=d2['vwap'],
                        mode='lines',name=str(exchanges[1])+' '+crypto+': Vwap',line=dict(color='lightsalmon')))
    fig.add_trace(go.Scatter(x=d3['timeStamp'], y=d3['vwap'],
                        mode='lines',name=str(exchanges[2])+' '+crypto+': Vwap',line=dict(color='lawngreen')))
    fig.update_xaxes(
            title_text = "TimeStamp",
            title_standoff = 25)

    fig.update_yaxes(
            title_text = "Vwap",
            title_standoff = 25)
    return fig.show()


#--- Visualizaciones por exchange y moneda del AV

def visualizationAV(data,crypto):
    d1=data[data['exchange']==str(exchanges[0])]
    d2=data[data['exchange']==str(exchanges[1])]
    d3=data[data['exchange']==str(exchanges[2])]
    fig = go.Figure(layout=dict(title=dict(text=crypto+" Ask Volume")))
    fig.add_trace(go.Scatter(x=d1['timeStamp'], y=d1['ask_volume'],
                        mode='lines',name=str(exchanges[0])+' '+crypto+': ask_volume',line=dict(color='skyblue')))
    fig.add_trace(go.Scatter(x=d2['timeStamp'], y=d2['ask_volume'],
                        mode='lines',name=str(exchanges[1])+' '+crypto+': ask_volume',line=dict(color='lightsalmon')))
    fig.add_trace(go.Scatter(x=d3['timeStamp'], y=d3['ask_volume'],
                        mode='lines',name=str(exchanges[2])+' '+crypto+': ask_volume',line=dict(color='lawngreen')))
    fig.update_xaxes(
            title_text = "TimeStamp",
            title_standoff = 25)

    fig.update_yaxes(
            title_text = "Ask_volume",
            title_standoff = 25)
    return fig.show()

#--- Visualizaciones por exchange y moneda del BV

def visualizationBV(data,crypto):
    d1=data[data['exchange']==str(exchanges[0])]
    d2=data[data['exchange']==str(exchanges[1])]
    d3=data[data['exchange']==str(exchanges[2])]
    fig = go.Figure(layout=dict(title=dict(text=crypto+" Bid Volume")))
    fig.add_trace(go.Scatter(x=d1['timeStamp'], y=d1['bid_volume'],
                        mode='lines',name=str(exchanges[0])+' '+crypto+': bid_volume',line=dict(color='skyblue')))
    fig.add_trace(go.Scatter(x=d2['timeStamp'], y=d2['bid_volume'],
                        mode='lines',name=str(exchanges[1])+' '+crypto+': bid_volume',line=dict(color='lightsalmon')))
    fig.add_trace(go.Scatter(x=d3['timeStamp'], y=d3['bid_volume'],
                        mode='lines',name=str(exchanges[2])+' '+crypto+': bid_volume',line=dict(color='lawngreen')))
    fig.update_xaxes(
            title_text = "TimeStamp",
            title_standoff = 25)

    fig.update_yaxes(
            title_text = "Bid_volume",
            title_standoff = 25)
    return fig.show()


#--- Visualizaciones por exchange y moneda del Volumen total

def visualizationVT(data,crypto):
    d1=data[data['exchange']==str(exchanges[0])]
    d2=data[data['exchange']==str(exchanges[1])]
    d3=data[data['exchange']==str(exchanges[2])]
    fig = go.Figure(layout=dict(title=dict(text=crypto+"total_volume")))
    fig.add_trace(go.Scatter(x=d1['timeStamp'], y=d1['total_volume'],
                        mode='lines',name=str(exchanges[0])+' '+crypto+': total_volume',line=dict(color='skyblue')))
    fig.add_trace(go.Scatter(x=d2['timeStamp'], y=d2['total_volume'],
                        mode='lines',name=str(exchanges[1])+' '+crypto+': total_volume',line=dict(color='lightsalmon')))
    fig.add_trace(go.Scatter(x=d3['timeStamp'], y=d3['total_volume'],
                        mode='lines',name=str(exchanges[2])+' '+crypto+': total_volume',line=dict(color='lawngreen')))
    fig.update_xaxes(
            title_text = "TimeStamp",
            title_standoff = 25)

    fig.update_yaxes(
            title_text = "total_volume",
            title_standoff = 25)
    return fig.show()

