import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

# 색상 설정
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
labels = ['삼성전자','SK하이닉스','LG전자','네이버','카카오']
ratio = [50, 20, 10, 10, 10]
# 확대 (sk하이닉스만)
explode = (0.0, 0.1, 0.0, 0.0, 0.0)

plt.pie(ratio,
        labels=labels,
        shadow=True,
        startangle=90,
        explode=explode,
        colors=colors,
        autopct='%1.1f%%') #범주가 차지하는 비율 표시
plt.show()