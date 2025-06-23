import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set visual style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load cleaned data
df = pd.read_csv('supermarket_sales_cleaned.csv')

## 1. Initial Data Exploration
print("=== 1. Initial Data Exploration ===")

# 1.1 DataFrame info
print("\n--- DataFrame Info ---")
print(df.info())

# 1.2 Descriptive statistics
print("\n--- Descriptive Statistics ---")
print(df.describe(include='all').transpose())

# 1.3 Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 1.4 Value counts for categorical variables
categorical_cols = ['branch', 'city', 'customer_type', 'gender', 'product_line', 'payment']
for col in categorical_cols:
    print(f"\n--- Value Counts for {col} ---")
    print(df[col].value_counts())

## 2. Missing Data Visualization
print("\n=== 2. Missing Data Visualization ===")
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap (None found in cleaned data)')
plt.show()

## 3. Distribution and Category Analysis
print("\n=== 3. Distribution and Category Analysis ===")

# 3.1 Histograms and boxplots for numerical variables
numerical_cols = ['unit_price', 'quantity', 'tax_5pc', 'total', 'cogs', 'gross_income', 'rating']
for col in numerical_cols:
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.histplot(data=df, x=col, kde=True, bins=20)
    plt.title(f'Distribution of {col}')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x=col)
    plt.title(f'Boxplot of {col}')
    
    plt.tight_layout()
    plt.show()

# 3.2 Count plots for categorical variables
for col in categorical_cols:
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)
    plt.show()

# 3.3 Pairplot for numerical variables
sns.pairplot(df[numerical_cols])
plt.suptitle('Pairplot of Numerical Variables', y=1.02)
plt.show()

# 3.4 Product line vs Total sales
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='product_line', y='total')
plt.title('Total Sales Distribution by Product Line')
plt.xticks(rotation=45)
plt.show()

## 4. Correlation Analysis
print("\n=== 4. Correlation Analysis ===")

# 4.1 Correlation heatmap
plt.figure(figsize=(12, 8))
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Correlation Heatmap of Numerical Variables')
plt.show()

# 4.2 Scatter plot of highly correlated variables
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='total', y='gross_income')
plt.title('Total vs Gross Income')
plt.show()

## 5. Grouping and Aggregation
print("\n=== 5. Grouping and Aggregation ===")

# 5.1 Sales by product line
product_line_stats = df.groupby('product_line')['total'].agg(['sum', 'mean', 'count', 'std'])
print("\n--- Sales Statistics by Product Line ---")
print(product_line_stats)

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='product_line', y='total', estimator=sum, ci=None)
plt.title('Total Sales by Product Line')
plt.xticks(rotation=45)
plt.show()

# 5.2 Sales by payment method and gender
payment_gender_stats = df.groupby(['payment', 'gender'])['total'].agg(['sum', 'mean', 'count'])
print("\n--- Sales Statistics by Payment Method and Gender ---")
print(payment_gender_stats)

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='payment', y='total', hue='gender', estimator=sum, ci=None)
plt.title('Total Sales by Payment Method and Gender')
plt.show()

# 5.3 Time-based analysis
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month_name()
df['day_of_week'] = df['date'].dt.day_name()

monthly_sales = df.groupby('month')['total'].agg(['sum', 'mean', 'count'])
print("\n--- Monthly Sales Statistics ---")
print(monthly_sales)

plt.figure(figsize=(10, 5))
sns.lineplot(data=df.groupby(['month', 'day_of_week'])['total'].sum().reset_index(), 
             x='month', y='total', hue='day_of_week', marker='o')
plt.title('Monthly Sales Trend by Day of Week')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

## 6. Outlier and Skewness Analysis
print("\n=== 6. Outlier and Skewness Analysis ===")

# 6.1 Check skewness
print("\n--- Skewness of Numerical Variables ---")
for col in numerical_cols:
    skewness = df[col].skew()
    print(f"{col}: {skewness:.2f}")

# 6.2 Visualize most skewed variables
most_skewed = ['quantity', 'gross_income', 'tax_5pc']
for col in most_skewed:
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.histplot(data=df, x=col, kde=True, bins=20)
    plt.title(f'Original Distribution of {col}')
    
    plt.subplot(1, 2, 2)
    sns.histplot(data=df, x=np.log1p(df[col]), kde=True, bins=20)
    plt.title(f'Log-Transformed Distribution of {col}')
    
    plt.tight_layout()
    plt.show()

# 6.3 Outlier analysis
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[numerical_cols])
plt.title('Boxplot of All Numerical Variables')
plt.xticks(rotation=45)
plt.show()



## Bonus: Time of Day Analysis
print("\n=== Bonus: Time of Day Analysis ===")

# Extract hour from time
df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour

# Sales by hour
hourly_sales = df.groupby('hour')['total'].agg(['sum', 'mean', 'count'])
print("\n--- Hourly Sales Statistics ---")
print(hourly_sales)

plt.figure(figsize=(12, 6))
sns.lineplot(data=df.groupby('hour')['total'].sum().reset_index(), 
             x='hour', y='total', marker='o')
plt.title('Total Sales by Hour of Day')
plt.xticks(range(24))
plt.grid(True)
plt.show()