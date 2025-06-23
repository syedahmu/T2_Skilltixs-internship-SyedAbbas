# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('supermarket_sales.csv')

## 1. Identify and handle missing values
print("=== 1. Handling Missing Values ===")
print("Missing values before cleaning:")
print(df.isnull().sum())

# Since there are no missing values in this dataset, here's how we would handle them if there were:
# For numerical columns: fill with mean/median or drop
# df['column_name'].fillna(df['column_name'].mean(), inplace=True)
# For categorical columns: fill with mode or 'Unknown'
# df['column_name'].fillna(df['column_name'].mode()[0], inplace=True)

## 2. Remove duplicate rows
print("\n=== 2. Removing Duplicates ===")
print(f"Number of rows before removing duplicates: {len(df)}")
df.drop_duplicates(inplace=True)
print(f"Number of rows after removing duplicates: {len(df)}")

## 3. Standardize text values
print("\n=== 3. Standardizing Text Values ===")

# Standardize gender values (Male/Female to M/F if needed)
df['Gender'] = df['Gender'].str.upper().str[0]  # Takes first character and capitalizes
print("\nGender values standardized:")
print(df['Gender'].value_counts())

# Standardize customer type
df['Customer type'] = df['Customer type'].str.title()
print("\nCustomer type standardized:")
print(df['Customer type'].value_counts())

# Standardize product line (remove extra spaces, capitalize properly)
df['Product line'] = df['Product line'].str.strip().str.title()
print("\nProduct line standardized:")
print(df['Product line'].value_counts())

# Standardize payment method
df['Payment'] = df['Payment'].str.title()
print("\nPayment method standardized:")
print(df['Payment'].value_counts())

## 4. Convert date formats to consistent type
print("\n=== 4. Standardizing Date Formats ===")

# Convert Date column to datetime (handles multiple formats)
df['Date'] = pd.to_datetime(df['Date'])

# Convert Time column to consistent time format
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

# Create a combined datetime column
df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))

print("\nDate and Time columns standardized:")
print(df[['Date', 'Time', 'DateTime']].head())

## 5. Rename column headers to be clean and uniform
print("\n=== 5. Cleaning Column Headers ===")

# Create dictionary for renaming columns
new_column_names = {
    'Invoice ID': 'invoice_id',
    'Branch': 'branch',
    'City': 'city',
    'Customer type': 'customer_type',
    'Gender': 'gender',
    'Product line': 'product_line',
    'Unit price': 'unit_price',
    'Quantity': 'quantity',
    'Tax 5%': 'tax_5pc',
    'Total': 'total',
    'Date': 'date',
    'Time': 'time',
    'Payment': 'payment',
    'cogs': 'cogs',
    'gross margin percentage': 'gross_margin_pc',
    'gross income': 'gross_income',
    'Rating': 'rating'
}

# Rename columns
df.rename(columns=new_column_names, inplace=True)

print("\nNew column names:")
print(df.columns.tolist())

## 6. Check and fix data types
print("\n=== 6. Fixing Data Types ===")

print("\nData types before fixing:")
print(df.dtypes)

# Ensure numerical columns are correct
numerical_cols = ['unit_price', 'quantity', 'tax_5pc', 'total', 'cogs', 'gross_income', 'rating']
for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Ensure categorical columns are strings
categorical_cols = ['invoice_id', 'branch', 'city', 'customer_type', 'gender', 'product_line', 'payment']
for col in categorical_cols:
    df[col] = df[col].astype('string')

print("\nData types after fixing:")
print(df.dtypes)

## Final check of cleaned data
print("\n=== Final Cleaned Data ===")
print("\nFirst 5 rows of cleaned data:")
print(df.head())

print("\nData types after cleaning:")
print(df.dtypes)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned data to new CSV
df.to_csv('supermarket_sales_cleaned.csv', index=False)
print("\nCleaned data saved to 'supermarket_sales_cleaned.csv'")