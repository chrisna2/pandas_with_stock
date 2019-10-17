import pandas_datareader.data as web
import matplotlib.pyplot as plt

lg = web.DataReader('066570.KS', 'yahoo')
samsung = web.DataReader('005930.KS', 'yahoo')

plt.plot(lg.index, lg['Close'], label='LG Electronics')
plt.plot(samsung.index, samsung['Close'], label='Samsung Electronics')

# 범례 위치
plt.legend(loc='upper left')

plt.show()