import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('heights_weights.csv')

# Basic Statistical Descriptions
mean_height = df['height'].mean()
median_height = df['height'].median()
std_height = df['height'].std()
mean_weight = df['weight'].mean()
median_weight = df['weight'].median()
std_weight = df['weight'].std()

print(f"Mean Height: {mean_height}")
print(f"Median Height: {median_height}")
print(f"Standard Deviation of Height: {std_height}")
print(f"Mean Weight: {mean_weight}")
print(f"Median Weight: {median_weight}")
print(f"Standard Deviation of Weight: {std_weight}")

# Data Visualization
# Histogram
plt.figure(figsize=(10, 5))
label1=plt.subplot(1, 2, 1)
label=sns.histplot(df["height"],kde=True)
plt.title('Height Distribution')
plt.legend(label.patches,["height"])
plt.legend(label1.lines,["Height"])
plt.suptitle("Komal")

plt.subplot(1, 2, 2)
sns.histplot(df['weight'], kde=True)
plt.title('Weight Distribution')
plt.legend(label.patches,["weight"])
plt.legend(label1.lines,["Weight"])



plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(6, 6))
sns.scatterplot(x='height', y='weight', data=df)
plt.title('Height vs. Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
