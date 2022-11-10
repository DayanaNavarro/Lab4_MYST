
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
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


#------ Libro de ordenes

ob_c1=fn.order_book(cryptos[0],seconds,exchanges)
ob_c2=fn.order_book(cryptos[1],seconds,exchanges)
ob_c3=fn.order_book(cryptos[2],seconds,exchanges)


#----OHLC

c1m1=fn.close_prices(exchanges,cryptos[0],ob_c1,0)
c1m2=fn.close_prices(exchanges,cryptos[0],ob_c1,1)
c1m3=fn.close_prices(exchanges,cryptos[0],ob_c1,2)

c2m1=fn.close_prices(exchanges,cryptos[1],ob_c2,0)
c2m2=fn.close_prices(exchanges,cryptos[1],ob_c2,1)
c2m3=fn.close_prices(exchanges,cryptos[1],ob_c2,2)

c3m1=fn.close_prices(exchanges,cryptos[2],ob_c3,0)
c3m2=fn.close_prices(exchanges,cryptos[2],ob_c3,1)
c3m3=fn.close_prices(exchanges,cryptos[2],ob_c3,2)

#----Diccionario


d={'Exchange_1':{'Crypto1':ob_c1[0],
                 'Closes':c1m1,
                 'Crypto2':ob_c2[0],
                 'Closes':c2m1,
                 'Crypto3':ob_c3[0],
                 'Closes':c3m1},
  'Exchange_2':{'Crypto1':ob_c1[1],
                 'Closes':c1m2,
                 'Crypto2':ob_c2[1],
                 'Closes':c2m2,
                 'Crypto3':ob_c3[1],
                 'Closes':c3m2},
  'Exchange_3':{'Crypto1':ob_c1[2],
                 'Closes':c1m3,
                 'Crypto2':ob_c2[2],
                 'Closes':c2m3,
                 'Crypto3':ob_c3[2],
                 'Closes':c3m3}}

#----- Visualización de la Microestructura

vac1=fn.verifavance2(ob_c1,limite,seconds,exchanges)
vac2=fn.verifavance2(ob_c2,limite,seconds,exchanges)
vac3=fn.verifavance2(ob_c3,limite,seconds,exchanges)

#----Gráficas


vs.visualization(vac1,cryptos[0])
vs.visualization(vac2,cryptos[1])
vs.visualization(vac3,cryptos[2])








