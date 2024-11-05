import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set display options
pd.set_option('display.max_columns', None)
sns.set(style='whitegrid')

# Creating the employment data directly in the code
data = {
    'year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'employment_rate': [67.1, 67.0, 68.3, 68.6, 69.0, 67.5, 66.0, 66.8, 67.5, 68.0]
}

# Create a DataFrame
dataset = pd.DataFrame(data)

# Display the first few rows of the dataset
print("Dataset:")
print(dataset)

# Check the structure of the dataset
print("\nDataset Info:")
print(dataset.info())

# 1. Line Plot: Employment Rate Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=dataset, x='year', y='employment_rate', marker='o')
plt.title('Employment Rate in India Over Time')
plt.xlabel('Year')
plt.ylabel('Employment Rate (%)')
plt.grid()
plt.show()

# 2. Bar Plot: Employment Rate by Year
plt.figure(figsize=(10, 6))
sns.barplot(x='year', y='employment_rate', data=dataset)
plt.title('Employment Rate by Year')
plt.xlabel('Year')
plt.ylabel('Employment Rate (%)')
plt.show()

# 3. Histogram: Distribution of Employment Rates
plt.figure(figsize=(10, 6))
sns.histplot(dataset['employment_rate'], bins=10, kde=True)
plt.title('Distribution of Employment Rates')
plt.xlabel('Employment Rate (%)')
plt.ylabel('Frequency')
plt.show()

# 4. Box Plot: Employment Rate Spread
plt.figure(figsize=(10, 6))
sns.boxplot(x='employment_rate', data=dataset)
plt.title('Box Plot of Employment Rate')
plt.xlabel('Employment Rate (%)')
plt.show()

# 5. Line Plot: Employment Rate Over the Last 5 Years
last_five_years = dataset[dataset['year'] >= dataset['year'].max() - 5]
plt.figure(figsize=(10, 6))
sns.lineplot(data=last_five_years, x='year', y='employment_rate', marker='o')
plt.title('Employment Rate in the Last 5 Years')
plt.xlabel('Year')
plt.ylabel('Employment Rate (%)')
plt.grid()
plt.show()
