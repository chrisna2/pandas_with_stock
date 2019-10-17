import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
from zipline.api import symbol, order
from zipline.finance import commission
from zipline import run_algorithm
import pandas as pd

pd.set_option('display.float_format', '{:3f}'.format)

# C:\Users\{}\.zipline\data  SPY_benchmark.csv 에 코스피 종목에 해당하는 날짜가 존재 하니 않는 경우
# 날짜의 인덱싱 오류가 발생할 수 있다. (zipline은 미국 시장 기준의 날짜 인덱싱을 한다.)
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2019, 2, 3)

# 임의 날짜를 입력 하고 에러를 발생시키지 않겠다면 종목을 kospi, kosdac이 아니라 미국 종목으로 해야 된다.
# 한국 종목을 조회 할려면 날짜라던가에 제약이 많은 것 같다.
# [원인 1] 야후 파이낸스에 GS 그룹의 주가 kospi 데이터가 제대로 입력되지 않아서 발생하는 문제이다. 현재는 삼성전자로 대체
# [원인 2] zipline 에서 기록된 인덱싱과 야후 파이낸싱에서 기록된 일자 데이터가 일치하지 않음
# [방법] 야후 파이낸스를 통해 한국기업의 주가를 확인 할려 면 토,일요일을 제외한 날짜 공백이 발생하는 일자는 피해야 한다.
# [추가] 한국 코스피 데이터를 제대로 읽어오는 회사가 별로 없는것 같다. 현재 까지는 야후가 유일하다.
# 그러면 다른 방법을 찾아야 한다. 키움 API를 활용해야 될 것 같다.
data = web.DataReader("005930.KS", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ['samsung']
data = data.tz_localize('UTC')

print(data)


def initialize(context):
    context.i = 0
    context.sym = symbol('samsung')
    context.set_commission(commission.PerDollar(cost=0.00165))


def handle_data(context, data):
    order(context.sym, 1)


start_utc = start.replace(tzinfo=datetime.timezone.utc)
end_utc = end.replace(tzinfo=datetime.timezone.utc)
result = run_algorithm(capital_base=100000000,
                       initialize=initialize,
                       handle_data=handle_data,
                       start=start_utc,
                       end=end_utc,
                       data=data)

plt.plot(result.index, result.portfolio_value)
plt.show()
