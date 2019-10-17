import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()

# y = x^2 그래프
x = range(0,100)
y = [v*v for v in x]
plt.plot(x, y)
plt.show()

# y = x^2 점 그래프
x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y, 'ro')
plt.show()

