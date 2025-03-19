import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

df = pd.DataFrame({
    'category': categories,
    'value': values
})
sns.barplot(x='category', y='value', data=df, palette='viridis')
plt.title('Seaborn Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()