import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

gs = web.DataReader('078930.KS', 'yahoo', '2014-01-01', '2016-03-06')

ma5 = gs['Close'].rolling(window=5).mean()
ma20 = gs['Close'].rolling(window=20).mean()
ma60 = gs['Close'].rolling(window=60).mean()
ma120 = gs['Close'].rolling(window=120).mean()

gs['ma5'] = ma5
gs['ma20'] = ma20
gs['ma60'] = ma60
gs['ma120'] = ma120

plt.plot(gs.index, gs['Close'], label = 'Close')
plt.plot(gs.index, gs['ma5'], label = 'ma5')
plt.plot(gs.index, gs['ma20'], label = 'ma20')
plt.plot(gs.index, gs['ma60'], label = 'ma60')
plt.plot(gs.index, gs['ma120'], label = 'ma120')

plt.legend(loc="best")

plt.grid()

plt.show()
