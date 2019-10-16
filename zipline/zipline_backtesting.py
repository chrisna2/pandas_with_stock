"""
2019-10-15
현재 아무것도 되지 않고 있다 뭘 놓치고 있는지 확인하기 위해
일단 zipline을 통한 백테스팅은 멈춘다.

2019-10-16
파이참 인터프리터를 잠깐 바꾸었다 다시 키니
잘 된다. 뭔가 이상하지만 잘되느 기분 좋다!!
"""
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline import run_algorithm

# data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)
data = web.DataReader("AAPL", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 1)


start_utc = start.replace(tzinfo=datetime.timezone.utc)
end_utc = end.replace(tzinfo=datetime.timezone.utc)
result = run_algorithm(start=start_utc, end=end_utc, initialize=initialize,
                       capital_base=10000, handle_data=handle_data, data=data)

plt.plot(result.index, result.portfolio_value)
plt.show()
