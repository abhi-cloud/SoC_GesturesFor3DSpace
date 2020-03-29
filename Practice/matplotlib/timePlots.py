# import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as m_dates

plt.style.use('fivethirtyeight')

dates = [
    datetime(2020, 3, 15),
    datetime(2020, 3, 29),
    datetime(2020, 3, 31),
    datetime(2020, 4, 10),
    datetime(2020, 4, 12),
    datetime(2020, 5, 5),
    datetime(2020, 5, 11),
]

y = [3, 7, 5, 4, 9, 2, 1]

plt.plot_date(dates, y, linestyle='solid', linewidth=2)
plt.gcf().autofmt_xdate()

date_format = m_dates.DateFormatter('%b %d')
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()