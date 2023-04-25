import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load an example dataset
iris = sns.load_dataset("iris")

# Data for the plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
data = pd.DataFrame({'x': x, 'sin(x)': y1, 'cos(x)': y2})

# Create a figure and a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Line plot
sns.lineplot(data=data, ax=axes[0, 0])
axes[0, 0].set_title("Line Plot")
# Scatter plot
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", style="species", ax=axes[0, 1])
axes[0, 1].set_title("Scatter Plot")

# Bar plot
titanic = sns.load_dataset("titanic")
print(titanic.columns)
sns.barplot(data=titanic, x="class", y="fare", hue="survived", ax=axes[1, 0])
axes[1, 0].set_title("Bar Plot")

# Histogram (distplot in Seaborn is deprecated, so use histplot instead)
sns.histplot(data=iris, x="petal_length", kde=True, color='purple', ax=axes[1, 1])
axes[1, 1].set_title("Histogram")

# Adjusting the layout and displaying the plots
plt.tight_layout()
plt.show()
# Scatter plot
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width",
                 hue="species", style="species", ax=axes[0, 1])
axes[0, 1].set_title("Scatter Plot")

# Bar plot
titanic = sns.load_dataset("titanic")
print(titanic.columns)
sns.barplot(data=titanic, x="class", y="fare", hue="survived", ax=axes[1, 0])
axes[1, 0].set_title("Bar Plot")

# Histogram (distplot in Seaborn is deprecated, so use histplot instead)
sns.histplot(data=iris, x="petal_length", kde=True, color='purple', ax=axes[1, 1])
axes[1, 1].set_title("Histogram")

# Adjusting the layout and displaying the plots
plt.tight_layout()
plt.show()