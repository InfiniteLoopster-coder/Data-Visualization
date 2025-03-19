import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]


plt.figure(figsize=(8, 5))
plt.plot(x, y, linestyle='-', marker='o', color='blue', label='Quadratic')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
plt.legend()
plt.grid(True)
plt.show()