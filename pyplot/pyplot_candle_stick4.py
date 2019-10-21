import pandas_datareader.data as web
import datetime
import mpl_finance
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

'''
매주 월요일 기준으로 x축 구분을 나눔
'''

start = datetime.datetime(2016, 3, 1)
end = datetime.datetime(2016, 3, 31)

skhynix = web.DataReader("000660.ks", "yahoo", start, end)
skhynix = skhynix[skhynix['Volume'] > 0]


fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
day_list = range(len(skhynix))

day_list = []
name_list = []
for i, day in enumerate(skhynix.index):
    if day.dayofweek == 0:
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d')+'(Mon)')

ax.xaxis.set_major_locator(ticker.FixedLocator(day_list)) # 항상 맞춰서 입력해 줄것
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))
mpl_finance.candlestick2_ohlc(ax,
                              skhynix['Open'],
                              skhynix['High'],
                              skhynix['Low'],
                              skhynix['Close'],
                              width=0.5,
                              colorup='r',
                              colordown='b')
plt.show()

