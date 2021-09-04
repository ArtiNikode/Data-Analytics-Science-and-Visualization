import pandas

df=pandas.read_csv('Netflix.csv')
df4=df.sort_values("IMDB Score",ascending=False)
result= df4.head(10)
#print(df4)
print(result)