from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("EZJ_L.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)
# print(df1.head())

df3 = pd.read_csv("RYA_L.csv")
df3['Date'] = pd.to_datetime(df3.Date)


'''
ax = df1.plot(x="Date", y="Close", style='r-', linewidth=0.6, label="Stock price, mean="+str(mean), title="Apple stock vs Iphone launch date", figsize=(17, 9))
df1.plot(x="Date", y="Close", style='-o', ms=7, markevery=indexes, linewidth=0, ax=ax, label="Iphone launch date")
plt.xlabel("Dates")
'''
plt.figure("EasyJet stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="Easy Jet")
plt.plot(df3["Date"], df3["Close"], 'b-', linewidth=1, label="Ryan Air")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
