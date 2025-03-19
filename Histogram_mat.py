import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()


