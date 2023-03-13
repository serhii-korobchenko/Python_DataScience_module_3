import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


my_data = pd.read_csv('my_data.csv')
#data = sns.load_dataset("mpg")

sns.set_style("darkgrid")
data = sns.load_dataset("mpg")
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)

plt.show()