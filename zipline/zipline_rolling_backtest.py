import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
from zipline.api import record, symbol, order_target
from zipline import run_algorithm, TradingAlgorithm

# data
start = datetime.datetime(2010, 1, 2)
end = datetime.datetime(2019, 1, 1)
data = web.DataReader("AAPL", "yahoo", start, end)

# plt.plot(data.index, data['Adj Close'])
# plt.show()

data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

# print(data.head())


def initialize(context):
    context.i = 0
    context.sym = symbol('AAPL')
    context.hold = False


def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return

    buy = False
    sell = False

    ma5 = data.history(context.sym, 'price', 5, '1d').mean()
    ma20 = data.history(context.sym, 'price', 20, '1d').mean()

    if ma5 > ma20 and context.hold == False:
        order_target(context.sym, 100)
        context.hold = True
        buy = True
    elif ma5 < ma20 and context.hold == True:
        order_target(context.sym, -100)
        context.hold = False
        sell = True

    record(AAPL=data.current(context.sym, "price"), ma5=ma5, ma20=ma20, buy=buy, sell=sell)

'''
algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)
'''

start_utc = start.replace(tzinfo=datetime.timezone.utc)
end_utc = end.replace(tzinfo=datetime.timezone.utc)
result = run_algorithm(start=start_utc, end=end_utc, initialize=initialize,
                       capital_base=100000, handle_data=handle_data, data=data)
'''
# 포트폴리오 그래프 투자 이익금 확인
plt.plot(result.index, result.portfolio_value)
plt.show()
'''

# 골든 크로스 데드 크로스 표시
plt.plot(result.index, result.ma5)
plt.plot(result.index, result.ma20)
plt.legend(loc='best')
plt.plot(result.loc[result.buy==True].index, result.ma5[result.buy == True], '^')
plt.plot(result.loc[result.sell==True].index, result.ma5[result.sell == True], 'v')

plt.show()