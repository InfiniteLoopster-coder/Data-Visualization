import matplotlib.pyplot as plt
import numpy as np

# Generate sample matrix data
matrix = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.title('Heatmaps Example')
plt.colorbar(label='Intensity')
plt.show()

