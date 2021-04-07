# https://stackoverflow.com/questions/66986076/matplotlib-time-on-x-axis-from-datetime-json

from scipy.stats import skewnorm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

fig, ax = plt.subplots(1, 1)
a = 4
x = np.linspace(skewnorm.ppf(0.01, a), skewnorm.ppf(0.99, a), 50)
d = pd.date_range("2021-04-06 12:00:00", "2021-04-06 16:00:00", 50)

ax.plot(d, skewnorm.pdf(x, a), 'b-', label='skewnorm pdf')

# from matplotlib.dates import AutoDateFormatter, AutoDateLocator
# xtick_locator = AutoDateLocator(minticks=3, maxticks=15)
# xtick_formatter = AutoDateFormatter(xtick_locator)
# ax.xaxis.set_major_locator(xtick_locator)
# ax.xaxis.set_major_formatter(xtick_formatter)
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))

fig.autofmt_xdate()
plt.show()

# used this code sample as a reference: https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html
# found out how to use scipy.skewnorm from here: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skewnorm.html. Stil not sure about all the values, though
# see autofmt_xdate(): https://matplotlib.org/stable/api/figure_api.html?highlight=autofmt#matplotlib.figure.Figure.autofmt_xdate
# pandas.date_range() is pretty useful here. Found out about this from https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html