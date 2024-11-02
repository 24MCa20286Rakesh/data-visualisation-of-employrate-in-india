# Importing necessary libraries
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
print(dataset.head())

# Check the structure of the dataset
print(dataset.info())

# Create a figure with multiple subplots
fig, axes = plt.subplots(3, 2, figsize=(15, 18))

# Line Plot: Employment Rate Over Time
sns.lineplot(data=dataset, x='year', y='employment_rate', marker='o', ax=axes[0, 0])
axes[0, 0].set_title('Employment Rate in India Over Time')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Employment Rate (%)')
axes[0, 0].grid()

# Bar Plot: Average Employment Rate by Year
avg_employment_rate = dataset.groupby('year')['employment_rate'].mean()
sns.barplot(x=avg_employment_rate.index, y=avg_employment_rate.values, ax=axes[0, 1])
axes[0, 1].set_title('Average Employment Rate by Year')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('Average Employment Rate (%)')

# Histogram: Distribution of Employment Rates
sns.histplot(dataset['employment_rate'], bins=10, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Distribution of Employment Rates')
axes[1, 0].set_xlabel('Employment Rate (%)')
axes[1, 0].set_ylabel('Frequency')

# Box Plot: Employment Rate Spread
sns.boxplot(x='employment_rate', data=dataset, ax=axes[1, 1])
axes[1, 1].set_title('Box Plot of Employment Rate')
axes[1, 1].set_xlabel('Employment Rate (%)')

# Line Plot: Employment Rate Over the Last 5 Years
last_five_years = dataset[dataset['year'] >= dataset['year'].max() - 5]
sns.lineplot(data=last_five_years, x='year', y='employment_rate', marker='o', ax=axes[2, 0])
axes[2, 0].set_title('Employment Rate in the Last 5 Years')
axes[2, 0].set_xlabel('Year')
axes[2, 0].set_ylabel('Employment Rate (%)')
axes[2, 0].grid()

# Hide the last subplot (if necessary)
axes[2, 1].axis('off')

# Adjust layout and show plots
plt.tight_layout()
plt.show()
