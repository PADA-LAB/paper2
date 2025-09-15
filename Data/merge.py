import pandas as pd

df1 = pd.read_csv('amazon.csv')
df2 = pd.read_csv('amazon_with_text.csv')

df1['Review_Text'] = df2['Review_Text']

df1.to_csv('merged_amazon.csv', index=False)

print(len(df1), len(df2))
print("clear process")
