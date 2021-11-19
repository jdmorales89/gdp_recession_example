import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gdp = pd.read_csv('gdp_recession_example/gdp.csv')
recession = pd.read_csv('gdp_recession_example/recession.csv')

x = [24, 25, 26]
y = [23, 24, 25]

plt.plot(x, y)
plt.show()

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(gdp)
print(recession)
