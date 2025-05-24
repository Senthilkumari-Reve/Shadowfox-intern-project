import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Advanced_Level_Project/IPL sample data.xlsx')
df.head()

# Show the first 5 rows
df.head()

# Get column names
print("Column Names:", df.columns.tolist())

# Check for null values
print("\nMissing Values:\n", df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# Drop unnamed and mostly-empty columns
df = df.drop(columns=['Unnamed: 11', 'Unnamed: 12'], errors='ignore')

# Replace missing values with 0 (or 'None' for strings, based on context)
df.fillna(0, inplace=True)

# Confirm cleaning
print("Missing Values After Cleaning:\n", df.isnull().sum())
df.head()

print(df['Clean Pick'].value_counts().head(10))


sns.countplot(x='Clean Pick', data=df, order=df['Clean Pick'].value_counts().index[:5])
plt.title('Top Clean Pick Entries')
plt.xlabel('Clean Pick')
plt.ylabel('Count')
plt.show()

columns = ['Catch', 'Fumble', 'Dropped Catch', 'Stumping']
for col in columns:
    print(f"\n{col} value counts:\n", df[col].value_counts())

    df[columns].apply(pd.Series.value_counts).T.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('IPL Fielding Action Distribution')
plt.ylabel('Count')
plt.xlabel('Action Type')
plt.legend(title='Value')
plt.show()

df['N->'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Most Frequent Teams or Outcomes (N->)')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

df.to_excel("Cleaned_IPL_Data.xlsx", index=False)