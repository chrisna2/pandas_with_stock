import matplotlib.pyplot as plt
import numpy as np


def horiz_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    plt.show()


def verti_plot():
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    plt.show()


def horiz_plot_graph():
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    x = range(0, 100)
    y = [v*v for v in x]

    ax1.plot(x, y)
    ax2.bar(x, y)

    plt.show()


def horiz_plot_sin():
    x = np.arange(0.0, 2*np.pi, 0.1)

    sin_y = np.sin(x)
    cos_y = np.cos(x)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(x, sin_y, 'b--')
    ax2.plot(x, cos_y, 'r--')

    plt.show()


if __name__ == '__main__':
    horiz_plot_sin()