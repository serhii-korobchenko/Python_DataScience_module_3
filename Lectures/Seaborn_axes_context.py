import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from numpy import median


data = sns.load_dataset("mpg")
sns.set_context("poster")
sns.scatterplot(x='mpg', y='displacement', data=data)

plt.show()