import pandas

df=pandas.read_csv('Netflix.csv')
df2=df[df['IMDB Score']<3]
print(df2)
