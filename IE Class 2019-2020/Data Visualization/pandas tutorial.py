import pandas as pd
import numpy as np
#link for understanding: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

s = pd.Series([6,8,3, np.nan, 6, 8])
print(s)

dates = pd.date_range('20191104', periods = 9)
print(dates)

#dataframe
df= pd.DataFrame(np.random.randn(9,4), index=dates, columns= list('ABCD')) # 9 by 4 (5 columns with index), with dates
print(df)

print(df.A) #structure within panda, shall be used to advantage. Can also: print(df["A"])

print(df.head(3))
print(df.tail(1))

print(df.describe())

#transposing: df.T
#to sort your data: df.sort_index(axis=1, ascending=False)

print("___________________________________________")
print(df.sort_index(axis=1, ascending=True))

#slicing in panda
print(df[2:4])
print(df.loc[[dates[2], dates[3]], ["B", "D"]])

print(df.iloc[3])

#boolean indexing
print(df[df>0])

print(df[df.A<0])
