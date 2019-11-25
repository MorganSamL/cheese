#yahoo finance data on apple stock from 2008 onwards
#iphone release date table

from matplotlib import pylab as plt
import pandas as pd

#convert from excel format to panda format. Panda figures out by itself which string is a date based on it's exisitng structure
pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("applestockdata.csv")
print(df1.head())
df1["Date"] = pd.to_datetime(df1.Date)  #last Date is the name that appears on data file, lower case sensitive, get it wrong and it's an error
#add from library: xlrd

df2 = pd.read_excel("iphonerelease dates.xlsx")
print(df2)
df2["Date"] = pd.to_datetime(df2.Date)
indexes = [] #you can also use boolean logic, only one for loop and each date finds you the index, saves a couple lines.
for date2 in df2.Date:
    for index, date1 in enumerate(df1.Date):
        if date2==date1:
            indexes.append(index)
print(indexes)
exit(1)

