import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


def graph_data(data):
    x = []
    y = []
    for index in range(0, len(data)):
        x.append(data[index][0])
        y.append(data[index][3])

    fig, ax = plt.subplots()
    ax.plot(x, y)

    fig.autofmt_xdate()
    # ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    plt.show()
