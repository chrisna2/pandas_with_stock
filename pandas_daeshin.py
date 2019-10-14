from pandas import Series, DataFrame

daeshin = {
    'open' : [11650, 11100, 11200, 11100, 11000],
    'high' : [12100, 11800, 11200, 11100, 11150],
    'low'  : [11600, 11050, 10900, 10950, 10900],
    'close': [11900, 11600, 11000, 11100, 11050]
}

#daeshin_day = DataFrame(daeshin)
#daeshin_day = DataFrame(daeshin, columns=['open', 'close', 'low', 'high'])

date = ['19.01.01','19.02.01','19.03.01','19.04.01','19.05,01']
daeshin_day = DataFrame(daeshin, columns=['open', 'close', 'low', 'high'], index=date)
print(daeshin_day)

close = daeshin_day['close']
print(close)

# latest = daeshin_day['19.05,01'] #에러발생
latest = daeshin_day.loc['19.05,01']
print(latest)

# 인덱스 확인
print(daeshin_day.index)
# 컬럼 확인
print(daeshin_day.columns)


