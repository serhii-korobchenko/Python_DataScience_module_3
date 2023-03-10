import matplotlib.pyplot as plt

import pandas as pd



date = pd.date_range(start='2021-09-01', freq='D', periods=8)
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')

# Labels of axis
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')

#Title of plot
plt.title('Дневная погода в г. Полтава', fontsize=15)


#Text on  plot
plt.text(date[0], 15, 'Осень достаточно теплая', color="blue")

#Legend on plot
plt.legend()

plt.show()