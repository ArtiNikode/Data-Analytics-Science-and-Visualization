import pandas

df=pandas.read_csv('Netflix.csv')
df3=df[df['Runtime']>125]
print(df3)
