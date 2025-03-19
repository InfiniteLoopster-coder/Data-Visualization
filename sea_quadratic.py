import seaborn as sns
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

data = {'x': x, 'y': y}
sns.lineplot(x='x', y='y', data=data, markers='o', label='Quadratic')
plt.title('Seaborn Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()