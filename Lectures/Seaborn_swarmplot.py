import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


my_data = pd.read_csv('my_data.csv')
#data = sns.load_dataset("mpg")

sns.set_style("darkgrid")

data = my_data
sns.swarmplot(x='origin', y='mpg', hue='origin', data=data)

plt.show()