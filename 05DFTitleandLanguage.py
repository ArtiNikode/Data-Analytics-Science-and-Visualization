import pandas

df=pandas.read_csv('Netflix.csv')
df5=df[['Title','Language']]
print(df5)