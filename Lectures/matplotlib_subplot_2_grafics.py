import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(2, 1)

axs[0].plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs[1].plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')

axs[0].set_title('Дневная', fontsize=10)
axs[1].set_title('Ночная', fontsize=10)

fig.suptitle('Температура в г. Полтава', fontsize=15)

plt.show()