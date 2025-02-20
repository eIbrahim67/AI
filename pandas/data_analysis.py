import pandas as pd

# Load the CSV file
df = pd.read_csv('data.csv')

# Debug: Print the column names to verify
print("Column Names in DataFrame:", df.columns)

# Step 1: Convert 'Value' column to numeric (adjust if column name is different)
if 'Value' in df.columns:
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
else:
    print("Error: 'Value' column not found. Please check the column names.")
    exit()

# Step 2: Handle missing values (replace NaN with 0)
df.fillna(0, inplace=True)

# Step 3: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 4: Filter rows where 'Value' is greater than 100
filtered_df = df[df['Value'] > 100]

# Step 5: Group data by 'Industry_name_NZSIOC' and calculate the mean of 'Value'
grouped_mean = df.groupby('Industry_name_NZSIOC')['Value'].mean()

# Step 6: Generate descriptive statistics
descriptive_stats = df.describe()

# Step 7: Compute the correlation matrix for numeric columns
correlation_matrix = df.corr()

# Display results
print("\nFiltered DataFrame (Value > 100):")
print(filtered_df)

print("\nGrouped Mean of 'Value' by 'Industry_name_NZSIOC':")
print(grouped_mean)

print("\nDescriptive Statistics:")
print(descriptive_stats)

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Optional: Save processed data to a new CSV file
df.to_csv('processed_data.csv', index=False)
