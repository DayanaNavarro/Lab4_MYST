
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
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
import functions as fn

cryptos=['BTC/USDT','BTC/USDC','ETH/USDT']
seconds=20
limite=20
exchanges=[ccxt.bitmart(),ccxt.bitforex(),ccxt.bibox()]

#------Libro de ordenes

ob_c1=fn.order_book(cryptos[0],seconds,exchanges)
ob_c2=fn.order_book(cryptos[1],seconds,exchanges)
ob_c3=fn.order_book(cryptos[2],seconds,exchanges)

#------OHLC

c1m1=fn.close_prices(exchanges,cryptos[0],ob_c1,0)
c1m2=fn.close_prices(exchanges,cryptos[0],ob_c1,1)
c1m3=fn.close_prices(exchanges,cryptos[0],ob_c1,2)

c2m1=fn.close_prices(exchanges,cryptos[1],ob_c2,0)
c2m2=fn.close_prices(exchanges,cryptos[1],ob_c2,1)
c2m3=fn.close_prices(exchanges,cryptos[1],ob_c2,2)


c3m1=fn.close_prices(exchanges,cryptos[2],ob_c3,0)
c3m2=fn.close_prices(exchanges,cryptos[2],ob_c3,1)
c3m3=fn.close_prices(exchanges,cryptos[2],ob_c3,2)


#-----Visualización de la Microestructura

vac1=fn.verifavance2(ob_c1,limite,seconds,exchanges)
vac2=fn.verifavance2(ob_c2,limite,seconds,exchanges)
vac3=fn.verifavance2(ob_c3,limite,seconds,exchanges)







