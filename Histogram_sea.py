import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

sns.histplot(data, bins=30, kde=True, color='green')
plt.title('Seaborn Histogram with KDE')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


