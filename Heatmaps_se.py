import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  

matrix = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))
sns.heatmap(matrix, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
plt.title('Seaborn Heatmaps Example')
plt.show()




