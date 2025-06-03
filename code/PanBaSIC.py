import pandas as pd
import numpy as np

# Sample DataFrame creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, np.nan],
    'Salary': [50000, 60000, np.nan, 80000, 90000],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']
}
df = pd.DataFrame(data)

# Basic Information
print(df.head())           # Display first 5 rows
print(df.info())           # DataFrame info
print(df.describe())       # Summary statistics
print(df.shape)            # Dimensions of DataFrame
print(df.dtypes)           # Data types of columns

# Handling Missing Data
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill NaN with mean
df.dropna(subset=['Salary'], inplace=True)       # Drop rows with NaN in Salary

# Column Operations
df['Tax'] = df['Salary'] * 0.1                  # Add a new column
df.rename(columns={'Age': 'Employee_Age'}, inplace=True)  # Rename column

# Indexing and Selection
print(df['Name'])                               # Select a single column
print(df[['Name', 'Salary']])                   # Select multiple columns
print(df.iloc[0:3])                             # Select rows by index
print(df.loc[df['Department'] == 'IT'])         # Filter rows based on condition

# Grouping and Aggregation
grouped = df.groupby('Department')
print(grouped['Salary'].mean())                 # Mean salary by department

# Sorting
df.sort_values(by='Salary', ascending=False, inplace=True)  # Sort by Salary

# Merging and Joining
data2 = {
    'Department': ['HR', 'IT', 'Finance'],
    'Head': ['John', 'Alice', 'Sam']
}
df2 = pd.DataFrame(data2)
merged = pd.merge(df, df2, on='Department', how='inner')    # Inner Join

# Pivot Table
pivot_table = pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')
print(pivot_table)

# Exporting and Importing
df.to_csv('output.csv', index=False)  # Export to CSV
new_df = pd.read_csv('output.csv')    # Read from CSV

# Advanced Features
df['Employee_Age'] = df['Employee_Age'].apply(lambda x: x + 1)  # Apply function
print(df.value_counts('Department'))           # Count unique values in Department

# Visualization (Simple Plotting)
df.plot(x='Employee_Age', y='Salary', kind='scatter', title='Age vs Salary')

# Display the final DataFrame
print(df)
