import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

industry = ['통신업','의료정밀','운수업창고','의약품','음식료품','전기가스업','서비스업','전기전자','종이목재','증권']
fluctuations = [1.83, 1.30, 1.30, 1.26, 1.06, 0.93, 0.77, 0.68, 0.65, 0.61]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

'''
세로 그래프에서 가로 그래프로 전환
'''
ypos = np.arange(10)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)

for i, rect in enumerate(rects):
    ax.text(0.95 * rect.get_width(),
            rect.get_y() + rect.get_height() / 2.0,
            str(fluctuations[i])+'%',
            ha='right',
            va='center')

plt.xlabel('등락률')
plt.show()