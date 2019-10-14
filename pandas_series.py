from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 92300, 95200])
print(kakao)
print(kakao[0])

# Series는 익덱스 값을 지정할 수 있다.
kakao2 = Series([92600, 92400, 92100, 92300, 95200],
                index=['2019-01-02',
                       '2019-02-09',
                       '2019-03-30',
                       '2019-04-19',
                       '2019-10-09',
                       ])
print(kakao2)
print(kakao2['2019-01-02'])

for date in kakao2.index:
    print(date)

for price in kakao2.values:
    print(price)


# SK, KT
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend

# 알아서 인덱스 값에 맞춰 덧셈이 수행 된다.
print(merge)
