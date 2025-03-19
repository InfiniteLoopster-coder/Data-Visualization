import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
value = [10, 24, 36, 18]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, value, color='skyblue', edgecolor='black')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()


# Adding value labels on top of the bars

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

plt.show()

