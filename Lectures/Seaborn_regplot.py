import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from numpy import median



my_data = pd.read_csv('my_data.csv')
data = sns.load_dataset("mpg")

sns.set_style("darkgrid")

#data = my_data
sns.lmplot(x="horsepower", y="displacement", data=data, x_estimator=median)

plt.show()