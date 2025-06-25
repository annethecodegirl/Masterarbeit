import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('scopus.csv')
print(df.head())
year_counts = df['Year'].value_counts().sort_index()
print(year_counts)
plt.figure(figsize=(10, 6))
year_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.title('Publication Trend: Household Carbon Footprint IO Studies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pub_trend.png')  # Save plot as PNG for LaTeX
plt.show()
top_journals = df['Source title'].value_counts().head(10)
print(top_journals)
print(df.columns.tolist())
doc_types = df['Document Type'].value_counts()
print(doc_types)
print(df['Cited by'].describe())

# Extract first author from Authors field
df['Lead Author'] = df['Authors'].dropna().str.split(';').str[0].str.strip()

# Count frequency of lead authors
lead_author_counts = df['Lead Author'].value_counts()
print(lead_author_counts.head(10))

# Count number of authors per paper
df['Num Authors'] = df['Authors'].dropna().str.split(';').apply(len)
print(df['Num Authors'].describe())

# Example: histogram of number of authors
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
df['Num Authors'].hist(bins=range(1, int(df['Num Authors'].max()+2)), edgecolor='black')
plt.xlabel('Number of Authors')
plt.ylabel('Number of Papers')
plt.title('Distribution of Co-authorship')
plt.tight_layout()
plt.savefig('coauthorship_dist.png')
plt.show()
