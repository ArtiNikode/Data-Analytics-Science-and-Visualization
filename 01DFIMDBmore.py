import pandas

df=pandas.read_csv('Netflix.csv')
df1=df[df['IMDB Score']>8]
print(df1)
