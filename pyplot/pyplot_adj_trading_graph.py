import matplotlib.pyplot as plt
import pandas_datareader.data as web

sk_hynix = web.DataReader("000660.KS", "yahoo")

fig = plt.figure(figsize=(12, 8))

top_axes = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)

bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

# 라벨 한글 입력시 그래프에서 글자 깨짐 발생.. 주의!
top_axes.plot(sk_hynix.index, sk_hynix['Close'], label='sk_hynix_close_value')
top_axes.legend(loc='upper left')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'], label="sk_hynix_exchange_volume")
bottom_axes.legend(loc='upper left')

plt.tight_layout()
plt.show()