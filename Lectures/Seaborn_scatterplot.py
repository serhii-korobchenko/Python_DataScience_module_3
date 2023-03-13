import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


my_data = pd.read_csv('my_data.csv')
#data = sns.load_dataset("mpg")

sns.set_style("darkgrid")

data = sns.load_dataset("mpg")
sns.scatterplot(x='mpg', y='displacement', hue= 'origin', data=my_data)

plt.show()